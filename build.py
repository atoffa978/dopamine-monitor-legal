#!/usr/bin/env python3
"""
Rebuild delle pagine HTML del sito dopamine-monitor-legal a partire dai .md
sorgente presenti accanto a questo script.

Requisiti:
    pip install markdown

Uso:
    python3 build.py

Output: rigenera privacy.html, terms.html (e lascia index.html, 404.html, .md
intatti, dato che sono mantenuti a mano).
"""
import markdown
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
SRC_PRIVACY = ROOT / "PRIVACY_POLICY.md"
SRC_TERMS = ROOT / "TERMS_OF_USE.md"

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
hr { border: none; border-top: 1px solid var(--rule); margin: 2em 0; }
.foot {
  margin-top: 56px; padding-top: 20px; border-top: 1px solid var(--rule);
  color: var(--muted); font-size: 0.85rem;
}
"""

PAGE_TMPL = """<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="index, follow">
<title>{title} — Dopamine Monitor</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://atoffa978.github.io/dopamine-monitor-legal/{canon}">
<style>{css}</style>
</head>
<body>
<div class="wrap">
<header class="top">
  <div class="brand"><a href="./" style="color:inherit;text-decoration:none">Dopamine Monitor</a></div>
  <nav>
    <a href="./">Indice</a>
    <a href="./privacy.html">Privacy</a>
    <a href="./terms.html">Termini</a>
  </nav>
</header>
<main>
{body}
</main>
<footer class="foot">
  Documento autoritativo in italiano. Versione raw: <a href="{raw}">{raw}</a>.<br>
  Contatti: <a href="mailto:dopamine.monitor.dev@gmail.com">dopamine.monitor.dev@gmail.com</a>
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

def build_page(src: Path, out_name: str, title: str, desc: str, raw_name: str):
    body = md_to_html(src)
    html = PAGE_TMPL.format(
        title=title, desc=desc, canon=out_name, css=CSS, body=body, raw=raw_name
    )
    (ROOT / out_name).write_text(html, encoding="utf-8")
    print(f"Wrote {out_name}")

def main():
    build_page(
        SRC_PRIVACY, "privacy.html",
        "Privacy Policy",
        "Privacy Policy di Dopamine Monitor — quali dati restano sul dispositivo, quali (solo con consenso) sono inviati a server UE, diritti GDPR.",
        "PRIVACY_POLICY.md",
    )
    build_page(
        SRC_TERMS, "terms.html",
        "Termini d'uso",
        "Termini d'uso di Dopamine Monitor — cos'è l'app, limitazioni del modello BLI, responsabilità, legge applicabile.",
        "TERMS_OF_USE.md",
    )

if __name__ == "__main__":
    main()
