#!/usr/bin/env python3
"""
html_to_md.py · reverse engineer HTML del banco → markdown source (v0.2)

Extrae frontmatter (cover meta) + secciones (h2.h2-num) + cuerpo
desde HTMLs generados manualmente · genera .md con esqueleto editable.

⚠️ LIMITACIÓN CONOCIDA:
   create_doc.py envuelve CADA línea no-markdown en <p>...</p>. Eso rompe
   tablas y SVGs HTML inline si se intenta regenerar el HTML desde el .md.

   FLUJO ESCALABLE REAL:
   1) Para docs NUEVOS del banco · escribir .md con markdown puro (texto,
      listas, tablas pipe `| col |`, callouts `> [!tipo]`, sidecars JSON
      para diagramas) → create_doc.py --apply genera HTML fielmente.
   2) Para docs LEGACY con SVG/tabla custom inline · usar este script para
      generar .md como REFERENCIA DOCUMENTAL · editar HTML directo.

   El .md generado por este script sirve para:
   - Tener una fuente editable de texto plano (review · diff · search)
   - Documentar la estructura de cada doc
   - Punto de partida si se decide reescribir el doc en markdown puro

Uso:
   python3 html_to_md.py 01-vision.html
   python3 html_to_md.py *.html --skip-existing
"""

import argparse
import re
import sys
from pathlib import Path
from html.parser import HTMLParser


ROOT = Path(__file__).parent
DOCS_DIR = ROOT / 'docs'


# ============================================================
# EXTRACCIÓN
# ============================================================

def get_first_match(pattern, html, flags=re.DOTALL, default=''):
    m = re.search(pattern, html, flags)
    return m.group(1).strip() if m else default


def extract_frontmatter(html, file_stem):
    """Extrae metadata del cover · devuelve dict para frontmatter YAML."""
    title = get_first_match(r'<h1 class="cover-title">(.*?)</h1>', html)
    subtitle = get_first_match(r'<p class="cover-subtitle">(.*?)</p>', html)
    doc_num = get_first_match(r'<div class="cover-doc-num">(.*?)</div>', html)

    # cover-meta-item con label/value pares
    meta_items = re.findall(
        r'<div class="cover-meta-label">(.*?)</div>\s*<div class="cover-meta-value">(.*?)</div>',
        html, re.DOTALL,
    )
    meta_map = {k.strip().lower(): v.strip() for k, v in meta_items}

    # Nav prev / next (primer nav.doc-nav del top)
    nav_match = re.search(
        r'<nav class="doc-nav"><a href="([^"]+)">.*?<a href="([^"]+)">',
        html, re.DOTALL,
    )
    prev_href = nav_match.group(1) if nav_match else 'index.html'
    next_href = nav_match.group(2) if nav_match else 'index.html'

    # number e id desde file_stem (ej: 01-vision)
    parts = file_stem.split('-', 1)
    number = parts[0] if parts and parts[0].isdigit() else ''
    doc_id = parts[1] if len(parts) > 1 else file_stem

    # Block: extraído del page-footer · primer span del primer footer
    block = get_first_match(
        r'<div class="page-footer"><span>([^<·]+)·?\s*([^<]*)</span>',
        html, default='',
    )

    return {
        'number': number,
        'id': doc_id,
        'title': title,
        'subtitle': subtitle,
        'block': block.strip() or 'Marketplace SMC',
        'author': meta_map.get('autor', 'SMC Team'),
        'version': meta_map.get('versión') or meta_map.get('version', '1.0'),
        'date': meta_map.get('fecha') or meta_map.get('date', '2026-05-26'),
        'status': meta_map.get('status', '🟢 Activo'),
        'prev': prev_href,
        'next': next_href,
    }


def extract_sections(html):
    """Extrae todas las <section class='page' id='...'> excepto cover y toc."""
    pattern = re.compile(
        r'<section class="page"[^>]*id="([^"]+)"[^>]*>(.*?)</section>',
        re.DOTALL,
    )
    return pattern.findall(html)


# ============================================================
# CONVERSIÓN HTML → MARKDOWN
# ============================================================

def section_to_md(section_id, section_html):
    """Convierte una <section> a bloque markdown `# NN · Title` + body."""
    # Extraer h2 con h2-num
    h2_match = re.search(
        r'<h2><span class="h2-num">(\d+)</span>([^<]+)</h2>',
        section_html,
    )
    if h2_match:
        num = h2_match.group(1)
        title = h2_match.group(2).strip()
        header = f'# {num} · {title}'
        body = section_html[h2_match.end():]
    else:
        # h2 sin h2-num
        h2_simple = re.search(r'<h2>([^<]+)</h2>', section_html)
        if h2_simple:
            header = f'# {h2_simple.group(1).strip()}'
            body = section_html[h2_simple.end():]
        else:
            header = f'# {section_id}'
            body = section_html

    # Limpiar page-footer del body
    body = re.sub(r'<div class="page-footer">.*?</div>', '', body, flags=re.DOTALL)

    # Convertir HTML simple a markdown
    body_md = html_to_md(body).strip()

    return f'{header}\n\n{body_md}\n'


