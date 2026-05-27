---
number: 02
id: bbp
title: Business<br>Blueprint
subtitle: "12 procesos end-to-end · cómo opera el negocio · NO cómo se construye el software."
block: Marketplace SMC
author: Functional-Lead + Cerebro
version: 1.0
date: 2026-05-25
status: 🟢 Activo
prev: index.html
next: index.html
---

# 00 · Mapa visual end-to-end

<div class="svg-container">
    <svg viewBox="0 0 900 520" xmlns="http://www.w3.org/2000/svg" style="background:#FAFAF7">
      <defs>
        <marker id="ar" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
          <polygon points="0 0, 10 3, 0 6" fill="#00C1C1"/>
        </marker>
        <linearGradient id="g1" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" stop-color="#00C1C1"/><stop offset="100%" stop-color="#0F766E"/>
        </linearGradient>
      </defs>

      <!-- Sourcing -->
      <rect x="40" y="30" width="160" height="60" rx="10" fill="white" stroke="#00C1C1" stroke-width="2"/>
      <text x="120" y="55" text-anchor="middle" font-weight="700" font-size="13">P01 · Sourcing</text>
      <text x="120" y="75" text-anchor="middle" font-size="10" fill="#64748B">Brief productos</text>

      <!-- Compra -->
      <rect x="240" y="30" width="160" height="60" rx="10" fill="white" stroke="#00C1C1" stroke-width="2"/>
      <text x="320" y="55" text-anchor="middle" font-weight="700" font-size="13">P02 · Compra Nexport</text>
      <text x="320" y="75" text-anchor="middle" font-size="10" fill="#64748B">OC + pago</text>

      <!-- Recepción -->
      <rect x="440" y="30" width="160" height="60" rx="10" fill="white" stroke="#00C1C1" stroke-width="2"/>
      <text x="520" y="55" text-anchor="middle" font-weight="700" font-size="13">P03 · Recepción</text>
      <text x="520" y="75" text-anchor="middle" font-size="10" fill="#64748B">+stock</text>

      <!-- Publicación -->
      <rect x="640" y="30" width="200" height="60" rx="10" fill="url(#g1)" stroke="none"/>
      <text x="740" y="55" text-anchor="middle" font-weight="700" font-size="13" fill="white">P04 · Publicación cross-canal</text>
      <text x="740" y="75" text-anchor="middle" font-size="10" fill="rgba(255,255,255,0.8)">N canales · 1 click</text>

      <!-- Canales venta -->
      <rect x="40" y="160" width="180" height="70" rx="10" fill="#FFE4E6" stroke="#F472B6" stroke-width="2"/>
      <text x="130" y="185" text-anchor="middle" font-weight="700" font-size="13">P05 · MeLi (B2C)</text>
      <text x="130" y="205" text-anchor="middle" font-size="10" fill="#831843">Webhook MeLi</text>

      <rect x="240" y="160" width="180" height="70" rx="10" fill="#DBEAFE" stroke="#3B82F6" stroke-width="2"/>
      <text x="330" y="185" text-anchor="middle" font-weight="700" font-size="13">P06 · D2C</text>
      <text x="330" y="205" text-anchor="middle" font-size="10" fill="#1E40AF">Storefront propio</text>

      <rect x="440" y="160" width="180" height="70" rx="10" fill="#FEF3C7" stroke="#F59E0B" stroke-width="2"/>
      <text x="530" y="185" text-anchor="middle" font-weight="700" font-size="13">P07 · B2G (Estado)</text>
      <text x="530" y="205" text-anchor="middle" font-size="10" fill="#92400E">Mercado Público</text>

      <rect x="640" y="160" width="180" height="70" rx="10" fill="#D1FAE5" stroke="#22C55E" stroke-width="2"/>
      <text x="730" y="185" text-anchor="middle" font-weight="700" font-size="13">P08 · B2B</text>
      <text x="730" y="205" text-anchor="middle" font-size="10" fill="#14532D">Quote builder</text>

      <!-- Fulfillment -->
      <rect x="240" y="290" width="400" height="60" rx="10" fill="white" stroke="#00C1C1" stroke-width="2"/>
      <text x="440" y="315" text-anchor="middle" font-weight="700" font-size="13">P09 · Fulfillment / Despacho</text>
      <text x="440" y="335" text-anchor="middle" font-size="10" fill="#64748B">Picking · packing · courier</text>

      <!-- Facturación -->
      <rect x="100" y="400" width="220" height="60" rx="10" fill="white" stroke="#7C3AED" stroke-width="2"/>
      <text x="210" y="425" text-anchor="middle" font-weight="700" font-size="13">P11 · Facturación DTE</text>
      <text x="210" y="445" text-anchor="middle" font-size="10" fill="#64748B">Boleta · factura SII</text>

      <rect x="380" y="400" width="180" height="60" rx="10" fill="white" stroke="#EF4444" stroke-width="2"/>
      <text x="470" y="425" text-anchor="middle" font-weight="700" font-size="13">P10 · Devolución</text>
      <text x="470" y="445" text-anchor="middle" font-size="10" fill="#64748B">Opcional · NC</text>

      <rect x="620" y="400" width="200" height="60" rx="10" fill="white" stroke="#7C3AED" stroke-width="2"/>
      <text x="720" y="425" text-anchor="middle" font-weight="700" font-size="13">P12 · Cobranza</text>
      <text x="720" y="445" text-anchor="middle" font-size="10" fill="#64748B">CxC monitoring</text>

      <!-- Flechas -->
      <line x1="200" y1="60" x2="240" y2="60" stroke="#00C1C1" stroke-width="2" marker-end="url(#ar)"/>
      <line x1="400" y1="60" x2="440" y2="60" stroke="#00C1C1" stroke-width="2" marker-end="url(#ar)"/>
      <line x1="600" y1="60" x2="640" y2="60" stroke="#00C1C1" stroke-width="2" marker-end="url(#ar)"/>
      <line x1="740" y1="90" x2="740" y2="160" stroke="#00C1C1" stroke-width="2" marker-end="url(#ar)"/>
      <line x1="740" y1="90" x2="530" y2="160" stroke="#00C1C1" stroke-width="1" stroke-dasharray="3,3" marker-end="url(#ar)"/>
      <line x1="740" y1="90" x2="330" y2="160" stroke="#00C1C1" stroke-width="1" stroke-dasharray="3,3" marker-end="url(#ar)"/>
      <line x1="740" y1="90" x2="130" y2="160" stroke="#00C1C1" stroke-width="1" stroke-dasharray="3,3" marker-end="url(#ar)"/>
      <line x1="130" y1="230" x2="240" y2="290" stroke="#00C1C1" stroke-width="2" marker-end="url(#ar)"/>
      <line x1="330" y1="230" x2="380" y2="290" stroke="#00C1C1" stroke-width="2" marker-end="url(#ar)"/>
      <line x1="530" y1="230" x2="500" y2="290" stroke="#00C1C1" stroke-width="2" marker-end="url(#ar)"/>
      <line x1="730" y1="230" x2="640" y2="290" stroke="#00C1C1" stroke-width="2" marker-end="url(#ar)"/>
      <line x1="440" y1="350" x2="210" y2="400" stroke="#7C3AED" stroke-width="2" marker-end="url(#ar)"/>
      <line x1="440" y1="350" x2="470" y2="400" stroke="#EF4444" stroke-width="2" stroke-dasharray="3,3" marker-end="url(#ar)"/>
      <line x1="320" y1="430" x2="380" y2="430" stroke="#7C3AED" stroke-width="2" marker-end="url(#ar)"/>
      <line x1="560" y1="430" x2="620" y2="430" stroke="#7C3AED" stroke-width="2" marker-end="url(#ar)"/>

      <text x="450" y="500" text-anchor="middle" font-size="11" fill="#64748B" font-style="italic">+ contabilidad automática · inventario real-time · Cerebro IA · compliance · analytics (transversales)</text>
    </svg>
  </div>

