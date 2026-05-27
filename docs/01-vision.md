---
number: 01
id: vision
title: Vision &<br>Prospect
subtitle: "Plataforma operativa unificada multi-canal · qué somos, para quién y qué resolvemos."
block: Marketplace SMC
author: Cerebro + PRM + War Room SMC
version: 1.0
date: 2026-05-25
status: 🟢 Activo
prev: index.html
next: index.html
---

# 01 · ¿Qué es Marketplace SMC?

**Marketplace SMC es UNA SOLA plataforma operativa que centraliza compra, inventario, venta multi-canal, fulfillment, contabilidad y analytics** para los 3 founders (Camila Bianchi · Javier Bianchi · Guillermo González León) operando comercio en Chile a través de canales B2C (MeLi), B2G (Mercado Público) y B2B simultáneamente.

  <div class="box box-premise">
    <div class="box-title">🎯 Estrategia Y1 · Reputation First</div>
    
Marketplace SMC opera bajo la **Estrategia Reputation First** (ver [Doc 17 · doc central del banco](17-estrategia-y1.html)). Y1 entero NO busca maximizar margen · busca construir reputación verde MeLi como base para escalar Y2+.

    
4 fases: **Fase 1 Reputación** (Q4-26 · 10 ventas) → **Fase 2 Escala** (Q1-27 · 30/mes) → **Fase 3 Diversificación** (Q2-27 · B2G + B2B) → **Fase 4 Consolidación** (Q3-27 · break-even). Path validado por referentes chilenos del e-commerce escalado.

  </div>

  <div class="box box-anti">
    <div class="box-title">⛔ No es</div>
    
- NO es un ERP genérico tipo Defontana o Bsale
- NO es un marketplace público (no se cobra a vendedores terceros)
- NO es un single-channel manager (no es Helium 10 ni Channable)
- NO es una tienda online individual (no es un storefront standalone)

  </div>

  <div class="box box-premise">
    <div class="box-title">✅ Sí es</div>
    
- Cockpit operativo del vendedor · todo bajo un mismo techo
- Plataforma multi-tenant que puede operar N marcas/canales sobre la misma base
- Source-of-truth único de inventario, clientes, pedidos, asientos contables
- Orquestador de adapters por canal (MeLi · Mercado Público · D2C · B2B · futuros)

  </div>

# 02 · North Star Metric

<blockquote>
    % de ingresos del usuario que se gestionan dentro de la plataforma (vs fuera de ella).
  </blockquote>

  
Si el usuario factura $10M/mes y solo $2M pasan por SMC Marketplace → North Star = 20%. Si todos los $10M pasan → North Star = 100%.

  <div class="box box-info">
    <div class="box-title">💡 Por qué importa</div>
    <p style="margin:0">Esta métrica obliga a que la plataforma sea ÚTIL para TODOS los canales del usuario, no solo el más fácil. Si solo cubrimos MeLi, el usuario seguirá usando 3 herramientas más afuera · North Star bajo · cliente no se apropia del Hub.</p>
  </div>

  <div class="kpi-grid">
    <div class="kpi">
      <div class="kpi-value">100%</div>
      <div class="kpi-label">Meta NS · año 2</div>
    </div>
    <div class="kpi">
      <div class="kpi-value">≥80%</div>
      <div class="kpi-label">Meta NS · año 1</div>
    </div>
    <div class="kpi">
      <div class="kpi-value">4+</div>
      <div class="kpi-label">Canales operados</div>
    </div>
  </div>

# 03 · Stakeholders

## Stakeholder principal · "el operador"

  <table>
    <thead><tr><th>Atributo</th><th>Detalle</th></tr></thead>
    <tbody>
      <tr><td>**Perfil**</td><td>Vendedor PYME chileno que opera 2+ canales simultáneamente</td></tr>
      <tr><td>**Facturación**</td><td>Entre $5M y $200M CLP/mes</td></tr>
      <tr><td>**Hoy usa**</td><td>Excel + 4-5 herramientas separadas (MeLi seller center + Shopify + Excel + ChileCompra + Defontana)</td></tr>
      <tr><td>**Dolor**</td><td>Pierde tiempo conciliando data · no tiene visibilidad cross-canal</td></tr>
      <tr><td>**Caso primario**</td><td>Guillermo (Smart Connection SpA → futuro Marketplace SMC SpA)</td></tr>
    </tbody>
  </table>

  