def html_to_md(s):
    """Conversión HTML → markdown best-effort."""
    # Párrafos
    s = re.sub(r'<p>(.*?)</p>', lambda m: '\n' + clean_inline(m.group(1)) + '\n', s, flags=re.DOTALL)

    # Listas
    s = re.sub(r'<ul>(.*?)</ul>', convert_list, s, flags=re.DOTALL)
    s = re.sub(r'<ol>(.*?)</ol>', lambda m: convert_list(m, ordered=True), s, flags=re.DOTALL)

    # Headers nivel 3-4
    s = re.sub(r'<h3>([^<]+)</h3>', r'\n## \1\n', s)
    s = re.sub(r'<h4>([^<]+)</h4>', r'\n### \1\n', s)

    # Bloques div.box → callouts markdown
    s = convert_callouts(s)

    # Tablas: dejar como HTML raw (markdown soporta HTML inline)
    # Las complejas con clases custom van mejor así

    # Inline cleanup
    s = clean_inline(s)

    # Compactar líneas vacías múltiples
    s = re.sub(r'\n{3,}', '\n\n', s)
    return s.strip()


def convert_list(match, ordered=False):
    inner = match.group(1)
    items = re.findall(r'<li>(.*?)</li>', inner, re.DOTALL)
    prefix = '1.' if ordered else '-'
    return '\n' + '\n'.join(f'{prefix} {clean_inline(it)}' for it in items) + '\n'


def convert_callouts(s):
    """div.box.box-XXX → > [!XXX] title\n> body."""
    pattern = re.compile(
        r'<div class="box box-([^"]+)"><div class="box-title">([^<]+)</div>(.*?)</div>',
        re.DOTALL,
    )

    def repl(m):
        kind = m.group(1)
        title = m.group(2).strip()
        body = clean_inline(re.sub(r'<p>(.*?)</p>', r'\1\n', m.group(3), flags=re.DOTALL).strip())
        body_lines = '\n'.join(f'> {l}' for l in body.split('\n'))
        return f'\n> [!{kind}] {title}\n{body_lines}\n'

    return pattern.sub(repl, s)


def clean_inline(s):
    s = re.sub(r'<strong>(.*?)</strong>', r'**\1**', s)
    s = re.sub(r'<em>(.*?)</em>', r'*\1*', s)
    s = re.sub(r'<code>(.*?)</code>', r'`\1`', s)
    s = re.sub(r'<a href="([^"]+)">([^<]+)</a>', r'[\2](\1)', s)
    s = re.sub(r'<br\s*/?>', '\n', s)
    # Limpiar tags vacíos restantes solo si son inline simples
    return s.strip()


# ============================================================
# MAIN
# ============================================================

def yaml_frontmatter(meta):
    lines = ['---']
    order = ['number', 'id', 'title', 'subtitle', 'block', 'author',
             'version', 'date', 'status', 'prev', 'next']
    for k in order:
        v = meta.get(k, '')
        if k == 'subtitle' and v:
            lines.append(f'{k}: "{v}"')
        else:
            lines.append(f'{k}: {v}')
    lines.append('---')
    return '\n'.join(lines)


def process_html(html_path, skip_existing=False):
    file_stem = html_path.stem
    md_path = DOCS_DIR / f'{file_stem}.md'

    if skip_existing and md_path.exists():
        print(f'⏭️  skip existente: {md_path.name}')
        return False

    html = html_path.read_text(encoding='utf-8')
    meta = extract_frontmatter(html, file_stem)
    sections = extract_sections(html)

    body_parts = []
    for sid, shtml in sections:
        # Skip cover y toc · ya están en frontmatter o autogenerados
        if sid in ('toc',):
            continue
        body_parts.append(section_to_md(sid, shtml))

    md = yaml_frontmatter(meta) + '\n\n' + '\n'.join(body_parts)

    DOCS_DIR.mkdir(exist_ok=True)
    md_path.write_text(md, encoding='utf-8')
    print(f'✅ generado: {md_path.name} ({len(sections)} secciones)')
    return True


def main():
    p = argparse.ArgumentParser()
    p.add_argument('files', nargs='+', help='HTMLs a procesar')
    p.add_argument('--skip-existing', action='store_true',
                   help='No sobreescribir .md ya existentes')
    args = p.parse_args()

    count = 0
    for f in args.files:
        path = Path(f).resolve()
        if not path.exists():
            print(f'❌ no existe: {f}')
            continue
        if process_html(path, args.skip_existing):
            count += 1
    print(f'\n✅ {count} .md generados/actualizados')


if __name__ == '__main__':
    main()
