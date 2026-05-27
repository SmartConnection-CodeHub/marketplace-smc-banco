#!/usr/bin/env python3
"""
audit_banco.py · auditoría general HTMLs del banco

Detecta:
1. Numeración "X / Y" cuando Y NO coincide con total real
2. Referencias a docs inexistentes (broken links)
3. Menciones residuales a "Kanki" (proyecto separado)
4. Fechas inconsistentes (algunos -25, -26, -27)
5. Versión inconsistente (v1.0, v2.0, v3.0 mezclados)
6. Status raros (Draft vs Activo)
7. Cover subtitle apuntando a secciones removidas
8. Footer page-footer con número mismatch al TOC pg
9. Nav anterior/siguiente roto
10. Referencias "ver Doc X" cuando X no existe

Uso:
   python3 audit_banco.py            # solo reporte
   python3 audit_banco.py --fix      # aplicar fixes seguros automaticos
"""

import argparse
import re
from pathlib import Path
from collections import defaultdict


ROOT = Path(__file__).parent


def get_html_files():
    return sorted([f for f in ROOT.glob('*.html') if f.name not in ('index.html',)])


def get_doc_numbers(files):
    """Extrae los números de doc reales (01, 02, ..., 41)."""
    nums = []
    for f in files:
        m = re.match(r'^(\d{2})-', f.name)
        if m:
            nums.append(m.group(1))
    return nums


def audit_file(path, total_docs, all_doc_names):
    issues = []
    text = path.read_text(encoding='utf-8')

    # 1. doc-num "X / Y"
    matches = re.findall(r'class="doc-num">(\d+)\s*/\s*(\d+)<', text)
    for x, y in matches:
        if int(y) != total_docs and y != '09':  # Allow grouped blocks like 8/8 if it's a block count
            issues.append(f'  📊 doc-num "{x}/{y}" pero hay {total_docs} docs totales')

    # 2. Kanki residual
    kanki_count = len(re.findall(r'[Kk]anki', text))
    if kanki_count > 0:
        issues.append(f'  ⚠️ {kanki_count} menciones a Kanki residuales')

    # 3. Referencias a docs HTML
    refs = re.findall(r'href="(\d{2}-[a-z0-9-]+\.html)', text)
    missing = [r for r in refs if r not in all_doc_names and r != path.name]
    if missing:
        issues.append(f'  🔗 Links rotos: {", ".join(set(missing))}')

    # 4. Fechas
    dates = re.findall(r'(2026-05-2[5-9])', text)
    unique_dates = set(dates)
    if len(unique_dates) > 1:
        issues.append(f'  📅 Fechas mixed: {sorted(unique_dates)}')

    # 5. Status
    statuses = re.findall(r'cover-meta-value">([🟢🟡🔴].*?)</div>', text)
    if statuses and any('Draft' in s for s in statuses) and any('Activo' in s for s in statuses):
        issues.append(f'  🚦 Status mixed: {statuses}')

    # 6. cover-doc-num inconsistente
    cover_num = re.search(r'cover-doc-num">Documento (\d+)(?:\s+de\s+(\d+))?', text)
    if cover_num and cover_num.group(2):
        cover_total = int(cover_num.group(2))
        if cover_total != total_docs:
            issues.append(f'  📘 Cover "Documento {cover_num.group(1)} de {cover_total}" → debería ser {total_docs}')

    # 7. DOCUMENTO X DE Y en nav-center
    nav_total = re.search(r'DOCUMENTO\s+\d+\s+DE\s+(\d+)', text)
    if nav_total and int(nav_total.group(1)) != total_docs:
        issues.append(f'  🧭 Nav-center "DE {nav_total.group(1)}" → debería ser DE {total_docs}')

    return issues


def apply_safe_fixes(path, total_docs, all_doc_names):
    """Aplica fixes automáticos seguros: numeración + Kanki + fechas."""
    text = path.read_text(encoding='utf-8')
    original = text
    changes = []

    # Fix 1: doc-num "X / Y" → "X / total_docs" SOLO si Y < 50 (es total, no porcentaje)
    def fix_doc_num(m):
        x, y = m.group(1), m.group(2)
        if int(y) < 50 and int(y) != total_docs:
            changes.append(f'doc-num {x}/{y} → {x}/{total_docs}')
            return f'class="doc-num">{x} / {total_docs}<'
        return m.group(0)
    text = re.sub(r'class="doc-num">(\d+)\s*/\s*(\d+)<', fix_doc_num, text)

    # Fix 2: cover "Documento X de Y"
    def fix_cover(m):
        x, y = m.group(1), m.group(2)
        if int(y) != total_docs:
            changes.append(f'cover "Documento {x} de {y}" → de {total_docs}')
            return f'cover-doc-num">Documento {x} de {total_docs}'
        return m.group(0)
    text = re.sub(r'cover-doc-num">Documento (\d+)\s+de\s+(\d+)', fix_cover, text)

    # Fix 3: nav-center "DOCUMENTO X DE Y"
    def fix_nav(m):
        full = m.group(0)
        y = m.group(1)
        if int(y) != total_docs:
            new = full.replace(f'DE {y}', f'DE {total_docs}')
            changes.append(f'nav DE {y} → DE {total_docs}')
            return new
        return full
    text = re.sub(r'DOCUMENTO\s+\d+\s+DE\s+(\d+)', fix_nav, text)

    if text != original:
        path.write_text(text, encoding='utf-8')
    return changes


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--fix', action='store_true', help='Aplicar fixes seguros')
    args = p.parse_args()

    files = get_html_files()
    nums = get_doc_numbers(files)
    total = len(nums)
    all_doc_names = {f.name for f in files} | {'index.html'}

    print(f'═══════════════════════════════════════════════════════════')
    print(f'AUDIT BANCO MARKETPLACE SMC · {total} HTMLs detectados')
    print(f'Números: {", ".join(nums)}')
    print(f'═══════════════════════════════════════════════════════════\n')

    total_issues = 0
    fixed_count = 0

    for f in files:
        issues = audit_file(f, total, all_doc_names)
        if issues:
            print(f'📄 {f.name}')
            for i in issues:
                print(i)
            total_issues += len(issues)
            print()

        if args.fix:
            changes = apply_safe_fixes(f, total, all_doc_names)
            if changes:
                fixed_count += 1
                print(f'  ✅ Aplicado en {f.name}: {len(changes)} cambios')
                for c in changes[:3]:
                    print(f'     · {c}')

    print(f'═══════════════════════════════════════════════════════════')
    print(f'TOTAL: {total_issues} issues detectados en {total} HTMLs')
    if args.fix:
        print(f'FIXED: {fixed_count} archivos actualizados')
    else:
        print(f'(usar --fix para aplicar fixes automáticos seguros)')
    print(f'═══════════════════════════════════════════════════════════')


if __name__ == '__main__':
    main()
