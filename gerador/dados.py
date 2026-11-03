# -*- coding: utf-8 -*-
"""Todo o conteúdo do site, em PT e EN. Editar aqui; depois rodar build.py."""

DOMINIO = "https://vertigocolor.com"
WHATSAPP = "https://wa.me/5554996799638"
WHATSAPP_FMT = "+55 (54) 99679-9638"
EMAIL = "germanomichelonsantos@gmail.com"
ENDERECO = "Av. Venâncio Aires, 907 — São Marcos, RS — Brasil"
INSTAGRAM = "https://www.instagram.com/germanomichelon/"
YOUTUBE = "https://www.youtube.com/@GermanoMichelon"
TIKTOK = "https://www.tiktok.com/@germanomichelon"
REDES_GERMANO = [INSTAGRAM, YOUTUBE, TIKTOK,
                 "https://www.threads.net/@germanomichelon",
                 "https://medium.com/@germanomichelon",
                 "https://germanomichelon.substack.com/",
                 "https://creators.spotify.com/pod/profile/germano-michelon-santos/"]
# Ficha pública no Google. Nota e número de avaliações conferidos em 03/11/2026: atualizar à mão.
GOOGLE_PERFIL = "https://www.google.com/maps?cid=1024686640801054637"
LINKEDIN_EMPRESA = "https://www.linkedin.com/company/vertigo-color/"
GOOGLE_NOTA = {"pt": "5,0 no Google · 16 avaliações", "en": "5.0 on Google · 16 reviews"}

CATEGORIAS = {
    "clipe": {"pt": "Videoclipe", "en": "Music Video"},
    "comercial": {"pt": "Comercial", "en": "Commercial"},
    "institucional": {"pt": "Institucional", "en": "Institutional"},
}

EQUIPE = [
    {
        "slug": "germano",
        "fundador": True,
        "nome": "Germano Michelon Santos",
        "cargo": {"pt": "Colorista sênior e fundador", "en": "Senior Colorist & Founder"},
        "foto": "equipe/germano.jpg",
        "bio": {
            "pt": "Fundador da Vertigo Color, estúdio pelo qual já passaram marcas como Nike, Mercedes-Benz, Michelin e Natura. Assina a cor de videoclipes de artistas como Violet Orlandi e Spektra. Atende do estúdio em São Marcos (RS) clientes do Brasil, dos Estados Unidos, da Europa, da Arábia Saudita e da Índia.",
            "en": "Founder of Vertigo Color, the studio behind work for brands like Nike, Mercedes-Benz, Michelin and Natura. He has graded music videos for artists such as Violet Orlandi and Spektra. From the studio in southern Brazil he serves clients across Brazil, the United States, Europe, Saudi Arabia and India.",
        },
    },
    {
        "slug": "rafael-batista",
        "fundador": True,
        "nome": "Rafael Pereira Batista",
        "cargo": {"pt": "Colorista sênior e fundador", "en": "Senior Colorist & Founder"},
        "foto": "equipe/rafael-batista.jpg",
        "bio": {
            "pt": "Sócio-fundador da Vertigo Color, trouxe para a empresa mais de uma década de experiência em pós-produção — e o nome Vertigo Color junto.",
            "en": "Co-founder of Vertigo Color, he brought over a decade of post-production experience to the company — and the Vertigo Color name with it.",
        },
    },
    {
        "slug": "rafael",
        "nome": "Rafael de Deus",
        "cargo": {"pt": "Colorista", "en": "Colorist"},
        "foto": "equipe/rafael.jpg",
        "bio": {
            "pt": "Colorista da Vertigo, com olhar apurado para publicidade e conteúdo institucional.",
            "en": "Vertigo colorist with a sharp eye for advertising and institutional work.",
        },
    },
    {
        "slug": "deisy",
        "nome": "Deisy Araújo",
        "cargo": {"pt": "Colorista", "en": "Colorist"},
        "foto": "equipe/deisy.jpg",
        "bio": {
            "pt": "Colorista da Vertigo, assina trabalhos para artistas como Xamã e Antonia Morais.",
            "en": "Vertigo colorist whose credits include work for artists such as Xamã and Antonia Morais.",
        },
    },
    {
        "slug": "jana",
        "nome": "Jana Spínola",
        "cargo": {"pt": "Colorista", "en": "Colorist"},
        "foto": "equipe/jana.jpg",
        "bio": {
            "pt": "Colorista da Vertigo, com trabalhos para a cantora Violet Orlandi e para marcas internacionais como a Metagenics.",
            "en": "Vertigo colorist with credits for singer Violet Orlandi and international brands such as Metagenics.",
        },
    },
]

