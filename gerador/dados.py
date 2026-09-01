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

CATEGORIAS = {
    "clipe": {"pt": "Videoclipe", "en": "Music Video"},
    "comercial": {"pt": "Comercial", "en": "Commercial"},
    "institucional": {"pt": "Institucional", "en": "Institutional"},
}

EQUIPE = [
    {
        "slug": "germano",
        "nome": "Germano Michelon Santos",
        "cargo": {"pt": "Colorista sênior e fundador", "en": "Senior Colorist & Founder"},
        "foto": "equipe/germano.jpg",
        "bio": {
            "pt": "Fundador da Vertigo Color, coloriu projetos para marcas como Nike, Mercedes-Benz, Michelin e Natura, além de videoclipes com milhões de visualizações. Atende do estúdio em São Marcos (RS) clientes do Brasil, dos Estados Unidos, da Europa, da Arábia Saudita e da Índia.",
            "en": "Founder of Vertigo Color, Germano has graded work for brands like Nike, Mercedes-Benz, Michelin and Natura, plus music videos with millions of views. From the studio in southern Brazil he serves clients across Brazil, the United States, Europe, Saudi Arabia and India.",
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
        "desc": {
            "pt": "Xamã sobre andaimes, neon rosa contra o entardecer do Rio. Cor que sustenta a atitude do clipe do início ao fim.",
            "en": "Xamã on scaffolding, pink neon against a Rio sunset. Grading that carries the video's attitude from first frame to last.",
        },
        "creditos": [
            ("Artista / Artist", "Xamã"),
            ("Color", "Deisy Araújo"),
        ],
        "n_galeria": 2,
    },
    {
        "slug": "uceff",
        "titulo": "UCEFF",
        "cliente": "UCEFF",
        "cat": "institucional",
        "colorista": "germano",
        "vimeo": "939662059",
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

CLIENTES_LOGOS = ["nike", "mercedes", "michelin", "natura", "lilly", "rga",
                  "verizon", "chillibeans", "national"]
CLIENTES_ALT = {"nike": "Nike", "mercedes": "Mercedes-Benz", "michelin": "Michelin",
                "natura": "Natura", "verizon": "Verizon", "chillibeans": "Chilli Beans",
                "national": "National Geographic", "lilly": "Eli Lilly", "rga": "R/GA"}

NOMES_FAMOSOS = "Ana Hickmann · Pocah · Leonardo · Cleo Pires · Antonia Morais · Xamã"

MOSAICO_N = 14

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
    {"pt": ("Sessão remota ao vivo", "Você acompanha e aprova em tempo real, de onde estiver."),
     "en": ("Live remote sessions", "Watch and approve in real time, wherever you are.")},
    {"pt": ("HDR e finalização", "Entrega em SDR, HDR e DCP, no padrão de cada janela de exibição."),
     "en": ("HDR & finishing", "SDR, HDR and DCP delivery, to the standard of every screen.")},
    {"pt": ("Look development", "Definição de look antes das filmagens, junto da direção e da fotografia."),
     "en": ("Look development", "Look design before the shoot, together with the director and DP.")},
]

SOBRE = {
    "pt": [
        "A Vertigo Color nasceu de uma obsessão singular pela imagem cinematográfica. Quando comecei a produzir meus próprios vídeos, a complexidade de luz, som e equipamento parecia infinita — mas o color grading fez sentido imediatamente. Incentivado por mentores como Filippo Cinotti, que provaram que uma carreira dedicada à cor era possível, investi tudo o que tinha em dominar o ofício.",
        "A virada veio ao unir forças com um sócio que trazia mais de uma década de pós-produção — e o nome Vertigo Color junto. Combinando dedicação obsessiva com experiência técnica profunda, construímos uma casa de pós-produção inteiramente em torno da arte e da ciência da cor.",
        "Hoje, a Vertigo é um dos estúdios de color grading mais procurados do Brasil — com foco global. Atendemos os Estados Unidos, a Europa, a Arábia Saudita e a Índia com o mesmo padrão, e operar a partir do Sul do país nos permite oferecer a esses mercados uma vantagem enorme: finalização de alto nível a um custo altamente competitivo, sem abrir mão de nenhum rigor.",
    ],
    "en": [
        "Vertigo Color was born from a singular obsession with the cinematic image. When I first set out to elevate my own productions, the endless complexities of lighting, sound and camera gear felt overwhelming — but color grading immediately clicked. Encouraged by industry mentors like Filippo Cinotti, who proved that a dedicated career in color was possible, I went all-in and invested everything I had into mastering the craft.",
        "The turning point came when I joined forces with a business partner who brought over a decade of post-production experience — and the name Vertigo Color with him. By combining obsessive dedication with deeply rooted technical expertise, we built a post-production house entirely around the art and science of the grade.",
        "Today, Vertigo stands as one of the most sought-after color grading studios in Brazil — with a global focus. We serve the United States, Europe, Saudi Arabia and India to the same standard, and operating from southern Brazil lets us offer those markets a massive advantage: world-class finishing at a highly competitive rate, with zero compromise on rigor.",
    ],
}

O2_TXT = {
    "pt": "Base em São Marcos, no Rio Grande do Sul, com sessões remotas ao vivo para qualquer lugar do mundo — hoje atendemos do Brasil aos Estados Unidos, Europa, Arábia Saudita e Índia. E quando o projeto pede presença no Rio de Janeiro, atendemos pela parceria com a O2, usando a infraestrutura deles.",
    "en": "Based in São Marcos, southern Brazil, with live remote sessions available worldwide — today we work with clients from Brazil to the United States, Europe, Saudi Arabia and India. And when a project calls for presence in Rio de Janeiro, we work through our partnership with O2, using their infrastructure.",
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
