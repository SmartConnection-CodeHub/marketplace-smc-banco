#!/usr/bin/env python3
"""
apply_adr.py · Marketplace SMC Banco · sync desde ADR

Toma un Architecture Decision Record (.md con frontmatter YAML) y aplica
sus secciones a los HTMLs del banco usando tags `<!-- ADR:NNNN/section -->`.

Uso:
   python3 apply_adr.py /path/ADR-0001.md --dry-run    # solo muestra cambios
   python3 apply_adr.py /path/ADR-0001.md --apply      # escribe HTMLs

Idempotente: si los tags ya existen, reemplaza el contenido entre ellos.
Si NO existen, inserta antes de un anchor predefinido.

Convención de tags:
   <!-- ADR:0001/pivot-v5 -->
       ...contenido renderizado...
   <!-- /ADR:0001/pivot-v5 -->
"""

import argparse
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent


# ============================================================
# PARSER DEL ADR
# ============================================================

def parse_frontmatter(md):
    """Extrae YAML frontmatter (--- ... ---) y body del markdown."""
    if not md.startswith('---'):
        return {}, md
    end = md.find('\n---\n', 4)
    if end < 0:
        return {}, md
    yaml_block = md[4:end]
    body = md[end + 5:]
    meta = {}
    for line in yaml_block.splitlines():
        if ':' in line:
            k, v = line.split(':', 1)
            meta[k.strip()] = v.strip()
    return meta, body


def parse_sections(body):
    """Parsea secciones nivel `# Title` del body markdown."""
    sections = {}
    current_title = None
    current_lines = []
    for line in body.splitlines():
        m = re.match(r'^# (.+)$', line)
        if m:
            if current_title:
                sections[current_title] = '\n'.join(current_lines).strip()
            current_title = m.group(1).strip()
            current_lines = []
        else:
            current_lines.append(line)
    if current_title:
        sections[current_title] = '\n'.join(current_lines).strip()
    return sections


# ============================================================
# RENDERERS · cada uno toma el body markdown de la sección y
# devuelve HTML branded SMC listo para insertar
# ============================================================

def render_pivot_v5(_section_body, adr_meta):
    """Doc 01 Vision · agrega sección pivot v5."""
    return '''<section class="page" id="s-v5">
  <h2><span class="h2-num">04b</span>Pivot v5 · Sistema de Oportunidades</h2>
  <div class="box box-warning">
    <div class="box-title">⚠️ Cambio estratégico 2026-05-26</div>
    <p style="margin:0">MeLi cerró sus APIs públicas detrás de <strong>PolicyAgent</strong>. El Developer Partner Program (DPP) exige USD 200K GMV/mes · imposible arrancar. <strong>Pivot:</strong> ahora somos "co-piloto de operación MeLi" usando APIs gratis chilenas/LATAM.</p>
  </div>
  <h3>Nuevo enfoque · 6 capas sin LLM masivo</h3>
  <table>
    <thead><tr><th>Capa</th><th>Función</th><th>LLM?</th></tr></thead>
    <tbody>
      <tr><td>1 · Sources</td><td>SoloTodo · Mercado Público · OpenFoodFacts · BCentral (gratis)</td><td>❌ HTTP fetch</td></tr>
      <tr><td>2 · Filters</td><td>Whitelist categorías · blacklist (libros · usados · sin stock)</td><td>❌ Reglas duras</td></tr>
      <tr><td>3 · Scoring</td><td>6 señales (multistore · spread · availability · stability · premium · meli)</td><td>❌ Math puro JS/SQL</td></tr>
      <tr><td>4 · Smart Cache</td><td>Tabla <code>mkt_opportunity_cache</code> · max 1000 filas · TTL diferenciado</td><td>❌ Solo storage</td></tr>
      <tr><td>5 · API</td><td><code>/api/opportunities/list</code> · 1 SQL query</td><td>❌ SQL</td></tr>
      <tr><td>6 · UI</td><td><code>/dashboard/oportunidades</code> · tabla con scores</td><td>❌ Render directo</td></tr>
      <tr><td>+ Opt-in</td><td>Click "Explicar" → Groq llama-3.3 · cache 24h</td><td>✅ Solo on-click</td></tr>
    </tbody>
  </table>
  <div class="box box-premise" style="margin-top:14px">
    <div class="box-title">🎯 Restricciones v5 (no transables)</div>
    <ul style="margin:0">
      <li>NO data lake masivo · cache ligero · no clonamos catálogo SoloTodo</li>
      <li>NO LLM en cada vista · scoring math puro · LLM solo on-click</li>
      <li>Stack 100% gratis · sin pagar APIs · sin scraping propio</li>
      <li>Usuario ve scores · NO ve la cocina interna</li>
    </ul>
  </div>
  <p style="margin-top:14px"><strong>Status:</strong> <span class="badge badge-active">''' + adr_meta.get('status', 'Design Approved') + '''</span> · Ver Doc 07 Architecture · Doc 08 Roadmap · ADR-0001 en repo marketplace.</p>
  <div class="page-footer"><span>Marketplace SMC · Blueprint v1.0 · ADR-0001</span><span>04b</span></div>
</section>'''


