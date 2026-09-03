#!/usr/bin/env python3
"""Processa as imagens do resgate para o site novo (docs/assets/img)."""
import os
import re
import glob
from PIL import Image, ImageOps

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIG = os.path.join(RAIZ, "_resgate", "imagens")
DEST = os.path.join(RAIZ, "docs", "assets", "img")


def acha(prefixo):
    """Encontra arquivo do resgate pelo prefixo numérico."""
    hits = glob.glob(os.path.join(ORIG, f"{prefixo:03d}_*"))
    if not hits:
        raise FileNotFoundError(prefixo)
    return hits[0]


def salva_jpg(im, caminho, largura, q=80, pb=False):
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    im = ImageOps.exif_transpose(im)
    if im.mode != "RGB":
        bg = Image.new("RGBA", im.size, (0, 0, 0, 255))
        bg.alpha_composite(im.convert("RGBA"))
        im = bg.convert("RGB")
    if pb:
        im = ImageOps.autocontrast(im.convert("L"), cutoff=1).convert("RGB")
    if im.width > largura:
        im = im.resize((largura, round(im.height * largura / im.width)), Image.LANCZOS)
    im.save(caminho, "JPEG", quality=q, optimize=True, progressive=True)
    return im.size


def processa(prefixo, rel, largura=1600, q=80, pb=False):
    im = Image.open(acha(prefixo))
    return salva_jpg(im, os.path.join(DEST, rel), largura, q, pb)


def logo_branco(prefixo, rel, largura=560):
    """Normaliza logo de cliente para branco sobre transparente."""
    im = Image.open(acha(prefixo)).convert("RGBA")
    a = im.getchannel("A")
    cobertura = sum(1 for p in a.getdata() if p > 40) / (im.width * im.height)
    if 0.005 < cobertura < 0.92:
        mask = a.point(lambda p: 255 if p > 40 else 0)
    else:
        # sem alpha útil: constrói máscara pela luminância (marca escura sobre claro
        # ou clara sobre escuro — decide pelo canto)
        g = im.convert("L")
        canto = g.getpixel((2, 2))
        if canto > 128:
            mask = g.point(lambda p: 255 if p < 110 else 0)
        else:
            mask = g.point(lambda p: 255 if p > 145 else 0)
    out = Image.new("RGBA", im.size, (255, 255, 255, 0))
    branco = Image.new("RGBA", im.size, (255, 255, 255, 255))
    out.paste(branco, (0, 0), mask)
    bbox = out.getbbox()
    if bbox:
        out = out.crop(bbox)
    if out.width > largura:
        out = out.resize((largura, round(out.height * largura / out.width)), Image.LANCZOS)
    caminho = os.path.join(DEST, rel)
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    out.save(caminho, "PNG", optimize=True)
    return out.size


# Os assets de marca (logo, símbolo, favicon) são gerados por gerador/marca.py,
# a partir dos arquivos oficiais da pasta "Marca Vertigo/".

# ---------- heróis ----------
processa(78, "herois/xama.jpg", 2400, 82)            # Xamã andaime (hero PT)
processa(40, "herois/deadmen.jpg", 2400, 82)         # Dead Men (hero EN)

# ---------- projetos: capa + galeria ----------
PROJETOS = {
    "taro-blood-milk-and-sky": {"capa": 5, "galeria": [5]},
    "dead-men-walk-alone": {"capa": 40, "galeria": [125, 144, 224, 142, 174, 117, 227, 40, 171, 49, 193, 114, 215, 154, 186, 21, 65, 123, 150, 120, 67, 232, 201, 106, 71, 196, 217]},
    "call-me": {"capa": 11, "galeria": [11, 121, 214]},
    "only-holy-water": {"capa": 12, "galeria": [12, 218, 81, 50, 137]},
    "my-voice-for-you": {"capa": 8, "galeria": [92, 85, 17, 176, 69, 151, 42, 156, 172, 223, 119, 166, 138, 109, 118, 84]},
    "puto-de-luxo": {"capa": 28, "galeria": [28]},
    "noug": {"capa": 6, "galeria": [6, 86, 199, 116, 220, 160, 187, 95, 102, 108]},
    "metagenics": {"capa": 13, "galeria": [13, 159, 68, 175, 165, 200, 126, 158]},
    "unisc": {"capa": 10, "galeria": [10, 163, 101, 122, 167, 229, 179, 20, 70, 157, 149, 112, 72, 115, 74, 192]},
    "uceff": {"capa": 7, "galeria": [228, 47, 197, 100, 48, 110, 80, 195, 139, 46, 107, 63, 170, 136, 216, 178, 173, 124, 177, 66, 143]},
}
tam_capas = {}
for slug, cfg in PROJETOS.items():
    tam_capas[slug] = processa(cfg["capa"], f"projetos/{slug}/capa.jpg", 1600, 80)
    for i, pref in enumerate(cfg["galeria"], 1):
        processa(pref, f"projetos/{slug}/g{i:02d}.jpg", 1600, 78)

# ---------- mosaico da home ----------
MOSAICO = [44, 225, 98, 203, 57, 188, 82, 22, 230, 132, 51, 129, 221, 104, 78]
for i, pref in enumerate(MOSAICO, 1):
    processa(pref, f"mosaico/m{i:02d}.jpg", 1000, 76)

