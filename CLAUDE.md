# Vertigo Color — site (vertigocolor.com)

Site institucional da Vertigo Color, estúdio de color grading de São Marcos/RS.
Estático, bilíngue (PT/EN), gerado por scripts Python e publicado pelo GitHub Pages
a partir da pasta `docs/`.

> **Este repositório é público.** Não registrar aqui (nem em commits) dados de conta,
> cobrança, credenciais ou informações internas do negócio.

## Como o projeto funciona

| Caminho | Papel |
|---|---|
| `gerador/dados.py` | **Todo o conteúdo**: textos PT/EN, projetos, créditos, equipe, clientes, serviços, contatos. Mudança de texto começa aqui. |
| `gerador/build.py` | Gera as páginas HTML em `docs/` a partir de `dados.py`. Textos de interface (menu, rótulos, títulos) ficam no dicionário `UI`. |
| `gerador/imagens.py` | Processa imagens do `_resgate/`, de `Fotos Equipe/` e de `Logos Clientes/` para `docs/assets/img/`. |
| `gerador/marca.py` | Gera logo, símbolo e favicon a partir dos arquivos oficiais de `Marca Vertigo/`. |
| `docs/` | O site publicado. **O HTML é gerado — não editar à mão.** Exceção: `docs/assets/css/site.css` e `docs/assets/js/site.js` são fontes editadas diretamente. |
| `_resgate/` | Backup completo do site antigo (Squarespace): imagens originais, textos, HTML. Não apagar. |
| `Fotos Equipe/`, `Logos Clientes/` | Pastas de entrega de arquivos (cada uma tem um `LEIA-ME.txt`). |
| `TODO.md` | Pendências combinadas. |

## Comandos

```bash
python3 gerador/marca.py     # só quando os arquivos de Marca Vertigo/ mudarem
python3 gerador/imagens.py   # quando entrar foto, logo ou imagem nova
python3 gerador/build.py     # sempre depois de mexer em dados.py ou build.py
cd docs && python3 -m http.server 8734   # preview em http://localhost:8734
```

O `.claude/launch.json` não funciona: o macOS bloqueia o acesso do servidor de preview
à pasta Desktop. Servir pelo terminal, como acima.

## Publicação

- Push na `main` → o GitHub Pages publica sozinho (pasta `/docs`). O domínio vem de
  `docs/CNAME`, que o `build.py` gera — não remover.
- Status do build: `gh api repos/germanomichelon/vertigocolor.com/pages/builds/latest -q .status`
- O CDN guarda cache por alguns minutos: testar com `?v=$RANDOM` antes de concluir que algo
  não publicou.
- O GitHub às vezes cria commits sozinho (ex.: ao mexer no domínio). Se o push for recusado,
  `git pull --rebase` e conferir o que veio antes de reenviar.
- O DNS fica no Squarespace (onde está registrado o domínio). Ao mexer nele, preservar os
  registros MX e TXT do Google.

## Marca e design — decisões do Gê (não reabrir)

- **Só preto puro `#000` e branco puro `#FFF`.** Tons intermediários apenas como branco com
  transparência. A única cor do site é a das imagens.
- **O logo nunca é recomposto, recortado, redesenhado nem invertido.** Usar os arquivos de
  `Marca Vertigo/` inteiros (o `marca.py` só apara margem vazia e redimensiona).
  `Logo só_.png` e `Logo_so_.ai` são da **Vertigo Filmes**, outra marca — não usar.
  Não existe versão preta oficial; se for necessária, pedir ao Gê.
- Barra superior alta, porque o logo é vertical: 132px no topo e 90px ao rolar (desktop).
- Tipografia: Archivo variável, auto-hospedada em `docs/assets/fonts/`.
- **Texto corrido justificado no site inteiro**, com hifenização (`hyphens: auto` seguindo o
  `lang` da página).
- Fotos da equipe em preto e branco. O retrato do Gê tem fundo preto e os dos demais, fundo
  claro — não uniformizar.
- Muro de clientes: logos convertidos para branco puro.

## Conteúdo

- **Bilíngue com pergunta na entrada** ("Você é brasileiro? · Are you Brazilian?"). É
  intencional — sinaliza alcance internacional — e não deve ser removida. A escolha fica em
  `localStorage` (`vc-lang`).
- PT e EN são **adaptados**, não traduzidos ao pé da letra. Toda mudança de texto vale para os
  dois idiomas.
- Rotas: PT em `/pt/` (`projetos/`, `equipe`, `sobre`, `contato`, `reuniao`); EN em `/en/`
  (`projects/`, `team`, `about`, `contact`, `meeting`).
- Equipe, nesta ordem: **Germano Michelon Santos** e **Rafael Pereira Batista** (fundadores,
  coloristas sênior), Rafael de Deus, Deisy Araújo, Jana Spínola.
  **São dois Rafaéis diferentes** — slugs `rafael-batista` e `rafael`.
- Todo projeto do portfólio leva o nome de quem o coloriu.
- Foco 100% estúdio: sem blog, sem curso ou mentoria (educação terá site próprio), sem
  formulários. Contato só por WhatsApp e e-mail. O "Pay us with Crypto" do rodapé fica.
- Mercados atendidos, quando houver lista: Brasil, Estados Unidos, Europa, Arábia Saudita e Índia.
- **Não inventar fatos** — créditos, clientes, datas, atribuições. Na dúvida, perguntar.
- A imagem do Xamã no andaime (abertura da home em PT) **não é do Puto de Luxo**; o projeto de
  origem é desconhecido, por isso o crédito é só "Xamã · color pela Vertigo".

## Imagens

- **Fotos da equipe**: `Fotos Equipe/<slug>.(jpg|png|heic)` → corte 4:5 enquadrando pelo topo e
  conversão para P&B. Fotos que já chegam em P&B não recebem autocontraste. Sem foto, entra um
  placeholder com o símbolo da marca.
- **Logos de clientes**: `Logos Clientes/<nome>.(png|jpg|svg)` → branco puro. Depois, incluir o
  nome em `CLIENTES_LOGOS` e `CLIENTES_ALT` (`dados.py`).
- Imagens do resgate são chamadas pelo prefixo numérico do arquivo em `_resgate/imagens/`
  (ex.: `78` = `078_XAMA 07 CLIP 2.PNG`). Antes de atribuir uma imagem a um projeto, conferir
  em `_resgate/imagens_por_pagina.txt` de qual página do site antigo ela veio — a home antiga
  tinha imagens soltas, sem projeto.

## Verificação visual

- Capturas com Chrome headless (`--headless=new --screenshot=...`). O painel de navegador do
  app congela rolagem e animações quando está oculto.
- Parâmetros de depuração em `site.js`: `?semanim` desliga animações e carrega todas as
  imagens; `?y=N` rola de verdade; `?t=N` desloca o conteúdo mantendo a barra fixa no topo.
- Capturas headless em largura de celular não são confiáveis (cortam conteúdo). Conferir o
  mobile no navegador do app com o preset mobile.
