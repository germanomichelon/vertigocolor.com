#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera o site estático da Vertigo Color em docs/ (PT + EN)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dados import (DOMINIO, WHATSAPP, WHATSAPP_FMT, EMAIL, ENDERECO, INSTAGRAM,
                   YOUTUBE, TIKTOK, CATEGORIAS, EQUIPE, PROJETOS, CLIENTES_LOGOS,
                   CLIENTES_ALT, NOMES_FAMOSOS, MOSAICO_N, DEPOIMENTOS, SERVICOS,
                   SOBRE, O2_TXT, REUNIAO)

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(RAIZ, "docs")

UI = {
    "pt": {
        "html_lang": "pt-BR", "outro": "en", "outro_rotulo": "EN",
        "nav": [("index.html", "Home"), ("portfolio.html", "Portfólio"), ("equipe.html", "Equipe"),
                ("sobre.html", "Sobre"), ("contato.html", "Contato")],
        "dir_proj": "projetos",
        "titulo_site": "Vertigo Color — Color grading para cinema, publicidade e música",
        "desc_site": "Estúdio brasileiro de color grading: filmes, séries, comerciais e videoclipes. Sessões remotas ao vivo para o mundo todo. Nike, Mercedes-Benz, Michelin e Natura já passaram pela nossa cor.",
        "hero_h1": "Somos<br>cor.",
        "hero_sub": "Estúdio de color grading para cinema, publicidade e música — do Brasil para o mundo.",
        "hero_img": "herois/xama.jpg",
        "hero_credito": "Xamã — Puto de Luxo · color por Deisy Araújo",
        "ver_portfolio": "Ver portfólio", "falar": "Chamar no WhatsApp",
        "trabalhos": "Trabalhos selecionados", "ver_tudo": "Ver o portfólio completo",
        "clientes": "Marcas que já passaram pela nossa cor",
        "nomes": "E artistas como", "servicos": "O que fazemos",
        "estrutura": "Estrutura", "depoimentos": "O que dizem sobre a nossa cor",
        "cta_titulo": "Vamos trabalhar juntos", "cta_email": "Enviar e-mail",
        "portfolio_h1": "Portfólio", "todos": "Todos",
        "equipe_h1": "Equipe", "equipe_sub": "Coloristas da Vertigo. Cada projeto do portfólio leva a assinatura de quem o coloriu.",
        "projetos_de": "Projetos",
        "sobre_h1": "Sobre a Vertigo",
        "contato_h1": "Contato", "whatsapp": "WhatsApp", "endereco": "Endereço", "redes": "Redes",
        "contato_sub": "Atendemos remoto, com sessão ao vivo, para qualquer lugar do mundo.",
        "creditos": "Créditos", "stills": "Stills", "anterior": "Anterior", "proximo": "Próximo",
        "voltar": "← Voltar ao portfólio", "color_por": "Color por",
        "direitos": "Todos os direitos reservados.",
        "alt_still": "still colorido pela Vertigo Color",
        "err_titulo": "Página não encontrada", "err_txt": "Este endereço não existe (ou mudou de lugar).",
        "err_cta": "Ir para a home",
    },
    "en": {
        "html_lang": "en", "outro": "pt", "outro_rotulo": "PT",
        "nav": [("index.html", "Home"), ("portfolio.html", "Work"), ("team.html", "Team"),
                ("about.html", "About"), ("contact.html", "Contact")],
        "dir_proj": "projects",
        "titulo_site": "Vertigo Color — Color grading for film, advertising and music",
        "desc_site": "Brazilian color grading studio: films, series, commercials and music videos. Live remote sessions worldwide. Nike, Mercedes-Benz, Michelin and Natura have been through our color.",
        "hero_h1": "We are<br>color.",
        "hero_sub": "A color grading studio for film, advertising and music — from Brazil to the world.",
        "hero_img": "herois/deadmen.jpg",
        "hero_credito": "Violet Orlandi — Dead Men Walk Alone · color by Germano Michelon",
        "ver_portfolio": "See the work", "falar": "Message us on WhatsApp",
        "trabalhos": "Selected work", "ver_tudo": "See the full portfolio",
        "clientes": "Brands that have been through our color",
        "nomes": "And artists like", "servicos": "What we do",
        "estrutura": "Infrastructure", "depoimentos": "What people say about our color",
        "cta_titulo": "Let's work together", "cta_email": "Send an e-mail",
        "portfolio_h1": "Work", "todos": "All",
        "equipe_h1": "Team", "equipe_sub": "Vertigo's colorists. Every project in the portfolio carries the signature of whoever graded it.",
        "projetos_de": "Projects",
        "sobre_h1": "About Vertigo",
        "contato_h1": "Contact", "whatsapp": "WhatsApp", "endereco": "Address", "redes": "Social",
        "contato_sub": "We work remotely, with live sessions, for clients anywhere in the world.",
        "creditos": "Credits", "stills": "Stills", "anterior": "Previous", "proximo": "Next",
        "voltar": "← Back to the portfolio", "color_por": "Color by",
        "direitos": "All rights reserved.",
        "alt_still": "still graded by Vertigo Color",
        "err_titulo": "Page not found", "err_txt": "This address doesn't exist (or has moved).",
        "err_cta": "Go to the homepage",
    },
}