# ---------- logos de clientes ----------
# Do resgate do site antigo:
LOGOS = {"nike": 77, "mercedes": 155, "michelin": 211, "natura": 208,
         "verizon": 59, "chillibeans": 18, "national": 205}
for nome, pref in LOGOS.items():
    print(nome, logo_branco(pref, f"logos/{nome}.png"))

# Novos, entregues na pasta "Logos Clientes/" (ver LEIA-ME lá dentro):
LOGOS_PASTA = os.path.join(RAIZ, "Logos Clientes")
if os.path.isdir(LOGOS_PASTA):
    for arq in sorted(os.listdir(LOGOS_PASTA)):
        nome, ext = os.path.splitext(arq)
        if ext.lower() not in (".png", ".jpg", ".jpeg", ".svg"):
            continue
        im = Image.open(os.path.join(LOGOS_PASTA, arq)).convert("RGBA")
        a = im.getchannel("A")
        cobertura = sum(1 for p in a.getdata() if p > 40) / (im.width * im.height)
        if 0.005 < cobertura < 0.92:
            mask = a.point(lambda p: 255 if p > 40 else 0)
        else:
            g = im.convert("L")
            claro = g.getpixel((2, 2)) > 128
            mask = g.point(lambda p: 255 if (p < 200 if claro else p > 60) else 0)
        out = Image.new("RGBA", im.size, (255, 255, 255, 0))
        out.paste(Image.new("RGBA", im.size, (255, 255, 255, 255)), (0, 0), mask)
        bb = out.getbbox()
        if bb:
            out = out.crop(bb)
        if out.width > 560:
            out = out.resize((560, round(out.height * 560 / out.width)), Image.LANCZOS)
        destino = os.path.join(DEST, "logos", f"{nome}.png")
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        out.save(destino, "PNG", optimize=True)
        print(f"{nome} (Logos Clientes/) {out.size}")

# ---------- equipe ----------
# Fotos novas entram pela pasta "Fotos Equipe/" (ver LEIA-ME lá dentro);
# se não houver arquivo lá, usa a foto resgatada do site antigo.
FOTOS_NOVAS = os.path.join(RAIZ, "Fotos Equipe")
EXTENSOES = (".jpg", ".jpeg", ".png", ".heic", ".HEIC", ".JPG", ".JPEG", ".PNG")


def foto_nova(nome):
    """Caminho da foto entregue pelo Gê, se existir."""
    for ext in EXTENSOES:
        caminho = os.path.join(FOTOS_NOVAS, nome + ext)
        if os.path.exists(caminho):
            return caminho
    return None


def corta_retrato(im, proporcao=4 / 5, viés_topo=0.38):
    """Corta para a proporção do site. Em fotos verticais mantém a parte de
    cima (onde está o rosto) em vez de cortar pelo centro geométrico."""
    alvo = proporcao
    atual = im.width / im.height
    if abs(atual - alvo) < 0.01:
        return im
    if atual > alvo:                      # larga demais: corta as laterais
        larg = round(im.height * alvo)
        esq = (im.width - larg) // 2
        return im.crop((esq, 0, esq + larg, im.height))
    alt = round(im.width / alvo)          # alta demais: corta em cima/embaixo
    topo = round((im.height - alt) * viés_topo)
    return im.crop((0, topo, im.width, topo + alt))


def retrato(nome, prefixo_resgate, largura=1000):
    """Gera o retrato P&B da equipe, preferindo a foto nova."""
    novo = foto_nova(nome)
    if novo:
        im = Image.open(novo)
        origem = f"Fotos Equipe/{os.path.basename(novo)}"
    else:
        im = Image.open(acha(prefixo_resgate))
        origem = "resgate do site antigo"
    im = ImageOps.exif_transpose(im)
    im = corta_retrato(im)
    tam = salva_jpg(im, os.path.join(DEST, f"equipe/{nome}.jpg"), largura, 84, pb=True)
    print(f"  equipe/{nome}.jpg: {tam[0]}x{tam[1]}  ({origem})")


print("Retratos da equipe:")
retrato("germano", 96)
retrato("rafael", 54)
retrato("deisy", 212)
retrato("jana", 89)

# foto grande da página Sobre (proporção 3x4, não é retrato fechado)
sobre_novo = foto_nova("germano-sobre")
if sobre_novo:
    im = ImageOps.exif_transpose(Image.open(sobre_novo))
    salva_jpg(im, os.path.join(DEST, "equipe/germano-sobre.jpg"), 1600, 82, pb=True)
    print("  equipe/germano-sobre.jpg (Fotos Equipe/)")
else:
    processa(191, "equipe/germano-sobre.jpg", 1600, 82, pb=True)

# folha de verificação dos logos sobre preto
sheet = Image.new("RGB", (4 * 300, 2 * 160), (0, 0, 0))
for i, nome in enumerate(LOGOS):
    l = Image.open(os.path.join(DEST, "logos", f"{nome}.png")).convert("RGBA")
    l.thumbnail((260, 120))
    sheet.paste(l, (20 + (i % 4) * 300, 20 + (i // 4) * 160), l)
sheet.save(os.path.join(RAIZ, "_resgate", "verifica_logos.jpg"), quality=85)

total = 0
arqs = 0
for dp, _, fns in os.walk(DEST):
    for fn in fns:
        total += os.path.getsize(os.path.join(dp, fn))
        arqs += 1
print(f"OK — {arqs} arquivos, {total/1e6:.1f} MB em docs/assets/img")
