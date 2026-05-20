#!/usr/bin/env python3
"""
Rebuild delle pagine HTML del sito dopamine-monitor-legal a partire dai .md
sorgente presenti accanto a questo script.

Bilingue IT/EN (M5):
  - PRIVACY_POLICY.md       -> privacy.html       (it)
  - PRIVACY_POLICY_EN.md    -> privacy-en.html    (en)
  - TERMS_OF_USE.md         -> terms.html         (it)
  - TERMS_OF_USE_EN.md      -> terms-en.html      (en)

L'italiano resta la lingua autoritativa per dispute legali. La versione
EN porta in chiaro una nota "Italian version prevails" sotto il titolo.

Requisiti:
    pip install markdown

Uso:
    python3 build.py

Output: rigenera 4 file .html. Lascia index.html, 404.html, .md intatti.
"""
import markdown
from pathlib import Path

ROOT = Path(__file__).parent.resolve()

CSS = """
:root {
  color-scheme: light dark;
  --bg: #ffffff;
  --fg: #1a1a1a;
  --muted: #5a5a5a;
  --rule: #e4e4e4;
  --accent: #1f6feb;
  --code-bg: #f5f5f5;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #15171a;
    --fg: #e8e8e8;
    --muted: #9a9a9a;
    --rule: #2a2d31;
    --accent: #58a6ff;
    --code-bg: #1f2227;
  }
}
* { box-sizing: border-box; }
html, body {
  margin: 0; padding: 0;
  background: var(--bg); color: var(--fg);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
               "Helvetica Neue", Arial, sans-serif;
  font-size: 16px; line-height: 1.55;
}
.wrap { max-width: 720px; margin: 0 auto; padding: 24px 20px 64px; }
.top {
  display: flex; align-items: center; justify-content: space-between;
  padding-bottom: 20px; border-bottom: 1px solid var(--rule);
  margin-bottom: 28px; flex-wrap: wrap; gap: 12px;
}
.top .brand { font-weight: 600; font-size: 1.05rem; letter-spacing: -0.01em; }
.top nav a { margin-left: 16px; color: var(--muted); text-decoration: none; font-size: 0.95rem; }
.top nav a:hover { color: var(--accent); }
.top nav .lang { margin-left: 16px; font-size: 0.85rem; letter-spacing: 0.04em; }
.top nav .lang .active { color: var(--fg); font-weight: 600; }
h1 { font-size: 1.7rem; line-height: 1.25; margin: 0 0 8px; letter-spacing: -0.02em; }
h2 { font-size: 1.25rem; margin-top: 2.2em; letter-spacing: -0.01em; }
h3 { font-size: 1.05rem; margin-top: 1.6em; }
p, li { font-size: 1rem; }
a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }
table { border-collapse: collapse; width: 100%; margin: 1em 0; font-size: 0.95rem; }
th, td { border: 1px solid var(--rule); padding: 8px 10px; text-align: left; vertical-align: top; }
th { background: var(--code-bg); font-weight: 600; }
code { background: var(--code-bg); padding: 1px 5px; border-radius: 3px;
  font-size: 0.9em; font-family: ui-monospace, "SF Mono", Menlo, Consolas, monospace; }
blockquote {
  border-left: 3px solid var(--accent);
  margin: 1.2em 0;
  padding: 0.4em 0 0.4em 1em;
  color: var(--muted);
  font-size: 0.95rem;
}
hr { border: none; border-top: 1px solid var(--rule); margin: 2em 0; }
.foot {
  margin-top: 56px; padding-top: 20px; border-top: 1px solid var(--rule);
  color: var(--muted); font-size: 0.85rem;
}
"""

# Etichette nav, per lingua. Lasciamo i path relativi così funziona sia in dev
# locale (file://) sia in produzione (github.io).
LABELS = {
    "it": {
        "nav_index":   ("./",              "Indice"),
        "nav_privacy": ("./privacy.html",  "Privacy"),
        "nav_terms":   ("./terms.html",    "Termini"),
        "lang_it_url": "./",
        "lang_en_url": "./index-en.html",  # creato a parte se serve; per ora i toggle pagina-pagina
        "footer": (
            "Documento autoritativo in italiano. "
            "Versione raw: <a href=\"{raw}\">{raw}</a>.<br>"
            "Contatti: <a href=\"mailto:dopamine.monitor.dev@gmail.com\">"
            "dopamine.monitor.dev@gmail.com</a>"
        ),
        "title_suffix": "— Dopamine Monitor",
    },
    "en": {
        "nav_index":   ("./",                 "Index"),
        "nav_privacy": ("./privacy-en.html",  "Privacy"),
        "nav_terms":   ("./terms-en.html",    "Terms"),
        "lang_it_url": "./",
        "lang_en_url": "./index-en.html",
        "footer": (
            "Authoritative document in Italian. "
            "Raw version: <a href=\"{raw}\">{raw}</a>.<br>"
            "Contact: <a href=\"mailto:dopamine.monitor.dev@gmail.com\">"
            "dopamine.monitor.dev@gmail.com</a>"
        ),
        "title_suffix": "— Dopamine Monitor",
    },
}