NOME_EQUIPE = {p["slug"]: p["nome"] for p in EQUIPE}


def caminho_pagina(lang, pagina, slug=None):
    """Caminho relativo à raiz de docs/ para uma página lógica."""
    if pagina == "projeto":
        return f"{lang}/{UI[lang]['dir_proj']}/{slug}.html"
    return f"{lang}/{pagina}.html"


def shell(lang, profundidade, titulo, desc, caminho, caminho_alt, og_img, corpo,
          ativo=None, com_lightbox=False):
    ui = UI[lang]
    p = "../" * profundidade
    outro = ui["outro"]
    nav_itens = []
    for arq, rot in ui["nav"][1:]:
        cur = ' aria-current="page"' if ativo == arq else ""
        nav_itens.append(f'<a href="{p}{lang}/{arq}"{cur}>{rot}</a>')
    nav_itens.append(
        f'<a class="nav-lang" data-set-lang="{outro}" href="{p}{caminho_alt}">{ui["outro_rotulo"]}</a>')
    alt_pt = caminho if lang == "pt" else caminho_alt
    alt_en = caminho if lang == "en" else caminho_alt
    lightbox = '\n<div class="lightbox" role="dialog" aria-label="zoom"><img alt=""></div>' if com_lightbox else ""
    redes = (f'<a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a>'
             f'<a href="{YOUTUBE}" target="_blank" rel="noopener">YouTube</a>'
             f'<a href="{TIKTOK}" target="_blank" rel="noopener">TikTok</a>')
    return f"""<!DOCTYPE html>
<html lang="{ui['html_lang']}" data-lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{DOMINIO}/{caminho}">
<link rel="alternate" hreflang="pt-BR" href="{DOMINIO}/{alt_pt}">
<link rel="alternate" hreflang="en" href="{DOMINIO}/{alt_en}">
<link rel="alternate" hreflang="x-default" href="{DOMINIO}/">
<meta property="og:title" content="{titulo}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{DOMINIO}/assets/img/{og_img}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#000000">
<link rel="icon" href="{p}favicon.ico">
<link rel="apple-touch-icon" href="{p}apple-touch-icon.png">
<link rel="preload" href="{p}assets/fonts/archivo-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{p}assets/css/site.css">
</head>
<body>
<header class="nav">
  <a class="nav-marca" href="{p}{lang}/index.html" aria-label="Vertigo Color — home">
    <img src="{p}assets/img/marca/logo-nav.png" alt="Vertigo Color">
  </a>
  <nav class="nav-links">{''.join(nav_itens)}</nav>
  <button class="nav-burger" aria-label="menu"><span></span><span></span><span></span></button>
</header>
{corpo}
<footer class="rodape">
  <div class="rodape-grade">
    <div>
      <div class="rodape-marca"><img src="{p}assets/img/marca/logo-nav.png" alt="Vertigo Color"></div>
      <a class="crypto" href="{p}{caminho_pagina(lang, 'contato' if lang == 'pt' else 'contact')}">Pay us with Crypto</a>
    </div>
    <div class="rodape-col">
      <a href="mailto:{EMAIL}">{EMAIL}</a>
      <a href="{WHATSAPP}" target="_blank" rel="noopener">{WHATSAPP_FMT}</a>
      <p>{ENDERECO}</p>
    </div>
    <div class="rodape-col">{redes}</div>
  </div>
  <div class="rodape-baixo">
    <span>© 2026 Vertigo Color. {ui['direitos']}</span>
    <a data-set-lang="{outro}" href="{p}{caminho_alt}">{'English version' if lang == 'pt' else 'Versão em português'}</a>
  </div>
</footer>{lightbox}
<script src="{p}assets/js/site.js"></script>
</body>
</html>"""