# bbp-procesos-section

<h2><span class="h2-num">00b</span>Procesos interactivos · 14 procesos · stock propio + dropshipping</h2>
  <p style="color:#475569;font-size:14px;line-height:1.6;margin-top:-8px;">Seleccioná uno de los 12 procesos (P01-P12) para ver su pipeline detallado. Click en cualquier paso para ver stack · acciones · errores comunes.</p>
  <div class="diagram-host kind-pipeline" id="bbp-procesos" data-kind="pipeline"></div>
  <script type="application/json" data-for="bbp-procesos">{"default": "P01", "scenarios": {"P01": {"title": "P01 · Sourcing", "sub": "Búsqueda de productos · matching mercado", "callout": "Identificar productos candidatos en SoloTodo y otras fuentes públicas Chile · score por margen y demanda.", "tags": ["Cerebro · scoring", "Fuentes Chile gratis"], "stages": [{"num": "01", "name": "Detectar", "boxes": [{"code": "P01-01", "label": "Scrape SoloTodo categorías", "kind": "search", "stack": "Cron diario · API pública"}, {"code": "P01-02", "label": "Cargar Open Food Facts si aplica", "kind": "search", "stack": "API OFF"}]}, {"num": "02", "name": "Scoring", "boxes": [{"code": "P01-03", "label": "6 señales sin LLM · multistore/spread/etc", "kind": "search", "stack": "Postgres + cerebro lógica"}]}, {"num": "03", "name": "Sugerir operador", "boxes": [{"code": "P01-04", "label": "Top oportunidades en dashboard", "kind": "notify", "stack": "UI cards + cerebro chat"}]}]}, "P02": {"title": "P02 · Compra a proveedores locales Chile", "sub": "Y1 prioridad · proveedores nacionales · ciclo corto · pago en CLP", "callout": "Modo primario Y1. Compramos a proveedores chilenos (mayoristas · distribuidores · marcas locales) · ciclo despacho 3-7 días · pago en CLP sin tipo de cambio · sin aduana ni LCL/FCL.", "tags": ["Y1 prioridad", "Ciclo corto", "Pago CLP"], "stages": [{"num": "01", "name": "Detectar proveedor", "boxes": [{"code": "P02-01", "label": "Match producto con proveedor local", "kind": "search", "stack": "Mercado Libre Mayorista · directorios · gremios"}, {"code": "P02-02", "label": "Validar precios + términos", "kind": "search", "stack": "Comparar 2-3 proveedores"}]}, {"num": "02", "name": "Cotizar", "boxes": [{"code": "P02-03", "label": "RFQ por WhatsApp / email", "kind": "create", "stack": "Contacto directo proveedor"}]}, {"num": "03", "name": "Confirmar OC", "boxes": [{"code": "P02-04", "label": "OC emitida · DTE 33 recibida", "kind": "doc", "stack": "Open Factura SII"}, {"code": "P02-05", "label": "Pago contado o 30 días", "kind": "pay", "stack": "Transferencia CLP"}]}, {"num": "04", "name": "Despacho proveedor", "boxes": [{"code": "P02-06", "label": "Proveedor despacha a bodega · 3-7 días", "kind": "doc", "stack": "Courier proveedor o retiro propio"}]}]}, "P02b": {"title": "P02b · Importación Nexport (Fase 2 · Y2+)", "sub": "Intermediario importador · LCL/FCL · ciclo largo · pago USD", "callout": "Fase 2 · NO Y1. Cuando volumen justifique · importamos vía Nexport (importador). Ciclo 30-90 días · pago USD · costo aduana · pero margen significativamente mayor.", "tags": ["Fase 2 · Y2+", "Importación LCL/FCL", "Pago USD"], "stages": [{"num": "01", "name": "Cotizar", "boxes": [{"code": "P02b-01", "label": "RFQ a Nexport", "kind": "create", "stack": "Email + portal Nexport"}]}, {"num": "02", "name": "Confirmar OC", "boxes": [{"code": "P02b-02", "label": "OC emitida USD + cláusulas Incoterm", "kind": "doc", "stack": "EXW · FOB · CIF según acuerdo"}, {"code": "P02b-03", "label": "Pago anticipado USD", "kind": "pay", "stack": "Transferencia internacional"}]}, {"num": "03", "name": "Tránsito + aduana", "boxes": [{"code": "P02b-04", "label": "ETA + manifest + DUS", "kind": "doc", "stack": "Nexport portal"}, {"code": "P02b-05", "label": "Pago aduana + IVA importación", "kind": "pay", "stack": "Agente aduana"}]}, {"num": "04", "name": "Recepción bodega Chile", "boxes": [{"code": "P02b-06", "label": "Llegada y entrada a P03", "kind": "doc", "stack": "Sigue flujo normal"}]}]}, "P03": {"title": "P03 · Recepción en bodega", "sub": "Conteo · QA · ingreso a inventario", "callout": "Llegada del lote a bodega. Verificación física + ingreso digital a Postgres.", "tags": ["Operación bodega", "QA físico"], "stages": [{"num": "01", "name": "Recepción física", "boxes": [{"code": "P03-01", "label": "Conteo + estado producto", "kind": "search", "stack": "Manual operador"}]}, {"num": "02", "name": "Ingreso inventario", "boxes": [{"code": "P03-02", "label": "Insert mkt_inventory", "kind": "create", "stack": "Postgres + adapter"}, {"code": "P03-03", "label": "Fotos al storage", "kind": "doc", "stack": "Supabase Storage"}]}]}, "P04": {"title": "P04 · Publicación cross-canal", "sub": "Listing en MeLi · D2C · MP · B2B", "callout": "Una vez en inventario, se publica simultáneamente en todos los canales activos del operador via Channel Adapter Pattern.", "tags": ["Cross-canal", "Adapter pattern"], "stages": [{"num": "01", "name": "MeLi", "boxes": [{"code": "P04-01", "label": "POST /items MeLi", "kind": "create", "stack": "MeLi API · OAuth"}]}, {"num": "02", "name": "D2C storefront", "boxes": [{"code": "P04-02", "label": "Insert catalog + ISR revalidate", "kind": "create", "stack": "Storefront Next.js"}]}, {"num": "03", "name": "MP catálogo", "boxes": [{"code": "P04-03", "label": "Update catálogo Mercado Público", "kind": "update", "stack": "MP API REST"}]}, {"num": "04", "name": "B2B portal", "boxes": [{"code": "P04-04", "label": "Sync portal B2B + cache invalidation", "kind": "update", "stack": "B2B API"}]}]}, "P05": {"title": "P05 · Venta MeLi (B2C marketplace ajeno)", "sub": "Fase reputación · Webhook · Aceptación · Despacho", "callout": "Canal alto volumen · 2 fases Y1: (1) Fase reputación = primeras 10 ventas SIN foco margen · regalar o costo + envío gratis para activar termómetro vendedor. (2) Fase escala = post 10 ventas verdes · Mercado Ads ON + foco margen.", "tags": ["MeLi · OAuth", "Volumen alto Y1", "Reputación primero"], "notes": "Estrategia reputación Y1 fase 1 basada en referentes chilenos del e-commerce: las primeras 10 ventas activan el algoritmo · NO buscan utilidad. Fotografía propia (no del proveedor) es non-negotiable.", "stages": [{"num": "01", "name": "Fase reputación (primeras 10)", "boxes": [{"code": "P05-00a", "label": "Configurar listado con foto pro propia + envío gratis", "kind": "create", "stack": "NO usar fotos del proveedor · diferenciar"}, {"code": "P05-00b", "label": "Vender a costo o regalar a contactos diferentes direcciones", "kind": "pay", "stack": "Activar termómetro vendedor MeLi"}]}, {"num": "02", "name": "Webhook MeLi", "boxes": [{"code": "P05-01", "label": "Validar firma + idempotency", "kind": "notify", "stack": "MeLi webhook"}]}, {"num": "03", "name": "Aceptar", "boxes": [{"code": "P05-02", "label": "Reservar stock", "kind": "update", "stack": "Postgres SELECT FOR UPDATE"}]}, {"num": "04", "name": "Despachar", "boxes": [{"code": "P05-03", "label": "Etiqueta courier + tracking", "kind": "doc", "stack": "Chilexpress/Starken"}]}, {"num": "05", "name": "Factura", "boxes": [{"code": "P05-04", "label": "DTE 39 boleta", "kind": "doc", "stack": "Open Factura"}]}, {"num": "06", "name": "Fase escala (post 10 ventas verdes)", "boxes": [{"code": "P05-05a", "label": "Activar Mercado Ads + medallas", "kind": "create", "stack": "Reputación validada · escalar con ADS"}, {"code": "P05-05b", "label": "Migrar a Full Fulfillment si rota bien", "kind": "update", "stack": "Stock en almacenes MeLi · mayor exposición"}]}]}, "P06": {"title": "P06 · Venta D2C (storefront propio)", "sub": "Tráfico ADS · checkout · post-venta", "callout": "Sin comisión marketplace · margen mayor pero requiere inversión ADS y skills marketing.", "tags": ["D2C", "ADS Meta/Google/TikTok"], "stages": [{"num": "01", "name": "Conversión", "boxes": [{"code": "P06-01", "label": "Landing → cart → checkout", "kind": "search", "stack": "Storefront Next.js"}]}, {"num": "02", "name": "Checkout", "boxes": [{"code": "P06-02", "label": "WebPay Plus o MercadoPago", "kind": "pay", "stack": "Pasarela seleccionable"}]}, {"num": "03", "name": "Despacho", "boxes": [{"code": "P06-03", "label": "Courier auto + tracking email", "kind": "doc", "stack": "Adapter pattern courier"}]}, {"num": "04", "name": "Post-venta", "boxes": [{"code": "P06-04", "label": "NPS · reseña · upsell", "kind": "notify", "stack": "Cerebro email + UI"}]}]}, "P07": {"title": "P07 · Venta B2G Mercado Público", "sub": "Detección licitación · postular · adjudicar", "callout": "Margen menor pero ticket alto. Ciclo más largo (días hasta semanas).", "tags": ["B2G", "Factura DTE 33"], "stages": [{"num": "01", "name": "Detectar", "boxes": [{"code": "P07-01", "label": "Sync licitaciones diarias 8am", "kind": "search", "stack": "MP API cron"}]}, {"num": "02", "name": "Postular", "boxes": [{"code": "P07-02", "label": "Generar oferta Cerebro", "kind": "create", "stack": "Template + AI"}, {"code": "P07-03", "label": "Enviar a MP", "kind": "notify", "stack": "MP API POST"}]}, {"num": "03", "name": "Adjudicar", "boxes": [{"code": "P07-04", "label": "Webhook resultado", "kind": "notify", "stack": "MP webhook"}]}, {"num": "04", "name": "Despacho + Factura", "boxes": [{"code": "P07-05", "label": "Guía + factura DTE 33", "kind": "doc", "stack": "Open Factura"}]}]}, "P08": {"title": "P08 · Venta B2B empresa privada", "sub": "RFQ · cotización · aprobación · despacho", "callout": "Ticket más alto · pago a 30/60/90 días · requiere historial cuentas y precios negociados.", "tags": ["B2B", "Pago diferido"], "stages": [{"num": "01", "name": "RFQ", "boxes": [{"code": "P08-01", "label": "Cliente envía RFQ", "kind": "create", "stack": "Portal B2B"}]}, {"num": "02", "name": "Cotizar", "boxes": [{"code": "P08-02", "label": "Pricing engine con descuentos volumen", "kind": "create", "stack": "Cerebro pricing"}]}, {"num": "03", "name": "Aprobar", "boxes": [{"code": "P08-03", "label": "Click aprobación cliente · firma HMAC", "kind": "update", "stack": "Portal B2B firma"}]}, {"num": "04", "name": "Cerrar", "boxes": [{"code": "P08-04", "label": "Despacho LTL · factura DTE 33", "kind": "doc", "stack": "Open Factura"}]}]}, "P09": {"title": "P09 · Fulfillment despacho", "sub": "Cotización · etiqueta · tracking · entrega", "callout": "Cross-cutting · usado por P05/P06/P07/P08. Adapter Pattern también acá: misma interfaz · distinto courier.", "tags": ["Logística", "Cross-canal"], "stages": [{"num": "01", "name": "Cotizar", "boxes": [{"code": "P09-01", "label": "Cotización por peso/volumen", "kind": "search", "stack": "Adapter courier"}]}, {"num": "02", "name": "Generar etiqueta", "boxes": [{"code": "P09-02", "label": "Etiqueta PDF + número tracking", "kind": "doc", "stack": "Courier API"}]}, {"num": "03", "name": "Tracking", "boxes": [{"code": "P09-03", "label": "Webhook updates courier", "kind": "notify", "stack": "Courier webhook"}]}, {"num": "04", "name": "Entrega", "boxes": [{"code": "P09-04", "label": "Confirmación entregado", "kind": "update", "stack": "Webhook final"}]}]}, "P10": {"title": "P10 · Devolución", "sub": "Opcional · ojalá poco · proceso reversa", "callout": "Devolución del cliente. Coordinación con courier en logística reversa. Nota de crédito SII si aplica.", "tags": ["Reversa", "Nota crédito DTE 61"], "stages": [{"num": "01", "name": "Solicitud", "boxes": [{"code": "P10-01", "label": "Cliente solicita devolución", "kind": "notify", "stack": "Soporte ticket / canal"}]}, {"num": "02", "name": "Aprobar", "boxes": [{"code": "P10-02", "label": "Validar política devolución", "kind": "search", "stack": "Reglas operador"}]}, {"num": "03", "name": "Logística reversa", "boxes": [{"code": "P10-03", "label": "Etiqueta courier reversa", "kind": "doc", "stack": "Courier API reverse"}]}, {"num": "04", "name": "Refund + NC", "boxes": [{"code": "P10-04", "label": "Reverso pago + DTE 61 nota crédito", "kind": "pay", "stack": "Pasarela + Open Factura"}]}]}, "P11": {"title": "P11 · Facturación electrónica", "sub": "DTE 33 · 39 · 61 · SII", "callout": "Cross-cutting con SII. Requiere autorización previa de tipos en SII. Status SMC SpA: solo exenta autorizada, pedir 33/39/61.", "tags": ["SII Chile", "DTE auto"], "stages": [{"num": "01", "name": "Trigger evento", "boxes": [{"code": "P11-01", "label": "Orden cerrada · monto > 0", "kind": "notify", "stack": "Evento pg_notify"}]}, {"num": "02", "name": "Determinar tipo DTE", "boxes": [{"code": "P11-02", "label": "39 boleta · 33 factura · 61 NC", "kind": "search", "stack": "Lógica negocio"}]}, {"num": "03", "name": "Emitir", "boxes": [{"code": "P11-03", "label": "POST a Open Factura", "kind": "doc", "stack": "Open Factura API"}]}, {"num": "04", "name": "Archivar", "boxes": [{"code": "P11-04", "label": "PDF al storage + email cliente", "kind": "doc", "stack": "Supabase Storage"}]}]}, "P12": {"title": "P12 · Conciliación financiera", "sub": "Pagos recibidos · DTE emitido · libro mayor", "callout": "Cierre del ciclo. Reconciliar lo que se cobró vs lo que se facturó. Reportes contador galvarez.cl mensual.", "tags": ["Contable", "F29 mensual"], "stages": [{"num": "01", "name": "Importar movimientos", "boxes": [{"code": "P12-01", "label": "Bank statement / pasarelas", "kind": "search", "stack": "Manual fase 1 · API fase 2"}]}, {"num": "02", "name": "Matching", "boxes": [{"code": "P12-02", "label": "Match pagos vs DTE", "kind": "search", "stack": "Lógica + cerebro asistencia"}]}, {"num": "03", "name": "Reporte mensual", "boxes": [{"code": "P12-03", "label": "Export contador galvarez.cl", "kind": "doc", "stack": "Excel + PDF"}]}, {"num": "04", "name": "F29 SII", "boxes": [{"code": "P12-04", "label": "Declaración mensual IVA", "kind": "doc", "stack": "SII Chile"}]}]}, "P13": {"title": "P13 · Dropshipping", "sub": "Vender sin stock propio · proveedor despacha directo al cliente final", "callout": "Modo paralelo al stock propio. Catálogo amplio sin capital atado. El producto se publica en canales sin tenerlo en bodega. Cuando entra venta · se propaga orden al proveedor (chileno o internacional) que despacha directo al cliente final.", "tags": ["Sin capital atado", "Margen 10-25%", "Escala catálogo rápido"], "notes": "Dropshipping permite explorar demanda sin riesgo · ideal Y1 para SKUs nuevos · para SKUs validados luego pasar a stock propio (P01-P02) para mejor margen.", "stages": [{"num": "01", "name": "Catálogo proveedor dropship", "boxes": [{"code": "P13-01", "label": "Sync catálogo proveedor (Supplier Adapter)", "kind": "search", "stack": "API · feed XML · CSV · scraping manual fallback"}, {"code": "P13-02", "label": "Filtrar SKUs aprobados · margen viable", "kind": "search", "stack": "Cerebro scoring + reglas operador"}]}, {"num": "02", "name": "Publicación cross-canal", "boxes": [{"code": "P13-03", "label": "Publicar en canales con flag is_dropship=true", "kind": "create", "stack": "Mismo Channel Adapter · marca producto como sin stock propio"}]}, {"num": "03", "name": "Venta cliente final", "boxes": [{"code": "P13-04", "label": "Webhook canal · orden recibida", "kind": "notify", "stack": "Mismo flujo que stock propio P05-P08"}]}, {"num": "04", "name": "Propagar OC al proveedor", "boxes": [{"code": "P13-05", "label": "Crear OC al proveedor dropship (Supplier Adapter)", "kind": "create", "stack": "API proveedor · API key · email automatizado · WhatsApp Business"}, {"code": "P13-06", "label": "Confirmar disponibilidad real-time", "kind": "search", "stack": "Si proveedor responde stock=0 · refund cliente + comunicación"}]}, {"num": "05", "name": "Despacho directo proveedor → cliente", "boxes": [{"code": "P13-07", "label": "Proveedor despacha al cliente · tracking compartido", "kind": "doc", "stack": "Courier del proveedor · webhook tracking · nuestro nombre en remitente opcional"}]}, {"num": "06", "name": "Cobro + factura nuestra", "boxes": [{"code": "P13-08", "label": "Cobro pasarela cliente + DTE emitido (mismo P11)", "kind": "pay", "stack": "Open Factura · DTE a nombre SMC SpA"}]}, {"num": "07", "name": "Liquidación al proveedor", "boxes": [{"code": "P13-09", "label": "Pagar al proveedor menos comisión nuestra", "kind": "pay", "stack": "Transferencia 7-15 días post-venta · acuerdo bilateral"}]}]}}}</script>