## Stakeholder secundario · "los socios"

  
- **3 founders Marketplace SMC SpA**: Camila Bianchi · Javier Bianchi · Guillermo González León (equity split TBD)
- Contadora externa (galvarez.cl) que necesita exportar data para F29/F22
- Operador de bodega (futuro · cuando exista bodega física)

  
## Stakeholder terciario · "los integradores"

  
APIs externas: MeLi, Mercado Público, Open Factura, MercadoPago, couriers, Groq IA. La plataforma debe ser AMIGABLE para integrar nuevas APIs sin refactor.

  <div class="box box-warning">
    <div class="box-title">🚫 Anti-stakeholders (NO son nuestro usuario)</div>
    <ul style="margin:0">
      <li>Vendedores grandes (&gt;$500M/mes) · ellos usan Oracle / SAP B1 / Microsoft Dynamics</li>
      <li>Vendedores de un solo canal · ellos no necesitan unificación</li>
      <li>Personas naturales sin SII activo · no podemos atenderlos legalmente</li>
    </ul>
  </div>

# 04 · Problemas que resolvemos

<div class="flow-diagram">
    <div class="flow-step">
      <div class="flow-step-num">1</div>
      <div class="flow-step-content">
        <div class="flow-step-title">"Excel paralelo"</div>
        <div class="flow-step-desc">3-5 sistemas de inventario distintos. Vende en MeLi y olvida bajar stock en Shopify. Resultado: oversell, multas, descontento.</div>
      </div>
    </div>
    <div class="flow-step">
      <div class="flow-step-num">2</div>
      <div class="flow-step-content">
        <div class="flow-step-title">"Ceguera cross-canal"</div>
        <div class="flow-step-desc">No sabe cuál canal vende más, dónde gana más margen, qué SKU rota mejor. Decide a ciegas dónde invertir publicidad.</div>
      </div>
    </div>
    <div class="flow-step">
      <div class="flow-step-num">3</div>
      <div class="flow-step-content">
        <div class="flow-step-title">"Facturación rota"</div>
        <div class="flow-step-desc">Vende en 4 canales · factura en 1 sistema · concilia mensual a mano · F29 mal · multas SII. Contadora cobra extra por desorden.</div>
      </div>
    </div>
    <div class="flow-step">
      <div class="flow-step-num">4</div>
      <div class="flow-step-content">
        <div class="flow-step-title">"Publicación duplicada"</div>
        <div class="flow-step-desc">Crear el mismo producto en 4 canales requiere subir título, fotos, precio, stock 4 veces. Cambio de precio = 4 updates.</div>
      </div>
    </div>
    <div class="flow-step">
      <div class="flow-step-num">5</div>
      <div class="flow-step-content">
        <div class="flow-step-title">"Cobranza ciega"</div>
        <div class="flow-step-desc">No sabe cuánto le debe MeLi · ChileCompra · sus clientes B2B. Cash flow es adivinanza.</div>
      </div>
    </div>
    <div class="flow-step">
      <div class="flow-step-num">6</div>
      <div class="flow-step-content">
        <div class="flow-step-title">"Supply chain a ciegas"</div>
        <div class="flow-step-desc">No sabe cuándo llega el próximo lote · cuánto stock real tiene · cuándo quedará sin SKU X. Decide compras por feeling.</div>
      </div>
    </div>
  </div>

# s-v5

<h2><span class="h2-num">04b</span>Pivot v5 · Sistema de Oportunidades</h2>
  <div class="box box-warning">
    <div class="box-title">⚠️ Cambio estratégico 2026-05-26</div>
    <p style="margin:0">MeLi cerró sus APIs públicas detrás de **PolicyAgent**. El Developer Partner Program (DPP) exige USD 200K GMV/mes · imposible arrancar. **Pivot:** ahora somos "co-piloto de operación MeLi" usando APIs gratis chilenas/LATAM.</p>
  </div>
  
## Nuevo enfoque · 6 capas sin LLM masivo

  <table>
    <thead><tr><th>Capa</th><th>Función</th><th>LLM?</th></tr></thead>
    <tbody>
      <tr><td>1 · Sources</td><td>SoloTodo · Mercado Público · OpenFoodFacts · BCentral (gratis)</td><td>❌ HTTP fetch</td></tr>
      <tr><td>2 · Filters</td><td>Whitelist categorías · blacklist (libros · usados · sin stock)</td><td>❌ Reglas duras</td></tr>
      <tr><td>3 · Scoring</td><td>6 señales (multistore · spread · availability · stability · premium · meli)</td><td>❌ Math puro JS/SQL</td></tr>
      <tr><td>4 · Smart Cache</td><td>Tabla `mkt_opportunity_cache` · max 1000 filas · TTL diferenciado</td><td>❌ Solo storage</td></tr>
      <tr><td>5 · API</td><td>`/api/opportunities/list` · 1 SQL query</td><td>❌ SQL</td></tr>
      <tr><td>6 · UI</td><td>`/dashboard/oportunidades` · tabla con scores</td><td>❌ Render directo</td></tr>
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
  <p style="margin-top:14px">**Status:** <span class="badge badge-active">design-approved · pending-implementation S1</span> · Ver Doc 07 Architecture · Doc 08 Roadmap · ADR-0001 en repo marketplace.</p>