def render_v5_architecture(_section_body, _adr_meta):
    """Doc 07 Architecture · sección 6 capas v5."""
    return '''<section class="page" id="hl-v5">
  <h2><span class="h2-num">01b</span>Arquitectura v5 · Opportunities System</h2>
  <div class="svg-container">
    <svg viewBox="0 0 700 540" xmlns="http://www.w3.org/2000/svg" style="background:#FAFAF7">
      <rect x="40" y="20" width="620" height="80" rx="10" fill="#0F172A"/>
      <text x="350" y="55" text-anchor="middle" fill="white" font-weight="800" font-size="14">USUARIO en /dashboard/oportunidades</text>
      <text x="350" y="78" text-anchor="middle" fill="rgba(255,255,255,0.7)" font-size="11">Tabla top-50 oportunidades · transparencia · sin saber qué hay debajo</text>

      <rect x="40" y="120" width="620" height="60" rx="10" fill="white" stroke="#7C3AED" stroke-width="2"/>
      <text x="350" y="148" text-anchor="middle" font-weight="700" font-size="13">6 · UI · render directo · cero LLM</text>
      <text x="350" y="165" text-anchor="middle" fill="#64748B" font-size="11">Tabla scores + filtros + transparencia</text>

      <rect x="40" y="200" width="620" height="60" rx="10" fill="white" stroke="#3B82F6" stroke-width="2"/>
      <text x="350" y="228" text-anchor="middle" font-weight="700" font-size="13">5 · API /api/opportunities/list · 1 SQL query · cero LLM</text>

      <rect x="40" y="280" width="620" height="60" rx="10" fill="white" stroke="#F472B6" stroke-width="2"/>
      <text x="350" y="308" text-anchor="middle" font-weight="700" font-size="13">4 · Smart Cache Supabase · max 1000 filas · TTL diferenciado</text>

      <rect x="40" y="360" width="620" height="60" rx="10" fill="white" stroke="#F59E0B" stroke-width="2"/>
      <text x="350" y="388" text-anchor="middle" font-weight="700" font-size="13">3 · Scoring Engine · 6 señales · math puro JS/SQL · cero LLM</text>

      <rect x="40" y="440" width="620" height="50" rx="10" fill="white" stroke="#22C55E" stroke-width="2"/>
      <text x="350" y="470" text-anchor="middle" font-weight="700" font-size="13">2 · Filters · whitelist + blacklist (libros · usados · sin stock)</text>

      <rect x="40" y="500" width="620" height="30" rx="6" fill="#0F172A"/>
      <text x="350" y="520" text-anchor="middle" fill="#00C1C1" font-family="monospace" font-size="12">1 · Sources gratis (SoloTodo · Mercado Público · OFF · BCentral)</text>
    </svg>
  </div>
  <h3>Scoring Engine · 6 señales</h3>
  <table>
    <thead><tr><th>#</th><th>Señal</th><th>Cómo se mide</th><th>Peso</th></tr></thead>
    <tbody>
      <tr><td>1</td><td>Multistore presence</td><td># stores con mismo SKU canónico</td><td>25%</td></tr>
      <tr><td>2</td><td>Price spread</td><td>(max - min) / min · &gt;15% = oportunidad</td><td>25%</td></tr>
      <tr><td>3</td><td>Availability rate</td><td># stores con is_available / total</td><td>15%</td></tr>
      <tr><td>4</td><td>Price stability</td><td>baja varianza precio 7d (demanda sostenida)</td><td>15%</td></tr>
      <tr><td>5</td><td>Category premium</td><td>tabla fija <code>mkt_category_premium</code></td><td>10%</td></tr>
      <tr><td>6</td><td>MeLi presence</td><td>producto también en store MeLi (id=260)?</td><td>10%</td></tr>
    </tbody>
  </table>
  <div class="box box-premise" style="margin-top:14px">
    <div class="box-title">🎯 Total score 0-10 · 1 SQL query · cero tokens LLM</div>
  </div>
  <div class="page-footer"><span>Marketplace SMC · Blueprint v1.0 · ADR-0001</span><span>03b</span></div>
</section>'''


