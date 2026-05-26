#!/usr/bin/env python3
"""
build.py · Marketplace SMC Banco · sistema build híbrido

Funcionalidades:
1. Reemplaza tokens {{VAR}} en HTMLs existentes con valores de config.json
2. Convierte .md nuevos (en docs/) a HTML branded usando template
3. Output: HTMLs actualizados en raíz del repo (servidos por GitHub Pages)

Uso:
   python3 build.py           # build completo
   python3 build.py --check   # solo valida tokens · no escribe
"""

import json
import re
import sys
import os
from pathlib import Path

ROOT     = Path(__file__).parent
CONFIG   = ROOT / "config.json"
DOCS_MD  = ROOT / "docs"
TEMPLATE = ROOT / "_template.html"

TOKEN_RE = re.compile(r"\{\{(\w+)\}\}")


def load_config():
    with open(CONFIG, encoding="utf-8") as f:
        return {k: v for k, v in json.load(f).items() if not k.startswith("_")}


def replace_tokens(content, config):
    """Reemplaza {{TOKEN}} con valor · reporta tokens no encontrados."""
    missing = set()

    def sub(m):
        key = m.group(1)
        if key in config:
            return config[key]
        missing.add(key)
        return m.group(0)

    out = TOKEN_RE.sub(sub, content)
    return out, missing


def process_html(path, config):
    """Aplica tokens en un HTML existente."""
    src = path.read_text(encoding="utf-8")
    out, missing = replace_tokens(src, config)
    if missing:
        print(f"   ⚠️  {path.name}: tokens sin valor: {', '.join(sorted(missing))}")
    if out != src:
        path.write_text(out, encoding="utf-8")
        return True
    return False


def main():
    if not CONFIG.exists():
        print(f"❌ Falta {CONFIG}")
        sys.exit(1)

    config = load_config()
    print(f"📋 Config cargado · {len(config)} variables")

    check_only = "--check" in sys.argv

    # 1. HTMLs existentes en raíz
    html_files = sorted(ROOT.glob("*.html"))
    changed = 0
    for h in html_files:
        if "_template" in h.name:
            continue
        if check_only:
            src = h.read_text(encoding="utf-8")
            out, missing = replace_tokens(src, config)
            if missing:
                print(f"   ⚠️  {h.name}: {len(missing)} tokens sin valor")
        else:
            if process_html(h, config):
                changed += 1
                print(f"   ✓ {h.name} (tokens reemplazados)")

    print(f"\n📊 HTMLs actualizados: {changed} de {len(html_files)}")

    # 2. Markdown files en docs/ (opcional · fase 2)
    if DOCS_MD.exists():
        md_files = list(DOCS_MD.glob("*.md"))
        if md_files:
            print(f"\n📝 Markdown files detectados: {len(md_files)}")
            print("   ℹ️  Conversión MD → HTML aún no implementada (fase 2)")
            print("   Por ahora: editá HTMLs directamente con tokens {{VAR}}")
            for m in md_files:
                print(f"      · {m.name}")

    print("\n✅ Build completado")


if __name__ == "__main__":
    main()