def cartao(lang, proj, p, grande=False):
    ui = UI[lang]
    cat = CATEGORIAS[proj["cat"]][lang]
    href = f"{p}{caminho_pagina(lang, 'projeto', proj['slug'])}"
    cls = "card grande" if grande else "card"
    return f"""<article class="{cls} reveal" data-cat="{proj['cat']}">
  <a href="{href}">
    <span class="card-cat">{cat}</span>
    <figure><img src="{p}assets/img/projetos/{proj['slug']}/capa.jpg" alt="{proj['titulo']} — {ui['alt_still']}" loading="lazy"></figure>
    <div class="card-info"><h3>{proj['titulo']}</h3><span class="cli">{proj['cliente']}</span></div>
  </a>
</article>"""


def secao_clientes(lang, p):
    ui = UI[lang]
    logos = "".join(
        f'<img src="{p}assets/img/logos/{l}.png" alt="{CLIENTES_ALT[l]}" loading="lazy">'
        for l in CLIENTES_LOGOS)
    return f"""<section class="secao clientes"><div class="miolo reveal">
  <p class="rotulo" style="text-align:center;margin-bottom:40px">{ui['clientes']}</p>
  <div class="clientes-grade">{logos}</div>
</div></section>"""


def secao_depoimentos(lang, branca=True):
    ui = UI[lang]
    itens = "".join(f"""<figure class="depo reveal">
    <blockquote>{d['texto'][lang]}</blockquote>
    <figcaption>{d['autor']} — {d['fonte'][lang]}</figcaption>
  </figure>""" for d in DEPOIMENTOS)
    cls = "secao faixa-branca" if branca else "secao"
    return f"""<section class="{cls}"><div class="miolo">
  <p class="rotulo reveal">{ui['depoimentos']}</p>
  <div class="depos" style="margin-top:36px">{itens}</div>
</div></section>"""


def secao_cta(lang, p):
    ui = UI[lang]
    return f"""<section class="secao"><div class="miolo reveal" style="text-align:center">
  <h2 class="display" style="margin-bottom:34px">{ui['cta_titulo']}</h2>
  <div class="linha-botoes" style="justify-content:center">
    <a class="botao cheio" href="{WHATSAPP}" target="_blank" rel="noopener">{ui['falar']}</a>
    <a class="botao" href="mailto:{EMAIL}">{ui['cta_email']}</a>
  </div>
</div></section>"""