# p1

<h2><span class="h2-num">P01</span>Sourcing · búsqueda de productos</h2>
  <div class="proc-card">
    <div class="proc-grid">
      <div class="proc-cell">**Actor**Operador + IA Cerebro (sugerencias)</div>
      <div class="proc-cell">**Trigger**Ampliar catálogo · stock bajo · oportunidad detectada</div>
      <div class="proc-cell">**Inputs**keyword · presupuesto · márgenes mínimos</div>
      <div class="proc-cell">**Outputs**Brief Sourcing (PDF + DB)</div>
    </div>
    
### Pasos

    <ol class="steps-list">
      <li>Operador define categoría/nicho a explorar (ej: "audífonos bluetooth")</li>
      <li>Sistema consulta histórico rotación SKUs similares</li>
      <li>IA sugiere keywords trending MeLi · precios competencia · márgenes</li>
      <li>Operador filtra: 3-5 candidatos</li>
      <li>Sistema arma "Brief Sourcing" con specs · MOQ · precio target</li>
      <li>Brief queda en `/sourcing/briefs/{id}` · pasa a P02</li>
    </ol>
    <div class="proc-grid">
      <div class="proc-cell">**Eventos**`sourcing.brief.created`</div>
      <div class="proc-cell">**KPIs**time-to-brief · % briefs que llegan a compra</div>
    </div>
  </div>

