# Lista do que falta — Site Vertigo Color

## Para o Gê (quando der)

- [ ] **Revisar os textos do site** (PT e EN), principalmente o Sobre e as descrições dos projetos. Qualquer ajuste: é só me dizer o que mudar.
- [ ] **Apontar o domínio para o site novo** — feito no painel do Squarespace, junto comigo (eu guio ou faço pelo seu Chrome). Leva ~10 minutos + algumas horas de propagação. Detalhe técnico: A records `185.199.108.153 / .109. / .110. / .111.` no apex + CNAME `www → germanomichelon.github.io`.
- [ ] **Depois do domínio apontado e funcionando**: cancelar só a assinatura do *site* no Squarespace (⚠️ manter o registro do **domínio**, que continua lá).
- [ ] **Antes/depois** (futuro): exportar do Resolve pares de frames (mesmo frame, versão log e versão final) de 2–3 projetos. Eu construo o slider interativo.
- [ ] **Filme e documentário** (futuro): mandar lista de projetos com título, link do vídeo e stills — eu adiciono no portfólio.
- [ ] **Rafa (sócio)** (daqui a alguns meses): foto + cargo + mini-bio para entrar na página de Equipe.
- [ ] **Estatísticas de visita** (opcional): se quiser saber quantas pessoas visitam o site, me pedir para instalar (GoatCounter ou Plausible, sem banner de cookies).

## Para o Claude (nos passos acima)

- [ ] No dia do DNS: reativar o `CNAME` (descomentar em `gerador/build.py`, rodar o build, commit) e configurar o domínio custom + HTTPS no GitHub Pages.
- [ ] Atualizar `og:` absolutas se algum dia o domínio mudar.

## Como editar o site (referência)

Todo o conteúdo (textos PT/EN, projetos, créditos, equipe) está em `gerador/dados.py`.
Depois de editar, gerar as páginas e conferir:

```bash
python3 gerador/build.py
```

Preview local: `cd docs && python3 -m http.server 8734` → http://localhost:8734