def pagina_home(lang):
    ui = UI[lang]
    p = "../"
    caminho = caminho_pagina(lang, "index")
    caminho_alt = caminho_pagina(ui["outro"], "index")
    cards = "".join(cartao(lang, pr, p) for pr in PROJETOS[:6])
    mosaico = "".join(
        f'<img src="{p}assets/img/mosaico/m{i:02d}.jpg" alt="" loading="lazy">'
        for i in range(1, MOSAICO_N + 1))
    servicos = "".join(f"""<div class="servico reveal"><h3>{s[lang][0]}</h3><p>{s[lang][1]}</p></div>"""
                       for s in SERVICOS)
    corpo = f"""<main>
<section class="hero">
  <div class="hero-fundo"><img src="{p}assets/img/{ui['hero_img']}" alt="" fetchpriority="high"></div>
  <div class="hero-conteudo miolo">
    <p class="rotulo">Color Grading · São Marcos RS · Rio de Janeiro</p>
    <h1 class="display">{ui['hero_h1']}</h1>
    <p class="hero-sub">{ui['hero_sub']}</p>
    <div class="linha-botoes">
      <a class="botao cheio" href="portfolio.html">{ui['ver_portfolio']}</a>
      <a class="botao" href="{WHATSAPP}" target="_blank" rel="noopener">{ui['falar']}</a>
    </div>
  </div>
  <span class="hero-credito">{ui['hero_credito']}</span>
</section>

<section class="secao"><div class="miolo">
  <p class="rotulo reveal">{ui['portfolio_h1']}</p>
  <h2 class="t-secao reveal">{ui['trabalhos']}</h2>
  <div class="grade">{cards}</div>
  <p class="reveal" style="margin-top:40px;text-align:center"><a class="botao" href="portfolio.html">{ui['ver_tudo']}</a></p>
</div></section>

{secao_clientes(lang, p)}

<section class="secao" style="padding-left:0;padding-right:0">
  <div class="marquee reveal"><div class="marquee-track">{mosaico}</div></div>
  <p class="nomes-famosos reveal">{ui['nomes']}: {NOMES_FAMOSOS}</p>
</section>

<section class="secao"><div class="miolo">
  <p class="rotulo reveal">{ui['servicos']}</p>
  <h2 class="t-secao reveal">{'Serviços' if lang == 'pt' else 'Services'}</h2>
  <div class="servicos-grade">{servicos}</div>
</div></section>

<section class="secao" style="padding-top:0"><div class="miolo reveal">
  <p class="rotulo">{ui['estrutura']}</p>
  <p class="prosa" style="margin-top:18px;font-size:clamp(1.15rem,2.2vw,1.7rem);font-weight:600;max-width:900px">{O2_TXT[lang]}</p>
</div></section>

{secao_depoimentos(lang)}
{secao_cta(lang, p)}
</main>"""
    return shell(lang, 1, ui["titulo_site"], ui["desc_site"], caminho, caminho_alt,
                 ui["hero_img"], corpo, ativo="index.html")


def pagina_portfolio(lang):
    ui = UI[lang]
    p = "../"
    caminho = caminho_pagina(lang, "portfolio")
    caminho_alt = caminho_pagina(ui["outro"], "portfolio")
    cats_presentes = []
    for pr in PROJETOS:
        if pr["cat"] not in cats_presentes:
            cats_presentes.append(pr["cat"])
    filtros = f'<button class="filtro ativo" data-f="todos">{ui["todos"]}</button>' + "".join(
        f'<button class="filtro" data-f="{c}">{CATEGORIAS[c][lang]}</button>' for c in cats_presentes)
    cards = "".join(cartao(lang, pr, p, grande=(i == 0)) for i, pr in enumerate(PROJETOS))
    titulo = f"{ui['portfolio_h1']} — Vertigo Color"
    desc = ("Filmes, comerciais e videoclipes colorizados pela Vertigo Color."
            if lang == "pt" else "Films, commercials and music videos graded by Vertigo Color.")
    corpo = f"""<main class="projeto-topo">
<section class="secao" style="padding-top:0"><div class="miolo">
  <h1 class="display reveal" style="margin-bottom:38px">{ui['portfolio_h1']}</h1>
  <div class="filtros reveal">{filtros}</div>
  <div class="grade">{cards}</div>
</div></section>
{secao_cta(lang, p)}
</main>"""
    return shell(lang, 1, titulo, desc, caminho, caminho_alt,
                 f"projetos/{PROJETOS[0]['slug']}/capa.jpg", corpo, ativo="portfolio.html")