def render_smart_cache(_section_body, _adr_meta):
    """Doc 05 Data Model · agrega tabla mkt_opportunity_cache."""
    return '''<section class="page" id="opp-cache">
  <h2><span class="h2-num">11</span>Smart Cache v5 · mkt_opportunity_cache</h2>
  <p>Tabla específica del sistema Opportunities (ADR-0001). NO es data lake · es cache ligero con TTL diferenciado.</p>
  <table>
    <thead><tr><th>Aspecto</th><th>Política</th></tr></thead>
    <tbody>
      <tr><td>Tamaño máximo</td><td>1.000 filas (~200 KB total)</td></tr>
      <tr><td>TTL Hot (n_queries&gt;5)</td><td>6h</td></tr>
      <tr><td>TTL Warm (n_queries 1-5)</td><td>12h</td></tr>
      <tr><td>TTL Cold (sin query 7d)</td><td>DELETE</td></tr>
      <tr><td>Cron limpieza</td><td><code>pg_cron</code> diario 3:00 AM</td></tr>
      <tr><td>Refresh</td><td>NO sync masivo · solo SKUs consultados</td></tr>
    </tbody>
  </table>
  <h3>Schema mkt_opportunity_cache</h3>
  <pre class="ascii">CREATE TABLE mkt_opportunity_cache (
  sku_canonico TEXT PRIMARY KEY,
  score NUMERIC,
  category TEXT,
  n_stores INTEGER,
  price_min NUMERIC,
  price_max NUMERIC,
  top_url TEXT,
  last_synced TIMESTAMPTZ,
  n_queries INTEGER DEFAULT 1
);

CREATE TABLE mkt_category_premium (
  category TEXT PRIMARY KEY,
  multiplier NUMERIC,  -- ej: accesorios celular 1.3x · línea blanca 0.9x
  active BOOLEAN DEFAULT true
);</pre>
  <div class="box box-info">
    <div class="box-title">💡 Por qué no data lake</div>
    <p style="margin:0">SoloTodo tiene 58K productos · clonarlos sería data lake. Solo entra al cache lo que alguien consultó. Si nadie pregunta más · se borra solo.</p>
  </div>
  <div class="page-footer"><span>Marketplace SMC · Blueprint v1.0 · ADR-0001</span><span>11b</span></div>
</section>'''