# ordem = ordem no portfólio; os 6 primeiros aparecem na home
PROJETOS = [
    {
        "slug": "dead-men-walk-alone",
        "titulo": "Dead Men Walk Alone",
        "cliente": "Violet Orlandi",
        "cat": "clipe",
        "colorista": "germano",
        "yt": "WIEzVr_BcgM",
        "publicado": "2024-08-13T06:00:28-07:00",
        "desc": {
            "pt": "Videoclipe gótico da cantora Violet Orlandi: veludo vinho, figuras encapuzadas e uma paleta que abraça o barroco sem perder a pele.",
            "en": "A gothic music video for singer Violet Orlandi: wine-red velvet, hooded figures and a palette that embraces the baroque without losing the skin tones.",
        },
        "creditos": [
            ("Artista / Artist", "Violet Orlandi"),
            ("Color", "Germano Michelon"),
        ],
        "n_galeria": 27,
    },
    {
        "slug": "puto-de-luxo",
        "titulo": "Puto de Luxo",
        "cliente": "Xamã",
        "cat": "clipe",
        "colorista": "deisy",
        "yt": "WhgDK3wDsyc",
        "publicado": "2022-11-29T07:00:10-08:00",
        "desc": {
            "pt": "Videoclipe do Xamã: couro preto, luz fria e contraste alto. Cor que sustenta a atitude do clipe do início ao fim.",
            "en": "A music video for Xamã: black leather, cold light and high contrast. Grading that carries the video's attitude from first frame to last.",
        },
        "creditos": [
            ("Artista / Artist", "Xamã"),
            ("Color", "Deisy Araújo"),
        ],
        "n_galeria": 1,
    },
    {
        "slug": "uceff",
        "titulo": "UCEFF",
        "cliente": "UCEFF",
        "cat": "institucional",
        "colorista": "germano",
        "vimeo": "939662059",
        "publicado": "2024-04-26",
        "desc": {
            "pt": "Filme institucional no alto de um heliponto ao nascer do sol: luz dourada, céu limpo e uma cidade inteira acordando ao fundo.",
            "en": "An institutional film on a helipad at sunrise: golden light, clean skies and a whole city waking up in the background.",
        },
        "creditos": [
            ("Cliente / Client", "UCEFF"),
            ("Color", "Germano Michelon"),
        ],
        "n_galeria": 21,
    },
    {
        "slug": "noug",
        "titulo": "Noug",
        "cliente": "Noug",
        "cat": "comercial",
        "colorista": "germano",
        "yt": "VGTqVr9rDbs",
        "publicado": "2024-03-23T13:20:20-07:00",
        "desc": {
            "pt": "Comercial de produto para a marca Noug: tons de areia, packshots limpos e uma tabela de cor construída para dar apetite.",
            "en": "Product commercial for Noug: sand tones, clean packshots and a color pipeline built to make the product irresistible.",
        },
        "creditos": [
            ("Cliente / Client", "Noug"),
            ("Color", "Germano Michelon"),
        ],
        "n_galeria": 10,
    },
    {
        "slug": "taro-blood-milk-and-sky",
        "titulo": "Taro / Blood, Milk and Sky",
        "cliente": "Violet Orlandi",
        "cat": "clipe",
        "colorista": "germano",
        "yt": "0ltQ3cdMEW8",
        "publicado": "2024-02-11T07:00:10-08:00",
        "desc": {
            "pt": "Mashup de Taro com Blood, Milk and Sky para a Violet Orlandi. Floresta, sangue e luz dura — um clipe onde a cor faz o papel de figurino.",
            "en": "A mashup of Taro and Blood, Milk and Sky for Violet Orlandi. Forest, blood and hard light — a video where color plays the role of wardrobe.",
        },
        "creditos": [
            ("Direção / Directed by", "Ricardo Gifford & Violet Orlandi"),
            ("Fotografia / Cinematography", "Daniel Freire"),
            ("Montagem / Edit", "Violet Orlandi & Guga Nascimento"),
            ("Color", "Germano Michelon"),
            ("Assistência de produção / Production Assistant", "Rafa Minerbo"),
            ("Sangue / Blood FX", "Luatiomi Makeup"),
        ],
        "n_galeria": 1,
    },
    {
        "slug": "unisc",
        "titulo": "UNISC — Comunidade",
        "cliente": "UNISC",
        "cat": "comercial",
        "colorista": "germano",
        "desc": {
            "pt": "Campanha da UNISC com dezenas de locações — obra, cozinha, piscina, hospital, biblioteca — e um desafio claro: fazer todas as luzes conversarem como um filme só.",
            "en": "A UNISC campaign across dozens of locations — construction site, kitchen, pool, hospital, library — with one clear challenge: making every light source speak the same language.",
        },
        "creditos": [
            ("Agência / Agency", "Sobe AE"),
            ("Direção / Direction", "Filipe Ferreira"),
            ("Direção de foto / Cinematography", "Luciano Paim"),
            ("Direção de arte e elenco / Art & Casting", "Luiza Scherer"),
            ("Produção / Production", "Renato Winckiewicz"),
            ("Assistência de câmera / Camera Assistant", "Lefosca"),
            ("Elétrica / Gaffer", "Evandro Zaka"),
            ("Make-up", "Monica Rizzetti"),
            ("Pós-produção / Post-production", "Brunno CG"),
            ("Color", "Germano Michelon"),
            ("Fotografia still / Stills", "Ale Siditadi"),
        ],
        "n_galeria": 16,
    },
    {
        "slug": "my-voice-for-you",
        "titulo": "My Voice for You",
        "cliente": "Spektra",
        "cat": "clipe",
        "colorista": "germano",
        "yt": "gkt3VPsZLfE",
        "publicado": "2024-07-12T06:00:06-07:00",
        "desc": {
            "pt": "Clipe em preto e branco para a banda Spektra. Sem cor para se esconder: aqui o trabalho é contraste, textura e densidade de prata.",
            "en": "A black-and-white music video for the band Spektra. Nowhere to hide without color: the work here is contrast, texture and silver density.",
        },
        "creditos": [
            ("Artista / Artist", "Spektra"),
            ("Direção / Directed by", "Thiago Kiss"),
            ("Color", "Germano Michelon"),
        ],
        "n_galeria": 16,
    },
    {
        "slug": "metagenics",
        "titulo": "Metagenics",
        "cliente": "Metagenics",
        "cat": "comercial",
        "colorista": "jana",
        "desc": {
            "pt": "Comercial de beleza e saúde sobre fundo preto: pele como protagonista absoluta, com uma cor precisa o bastante para aguentar close extremo.",
            "en": "A beauty and wellness commercial on pure black: skin as the absolute protagonist, with grading precise enough to survive extreme close-ups.",
        },
        "creditos": [
            ("Cliente / Client", "Metagenics"),
            ("Color", "Jana Spínola"),
        ],
        "n_galeria": 8,
    },
    {
        "slug": "call-me",
        "titulo": "Call Me (Blondie cover)",
        "cliente": "Violet Orlandi",
        "cat": "clipe",
        "colorista": "jana",
        "yt": "dyCRluZZCHs",
        "publicado": "2024-03-03T06:51:29-08:00",
        "desc": {
            "pt": "Cover acústico de Call Me, da Blondie, em preto e branco de estúdio — grão fino e cinzas com personalidade.",
            "en": "An acoustic cover of Blondie's Call Me in studio black-and-white — fine grain and grays with personality.",
        },
        "creditos": [
            ("Direção / Directed by", "Ricardo Gifford & Violet Orlandi"),
            ("Montagem / Edit", "Violet Orlandi"),
            ("Color", "Jana Spínola"),
            ("Produção / Produced by", "Ricardo Gifford"),
        ],
        "n_galeria": 3,
    },
    {
        "slug": "only-holy-water",
        "titulo": "Only Holy Water (Acoustic)",
        "cliente": "Violet Orlandi",
        "cat": "clipe",
        "colorista": "jana",
        "yt": "cjxyjiDIGuY",
        "publicado": "2024-02-25T10:00:08-08:00",
        "desc": {
            "pt": "Versão acústica em uma sala de outono: madeira, macieira e uma paleta quente de filme fotográfico.",
            "en": "An acoustic session in an autumn room: wood, an apple tree and a warm, film-stock palette.",
        },
        "creditos": [
            ("Direção / Directed by", "Ricardo Gifford & Violet Orlandi"),
            ("Montagem / Edit", "Violet Orlandi"),
            ("Color", "Jana Spínola"),
            ("Produção / Produced by", "Ricardo Gifford"),
        ],
        "n_galeria": 5,
    },
]