def pagina_projeto(lang, i):
    ui = UI[lang]
    proj = PROJETOS[i]
    p = "../../"
    caminho = caminho_pagina(lang, "projeto", proj["slug"])
    caminho_alt = caminho_pagina(ui["outro"], "projeto", proj["slug"])
    cat = CATEGORIAS[proj["cat"]][lang]
    colorista = NOME_EQUIPE[proj["colorista"]]

    if proj.get("yt"):
        video = f"""<div class="embed reveal" data-yt="{proj['yt']}" role="button" tabindex="0" aria-label="play">
      <img src="{p}assets/img/projetos/{proj['slug']}/capa.jpg" alt="{proj['titulo']}" fetchpriority="high">
      <span class="embed-play"></span></div>"""
    elif proj.get("vimeo"):
        video = f"""<div class="embed reveal" data-vimeo="{proj['vimeo']}" role="button" tabindex="0" aria-label="play">
      <img src="{p}assets/img/projetos/{proj['slug']}/capa.jpg" alt="{proj['titulo']}" fetchpriority="high">
      <span class="embed-play"></span></div>"""
    else:
        video = f"""<figure class="reveal" style="border:1px solid var(--b12)">
      <img src="{p}assets/img/projetos/{proj['slug']}/capa.jpg" alt="{proj['titulo']} — {ui['alt_still']}" fetchpriority="high"></figure>"""

    creditos = "".join(
        f"<li><span>{rot.split(' / ')[0] if lang == 'pt' else rot.split(' / ')[-1]}</span><span>{val}</span></li>"
        for rot, val in proj["creditos"])
    galeria = "".join(
        f'<img src="{p}assets/img/projetos/{proj["slug"]}/g{n:02d}.jpg" alt="{proj["titulo"]} — {ui["alt_still"]} {n}" loading="lazy">'
        for n in range(1, proj["n_galeria"] + 1))

    ant = PROJETOS[(i - 1) % len(PROJETOS)]
    prox = PROJETOS[(i + 1) % len(PROJETOS)]
    titulo = f"{proj['titulo']} · {proj['cliente']} — Vertigo Color"
    corpo = f"""<main class="projeto-topo">
<section class="secao" style="padding-top:0;padding-bottom:40px"><div class="miolo">
  <p class="rotulo reveal">{cat} · {proj['cliente']}</p>
  <h1 class="display reveal" style="font-size:clamp(2.2rem,6.5vw,5.5rem)">{proj['titulo']}</h1>
  <div class="projeto-meta reveal"><span class="mudo">{ui['color_por']} <strong>{colorista}</strong></span></div>
  <p class="prosa reveal mudo" style="max-width:760px">{proj['desc'][lang]}</p>
</div></section>
<section style="padding:0 var(--pad)"><div class="miolo">{video}</div></section>
<section class="secao"><div class="miolo">
  <p class="rotulo reveal">{ui['creditos']}</p>
  <ul class="creditos reveal" style="margin-top:22px">{creditos}</ul>
</div></section>
<section class="secao" style="padding-top:0"><div class="miolo">
  <p class="rotulo reveal" style="margin-bottom:22px">{ui['stills']}</p>
  <div class="galeria">{galeria}</div>
  <p class="reveal" style="margin-top:34px"><a href="{p}{caminho_pagina(lang, 'portfolio')}" class="mudo">{ui['voltar']}</a></p>
</div></section>
<nav class="projeto-nav">
  <a href="{ant['slug']}.html"><span class="rotulo">{ui['anterior']}</span><br><strong>{ant['titulo']}</strong></a>
  <a class="prox" href="{prox['slug']}.html"><span class="rotulo">{ui['proximo']}</span><br><strong>{prox['titulo']}</strong></a>
</nav>
{secao_cta(lang, p)}
</main>"""
    return shell(lang, 2, titulo, proj["desc"][lang], caminho, caminho_alt,
                 f"projetos/{proj['slug']}/capa.jpg", corpo, ativo="portfolio.html",
                 com_lightbox=True)


