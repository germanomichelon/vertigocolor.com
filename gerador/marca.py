#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera os assets de marca do site a partir dos arquivos OFICIAIS em 'Marca Vertigo/'.

Regra: o desenho da marca nunca é recomposto nem redesenhado. O único tratamento
aplicado é aparar a margem transparente vazia em volta e reduzir a resolução.
"""
import os
from PIL import Image

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OFICIAL = os.path.join(RAIZ, "Marca Vertigo")
DEST = os.path.join(RAIZ, "docs", "assets", "img", "marca")
os.makedirs(DEST, exist_ok=True)


def apara(im):
    """Remove só a moldura transparente vazia (não altera o desenho)."""
    bb = im.getchannel("A").getbbox()
    return im.crop(bb) if bb else im


def salva(im, nome, largura=None, altura=None):
    if largura:
        im = im.resize((largura, round(im.height * largura / im.width)), Image.LANCZOS)
    elif altura:
        im = im.resize((round(im.width * altura / im.height), altura), Image.LANCZOS)
    caminho = os.path.join(DEST, nome)
    im.save(caminho, "PNG", optimize=True)
    print(f"  {nome}: {im.size[0]}x{im.size[1]}  ({os.path.getsize(caminho)/1024:.0f} KB)")
    return im


print("Logo oficial completo (VERTIGO COLOR):")
logo = apara(Image.open(os.path.join(OFICIAL, "Logo Vertigo.png")).convert("RGBA"))
salva(logo, "logo.png", largura=1200)      # portão de entrada / usos grandes
salva(logo, "logo-nav.png", largura=450)   # rodapé (3x de 150px, para telas retina)

print("Símbolo oficial isolado (arquivo Favicon.png):")
simbolo = apara(Image.open(os.path.join(OFICIAL, "Favicon.png")).convert("RGBA"))
salva(simbolo, "simbolo.png", altura=600)

print("Favicon (versão com fundo preto):")
fav = Image.open(os.path.join(OFICIAL, "Favicon com fundo.png")).convert("RGBA")
docs = os.path.join(RAIZ, "docs")
fav.resize((180, 180), Image.LANCZOS).convert("RGB").save(
    os.path.join(docs, "apple-touch-icon.png"), "PNG", optimize=True)
fav.resize((256, 256), Image.LANCZOS).save(
    os.path.join(docs, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
print(f"  favicon.ico + apple-touch-icon.png")

# remove assets que eu havia fabricado (lockup recomposto / inversão)
for obsoleto in [os.path.join(DEST, "logo-branco.png"),
                 os.path.join(DEST, "simbolo-branco.png"),
                 os.path.join(RAIZ, "marca", "logo-vertigo-preto.png")]:
    if os.path.exists(obsoleto):
        os.remove(obsoleto)
        print(f"  removido: {os.path.relpath(obsoleto, RAIZ)}")

print("OK — assets de marca gerados dos arquivos oficiais.")