# p2

<h2><span class="h2-num">P02</span>Compra a Nexport (intermediario importador)</h2>
  <div class="proc-card">
    <div class="proc-grid">
      <div class="proc-cell">**Actor**Operador + Nexport</div>
      <div class="proc-cell">**Trigger**Brief Sourcing aprobado</div>
      <div class="proc-cell">**Inputs**Brief aprobado</div>
      <div class="proc-cell">**Outputs**OC · pago registrado · shipment</div>
    </div>
    
### Pasos

    <ol class="steps-list">
      <li>Operador envía Brief a Nexport (WhatsApp · email · portal)</li>
      <li>Nexport cotiza en CLP+IVA + lead time</li>
      <li>Operador registra cotización en `/sourcing/quotes/{id}`</li>
      <li>Operador emite OC en Hub con términos pago (ej: 50% adelanto · 50% B/L)</li>
      <li>Transferencia primer pago · registro CxP</li>
      <li>Nexport confirma · envía tracking estimado</li>
      <li>Hub crea registro shipment `/sourcing/shipments/{id}` con ETA</li>
    </ol>
    <div class="box box-info">
      <div class="box-title">💡 Notas legales</div>
      <ul style="margin:0">
        <li>Factura llega de Nexport (proveedor chileno · CLP + IVA 19%)</li>
        <li>IVA crédito se acumula en F29 mes correspondiente</li>
        <li>NO hay tipo de cambio · NO hay aduana de tu lado</li>
      </ul>
    </div>
    <div class="proc-grid">
      <div class="proc-cell">**Eventos**`purchase.po.created` · `purchase.payment.made` · `purchase.shipment.in-transit`</div>
      <div class="proc-cell">**KPIs**time-to-PO · % OC en plazo · variación precio</div>
    </div>
  </div>

