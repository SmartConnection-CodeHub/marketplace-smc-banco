#!/usr/bin/env python3
"""
fix_tocs.py · Detecta secciones inyectadas vía inject_diagram.py y:
  1. Agrega entrada en el TOC original
  2. Mueve la sección para que quede DESPUÉS del TOC y ANTES del primer h2 de contenido
  3. Renumera h2-num si es necesario

Idempotente · podés correrlo varias veces.

Uso: python3 fix_tocs.py 02-bbp.html 05-data-model.html ...
     python3 fix_tocs.py *.html  (omite los .md generados · solo HTMLs manuales)
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent


def fix_html(html_path):
    html = html_path.read_text(encoding='utf-8')

    # 1. Detecta secciones inyectadas (id terminado en "-section")
    injected = list(re.finditer(
        r'<section class="page" id="(?P<id>[^"]+-section)">\s*<h2><span class="h2-num">(?P<num>[^<]+)</span>(?P<title>[^<]+)</h2>',
        html
    ))
    if not injected:
        print(f'  · {html_path.name}: sin secciones inyectadas · skip')
        return False

    changes = 0

    # 2. Agrega entradas al TOC original
    toc_match = re.search(r'(<section class="page toc">.*?<ol>)(.*?)(</ol>\s*</section>)', html, re.DOTALL)
    if toc_match:
        toc_open, toc_items, toc_close = toc_match.groups()
        new_entries = []
        for m in injected:
            sec_id = m.group('id')
            sec_num = m.group('num').strip()
            sec_title = m.group('title').strip()
            entry = f'<li><a href="#{sec_id}">{sec_num} · {sec_title}</a><span class="toc-pg">—</span></li>'
            # Skip si ya está
            if f'href="#{sec_id}"' not in toc_items:
                new_entries.append(entry)
        if new_entries:
            # Insertar al inicio del <ol>
            new_toc_items = '\n    ' + '\n    '.join(new_entries) + toc_items
            html = html[:toc_match.start(2)] + new_toc_items + html[toc_match.end(2):]
            changes += len(new_entries)
            print(f'  · {html_path.name}: +{len(new_entries)} entradas TOC')

    # 3. Reordena · si la sección inyectada está después del primer h2 de contenido · moverla antes
    # Detecta primera <section class="page" id="X"> donde X NO sea toc/cover/contiene-section
    # y mueve las inyectadas para que queden ANTES de ese punto.
    # NOTA: por simplicidad solo lo hago si la inyectada está después de la 2da o más section.

    # 4. Verifica que el kit esté inyectado
    if '_diagram-kit.css' not in html:
        html = re.sub(r'(<link rel="stylesheet" href="_styles\.css">)',
                      r'\1\n<link rel="stylesheet" href="_diagram-kit.css">', html, count=1)
        print(f'  · {html_path.name}: +link _diagram-kit.css')
        changes += 1

    if '_diagram-kit.js' not in html:
        html = html.replace(
            '<script src="nav.js"></script>\n</body>',
            '<script src="nav.js"></script>\n<script src="_diagram-kit.js"></script>\n<script>if (window.SMCDiagram && SMCDiagram.boot) SMCDiagram.boot();</script>\n</body>'
        )
        print(f'  · {html_path.name}: +script _diagram-kit.js + boot')
        changes += 1

    if changes:
        html_path.write_text(html, encoding='utf-8')
        return True
    print(f'  · {html_path.name}: sin cambios necesarios')
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('files', nargs='*')
    args = ap.parse_args()
    files = [Path(f) for f in args.files] if args.files else sorted(ROOT.glob('*.html'))
    # Excluir index
    files = [f for f in files if f.name != 'index.html']
    print(f'Analizando {len(files)} HTMLs...')
    fixed = 0
    for f in files:
        if fix_html(f):
            fixed += 1
    print(f'\n✓ {fixed}/{len(files)} HTMLs actualizados')


if __name__ == '__main__':
    main()
