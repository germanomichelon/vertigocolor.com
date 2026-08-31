#!/usr/bin/env python3
"""Mapeia imagens por página e gera folhas de contato para inspeção visual."""
import csv
import html as htmllib
import os
import re
from PIL import Image, ImageDraw

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "contato_sheets")
os.makedirs(OUT, exist_ok=True)

url2file = {}
for row in csv.DictReader(open(os.path.join(BASE, "imagens_mapa.csv"))):
    if row["status"] == "ok":
        url2file[row["url"]] = row["arquivo"]

IMG_RE = re.compile(r"(?:https?:)?//(?:images\.squarespace-cdn\.com|static1\.squarespace\.com)/[^\"'\s\\<>)]+")

def norm(u):
    u = u.replace("\\/", "/")
    u = htmllib.unescape(u)
    if u.startswith("//"):
        u = "https:" + u
    return u.split("?")[0].split("#")[0]

PAGES = ["home", "artists", "about-1", "amarcarreunioes",
         "portflio-germano__project-one-f5w4d-yx6tr", "portflio-germano__noug-commercial",
         "portflio-germano__uceff", "portflio-germano__my-voice-for-you-spektra",
         "portflio-germano__dead-men-walk-alone-violet-orlandi", "portflio-germano__cmercial-unisc",
         "portflio-deisy__project-one-f5w4d-yta7g",
         "portflio-jana__blondie-call-me-violet-orlandi-acoustic-cover",
         "portflio-jana__metagenics", "portflio-jana__violet-orlandi-only-holy-water-acoustic",
         "portflio-germano", "portflio-deisy", "portflio-jana"]

# arquivos comuns a todas as paginas (logo, favicon) - detectar por frequencia
page_files = {}
freq = {}
for slug in PAGES:
    raw = open(os.path.join(BASE, "html", slug + ".html"), encoding="utf-8", errors="replace").read()
    files = []
    for m in IMG_RE.finditer(raw):
        f = url2file.get(norm(m.group(0)))
        if f and f not in files:
            files.append(f)
    page_files[slug] = files
    for f in files:
        freq[f] = freq.get(f, 0) + 1

common = {f for f, n in freq.items() if n >= 10}

with open(os.path.join(BASE, "imagens_por_pagina.txt"), "w") as f:
    for slug in PAGES:
        uniq = [x for x in page_files[slug] if x not in common]
        f.write(f"== {slug} ({len(uniq)})\n")
        for x in uniq:
            f.write(f"   {x}\n")

THUMB = 280
COLS = 5
for slug in PAGES:
    uniq = [x for x in page_files[slug] if x not in common]
    if not uniq:
        continue
    rows = (len(uniq) + COLS - 1) // COLS
    sheet = Image.new("RGB", (COLS * (THUMB + 8) + 8, rows * (THUMB * 9 // 16 + 30 + 8) + 8), (20, 20, 20))
    dr = ImageDraw.Draw(sheet)
    for i, fn in enumerate(uniq):
        try:
            im = Image.open(os.path.join(BASE, "imagens", fn)).convert("RGB")
        except Exception:
            continue
        im.thumbnail((THUMB, THUMB * 9 // 16))
        cx = 8 + (i % COLS) * (THUMB + 8)
        cy = 8 + (i // COLS) * (THUMB * 9 // 16 + 38)
        sheet.paste(im, (cx, cy))
        dr.text((cx, cy + THUMB * 9 // 16 + 4), fn[:38], fill=(230, 230, 230))
    sheet.save(os.path.join(OUT, f"sheet_{slug}.jpg"), quality=80)

print("comuns (nav/logo):", sorted(common))
print("sheets gerados:", len(os.listdir(OUT)))