# p3

<h2><span class="h2-num">P03</span>Recepción en bodega</h2>
  <div class="proc-card">
    <div class="proc-grid">
      <div class="proc-cell">**Actor**Operador (o bodeguero futuro)</div>
      <div class="proc-cell">**Trigger**Llegada física de mercadería</div>
      <div class="proc-cell">**Inputs**Mercadería + OC referenciada</div>
      <div class="proc-cell">**Outputs**Stock disponible + acta firmada</div>
    </div>
    
### Pasos

    <ol class="steps-list">
      <li>Recibe paquete · verifica embalaje</li>
      <li>Hub → /warehouse/recepcion → escanea código OC (QR de P02)</li>
      <li>Hub muestra lista esperada (SKU · cantidad · descripción)</li>
      <li>Cuenta físicamente · marca cada SKU como recibido</li>
      <li>Si discrepancia (cantidad menor · daños) → registra novedad + foto</li>
      <li>Asigna ubicación física (rack · pasillo · bin)</li>
      <li>Hub actualiza `inventory.physical_stock` · genera etiquetas barcode</li>
      <li>Genera Acta de Recepción PDF (firmable digital)</li>
    </ol>
    <div class="box box-decision">
      <div class="box-title">📒 Asiento contable automático</div>
      <pre style="margin:0; font-size:11px;">DEBE: Mercadería (existencia) por valor neto compra
