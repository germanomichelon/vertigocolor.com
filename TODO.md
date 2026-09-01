# Lista do que falta — Site Vertigo Color

## Para o Gê (quando der)

- [ ] **Revisar os textos do site** (PT e EN), principalmente o Sobre e as descrições dos projetos. Qualquer ajuste: é só me dizer o que mudar.
- [x] ~~**Apontar o domínio para o site novo**~~ — FEITO em 31/08/2026. Os 4 registros A do GitHub Pages e o CNAME `www` estão salvos no Squarespace; os MX do Google (e-mail) foram preservados.
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

---

## DNS: o que foi feito (Squarespace) — CONCLUÍDO em 31/08/2026

**Onde:** account.squarespace.com → Domínios → vertigocolor.com → DNS → Configurações de DNS.
O painel pede um código de autenticação enviado para germano.ms.gms@gmail.com.

**1. Apagar o grupo "Padrões do Squarespace"** (ícone de lixeira vermelho no canto do grupo).
São os 4 registros A que apontam para o Squarespace + o CNAME `www → ext-sq.squarespace.com`.

**2. Em "Registros personalizados" → ADICIONAR REGISTRO**, criar 5 registros:

| Tipo  | Nome | Dados |
|-------|------|-------------------------|
| A     | @    | 185.199.108.153 |
| A     | @    | 185.199.109.153 |
| A     | @    | 185.199.110.153 |
| A     | @    | 185.199.111.153 |
| CNAME | www  | germanomichelon.github.io |

(TTL pode ficar no padrão. Os 4 IPs são os do GitHub Pages.)

**⚠️ NÃO MEXER** nestes — são o e-mail e as verificações do Google:
- grupo **Google Workspace** (os 5 registros MX `aspmx.l.google.com` etc.) — apagar isso derruba o e-mail @vertigocolor.com;
- CNAME `42461021 → google.com` e TXT `google-gws-recovery-domain-verification=42461021`;
- os grupos "Campanhas por E-mail do Squarespace" e "Vinculação do domínio Squarespace" podem ficar (inofensivos).

**3. Depois de salvar:** a troca leva de alguns minutos até ~4 horas (o TTL atual é de 4 horas).
Me avise que eu confirmo a propagação, ligo o HTTPS no GitHub e testo o site inteiro no domínio.

**4. Só depois de tudo funcionando:** cancelar a assinatura do *site* Squarespace —
mantendo o **registro do domínio** (renova 3/out/2026, US$ 20/ano) e o e-mail.