CLIENTES_LOGOS = ["nike", "mercedes", "michelin", "natura", "mounjaro", "rga",
                  "verizon", "chillibeans", "national"]
CLIENTES_ALT = {"nike": "Nike", "mercedes": "Mercedes-Benz", "michelin": "Michelin",
                "natura": "Natura", "verizon": "Verizon", "chillibeans": "Chilli Beans",
                "national": "National Geographic", "rga": "R/GA",
                "mounjaro": "Mounjaro"}

NOMES_FAMOSOS = "Ana Hickmann · Pocah · Leonardo · Cleo Pires · Antonia Morais · Xamã"

MOSAICO_N = 15

DEPOIMENTOS = [
    {
        "texto": {
            "pt": "Excelente! Nível técnico impecável, agilidade no pré-atendimento, durante e pós-entrega do trabalho. Meu próximo clipe será colorido por eles novamente.",
            "en": "Excellent! Impeccable technical level and fast responses before, during and after delivery. My next music video will be graded by them again.",
        },
        "autor": "Ale de Maria",
        "fonte": {"pt": "avaliação no Google", "en": "Google review"},
    },
    {
        "texto": {
            "pt": "Profissionais altamente qualificados e com alto senso artístico. A Vertigo tem colorizado filmes, publicidade e institucionais para nós com rapidez e muita qualidade.",
            "en": "Highly qualified professionals with a strong artistic sense. Vertigo has been grading films, advertising and institutional work for us with speed and great quality.",
        },
        "autor": "Filipe Ferreira",
        "fonte": {"pt": "avaliação no Google", "en": "Google review"},
    },
    {
        "texto": {
            "pt": "Qualidade indiscutível, difícil encontrar coloristas com essa qualidade!",
            "en": "Unquestionable quality — it's hard to find colorists at this level!",
        },
        "autor": "Carlos Damasceno",
        "fonte": {"pt": "cineasta, avaliação no Google", "en": "filmmaker, Google review"},
    },
]