def render_v5_api(_section_body, _adr_meta):
    """Doc 06 API Catalog · agrega endpoints opportunities."""
    return '''<section class="page" id="opp-api">
  <h2><span class="h2-num">11</span>Endpoints v5 · Opportunities System</h2>
  <p>Endpoints específicos del sistema Opportunities (ADR-0001). Sources + scoring + cache + render.</p>

  <h3>Sources externas</h3>
  <div class="endpoint" style="background:white;border:1px solid var(--ink-200);border-radius:10px;padding:16px 20px;margin:10px 0">
    <span style="background:#DBEAFE;color:#1E40AF;padding:2px 10px;border-radius:4px;font-family:'JetBrains Mono',monospace;font-size:11px;font-weight:700;margin-right:10px">GET</span>
    <span style="font-family:'JetBrains Mono',monospace;font-size:14px;font-weight:600">/api/solotodo/test</span>
    <div style="font-size:13px;color:var(--ink-500);margin-top:6px">Test conexión SoloTodo · 58.611 productos MeLi Chile · 564 stores</div>
  </div>
  <div class="endpoint" style="background:white;border:1px solid var(--ink-200);border-radius:10px;padding:16px 20px;margin:10px 0">
    <span style="background:#DBEAFE;color:#1E40AF;padding:2px 10px;border-radius:4px;font-family:'JetBrains Mono',monospace;font-size:11px;font-weight:700;margin-right:10px">GET</span>
    <span style="font-family:'JetBrains Mono',monospace;font-size:14px;font-weight:600">/api/mercadopublico/test</span>
    <div style="font-size:13px;color:var(--ink-500);margin-top:6px">Test conexión ChileCompra B2G · requiere ticket env var</div>
  </div>

  <h3>Opportunities Engine</h3>
  <div class="endpoint" style="background:white;border:1px solid var(--ink-200);border-radius:10px;padding:16px 20px;margin:10px 0">
    <span style="background:#D1FAE5;color:#14532D;padding:2px 10px;border-radius:4px;font-family:'JetBrains Mono',monospace;font-size:11px;font-weight:700;margin-right:10px">POST</span>
    <span style="font-family:'JetBrains Mono',monospace;font-size:14px;font-weight:600">/api/opportunities/build</span>
    <div style="font-size:13px;color:var(--ink-500);margin-top:6px">Computa scoring · escribe en mkt_opportunity_cache · devuelve {count: 50-200}</div>
  </div>
  <div class="endpoint" style="background:white;border:1px solid var(--ink-200);border-radius:10px;padding:16px 20px;margin:10px 0">
    <span style="background:#DBEAFE;color:#1E40AF;padding:2px 10px;border-radius:4px;font-family:'JetBrains Mono',monospace;font-size:11px;font-weight:700;margin-right:10px">GET</span>
    <span style="font-family:'JetBrains Mono',monospace;font-size:14px;font-weight:600">/api/opportunities/list?category=X&amp;score_min=Y</span>
    <div style="font-size:13px;color:var(--ink-500);margin-top:6px">Lee desde cache · agrega filtros user · ordena por score · sin LLM</div>
  </div>
  <div class="endpoint" style="background:white;border:1px solid var(--ink-200);border-radius:10px;padding:16px 20px;margin:10px 0">
    <span style="background:#D1FAE5;color:#14532D;padding:2px 10px;border-radius:4px;font-family:'JetBrains Mono',monospace;font-size:11px;font-weight:700;margin-right:10px">POST</span>
    <span style="font-family:'JetBrains Mono',monospace;font-size:14px;font-weight:600">/api/opportunities/explain/:sku</span>
    <div style="font-size:13px;color:var(--ink-500);margin-top:6px">LLM opt-in · Groq llama-3.3 · response cacheado 24h · 1 call/día max por SKU</div>
  </div>

  <h3>Cron</h3>
  <div class="endpoint" style="background:white;border:1px solid var(--ink-200);border-radius:10px;padding:16px 20px;margin:10px 0">
    <span style="background:#FEF3C7;color:#92400E;padding:2px 10px;border-radius:4px;font-family:'JetBrains Mono',monospace;font-size:11px;font-weight:700;margin-right:10px">CRON</span>
    <span style="font-family:'JetBrains Mono',monospace;font-size:14px;font-weight:600">pg_cron · 3:00 AM diario</span>
    <div style="font-size:13px;color:var(--ink-500);margin-top:6px">Limpieza TTL · borra cold · si tabla &gt;1000 drop lowest score</div>
  </div>
  <div class="page-footer"><span>Marketplace SMC · Blueprint v1.0 · ADR-0001</span><span>13b</span></div>
</section>'''