HABER: Proveedores (Nexport) por valor compra
+ asiento separado IVA crédito si aplica</pre>
    </div>
  </div>

# p4

<h2><span class="h2-num">P04</span>Publicación cross-canal</h2>
  <div class="proc-card">
    <div class="proc-grid">
      <div class="proc-cell">**Actor**Operador + Sistema (auto-publish)</div>
      <div class="proc-cell">**Trigger**Producto nuevo en inventario · o publicar existente en canal nuevo</div>
    </div>
    
### Pasos

    <ol class="steps-list">
      <li>Operador entra a `/inventory/sku/{id}` · "Publicar en canales"</li>
      <li>Hub muestra checklist: MeLi · D2C · Mercado Público · B2B · Falabella (si conectados)</li>
      <li>Operador marca canales destino</li>
      <li>Hub aplica `price-rules` por canal (landed cost + markup + comisión + IVA)</li>
      <li>Operador revisa precio sugerido por canal · ajusta si quiere</li>
      <li>Hub llama al adapter de cada canal seleccionado</li>
      <li>Cada adapter responde OK/error · Hub registra estado en `inventory.channel_sync_status`</li>
    </ol>
    <div class="box box-premise">
      <div class="box-title">🎯 Premisa core</div>
      <p style="margin:0">**publicar en N canales = 1 click. No 4 forms.**</p>
    </div>
  </div>

# p5

<h2><span class="h2-num">P05</span>Venta MeLi (B2C marketplace ajeno)</h2>
  <div class="proc-card">
    
### Flujo

    <ol class="steps-list">
      <li>MeLi envía webhook a `/api/webhooks/meli` con orden nueva</li>
      <li>Hub valida HMAC · crea registro `orders` con `channel='meli'`</li>
      <li>Hub reserva stock (`inventory.reservations` +1)</li>
      <li>Cliente queda como `customers` con `is_meli_anonymous=true`</li>
      <li>Hub crea task fulfillment → cola `/fulfillment/pendientes`</li>
      <li>Operador gestiona despacho (P09)</li>
      <li>MeLi confirma pago liberado (14-21 días) → registro `payments` status=paid</li>
      <li>CxC contra MeLi se actualiza</li>
    </ol>
    <div class="box box-warning">
      <div class="box-title">⚠️ Excepciones críticas</div>
      <ul style="margin:0">
        <li>Webhook duplicado · check idempotency obligatorio</li>
        <li>Stock insuficiente · OVERSELL · alerta crítica · NO debe pasar nunca</li>
      </ul>
    </div>
  </div>

# p6

<h2><span class="h2-num">P06</span>Venta D2C (storefront propio)</h2>
  <div class="proc-card">
    
### Flujo

    <ol class="steps-list">
      <li>Cliente en storefront de marca propia agrega productos al carrito</li>
      <li>Checkout: ingresa datos + paga (WebPay/MercadoPago/transferencia)</li>
      <li>Hub recibe orden vía API directa (no webhook · es nuestro propio storefront)</li>
      <li>Mismo flow MeLi: orden + reserva stock + customer + task fulfillment</li>
      <li>Cliente queda como `customers` con datos completos (no anónimo)</li>
      <li>Boleta/factura electrónica se emite automático (P11)</li>
      <li>Pago se acredita (WebPay 24h · transferencia manual)</li>
    </ol>
    <div class="proc-grid">
      <div class="proc-cell">**Eventos**`order.created` · `dte.issued` · `payment.received`</div>
      <div class="proc-cell">**KPIs**conversion rate · ticket promedio · abandono carrito</div>
    </div>
  </div>

# p7

<h2><span class="h2-num">P07</span>Venta B2G · Mercado Público (Estado)</h2>
  <div class="proc-card">
    
### Flujo

    <ol class="steps-list">
      <li>Hub monitorea API Mercado Público diariamente</li>
      <li>Filtra licitaciones por categorías propias · región · monto</li>
      <li>Operador revisa "Bandeja Oportunidades" `/channels/mp/licitaciones-abiertas`</li>
      <li>Decide ofertar → "Preparar oferta"</li>
      <li>Hub pre-llena form con productos catálogo CM + precio + plazo entrega</li>
      <li>Operador adjunta certificados · garantía bancaria si aplica</li>
      <li>Hub envía oferta vía API MP (o exporta XML para upload manual)</li>
      <li>Si adjudican → orden con `channel='mp'`</li>
      <li>Operador entrega · genera acta recepción Estado</li>
      <li>Hub emite factura · carga en sistema MP</li>
      <li>Estado paga 30-90 días después · Hub trackea CxC</li>
    </ol>
    <div class="box box-warning">
      <div class="box-title">⚠️ Plazo pago Estado</div>
      <p style="margin:0">30-90 días post entrega · planificar cash flow · NO depender de pago rápido B2G</p>
    </div>
  </div>