# 05 · Modelo de negocio · 4 fases

<table>
    <thead>
      <tr><th>Fase</th><th>Cuándo</th><th>Qué pasa</th><th>Status</th></tr>
    </thead>
    <tbody>
      <tr>
        <td>**Fase 1**
Uso interno SMC</td>
        <td>2026 Q2-Q3</td>
        <td>Herramienta interna del propio Guillermo · operada bajo SMC SpA (ampliando giro) o Marketplace SMC SpA cuando se constituya · sin facturación a terceros</td>
        <td><span class="badge badge-active">En curso</span></td>
      </tr>
      <tr>
        <td>**Fase 2**
Marca propia única</td>
        <td>2026 Q4 - 2027 Q1</td>
        <td>Migrar back-office de la marca propia inicial al Hub · validar arquitectura multi-tenant con caso real</td>
        <td><span class="badge badge-pending">Próxima</span></td>
      </tr>
      <tr>
        <td>**Fase 3**
2-3 marcas internas</td>
        <td>2027</td>
        <td>Operar Marketplace SMC con 2-3 marcas propias + caso vertical X · validar plug-and-play de nuevos canales</td>
        <td><span class="badge badge-future">Futura</span></td>
      </tr>
      <tr>
        <td>**Fase 4**
SaaS para PYMEs</td>
        <td>2028+</td>
        <td>Si fases 1-3 funcionan · ofrecer a otros vendedores PYME · modelo subscription $100-300K CLP/mes por tenant</td>
        <td><span class="badge badge-future">Opcional</span></td>
      </tr>
    </tbody>
  </table>

  <div class="box box-info">
    <div class="box-title">💡 Nota importante</div>
    <p style="margin:0">La fase 4 es opcional. La plataforma puede vivir feliz solo como uso interno de Marketplace SMC SpA. No se condiciona el diseño a que se convierta en SaaS · pero la arquitectura multi-tenant permite hacerlo sin refactor cuando se decida.</p>
  </div>

# 06 · Valores de diseño · qué NO transamos

<table>
    <thead><tr><th>#</th><th>Valor</th><th>Descripción</th></tr></thead>
    <tbody>
      <tr>
        <td>**1**</td>
        <td>**Single Source of Truth**</td>
        <td>1 inventario · 1 catálogo clientes · 1 catálogo productos · 1 chart of accounts. Cualquier duplicación = anti-patrón.</td>
      </tr>
      <tr>
        <td>**2**</td>
        <td>**Channel Adapter Pattern**</td>
        <td>Cada canal externo (MeLi, MP, etc.) se conecta vía adapter que implementa interfaz estándar. Agregar canal nuevo = escribir 1 adapter · no tocar core.</td>
      </tr>
      <tr>
        <td>**3**</td>
        <td>**Event-driven Accounting**</td>
        <td>Cada operación (venta · compra · devolución) emite evento que el módulo contable consume automático. NO existe "registro manual de asiento".</td>
      </tr>
      <tr>
        <td>**4**</td>
        <td>**Multi-tenant desde día 1**</td>
        <td>tenant_id en TODAS las tablas. Aunque hoy haya 1 tenant · arquitectura soporta N. Permite agregar marcas propias sin refactor.</td>
      </tr>
      <tr>
        <td>**5**</td>
        <td>**Honestidad UI**</td>
        <td>Si una pantalla muestra data MOCK · etiqueta visible "mock". Si un cron pendiente · etiqueta "pendiente". Cero teatro. Cero Math.random.</td>
      </tr>
      <tr>
        <td>**6**</td>
        <td>**Escalable gradualmente**</td>
        <td>Empezar simple (1 bodega · 1 marca · 2 canales) pero SIN cementar decisiones que impidan crecer (multi-bodega · multi-marca · N canales).</td>
      </tr>
      <tr>
        <td>**7**</td>
        <td>**Compliance Chile nativo**</td>
        <td>F29 · F22 · DTE · libro IVA · F30 · F30-1 · todo respetando normativa SII desde el primer día. Sin parches "cuando crezca lo agrego".</td>
      </tr>
    </tbody>
  </table>

# 07 · Decisiones diferidas a docs siguientes

<table>
    <thead><tr><th>Decisión</th><th>Documento donde se resuelve</th></tr></thead>
    <tbody>
      <tr><td>Cuáles 12 procesos exactos</td><td>[Doc 02 · BBP](02-bbp.html)</td></tr>
      <tr><td>Qué tablas exactas</td><td>Doc 05 · Data Model</td></tr>
      <tr><td>Qué stack técnico (Next? Rails? Django?)</td><td>Doc 07 · Architecture</td></tr>
      <tr><td>Cuándo se construye qué</td><td>Doc 08 · Roadmap</td></tr>
      <tr><td>Cómo se ve cada pantalla</td><td>Doc 09 · Maquetas</td></tr>
      <tr><td>Pricing del SaaS futuro</td><td>Documento aparte cuando se decida Fase 4</td></tr>
    </tbody>
  </table>