def render_v5_roadmap(_section_body, _adr_meta):
    """Doc 08 Roadmap · agrega Sprint Plan v5."""
    return '''<section class="page" id="roadmap-v5">
  <h2><span class="h2-num">03</span>Roadmap v5 · Opportunities Sprints</h2>
  <div class="box box-warning">
    <div class="box-title">⚠️ Pivot 2026-05-26 · v4 legacy</div>
    <p style="margin:0">El roadmap F0-F7 de arriba es la versión v4 (multi-canal full). Tras pivot post-PolicyAgent · se prioriza primero v5 Opportunities (3 sprints) · v4 queda pausado hasta MeLi DPP aprobado.</p>
  </div>
  <table>
    <thead><tr><th>Sprint</th><th>Entregable funcional</th><th>Tokens estimados</th><th>Status</th></tr></thead>
    <tbody>
      <tr><td><strong>S1 "tubería"</strong></td><td>Backend completo sin UI · SQL migration · scoring.ts · filters.ts · /api/opportunities/build · /api/opportunities/list · cron pg_cron 3am · curl validable</td><td>15-20% sesión</td><td><span class="badge badge-pending">Pending</span></td></tr>
      <tr><td><strong>S2 "ducha"</strong></td><td>Página <code>/dashboard/oportunidades</code> tabla básica · top-50 visible · sin filtros aún</td><td>8-10% sesión</td><td><span class="badge badge-future">Próximo</span></td></tr>
      <tr><td><strong>S3 "grifos finos"</strong></td><td>Filtros UI client-side · botón Explicar con Groq cacheado 24h · tooltips transparencia</td><td>10-12% sesión</td><td><span class="badge badge-future">Después</span></td></tr>
    </tbody>
  </table>
  <p>Cada sesión deja algo funcional. NO hace falta esperar S3 para validar S1.</p>

  <h3>Estado actual</h3>
  <ul>
    <li>✅ <code>/api/solotodo/test</code> deployed (commit 876e5c9)</li>
    <li>✅ <code>/api/mercadopublico/test</code> deployed (commit db51105)</li>
    <li>✅ Cards en /dashboard/settings con botón Probar conexión</li>
    <li>⏳ Sprint 1 · SQL migration <code>mkt_opportunity_cache</code> + <code>mkt_category_premium</code></li>
    <li>⏳ Sprint 1 · <code>lib/scoring.ts</code> · <code>lib/filters.ts</code></li>
    <li>⏳ Sprint 1 · 2 endpoints + pg_cron</li>
    <li>⏳ Sprint 2 · página /dashboard/oportunidades</li>
    <li>⏳ Sprint 3 · filtros + Explicar Groq</li>
  </ul>

  <div class="box box-info">
    <div class="box-title">💡 Pendientes humanos (no técnicos)</div>
    <ul style="margin:0">
      <li>Configurar env <code>MERCADOPUBLICO_TICKET</code> en Amplify (registro free)</li>
      <li>Crear cuenta BCentral si se quiere conectar UF oficial</li>
      <li>Rotar Client Secret MeLi · pegado en chat plano sesión 2026-05-26</li>
    </ul>
  </div>
  <div class="page-footer"><span>Marketplace SMC · Blueprint v1.0 · ADR-0001</span><span>12b</span></div>
</section>'''


# ============================================================
# MAPPING · ADR section → target file + anchor + render
# ============================================================

MAPPING = {
    'ADR-0001': {
        'pivot-v5': {
            'file': '01-vision.html',
            'anchor_before': '<!-- ===== 5 Modelo negocio ===== -->',
            'render': render_pivot_v5,
        },
        'v5-architecture': {
            'file': '07-architecture.html',
            'anchor_before': '<section class="page" id="stack">',
            'render': render_v5_architecture,
        },
        'smart-cache': {
            'file': '05-data-model.html',
            'anchor_before': '</div>\n<nav class="doc-nav"><a href="04-rfp.html">',
            'render': render_smart_cache,
        },
        'v5-api': {
            'file': '06-api-catalog.html',
            'anchor_before': '</div>\n<nav class="doc-nav"><a href="05-data-model.html">',
            'render': render_v5_api,
        },
        'v5-roadmap': {
            'file': '08-roadmap.html',
            'anchor_before': '<section class="page" id="f0">',
            'render': render_v5_roadmap,
        },
    }
}


# ============================================================
# APLICAR PATCHES
# ============================================================