def pagina_equipe(lang):
    ui = UI[lang]
    p = "../"
    caminho = caminho_pagina(lang, "equipe" if lang == "pt" else "team")
    caminho_alt = caminho_pagina(ui["outro"], "equipe" if ui["outro"] == "pt" else "team")
    pessoas = []
    for pe in EQUIPE:
        projs = [pr for pr in PROJETOS if pr["colorista"] == pe["slug"]]
        links = " · ".join(
            f'<a href="{p}{caminho_pagina(lang, "projeto", pr["slug"])}">{pr["titulo"]}</a>'
            for pr in projs[:4])
        bloco_links = f'<p class="proj-links"><span class="rotulo">{ui["projetos_de"]}</span><br>{links}</p>' if links else ""
        pessoas.append(f"""<article class="pessoa reveal">
  <figure><img src="{p}assets/img/{pe['foto']}" alt="{pe['nome']}" loading="lazy"></figure>
  <h3>{pe['nome']}</h3>
  <p class="cargo">{pe['cargo'][lang]}</p>
  <p>{pe['bio'][lang]}</p>
  {bloco_links}
</article>""")
    titulo = f"{ui['equipe_h1']} — Vertigo Color"
    corpo = f"""<main class="projeto-topo">
<section class="secao" style="padding-top:0"><div class="miolo">
  <h1 class="display reveal">{ui['equipe_h1']}</h1>
  <p class="prosa reveal mudo" style="margin:22px 0 48px">{ui['equipe_sub']}</p>
  <div class="equipe-grade">{''.join(pessoas)}</div>
</div></section>
{secao_cta(lang, p)}
</main>"""
    return shell(lang, 1, titulo, ui["equipe_sub"], caminho, caminho_alt,
                 "equipe/germano.jpg", corpo, ativo="equipe.html" if lang == "pt" else "team.html")


def pagina_sobre(lang):
    ui = UI[lang]
    p = "../"
    caminho = caminho_pagina(lang, "sobre" if lang == "pt" else "about")
    caminho_alt = caminho_pagina(ui["outro"], "sobre" if ui["outro"] == "pt" else "about")
    paragrafos = "".join(f"<p>{t}</p>" for t in SOBRE[lang])
    titulo = f"{ui['sobre_h1']} — Vertigo Color"
    desc = SOBRE[lang][2][:155]
    corpo = f"""<main class="projeto-topo">
<section class="secao" style="padding-top:0"><div class="miolo">
  <h1 class="display reveal" style="margin-bottom:44px">{ui['sobre_h1']}</h1>
  <div class="duas-colunas">
    <div class="prosa reveal">{paragrafos}</div>
    <figure class="reveal"><img src="{p}assets/img/equipe/germano-sobre.jpg" alt="Germano Michelon Santos" loading="lazy"></figure>
  </div>
</div></section>
<section class="secao" style="padding-top:0"><div class="miolo reveal">
  <p class="rotulo">{ui['estrutura']}</p>
  <p class="prosa" style="margin-top:18px;font-size:clamp(1.15rem,2.2vw,1.7rem);font-weight:600;max-width:900px">{O2_TXT[lang]}</p>
  <p class="mudo" style="margin-top:14px">{ENDERECO}</p>
</div></section>
{secao_clientes(lang, p)}
{secao_cta(lang, p)}
</main>"""
    return shell(lang, 1, titulo, desc, caminho, caminho_alt, "equipe/germano-sobre.jpg",
                 corpo, ativo="sobre.html" if lang == "pt" else "about.html")


def pagina_contato(lang):
    ui = UI[lang]
    p = "../"
    caminho = caminho_pagina(lang, "contato" if lang == "pt" else "contact")
    caminho_alt = caminho_pagina(ui["outro"], "contato" if ui["outro"] == "pt" else "contact")
    titulo = f"{ui['contato_h1']} — Vertigo Color"
    corpo = f"""<main class="projeto-topo">
<section class="secao contato-grande" style="padding-top:0"><div class="miolo">
  <h1 class="display reveal" style="margin-bottom:20px">{ui['contato_h1']}</h1>
  <p class="prosa reveal mudo" style="margin-bottom:44px">{ui['contato_sub']}</p>
  <p class="reveal"><a class="email" href="mailto:{EMAIL}">{EMAIL}</a></p>
  <div class="contato-lista">
    <div class="item reveal"><span class="rotulo">{ui['whatsapp']}</span>
      <a class="botao cheio" href="{WHATSAPP}" target="_blank" rel="noopener">{WHATSAPP_FMT}</a></div>
    <div class="item reveal"><span class="rotulo">{ui['endereco']}</span>
      <p class="mudo">{ENDERECO}</p></div>
    <div class="item reveal"><span class="rotulo">{ui['redes']}</span>
      <p><a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a> · <a href="{YOUTUBE}" target="_blank" rel="noopener">YouTube</a> · <a href="{TIKTOK}" target="_blank" rel="noopener">TikTok</a></p></div>
  </div>
</div></section>
</main>"""
    return shell(lang, 1, titulo, ui["contato_sub"], caminho, caminho_alt,
                 "herois/xama.jpg" if lang == "pt" else "herois/deadmen.jpg",
                 corpo, ativo="contato.html" if lang == "pt" else "contact.html")