# Mapping pagina IT <-> EN per il toggle lingua.
PAGE_TWIN = {
    "privacy.html":    "privacy-en.html",
    "privacy-en.html": "privacy.html",
    "terms.html":      "terms-en.html",
    "terms-en.html":   "terms.html",
}

PAGE_TMPL = """<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="index, follow">
<title>{title} {title_suffix}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://atoffa978.github.io/dopamine-monitor-legal/{canon}">
<link rel="alternate" hreflang="{lang}" href="https://atoffa978.github.io/dopamine-monitor-legal/{canon}">
<link rel="alternate" hreflang="{other_lang}" href="https://atoffa978.github.io/dopamine-monitor-legal/{twin}">
<style>{css}</style>
</head>
<body>
<div class="wrap">
<header class="top">
  <div class="brand"><a href="./" style="color:inherit;text-decoration:none">Dopamine Monitor</a></div>
  <nav>
    <a href="{nav_idx_url}">{nav_idx_label}</a>
    <a href="{nav_priv_url}">{nav_priv_label}</a>
    <a href="{nav_terms_url}">{nav_terms_label}</a>
    <span class="lang">
      <a href="{twin_it}" class="{cls_it}">IT</a>
      <span style="color:var(--rule)"> | </span>
      <a href="{twin_en}" class="{cls_en}">EN</a>
    </span>
  </nav>
</header>
<main>
{body}
</main>
<footer class="foot">
  {footer}
</footer>
</div>
</body>
</html>
"""

def md_to_html(src: Path) -> str:
    return markdown.markdown(
        src.read_text(encoding="utf-8"),
        extensions=["tables", "fenced_code", "sane_lists"],
        output_format="html5",
    )

def build_page(src: Path, out_name: str, title: str, desc: str,
               raw_name: str, lang: str):
    body = md_to_html(src)
    labels = LABELS[lang]
    other = "en" if lang == "it" else "it"
    twin = PAGE_TWIN[out_name]
    # Per il toggle: se la pagina è IT, "IT" è attivo e linka a se stessa,
    # "EN" linka al twin. E viceversa.
    if lang == "it":
        twin_it, twin_en = out_name, twin
        cls_it, cls_en = "active", ""
    else:
        twin_it, twin_en = twin, out_name
        cls_it, cls_en = "", "active"
    nav_idx_url,   nav_idx_label   = labels["nav_index"]
    nav_priv_url,  nav_priv_label  = labels["nav_privacy"]
    nav_terms_url, nav_terms_label = labels["nav_terms"]
    footer = labels["footer"].format(raw=raw_name)
    html = PAGE_TMPL.format(
        lang=lang, other_lang=other,
        title=title, title_suffix=labels["title_suffix"], desc=desc,
        canon=out_name, twin=twin, css=CSS, body=body, footer=footer,
        nav_idx_url=nav_idx_url, nav_idx_label=nav_idx_label,
        nav_priv_url=nav_priv_url, nav_priv_label=nav_priv_label,
        nav_terms_url=nav_terms_url, nav_terms_label=nav_terms_label,
        twin_it=twin_it, twin_en=twin_en, cls_it=cls_it, cls_en=cls_en,
    )
    (ROOT / out_name).write_text(html, encoding="utf-8")
    print(f"Wrote {out_name}")

def main():
    # IT
    build_page(
        ROOT / "PRIVACY_POLICY.md", "privacy.html",
        "Privacy Policy",
        "Privacy Policy di Dopamine Monitor — quali dati restano sul dispositivo, quali (solo con consenso) sono inviati a server UE, diritti GDPR.",
        "PRIVACY_POLICY.md", "it",
    )
    build_page(
        ROOT / "TERMS_OF_USE.md", "terms.html",
        "Termini d'uso",
        "Termini d'uso di Dopamine Monitor — cos'è l'app, limitazioni del modello, responsabilità, legge applicabile.",
        "TERMS_OF_USE.md", "it",
    )
    # EN
    build_page(
        ROOT / "PRIVACY_POLICY_EN.md", "privacy-en.html",
        "Privacy Policy",
        "Dopamine Monitor's Privacy Policy — what data stays on the device, what is sent (only with explicit consent) to EU servers, GDPR rights.",
        "PRIVACY_POLICY_EN.md", "en",
    )
    build_page(
        ROOT / "TERMS_OF_USE_EN.md", "terms-en.html",
        "Terms of Use",
        "Dopamine Monitor's Terms of Use — what the app is, model limitations, liability, governing law.",
        "TERMS_OF_USE_EN.md", "en",
    )

if __name__ == "__main__":
    main()