def make_block(adr_id, section_id, html_content):
    """Envuelve HTML con tags ADR para idempotencia."""
    return f'<!-- ADR:{adr_id}/{section_id} -->\n{html_content}\n<!-- /ADR:{adr_id}/{section_id} -->\n'


def apply_to_html(html_path, adr_id, section_id, html_content, anchor_before):
    """Inserta o reemplaza bloque ADR en un HTML. Returns (new_src|None, action|error)."""
    if not html_path.exists():
        return None, f'File not found: {html_path}'

    src = html_path.read_text(encoding='utf-8')
    block = make_block(adr_id, section_id, html_content)

    # Caso 1: tags YA existen → reemplazar contenido
    pattern = re.compile(
        rf'<!-- ADR:{re.escape(adr_id)}/{re.escape(section_id)} -->.*?<!-- /ADR:{re.escape(adr_id)}/{re.escape(section_id)} -->\n?',
        re.DOTALL
    )
    if pattern.search(src):
        new_src = pattern.sub(block, src)
        action = 'replaced'
    # Caso 2: tags NO existen → insertar antes del anchor
    else:
        if anchor_before not in src:
            return None, f'Anchor not found: {anchor_before[:60]}...'
        new_src = src.replace(anchor_before, block + '\n' + anchor_before, 1)
        action = 'inserted'

    if new_src == src:
        return None, 'No changes'

    return new_src, action


def main():
    ap = argparse.ArgumentParser(description='Apply ADR sections to Banco HTMLs')
    ap.add_argument('adr_path', help='Path al ADR .md')
    ap.add_argument('--apply', action='store_true', help='Escribe cambios')
    ap.add_argument('--dry-run', action='store_true', help='Solo muestra qué cambiaría')
    args = ap.parse_args()

    adr_path = Path(args.adr_path).expanduser().resolve()
    if not adr_path.exists():
        print(f'❌ ADR not found: {adr_path}')
        sys.exit(1)

    print(f'📖 Leyendo ADR: {adr_path}')
    md = adr_path.read_text(encoding='utf-8')
    meta, body = parse_frontmatter(md)
    adr_title = meta.get('title', '')
    adr_id_match = re.search(r'ADR-(\d{4})', adr_title)
    if not adr_id_match:
        print(f'❌ No se detecta ADR-NNNN en title: {adr_title}')
        sys.exit(1)
    adr_id = f'ADR-{adr_id_match.group(1)}'
    print(f'   ADR ID: {adr_id} · status: {meta.get("status", "?")}')

    if adr_id not in MAPPING:
        print(f'❌ ADR {adr_id} no tiene mapping configurado.')
        print(f'   Agrega entrada en MAPPING del script.')
        sys.exit(1)

    sections = MAPPING[adr_id]
    print(f'\n🗺️  Mapping · {len(sections)} secciones · {adr_id} → banco docs:\n')

    results = []
    for section_id, cfg in sections.items():
        html_path = ROOT / cfg['file']
        html_content = cfg['render']('', meta)
        result, action = apply_to_html(
            html_path, adr_id, section_id, html_content, cfg['anchor_before']
        )
        if result is None:
            print(f'   ❌ {cfg["file"]} · {section_id}: {action}')
            results.append((cfg['file'], section_id, None, action))
        else:
            print(f'   ✓ {cfg["file"]} · {section_id} · {action}')
            results.append((cfg['file'], section_id, result, action))

    if args.dry_run or not args.apply:
        print('\n🔍 DRY-RUN · no se escribieron archivos. Usa --apply para escribir.')
        return

    print('\n💾 Aplicando cambios...')
    written = 0
    for file_name, section_id, new_src, action in results:
        if new_src is None:
            continue
        (ROOT / file_name).write_text(new_src, encoding='utf-8')
        written += 1
        print(f'   ✓ {file_name} escrito ({action})')

    print(f'\n✅ Listo · {written} archivos actualizados.')
    print(f'\n📦 Siguiente paso · validar local · luego:')
    print(f'   git add -A && git commit -m "feat: sync banco con {adr_id}" && git push')


if __name__ == '__main__':
    main()