def pagina_reuniao(lang):
    ui = UI[lang]
    r = REUNIAO[lang]
    p = "../"
    caminho = caminho_pagina(lang, "reuniao" if lang == "pt" else "meeting")
    caminho_alt = caminho_pagina(ui["outro"], "reuniao" if ui["outro"] == "pt" else "meeting")
    blocos = "".join(f'<div class="servico reveal"><h3>{t}</h3><p>{d}</p></div>' for t, d in r["blocos"])
    titulo = f"{r['titulo']} — Vertigo Color"
    corpo = f"""<main class="projeto-topo">
<section class="secao" style="padding-top:0"><div class="miolo">
  <h1 class="display reveal" style="max-width:1000px">{r['titulo']}</h1>
  <p class="prosa reveal mudo" style="margin:26px 0 40px;max-width:640px">{r['sub']}</p>
  <p class="reveal"><a class="botao cheio" href="{WHATSAPP}" target="_blank" rel="noopener">{r['cta']}</a>
  <span class="mudo" style="display:block;margin-top:12px;font-size:0.9rem">{r['cta_sub']}</span></p>
</div></section>
<section class="secao"><div class="miolo"><div class="servicos-grade" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr))">{blocos}</div></div></section>
{secao_depoimentos(lang)}
{secao_cta(lang, p)}
</main>"""
    return shell(lang, 1, titulo, r["sub"], caminho, caminho_alt, "herois/xama.jpg", corpo)


def pagina_portao():
    corpo = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Vertigo Color</title>
<meta name="description" content="Vertigo Color — estúdio brasileiro de color grading. Brazilian color grading studio.">
<link rel="canonical" href="__DOMINIO__/">
<link rel="alternate" hreflang="pt-BR" href="__DOMINIO__/pt/index.html">
<link rel="alternate" hreflang="en" href="__DOMINIO__/en/index.html">
<link rel="alternate" hreflang="x-default" href="__DOMINIO__/">
<meta property="og:title" content="Vertigo Color">
<meta property="og:description" content="Color grading — do Brasil para o mundo / from Brazil to the world.">
<meta property="og:image" content="__DOMINIO__/assets/img/herois/xama.jpg">
<meta name="theme-color" content="#000000">
<link rel="icon" href="favicon.ico">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="preload" href="assets/fonts/archivo-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/site.css">
<script>
try {
  var l = localStorage.getItem("vc-lang");
  if (l === "pt" || l === "en") { location.replace(l + "/index.html"); }
} catch (e) {}
</script>
</head>
<body>
<div class="portao">
  <div class="portao-topo">
    <img class="logo" src="assets/img/marca/logo.png" alt="Vertigo Color">
    <p class="portao-pergunta">Você é brasileiro? · Are you Brazilian?</p>
  </div>
  <div class="portao-opcoes">
    <a class="portao-opcao" href="pt/index.html" data-set-lang="pt" onclick="try{localStorage.setItem('vc-lang','pt')}catch(e){}">
      <span class="rotulo">Sim — continuar em</span>
      <strong>Português</strong>
    </a>
    <a class="portao-opcao" href="en/index.html" data-set-lang="en" onclick="try{localStorage.setItem('vc-lang','en')}catch(e){}">
      <span class="rotulo">No — continue in</span>
      <strong>English</strong>
    </a>
  </div>
