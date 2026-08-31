#!/usr/bin/env python3
"""Baixa todas as imagens do resgate na maior resolução disponível."""
import csv
import os
import re
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "imagens")
os.makedirs(OUT, exist_ok=True)

urls = [ln.strip() for ln in open(os.path.join(BASE, "imagens_todas.txt")) if ln.strip()]

HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}


def fetch(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read(), r.headers.get("Content-Type", "")


def safe_name(url, idx):
    tail = url.rstrip("/").split("/")[-1]
    tail = urllib.parse.unquote(tail).replace("+", " ")
    tail = re.sub(r"[^\w.\- ]", "_", tail)[:80] or "img"
    if "." not in tail:
        tail += ".jpg"
    return f"{idx:03d}_{tail}"


def grab(i_url):
    i, url = i_url
    variants = [url + "?format=original", url + "?format=2500w", url]
    if "static1.squarespace.com" in url:
        variants = [url]
    for v in variants:
        try:
            data, ctype = fetch(v)
            if len(data) > 500:
                name = safe_name(url, i)
                with open(os.path.join(OUT, name), "wb") as f:
                    f.write(data)
                return (url, name, len(data), v.split("?")[-1] if "?" in v else "plain", "ok")
        except Exception as e:
            last = str(e)[:60]
            continue
    return (url, "", 0, "", f"FALHOU: {last}")


results = []
with ThreadPoolExecutor(max_workers=8) as ex:
    futs = [ex.submit(grab, (i, u)) for i, u in enumerate(urls, 1)]
    for f in as_completed(futs):
        results.append(f.result())

results.sort(key=lambda r: r[1] or "zzz")
with open(os.path.join(BASE, "imagens_mapa.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["url", "arquivo", "bytes", "variante", "status"])
    w.writerows(results)

ok = [r for r in results if r[4] == "ok"]
fail = [r for r in results if r[4] != "ok"]
total = sum(r[2] for r in ok)
print(f"OK: {len(ok)}/{len(results)}  total {total/1e6:.1f} MB")
for r in fail:
    print("FALHOU:", r[0], r[4])