SERVICOS = [
    {"pt": ("Color grading para cinema e série", "DI completo para longas, curtas e séries, do dailies ao master."),
     "en": ("Color grading for film & TV", "Full DI for features, shorts and series, from dailies to master.")},
    {"pt": ("Publicidade", "Comerciais e branded content com a consistência que a marca exige."),
     "en": ("Advertising", "Commercials and branded content with the consistency brands demand.")},
    {"pt": ("Videoclipe", "Looks autorais para artistas — do naturalista ao extremo."),
     "en": ("Music videos", "Signature looks for artists — from naturalistic to extreme.")},
    {"pt": ("Atendimento remoto", "Trabalhamos à distância: acertamos o look nas primeiras cenas e só seguimos depois da sua aprovação."),
     "en": ("Remote color grading", "We work in your timezone, lock the look on the first few scenes and only move on once you've signed off.")},
    {"pt": ("HDR e finalização", "Entrega em SDR, HDR e DCP, no padrão de cada janela de exibição."),
     "en": ("HDR & finishing", "SDR, HDR and DCP delivery, to the standard of every screen.")},
    {"pt": ("Look development", "Definição de look antes das filmagens, junto da direção e da fotografia."),
     "en": ("Look development", "Look design before the shoot, together with the director and DP.")},
]