</div>
</body>
</html>"""
    return corpo.replace("__DOMINIO__", DOMINIO)


def pagina_404():
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>404 — Vertigo Color</title>
<meta name="robots" content="noindex">
<meta name="theme-color" content="#000000">
<link rel="icon" href="/favicon.ico">
<link rel="stylesheet" href="/assets/css/site.css">
</head>
<body>
<div class="pagina-central">
  <img src="/assets/img/marca/logo.png" alt="Vertigo Color" style="width:min(300px,70vw)">
  <h1 class="display" style="font-size:clamp(2rem,7vw,4.5rem)">404</h1>
  <p class="mudo">{UI['pt']['err_txt']}<br>{UI['en']['err_txt']}</p>
  <div class="linha-botoes" style="justify-content:center">
    <a class="botao" href="/pt/index.html">{UI['pt']['err_cta']}</a>
    <a class="botao" href="/en/index.html">{UI['en']['err_cta']}</a>
  </div>
</div>
</body>
</html>"""


def sitemap():
    urls = [("", None)]
    paginas = [("index", "index"), ("portfolio", "portfolio"), ("equipe", "team"),
               ("sobre", "about"), ("contato", "contact"), ("reuniao", "meeting")]
    linhas = []
    for pt_p, en_p in paginas:
        for lang, pg in (("pt", pt_p), ("en", en_p)):
            alt_pt = f"{DOMINIO}/pt/{pt_p}.html"
            alt_en = f"{DOMINIO}/en/{en_p}.html"
            linhas.append(f"""  <url><loc>{DOMINIO}/{lang}/{pg}.html</loc>
    <xhtml:link rel="alternate" hreflang="pt-BR" href="{alt_pt}"/>
    <xhtml:link rel="alternate" hreflang="en" href="{alt_en}"/></url>""")
    for pr in PROJETOS:
        alt_pt = f"{DOMINIO}/pt/projetos/{pr['slug']}.html"
        alt_en = f"{DOMINIO}/en/projects/{pr['slug']}.html"
        for u in (alt_pt, alt_en):
            linhas.append(f"""  <url><loc>{u}</loc>
    <xhtml:link rel="alternate" hreflang="pt-BR" href="{alt_pt}"/>
    <xhtml:link rel="alternate" hreflang="en" href="{alt_en}"/></url>""")
    corpo = "\n".join(linhas)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url><loc>{DOMINIO}/</loc></url>
{corpo}
</urlset>"""


def escreve(caminho, conteudo):
    caminho = os.path.join(DOCS, caminho)
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(conteudo)


def main():
    n = 0
    escreve("index.html", pagina_portao()); n += 1
    escreve("404.html", pagina_404()); n += 1
    escreve("sitemap.xml", sitemap()); n += 1
    escreve("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {DOMINIO}/sitemap.xml\n"); n += 1
    # CNAME: reativar quando o DNS do Squarespace apontar para o GitHub Pages
    # escreve("CNAME", "vertigocolor.com\n")
    escreve(".nojekyll", ""); n += 1

    for lang in ("pt", "en"):
        escreve(caminho_pagina(lang, "index"), pagina_home(lang)); n += 1
        escreve(caminho_pagina(lang, "portfolio"), pagina_portfolio(lang)); n += 1
        escreve(caminho_pagina(lang, "equipe" if lang == "pt" else "team"), pagina_equipe(lang)); n += 1
        escreve(caminho_pagina(lang, "sobre" if lang == "pt" else "about"), pagina_sobre(lang)); n += 1
        escreve(caminho_pagina(lang, "contato" if lang == "pt" else "contact"), pagina_contato(lang)); n += 1
        escreve(caminho_pagina(lang, "reuniao" if lang == "pt" else "meeting"), pagina_reuniao(lang)); n += 1
        for i in range(len(PROJETOS)):
            escreve(caminho_pagina(lang, "projeto", PROJETOS[i]["slug"]), pagina_projeto(lang, i)); n += 1

    print(f"OK — {n} arquivos gerados em docs/")


if __name__ == "__main__":
    main()