# p8

<h2><span class="h2-num">P08</span>Venta B2B (empresa privada)</h2>
  <div class="proc-card">
    
### Flujo

    <ol class="steps-list">
      <li>Operador crea/busca cliente en `/channels/b2b/clientes`</li>
      <li>"Nueva cotización" → arma quote (SKUs + cantidades + precio mayorista)</li>
      <li>Hub genera PDF cotización · envía email automático al cliente</li>
      <li>Cliente aprueba (responde email o click link aprobación)</li>
      <li>Hub convierte cotización en orden · reserva stock · crea task fulfillment</li>
      <li>Hub emite factura electrónica (33)</li>
      <li>Operador despacha (P09)</li>
      <li>Cliente paga según términos (normalmente 15-30 días)</li>
      <li>Hub trackea CxC (P12)</li>
    </ol>
    <div class="proc-grid">
      <div class="proc-cell">**KPIs**conversion quote→orden · ticket promedio B2B · % cobrado en tiempo</div>
      <div class="proc-cell">**Eventos**`b2b.quote.created` · `b2b.quote.approved`</div>
    </div>
  </div>

# p9

<h2><span class="h2-num">P09</span>Fulfillment · despacho</h2>
  <div class="proc-card">
    
### Flujo

    <ol class="steps-list">
      <li>Operador entra a `/fulfillment/pendientes` · ve cola priorizada</li>
      <li>Hub genera picking list (qué SKU sacar de qué ubicación)</li>
      <li>Operador hace picking físico · marca SKUs picked</li>
      <li>Packing: arma paquete · pesa · mide</li>
      <li>Hub elige courier según regla (MeLi → Chilexpress · B2B → Starken)</li>
      <li>API courier genera etiqueta envío</li>
      <li>Operador pega etiqueta · entrega a retiro courier</li>
      <li>Hub registra tracking number · monitorea estado</li>
      <li>Cuando courier marca entregado → Hub actualiza orden status=delivered</li>
      <li>Webhook al canal correspondiente confirma entrega</li>
    </ol>
    <div class="box box-decision">
      <div class="box-title">📒 Asiento contable automático (al shipped)</div>
      <pre style="margin:0; font-size:11px;">DEBE: Costo de venta (CMV) por landed cost
HABER: Mercadería (existencia) por landed cost</pre>
    </div>
  </div>

# p10

<h2><span class="h2-num">P10</span>Devolución (opcional · ojalá poco)</h2>
  <div class="proc-card">
    
### Flujo

    <ol class="steps-list">
      <li>Cliente solicita por canal correspondiente (motivo: defecto · arrepentimiento · diferente al esperado)</li>
      <li>Operador valida motivo · aprueba RMA</li>
      <li>Hub crea ticket `/fulfillment/devoluciones/{id}`</li>
      <li>Cliente envía producto de vuelta</li>
      <li>Operador recibe · inspecciona estado</li>
      <li>Si OK · stock vuelve a inventario (`inventory.adjustments` IN)</li>
      <li>Hub emite Nota de Crédito Electrónica (NC 61) al canal de origen</li>
      <li>Reembolsa pago al cliente (transferencia · WebPay reverse)</li>
    </ol>
  </div>

# p11

<h2><span class="h2-num">P11</span>Facturación · DTE Chile</h2>
  <div class="proc-card">
    
### Flujo

    <ol class="steps-list">
      <li>Orden status=approved → Hub trigger emisión DTE</li>
      <li>Decide tipo documento según cliente:
        
- Persona natural sin RUT → **Boleta Electrónica (39)**
- Empresa con RUT → **Factura Electrónica (33)**
- Cliente exento → **Factura Exenta (34)**

      </li>
      <li>Llama API Open Factura (o SII MIPYME directo)</li>
      <li>Recibe folio + XML firmado + PDF</li>
      <li>Guarda en `dte.documents`</li>
      <li>Envía PDF al cliente por email</li>
      <li>Reporta automático al SII (libro IVA digital)</li>
    </ol>
    <div class="box box-decision">
      <div class="box-title">📒 Asiento contable automático</div>
      <pre style="margin:0; font-size:11px;">DEBE: Clientes (cuentas por cobrar) por total con IVA
HABER: Ventas afectas por neto
HABER: IVA débito por IVA</pre>
    </div>
  </div>

# p12

<h2><span class="h2-num">P12</span>Cobranza</h2>
  <div class="proc-card">
    
### Flujo

    <ol class="steps-list">
      <li>Hub monitorea diariamente `/finanzas/cuentas-por-cobrar`</li>
      <li>Calcula días restantes hasta vencimiento por cliente/canal</li>
      <li>5 días antes → recordatorio automático cliente (email)</li>
      <li>0 días → alerta operador</li>
      <li>+7 días → segundo recordatorio + alerta amarilla</li>
      <li>+15 días → llamada manual del operador</li>
      <li>+30 días → escalamiento (gestión cobranza)</li>
      <li>Pago llega → conciliación · Hub matchea pago con factura → `paid`</li>
      <li>Genera asiento contable</li>
    </ol>
    <div class="box box-decision">
      <div class="box-title">📒 Asiento contable automático (al cobrar)</div>
      <pre style="margin:0; font-size:11px;">DEBE: Bancos (cuenta corriente) por monto recibido
HABER: Clientes (CxC) por monto recibido</pre>
    </div>
  </div>

# p13

<h2><span class="h2-num">P13</span>Dropshipping multi-proveedor (Fase 3+)</h2>
  <div class="proc-card">
    