SOBRE = {
    "pt": [
        "A Vertigo Color nasceu de uma obsessão singular pela imagem cinematográfica. Quando comecei a produzir meus próprios vídeos, a complexidade de luz, som e equipamento parecia infinita — mas o color grading fez sentido imediatamente. Incentivado por mentores como Filippo Cinotti, que provaram que uma carreira dedicada à cor era possível, investi tudo o que tinha em dominar o ofício.",
        "A virada veio ao unir forças com Rafael Pereira Batista, um sócio que trazia mais de uma década de pós-produção — e o nome Vertigo Color junto. Combinando dedicação obsessiva com experiência técnica profunda, construímos uma casa de pós-produção inteiramente em torno da arte e da ciência da cor.",
        "Hoje, a Vertigo é um dos estúdios de color grading mais procurados do Brasil — com foco global. Atendemos os Estados Unidos, a Europa, a Arábia Saudita e a Índia com o mesmo padrão, e operar a partir do Sul do país nos permite oferecer a esses mercados uma vantagem enorme: finalização de alto nível a um custo altamente competitivo, sem abrir mão de nenhum rigor.",
    ],
    "en": [
        "Vertigo Color was born from a singular obsession with the cinematic image. When I first set out to elevate my own productions, the endless complexities of lighting, sound and camera gear felt overwhelming — but color grading immediately clicked. Encouraged by industry mentors like Filippo Cinotti, who proved that a dedicated career in color was possible, I went all-in and invested everything I had into mastering the craft.",
        "The turning point came when I joined forces with Rafael Pereira Batista, a business partner who brought over a decade of post-production experience — and the name Vertigo Color with him. By combining obsessive dedication with deeply rooted technical expertise, we built a post-production house entirely around the art and science of the grade.",
        "Today, Vertigo stands as one of the most sought-after color grading studios in Brazil — with a global focus. We serve the United States, Europe, Saudi Arabia and India to the same standard, and operating from South America lets us offer those markets a massive advantage: world-class finishing at a highly competitive rate, with zero compromise on rigor.",
    ],
}

O2_TXT = {
    "pt": "Base em São Marcos, no Rio Grande do Sul, com atendimento remoto para qualquer lugar do mundo — hoje atendemos do Brasil aos Estados Unidos, Europa, Arábia Saudita e Índia. E quando o projeto pede presença no Rio de Janeiro, atendemos pela parceria com a O2, usando a infraestrutura deles.",
    "en": "Based in São Marcos, southern Brazil, working remotely worldwide — today we work with clients from Brazil to the United States, Europe, Saudi Arabia and India. And when a project calls for presence in Rio de Janeiro, we work through our partnership with O2, using their infrastructure.",
}

