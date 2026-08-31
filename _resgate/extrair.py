#!/usr/bin/env python3
"""Extrai textos, imagens e vídeos do resgate do site vertigocolor.com (Squarespace)."""
import json
import os
import re
import html as htmllib
from html.parser import HTMLParser

BASE = os.path.dirname(os.path.abspath(__file__))
HTML_DIR = os.path.join(BASE, "html")
JSON_DIR = os.path.join(BASE, "paginas")
TXT_DIR = os.path.join(BASE, "textos")
os.makedirs(TXT_DIR, exist_ok=True)

IMG_RE = re.compile(r"(?:https?:)?//images\.squarespace-cdn\.com/[^\"'\s\\<>)]+")
STATIC_RE = re.compile(r"(?:https?:)?//static1\.squarespace\.com/static/[^\"'\s\\<>)]+\.(?:png|jpe?g|gif|svg|pdf|mp4|webp)[^\"'\s\\<>)]*")
YT_RE = re.compile(r"(?:https?:)?(?://|\\/\\/)(?:www\.)?(?:youtube\.com(?:/|\\/)(?:watch\?v=|embed(?:/|\\/))|youtu\.be(?:/|\\/))([\w-]{6,})")
VIMEO_RE = re.compile(r"(?:https?:)?(?://|\\/\\/)(?:player\.)?vimeo\.com(?:/|\\/)(?:video(?:/|\\/))?(\d{6,})")
MP4_RE = re.compile(r"(?:https?:)?//[^\"'\s\\<>)]+\.mp4[^\"'\s\\<>)]*")

SKIP_TAGS = {"script", "style", "noscript", "svg", "iframe", "head"}
BLOCK_TAGS = {"p", "div", "h1", "h2", "h3", "h4", "h5", "h6", "li", "br", "section", "article", "figcaption", "blockquote", "tr"}


class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.skip_depth = 0
        self.title = ""
        self.in_title = False
        self.metas = {}

    def handle_starttag(self, tag, attrs):
        if tag in SKIP_TAGS:
            self.skip_depth += 1
        if tag == "title":
            self.in_title = True
        if tag == "meta":
            a = dict(attrs)
            key = a.get("name") or a.get("property")
            if key and a.get("content"):
                self.metas[key] = a["content"]
        if tag in BLOCK_TAGS:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in SKIP_TAGS and self.skip_depth > 0:
            self.skip_depth -= 1
        if tag == "title":
            self.in_title = False
        if tag in BLOCK_TAGS:
            self.parts.append("\n")

    def handle_data(self, data):
        if self.in_title:
            self.title += data
            return
        if self.skip_depth == 0 and data.strip():
            self.parts.append(data)

    def text(self):
        raw = "".join(self.parts)
        lines = [re.sub(r"\s+", " ", ln).strip() for ln in raw.split("\n")]
        out = []
        for ln in lines:
            if ln and (not out or out[-1] != ln):
                out.append(ln)
        return "\n".join(out)


def norm_url(u):
    u = u.replace("\\/", "/")
    u = htmllib.unescape(u)
    if u.startswith("//"):
        u = "https:" + u
    u = u.split("?")[0].split("#")[0]
    return u


all_imgs = {}   # base url -> set(pages)
all_videos = {} # url -> set(pages)
page_meta = {}

for fn in sorted(os.listdir(HTML_DIR)):
    if not fn.endswith(".html"):
        continue
    slug = fn[:-5]
    raw = open(os.path.join(HTML_DIR, fn), encoding="utf-8", errors="replace").read()

    p = TextExtractor()
    try:
        p.feed(raw)
    except Exception as e:
        print(f"parser fail {fn}: {e}")
    text = p.text()

    with open(os.path.join(TXT_DIR, slug + ".txt"), "w", encoding="utf-8") as f:
        f.write(f"=== {slug} ===\nTITLE: {p.title.strip()}\n")
        for k in ("description", "og:title", "og:description", "og:image"):
            if k in p.metas:
                f.write(f"{k.upper()}: {p.metas[k]}\n")
        f.write("\n" + text + "\n")
    page_meta[slug] = {"title": p.title.strip(), "desc": p.metas.get("description", "")}

    searchable = raw + "\n"
    jf = os.path.join(JSON_DIR, slug + ".json")
    if os.path.exists(jf):
        try:
            searchable += json.dumps(json.load(open(jf)), ensure_ascii=False)
        except Exception:
            searchable += open(jf, encoding="utf-8", errors="replace").read()

    for m in IMG_RE.finditer(searchable):
        u = norm_url(m.group(0))
        all_imgs.setdefault(u, set()).add(slug)
    for m in STATIC_RE.finditer(searchable):
        u = norm_url(m.group(0))
        all_imgs.setdefault(u, set()).add(slug)
    for m in YT_RE.finditer(searchable):
        u = "https://www.youtube.com/watch?v=" + m.group(1)
        all_videos.setdefault(u, set()).add(slug)
    for m in VIMEO_RE.finditer(searchable):
        u = "https://vimeo.com/" + m.group(1)
        all_videos.setdefault(u, set()).add(slug)
    for m in MP4_RE.finditer(searchable):
        u = norm_url(m.group(0))
        all_videos.setdefault(u, set()).add(slug)

# imagens do sitemap tambem
sm = os.path.join(BASE, "imagens_sitemap.txt")
if os.path.exists(sm):
    for ln in open(sm):
        u = norm_url(ln.strip())
        if u:
            all_imgs.setdefault(u, set()).add("(sitemap)")

with open(os.path.join(BASE, "imagens_todas.txt"), "w") as f:
    for u in sorted(all_imgs):
        f.write(u + "\n")

with open(os.path.join(BASE, "inventario.md"), "w", encoding="utf-8") as f:
    f.write("# Inventário do resgate — vertigocolor.com\n\n")
    f.write(f"Páginas: {len(page_meta)} | Imagens únicas: {len(all_imgs)} | Vídeos: {len(all_videos)}\n\n")
    f.write("## Vídeos por página\n\n")
    for u in sorted(all_videos):
        f.write(f"- {u}  ← {', '.join(sorted(all_videos[u]))}\n")
    f.write("\n## Páginas (título / meta)\n\n")
    for slug in sorted(page_meta):
        m = page_meta[slug]
        f.write(f"- **{slug}** — {m['title']}" + (f" — _{m['desc']}_" if m["desc"] else "") + "\n")

print(f"paginas={len(page_meta)} imagens={len(all_imgs)} videos={len(all_videos)}")