# 08 · Criterios de éxito

### Fase 1 · Uso interno SMC

  
- Cierre mensual F29 desde Hub sin Excel paralelo
- &gt;80% órdenes cross-canal vistas en 1 dashboard
- 0 oversell por desync de inventario
- Tiempo conciliación mensual reducido 70% vs hoy

  
### Fase 2 · Marca propia migrada

  
- Marca propia opera 100% desde el Hub · solo storefront vive aparte
- Stock unificado · venta en storefront descuenta de inventario maestro
- Cierre contable marca propia + SMC mismo balance

  
### Fase 3 · 2-3 marcas

  
- Plug nuevo tenant en &lt;1 día (no semanas)
- Plug nuevo canal externo en &lt;1 sprint
- Métricas por marca + consolidadas (drill-down)

  
### Fase 4 · SaaS

  
- Onboarding cliente PYME en &lt;2 horas (no consulting)
- Churn &lt;5% anual · CAC &lt; 3 meses de MRR

# 09 · Anti-alcance · lo que NO promete

<div class="box box-anti">
    <div class="box-title">⛔ Este documento NO promete</div>
    <ul style="margin:0">
      <li>NO promete que será SaaS comercial (es opcional)</li>
      <li>NO promete reemplazar al contador (asiste pero no decide tributario)</li>
      <li>NO promete vender por canales que no tienen API (Cencosud · supplier portals)</li>
      <li>NO promete construirse en 1 mes (es proyecto enterprise · ver Doc 08 Roadmap)</li>
    </ul>
  </div>

# 10 · Una analogía para alinear

<blockquote style="font-size: 18px; line-height: 1.7;">
    **Marketplace SMC es el "Stripe del vendedor multi-canal chileno":**

    Stripe unifica el cobro · cualquier integración · una sola API.

    Marketplace SMC unifica la operación · cualquier canal · una sola plataforma.

    Stripe escondió la complejidad de Visa/Mastercard/Amex bajo `/charge`.

    Marketplace SMC esconde MeLi/MP/B2B/D2C bajo `/sell`.
  </blockquote>

  <div class="svg-container">
    <svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arr" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
          <polygon points="0 0, 10 3, 0 6" fill="#00C1C1"/>
        </marker>
      </defs>
      <rect x="320" y="100" width="160" height="60" rx="12" fill="#0F172A"/>
      <text x="400" y="135" text-anchor="middle" fill="#00C1C1" font-family="Inter" font-weight="700" font-size="16">/sell</text>
      <text x="400" y="170" text-anchor="middle" fill="#94A3B8" font-family="Inter" font-size="10">Marketplace SMC API</text>

      <rect x="20" y="20" width="140" height="50" rx="8" fill="#FFE4E6" stroke="#F472B6" stroke-width="2"/>
      <text x="90" y="50" text-anchor="middle" fill="#831843" font-weight="600" font-size="13">MeLi adapter</text>

      <rect x="20" y="190" width="140" height="50" rx="8" fill="#FEF3C7" stroke="#F59E0B" stroke-width="2"/>
      <text x="90" y="220" text-anchor="middle" fill="#92400E" font-weight="600" font-size="13">Mercado Público</text>

      <rect x="640" y="20" width="140" height="50" rx="8" fill="#DBEAFE" stroke="#3B82F6" stroke-width="2"/>
      <text x="710" y="50" text-anchor="middle" fill="#1E40AF" font-weight="600" font-size="13">D2C Storefront</text>

      <rect x="640" y="190" width="140" height="50" rx="8" fill="#D1FAE5" stroke="#22C55E" stroke-width="2"/>
      <text x="710" y="220" text-anchor="middle" fill="#14532D" font-weight="600" font-size="13">B2B Quote</text>

      <line x1="160" y1="45" x2="320" y2="115" stroke="#00C1C1" stroke-width="2" marker-end="url(#arr)"/>
      <line x1="160" y1="215" x2="320" y2="145" stroke="#00C1C1" stroke-width="2" marker-end="url(#arr)"/>
      <line x1="480" y1="115" x2="640" y2="45" stroke="#00C1C1" stroke-width="2" marker-end="url(#arr)"/>
      <line x1="480" y1="145" x2="640" y2="215" stroke="#00C1C1" stroke-width="2" marker-end="url(#arr)"/>
    </svg>
  </div>

  <p style="text-align:center; color: var(--ink-500); font-size: 13px; margin-top: -16px;">
    *1 API · N adapters · N canales · operador NO ve la complejidad*
  </p>