REUNIAO = {
    "pt": {
        "titulo": "Transforme seus vídeos em filmes",
        "sub": "Com color grading é possível transformar imagens comuns, de câmeras acessíveis, em filmes de altíssimo nível visual.",
        "blocos": [
            ("Câmera básica?", "Antes de julgar a sua câmera, tenha certeza de que está extraindo toda a qualidade que ela pode entregar."),
            ("Difícil se destacar?", "Um visual de qualidade é a forma mais óbvia de se destacar aos olhos do seu cliente — e especialistas em cada área elevam o resultado inteiro."),
            ("A luz mudou no meio do dia?", "Fazer takes diferentes conversarem como um filme só é a nossa especialidade."),
            ("Mais emoção", "Cada frame pode apoiar a história e conduzir a emoção de quem assiste."),
        ],
        "cta": "Chamar no WhatsApp",
        "cta_sub": "Reunião sem compromisso, direto com a Vertigo.",
    },
    "en": {
        "titulo": "Transform your videos into films",
        "sub": "Color grading can turn ordinary footage from accessible cameras into films with world-class visual quality.",
        "blocos": [
            ("Basic camera?", "Before blaming your camera, make sure you're extracting every bit of quality it can deliver."),
            ("Hard to stand out?", "A premium look is the most obvious way to stand out to your clients — and specialists in each craft raise the whole result."),
            ("Light changed mid-day?", "Making different takes speak as one film is our specialty."),
            ("More emotion", "Every frame can support the story and guide what the audience feels."),
        ],
        "cta": "Message us on WhatsApp",
        "cta_sub": "A no-strings meeting, straight with Vertigo.",
    },
}

# Endereços do site antigo (Squarespace) que continuam circulando em e-mails e buscadores.
# Caminho antigo -> (página em PT, página em EN, idioma principal). Vira uma página de
# redirecionamento em docs/; quem clica vai para o idioma do navegador ou o já escolhido.
_HOME = ("pt/index.html", "en/index.html", "pt")
_ENTRADA = ("", "", "pt")
_EQUIPE = ("pt/equipe.html", "en/team.html", "en")
_REUNIAO = ("pt/reuniao.html", "en/meeting.html", "pt")


def _projeto(slug):
    return (f"pt/projetos/{slug}.html", f"en/projects/{slug}.html", "pt")


REDIRECIONAMENTOS = {
    "home": _ENTRADA,
    "about-1": ("pt/sobre.html", "en/about.html", "en"),
    "artists": _EQUIPE,
    "contact": ("pt/contato.html", "en/contact.html", "en"),
    "amarcarreunioes": _REUNIAO,
    "amarcarreunioes-1": _REUNIAO,
    "amarcarreunioes-2": ("pt/reuniao.html", "en/meeting.html", "en"),
    "portflio-germano": _EQUIPE,
    "portflio-germano/project-one-f5w4d-yx6tr": _projeto("taro-blood-milk-and-sky"),
    "portflio-germano/noug-commercial": _projeto("noug"),
    "portflio-germano/uceff": _projeto("uceff"),
    "portflio-germano/my-voice-for-you-spektra": _projeto("my-voice-for-you"),
    "portflio-germano/dead-men-walk-alone-violet-orlandi": _projeto("dead-men-walk-alone"),
    "portflio-germano/cmercial-unisc": _projeto("unisc"),
    "portflio-deisy": _EQUIPE,
    "portflio-deisy/project-one-f5w4d-yta7g": _projeto("puto-de-luxo"),
    "portflio-jana": _EQUIPE,
    "portflio-jana/blondie-call-me-violet-orlandi-acoustic-cover": _projeto("call-me"),
    "portflio-jana/metagenics": _projeto("metagenics"),
    "portflio-jana/violet-orlandi-only-holy-water-acoustic": _projeto("only-holy-water"),
    # Blog e curso saíram do site; quando existir o site de educação, apontar para lá.
    "profissaocolorista": _HOME,
    "cadastro-vivendo-de-color-grading": _HOME,
    "newsletter": _HOME,
    "blog": _HOME,
    "blog/alm-da-letra-criando-videoclipes-que-ressonam-profundamente": _HOME,
    "blog/como-ser-um-freelancer-bem-sucedido-mesmo-sendo-tmido": _HOME,
    "blog/eleve-seu-preo-como-aumentar-o-valor-do-seu-trabalho-para-clientes-atuais": _HOME,
    "blog/freelancer-voc-no-precisa-ser-o-melhor": _HOME,
    "blog/fulano-consegue-fazer-por-menos": _HOME,
    "blog/guia-prtico-para-coloristas-passo-a-passo-para-color-grading-de-projetos": _HOME,
    "blog/kjzb6m6v30dki2kousczbb1l96oelf": _HOME,
    "blog/o-conhecimento-que-todo-editor-de-vdeo-deveria-ter-e-normalmente-no-tem": _HOME,
    "blog/o-seu-feed-est-te-deixando-pobre": _HOME,
    "blog/quando-o-projeto-vai-ficando-maior-ao-longo-da-execuo-guia-para-freelancers": _HOME,
    "blog/um-erro-sobre-dinheiro-que-muito-freelancer-comete": _HOME,
}