### Flujo

    <ol class="steps-list">
      <li>Founder registra proveedor con auth_mode (api_key · oauth · email · whatsapp) vía POST /api/suppliers</li>
      <li>Cron 6h sync catálogo proveedor → mkt_supplier_products</li>
      <li>SKUs filtrados por margen 15%+ entran al catálogo SMC con is_dropship=true</li>
      <li>Publicación a canales (MeLi · D2C · MP) marca producto como dropship internamente</li>
      <li>Venta entra por cualquier canal → webhook procesado igual</li>
      <li>Si is_dropship=true → POST /api/suppliers/:id/purchase-orders propaga OC al proveedor</li>
      <li>Confirmar stock disponible real-time · si stock=0 refund + email comprador automático</li>
      <li>Proveedor despacha directo al cliente final · webhook tracking sync con order SMC</li>
      <li>Cobro a cliente final · DTE emitido a nombre SMC SpA · proveedor cobra a SMC 7-15d después</li>
      <li>Cerebro monitor: si SKU > $5M CLP/mes 2 meses → alerta migración stock local</li>
    </ol>
    <div class="box box-decision">
      <div class="box-title">📒 Modelo dropshipping vs stock local</div>
      <ul style="margin:0; font-size:12px;">
        <li><strong>Dropshipping</strong>: margen 10-25% · sin capital atado · escala catálogo rápido</li>
        <li><strong>Stock local</strong>: margen 28-40% · capital atado · ciclo despacho propio</li>
        <li><strong>Estrategia</strong>: dropship para PROBAR · stock local cuando funciona</li>
      </ul>
    </div>
  </div>

# p14

<h2><span class="h2-num">P14</span>Publicidad multicanal (Mercado Ads · Meta · Google · TikTok)</h2>
  <div class="proc-card">
    
### Flujo

    <ol class="steps-list">
      <li>Founder conecta cuentas publicitarias con OAuth vía POST /api/ads/accounts (4 providers)</li>
      <li>Crea campaña multi-canal con presupuesto + SKUs promocionados vía POST /api/ads/campaigns</li>
      <li>Cron diario sync métricas de cada provider → mkt_ads_metrics (impressions · clicks · conv · spend · revenue)</li>
      <li>Trigger Postgres calcula ROAS auto · si &lt;1.5 por 7 días → pg_notify('ads_roas_low')</li>
      <li>Listener dispara alerta UI founder · sugerencia pausa o cambio creatividad</li>
      <li>Conversion events server-side: cada venta → POST /api/ads/events con event_id idempotente</li>
      <li>Cron 5min envía batch events a Meta CAPI · Google Enhanced Conversions · TikTok Events</li>
      <li>Cada provider devuelve attribution · sync con campaign metrics</li>
      <li>Dashboard ROAS consolidado cross-provider · drill-down por SKU/canal</li>
      <li>Y2 escalado: pixels client-side D2C storefront + retargeting audiences custom</li>
    </ol>
    <div class="box box-decision">
      <div class="box-title">📒 Por qué server-side (CAPI/Enhanced/Events)</div>
      <ul style="margin:0; font-size:12px;">
        <li><strong>iOS 14.5+ tracking</strong>: pixels client-side perdieron 60% accuracy · CAPI recupera</li>
        <li><strong>Ad blockers</strong>: 20-30% usuarios bloquean pixels · server-side bypass</li>
        <li><strong>Idempotency</strong>: event_id evita doble counting cuando ambos pixel+CAPI activos</li>
        <li><strong>Privacy</strong>: hashed PII (SHA-256 email/phone) sigue Ley 19.628 + GDPR</li>
      </ul>
    </div>
    <div class="box box-anti">
      <div class="box-title">🚫 Anti-patrones</div>
      <ul style="margin:0; font-size:12px;">
        <li>Activar todos los providers desde día 1 · empezar 1 (Mercado Ads · ya conectado a MeLi)</li>
        <li>Subir presupuesto sin medir 14 días · esperar señal ROAS estable</li>
        <li>Olvidar pausar campañas obsoletas · presupuesto sigue corriendo</li>
        <li>Atribución last-click solo · usar multi-touch en Y2</li>
      </ul>
    </div>
  </div>

# tr

<h2><span class="h2-num">T</span>Procesos transversales</h2>
  <table>
    <thead><tr><th>ID</th><th>Proceso</th><th>Qué hace</th></tr></thead>
    <tbody>
      <tr><td>**T1**</td><td>Contabilidad automática (event-driven)</td><td>Cada evento de los 12 procesos dispara asientos contables en plan de cuentas configurable. F29 mensual + libro IVA + auxiliar de clientes/proveedores automático.</td></tr>
      <tr><td>**T2**</td><td>Inventario real-time (SSoT)</td><td>Cada venta/recepción/devolución/merma actualiza inventario inmediato. Cross-canal sincroniza stock vía webhook a cada adapter.</td></tr>
      <tr><td>**T3**</td><td>Cerebro IA (sugerencias proactivas)</td><td>Analiza data de los 12 procesos · genera alertas: "stock bajo SKU X" · "MeLi vendiste 30% menos esta semana" · "comprá más del proveedor Y".</td></tr>
      <tr><td>**T4**</td><td>Compliance (vencimientos y validaciones)</td><td>F30/F30-1 · garantías bancarias · vigencia ChileProveedores · libro IVA digital · F22 anual. Alertas antes de vencer.</td></tr>
      <tr><td>**T5**</td><td>Analytics (cross-data)</td><td>Dashboards consolidados por canal · marca · vertical · producto. Decisiones de pricing · canal · sourcing basadas en margen real.</td></tr>
    </tbody>
  </table>

  <div class="box box-premise" style="margin-top: 32px;">
    <div class="box-title">🎯 Premisa CORE recordada</div>
    <p style="margin:0">**NO duplicar esfuerzo · NO duplicar data · NO duplicar lógica.**</p>
    <ul style="margin:8px 0 0">
      <li>1 inventario para los 12 procesos</li>
      <li>1 catálogo de clientes</li>
      <li>1 plan de cuentas</li>
      <li>1 tabla de órdenes (con channel como columna)</li>
      <li>N adapters por canal externo</li>
    </ul>
  </div>
