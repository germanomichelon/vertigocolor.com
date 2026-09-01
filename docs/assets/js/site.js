/* VERTIGO COLOR — interações. Vanilla JS, zero dependências. */
(function () {
  "use strict";

  // ajuda de captura/depuração: ?semanim desliga animações e carrega tudo;
  // ?y=2400 rola até a posição (?t=2400 desloca via transform, para painéis
  // que não processam rolagem)
  var q = location.search;
  var my = q.match(/[?&]y=(\d+)/);
  var mt = q.match(/[?&]t=(\d+)/);
  if (my || mt || /[?&]semanim/.test(q)) {
    document.documentElement.classList.add("sem-anim");
    document.addEventListener("DOMContentLoaded", function () {
      document.querySelectorAll("img[loading=lazy]").forEach(function (im) {
        im.loading = "eager";
      });
      if (mt) {
        // desloca só o conteúdo; a barra fixa continua no topo
        document.querySelectorAll("body > main, body > .rodape").forEach(function (el) {
          el.style.transform = "translateY(-" + mt[1] + "px)";
        });
      }
      if (my) {
        try { history.scrollRestoration = "manual"; } catch (e) {}
        window.scrollTo(0, parseInt(my[1], 10));
        setTimeout(function () { window.scrollTo(0, parseInt(my[1], 10)); }, 300);
      }
    });
  }

  var LANG_KEY = "vc-lang";

  function salvaIdioma(l) {
    try { localStorage.setItem(LANG_KEY, l); } catch (e) { /* modo privado */ }
  }

  // memoriza o idioma da página atual (páginas /pt/ e /en/ declaram data-lang no <html>)
  var lang = document.documentElement.getAttribute("data-lang");
  if (lang) salvaIdioma(lang);

  // troca de idioma explícita também memoriza
  document.addEventListener("click", function (ev) {
    var a = ev.target.closest("[data-set-lang]");
    if (a) salvaIdioma(a.getAttribute("data-set-lang"));
  });

  // ---------- nav ----------
  var nav = document.querySelector(".nav");
  if (nav) {
    var aoRolar = function () {
      nav.classList.toggle("solida", window.scrollY > 24);
    };
    aoRolar();
    window.addEventListener("scroll", aoRolar, { passive: true });
  }
  var burger = document.querySelector(".nav-burger");
  if (burger) {
    burger.addEventListener("click", function () {
      document.body.classList.toggle("menu-aberto");
    });
    document.querySelectorAll(".nav-links a").forEach(function (a) {
      a.addEventListener("click", function () {
        document.body.classList.remove("menu-aberto");
      });
    });
  }

  // ---------- reveal ao rolar ----------
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && reveals.length) {
    var io = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add("on");
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("on"); });
  }

  // ---------- filtros do portfólio ----------
  var filtros = document.querySelectorAll(".filtro");
  filtros.forEach(function (b) {
    b.addEventListener("click", function () {
      filtros.forEach(function (x) { x.classList.remove("ativo"); });
      b.classList.add("ativo");
      var f = b.getAttribute("data-f");
      document.querySelectorAll(".card[data-cat]").forEach(function (c) {
        c.classList.toggle("escondido", f !== "todos" && c.getAttribute("data-cat") !== f);
      });
    });
  });

  // ---------- vídeo: fachada -> iframe só no clique ----------
  document.querySelectorAll(".embed").forEach(function (em) {
    em.addEventListener("click", function () {
      if (em.querySelector("iframe")) return;
      var src = "";
      if (em.dataset.yt) {
        src = "https://www.youtube-nocookie.com/embed/" + em.dataset.yt + "?autoplay=1&rel=0";
      } else if (em.dataset.vimeo) {
        src = "https://player.vimeo.com/video/" + em.dataset.vimeo + "?autoplay=1&dnt=1";
      }
      if (!src) return;
      var f = document.createElement("iframe");
      f.src = src;
      f.allow = "autoplay; fullscreen; picture-in-picture; encrypted-media";
      f.allowFullscreen = true;
      em.appendChild(f);
    }, { once: false });
  });

  // ---------- lightbox da galeria ----------
  var lb = document.querySelector(".lightbox");
  if (lb) {
    var lbImg = lb.querySelector("img");
    document.querySelectorAll(".galeria img").forEach(function (img) {
      img.addEventListener("click", function () {
        lbImg.src = img.currentSrc || img.src;
        lb.classList.add("aberta");
      });
    });
    lb.addEventListener("click", function () { lb.classList.remove("aberta"); });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") lb.classList.remove("aberta");
    });
  }

  // ---------- marquee: duplica a trilha para loop contínuo ----------
  document.querySelectorAll(".marquee-track").forEach(function (t) {
    t.innerHTML += t.innerHTML;
  });
})();