# Perguntas frequentes: só o que o Gê respondeu (03/11/2026). Os prazos já somam os 2 dias de
# conform que ele pediu. Nunca publicar valores. Agenda: falar da capacidade da equipe.
PERGUNTAS = {
    "pt": {
        "h1": "Perguntas frequentes",
        "rodape": "Perguntas frequentes",
        "titulo": "Perguntas frequentes sobre color grading — Vertigo Color",
        "desc": "Forma de cobrança, prazos e agenda: o que mais nos perguntam sobre color grading e colorização de filmes.",
        "chamada": "Como cobramos, prazos e agenda: veja as perguntas frequentes",
        "itens": [
            {"q": "Quanto custa o color grading de um projeto?",
             "a": "Depende do projeto. Normalmente cobramos por projeto, mas às vezes é por diária ou por minuto, dependendo do cliente. Conte como é o seu e mandamos o orçamento."},
            {"q": "Quanto tempo demora a colorização de um filme ou comercial?",
             "a": "Depende muito do projeto. Em média:",
             "lista": [("Comercial de 30 segundos", "3 dias"), ("Videoclipe", "5 a 6 dias"),
                       ("Curta-metragem", "17 dias"), ("Longa-metragem", "1 mês e 2 dias")],
             "nota": "Esses prazos já incluem cerca de 2 dias para receber o projeto do editor, fazer o conform e entregar."},
            {"q": "Vocês têm agenda para o meu projeto?",
             "a": "Normalmente, sim. Somos cinco coloristas, então um projeto novo não precisa esperar outro terminar. Mande a data de entrega e confirmamos."},
        ],
    },
    "en": {
        "h1": "Frequently asked questions",
        "rodape": "FAQ",
        "titulo": "Color grading FAQ — Vertigo Color",
        "desc": "How we charge, turnaround times and availability: the questions we hear most about color grading.",
        "chamada": "How we charge, turnaround and availability: see the FAQ",
        "itens": [
            {"q": "How much does color grading cost?",
             "a": "It depends on the project. We usually charge per project, but sometimes it's per day or per minute, depending on the client. Tell us about yours and we'll send you a quote."},
            {"q": "How long does color grading take?",
             "a": "It depends a lot on the project. On average:",
             "lista": [("30-second commercial", "3 days"), ("Music video", "5 to 6 days"),
                       ("Short film", "17 days"), ("Feature film", "1 month and 2 days")],
             "nota": "These times already include about 2 days to receive the project from the editor, conform it and deliver."},
            {"q": "Do you have availability for my project?",
             "a": "Usually, yes. There are five colorists on the team, so a new project doesn't have to wait for another one to finish. Send us your delivery date and we'll confirm."},
        ],
    },
}
