---
number: 03
id: requirements
title: Requirements
subtitle: "Funcionales + no funcionales · qué debe hacer el sistema y con qué calidad."
block: Marketplace SMC
author: PM + Architect + Cerebro
version: 1.0
date: 2026-05-25
status: 🟢 Activo
prev: index.html
next: index.html
---

# 01 · Sistema de priorización

<div class="box box-premise">
    <div class="box-title">🎯 Hilo conductor · Estrategia Y1 Reputation First</div>
    
Toda priorización Y1 sigue la **Estrategia Y1 · Reputation First** (ver [Doc 17](17-estrategia-y1.html)). Features que habilitan las 4 fases (Reputación → Escala → Diversificación → Consolidación) son P1. Features que NO mueven el hito de fase actual son P3-P4.

    
- **Q4 2026 · Fase 1 Reputación** · P1 = publicar con fotos pro · gestionar reputación · despachar ágil para llegar a 10 ventas verdes
- **Q1 2027 · Fase 2 Escala** · P1 = Mercado Ads · Full Fulfillment MeLi · tracking medallas
- **Q2 2027 · Fase 3 Diversificación** · P1 = Mercado Público sync · B2B RFQ · portal cliente
- **Q3 2027 · Fase 4 Consolidación** · P1 = analytics consolidados · evaluación Nexport · ajustes data-driven

  </div>

  <table>
    <thead><tr><th>Nivel</th><th>Etiqueta</th><th>Significa</th></tr></thead>
    <tbody>
      <tr><td><span class="badge badge-blocked">P1</span></td><td>Crítico</td><td>Sin esto la fase Y1 actual NO avanza · habilita hito de la fase</td></tr>
      <tr><td><span class="badge badge-pending">P2</span></td><td>Importante</td><td>Necesario fase siguiente · puede esperar 1-2 sprints</td></tr>
      <tr><td><span class="badge badge-future">P3</span></td><td>Deseable</td><td>Mejora UX · agrega valor · planificable Q3-Q4 Y1 o Y2</td></tr>
      <tr><td><span class="badge badge-future">P4</span></td><td>Opcional</td><td>Nice-to-have · solo si hay capacidad sobrante</td></tr>
    </tbody>
  </table>

# 02 · Funcionales · Inventario &amp; Catálogo

<div class="req-card req-prio-1"><span class="req-id">FR-INV-01</span>**P1** · El sistema debe mantener UN inventario físico maestro por tenant · con stock real-time.</div>
  <div class="req-card req-prio-1"><span class="req-id">FR-INV-02</span>**P1** · El sistema debe permitir SKU master con: código interno, EAN/UPC, dimensiones, peso, categorías, variantes (talla/color).</div>
  <div class="req-card req-prio-1"><span class="req-id">FR-INV-03</span>**P1** · El sistema debe descontar stock al confirmar venta en CUALQUIER canal · sincronización inmediata cross-canal.</div>
  <div class="req-card req-prio-1"><span class="req-id">FR-INV-04</span>**P1** · El sistema debe permitir ajustes manuales con motivo (merma, daño, recuento, devolución).</div>
  <div class="req-card req-prio-2"><span class="req-id">FR-INV-05</span>**P2** · El sistema debe soportar reservas (stock asignado a orden pendiente vs físico disponible).</div>
  <div class="req-card req-prio-2"><span class="req-id">FR-INV-06</span>**P2** · El sistema debe asignar ubicaciones físicas (rack/pasillo/estante/bin) a cada SKU.</div>
  <div class="req-card req-prio-3"><span class="req-id">FR-INV-07</span>**P3** · El sistema debe soportar múltiples bodegas (Stgo + regiones) con stock por bodega.</div>
  <div class="req-card req-prio-3"><span class="req-id">FR-INV-08</span>**P3** · El sistema debe generar etiquetas barcode imprimibles (Code 128, QR).</div>

# 03 · Funcionales · Ventas Multi-Canal

<div class="req-card req-prio-1"><span class="req-id">FR-CH-01</span>**P1** · El sistema debe publicar 1 SKU en N canales con 1 click (Channel Adapter Pattern).</div>
  <div class="req-card req-prio-1"><span class="req-id">FR-CH-02</span>**P1** · El sistema debe aplicar pricing diferenciado por canal (landed + markup + comisión + IVA).</div>
  <div class="req-card req-prio-1"><span class="req-id">FR-CH-03</span>**P1** · Cada canal debe implementar interfaz CanalAdapter con métodos: publish, syncStock, fetchOrders, fulfillOrder, syncPrice.</div>
  <div class="req-card req-prio-1"><span class="req-id">FR-CH-04</span>**P1** · El sistema debe recibir webhooks de canales externos (MeLi, Falabella futuro) con HMAC validation.</div>
  <div class="req-card req-prio-1"><span class="req-id">FR-CH-05</span>**P1** · El sistema debe registrar TODA orden en tabla común `orders` con columna `channel` (no tablas separadas).</div>
  <div class="req-card req-prio-2"><span class="req-id">FR-CH-06</span>**P2** · El sistema debe soportar quote builder B2B (selección SKUs → PDF cotización → aprobación email).</div>
  <div class="req-card req-prio-2"><span class="req-id">FR-CH-07</span>**P2** · El sistema debe monitorear API Mercado Público diariamente · filtrar licitaciones por keywords del operador.</div>
  <div class="req-card req-prio-2"><span class="req-id">FR-CH-08</span>**P2** · El sistema debe permitir storefront D2C con checkout propio (carrito + pasarela).</div>
  <div class="req-card req-prio-3"><span class="req-id">FR-CH-09</span>**P3** · El sistema debe soportar canal "manual" (Cencosud · scrape semanal + upload CSV).</div>

# 04 · Funcionales · Sourcing &amp; Supply Chain

<div class="req-card req-prio-2"><span class="req-id">FR-SUP-01</span>**P2** · El sistema debe gestionar proveedores (Nexport · futuros) con CRM ligero.</div>
  <div class="req-card req-prio-2"><span class="req-id">FR-SUP-02</span>**P2** · El sistema debe permitir órdenes de compra (PO) con términos de pago (50/50 · 100% adelanto · etc).</div>
  <div class="req-card req-prio-2"><span class="req-id">FR-SUP-03</span>**P2** · El sistema debe trackear shipments con ETA · alertas pre-arribo.</div>
  <div class="req-card req-prio-2"><span class="req-id">FR-SUP-04</span>**P2** · El sistema debe registrar recepción con match contra PO · detectar discrepancias (cantidad/daños).</div>
  <div class="req-card req-prio-1"><span class="req-id">FR-SUP-05</span>**P1** · El sistema debe calcular landed cost por SKU (FOB + flete + IVA + transporte interno).</div>
  <div class="req-card req-prio-1"><span class="req-id">FR-SUP-06</span>**P1** · El sistema debe integrarse con couriers (Chilexpress · Starken · Bluexpress) para generar etiquetas envío.</div>
  <div class="req-card req-prio-2"><span class="req-id">FR-SUP-07</span>**P2** · El sistema debe permitir reglas de despacho ("MeLi → Chilexpress" · "B2B → Starken").</div>
  <div class="req-card req-prio-3"><span class="req-id">FR-SUP-08</span>**P3** · El sistema debe gestionar devoluciones (RMA) con flujo aprobación + NC.</div>

# 05 · Funcionales · Finanzas &amp; Contabilidad

<div class="req-card req-prio-1"><span class="req-id">FR-FIN-01</span>**P1** · El sistema debe emitir DTE (Factura 33, Boleta 39, NC 61, ND 56, Factura Exenta 34) vía Open Factura o SII MIPYME.</div>
  <div class="req-card req-prio-1"><span class="req-id">FR-FIN-02</span>**P1** · El sistema debe generar asientos contables automáticos por cada evento (venta · compra · pago · devolución).</div>
  <div class="req-card req-prio-1"><span class="req-id">FR-FIN-03</span>**P1** · El sistema debe mantener cuentas por cobrar (CxC) y por pagar (CxP) con vencimientos.</div>
  <div class="req-card req-prio-1"><span class="req-id">FR-FIN-04</span>**P1** · El sistema debe alertar facturas vencidas: 5 días antes · al día · +7 · +15 · +30.</div>
  <div class="req-card req-prio-2"><span class="req-id">FR-FIN-05</span>**P2** · El sistema debe calcular margen real por SKU = Precio − Landed − Comisión canal − Logística − IVA débito.</div>
  <div class="req-card req-prio-2"><span class="req-id">FR-FIN-06</span>**P2** · El sistema debe pre-generar resumen para F29 mensual (ventas afectas + IVA débito + IVA crédito).</div>
  <div class="req-card req-prio-2"><span class="req-id">FR-FIN-07</span>**P2** · El sistema debe forecastear flujo de caja a 30/60/90 días.</div>
  <div class="req-card req-prio-3"><span class="req-id">FR-FIN-08</span>**P3** · El sistema debe sugerir precio óptimo por canal vía IA (vs competencia · margen target).</div>

# 06 · Funcionales · IA &amp; Analytics

<div class="req-card req-prio-2"><span class="req-id">FR-AI-01</span>**P2** · El sistema debe ofrecer chat IA contextual sobre la data del operador (Cerebro IA).</div>
  <div class="req-card req-prio-2"><span class="req-id">FR-AI-02</span>**P2** · El sistema debe generar insights semanales auto-reporte (lunes 9am).</div>
  <div class="req-card req-prio-3"><span class="req-id">FR-AI-03</span>**P3** · El sistema debe sugerir SKUs a re-comprar según rotación + lead time proveedor.</div>
  <div class="req-card req-prio-2"><span class="req-id">FR-AN-01</span>**P2** · El sistema debe mostrar dashboard consolidado: revenue · margen · órdenes · ticket promedio · split por canal.</div>
  <div class="req-card req-prio-2"><span class="req-id">FR-AN-02</span>**P2** · El sistema debe permitir drill-down por canal · marca (tenant) · vertical · producto · período.</div>
  <div class="req-card req-prio-3"><span class="req-id">FR-AN-03</span>**P3** · El sistema debe analizar rotación por SKU · top performers · slow movers.</div>
  <div class="req-card req-prio-3"><span class="req-id">FR-AN-04</span>**P3** · El sistema debe medir ROI por canal de venta y por proveedor.</div>

# 07 · No funcionales · Performance

<table>
    <thead><tr><th>ID</th><th>Métrica</th><th>Target</th><th>Prio</th></tr></thead>
    <tbody>
      <tr><td>NFR-P-01</td><td>Latencia API GET (p95)</td><td>&lt; 300ms</td><td><span class="badge badge-blocked">P1</span></td></tr>
      <tr><td>NFR-P-02</td><td>Latencia API POST (p95)</td><td>&lt; 800ms</td><td><span class="badge badge-blocked">P1</span></td></tr>
      <tr><td>NFR-P-03</td><td>Time-to-interactive Dashboard</td><td>&lt; 2s</td><td><span class="badge badge-pending">P2</span></td></tr>
      <tr><td>NFR-P-04</td><td>Webhook processing</td><td>&lt; 500ms ack</td><td><span class="badge badge-blocked">P1</span></td></tr>
      <tr><td>NFR-P-05</td><td>Sync inventory cross-canal</td><td>&lt; 30s end-to-end</td><td><span class="badge badge-blocked">P1</span></td></tr>
      <tr><td>NFR-P-06</td><td>Generación DTE</td><td>&lt; 3s</td><td><span class="badge badge-pending">P2</span></td></tr>
      <tr><td>NFR-P-07</td><td>Build app</td><td>&lt; 3 min</td><td><span class="badge badge-future">P3</span></td></tr>
    </tbody>
  </table>

# 08 · No funcionales · Seguridad

<div class="req-card req-prio-1"><span class="req-id">NFR-S-01</span>**P1** · El sistema debe implementar Row Level Security (RLS) en TODAS las tablas con `tenant_id`.</div>
  <div class="req-card req-prio-1"><span class="req-id">NFR-S-02</span>**P1** · Las credenciales OAuth de canales externos deben guardarse cifradas at rest (AES-256).</div>
  <div class="req-card req-prio-1"><span class="req-id">NFR-S-03</span>**P1** · Todas las APIs internas deben autenticar con JWT o sesión httpOnly.</div>
  <div class="req-card req-prio-1"><span class="req-id">NFR-S-04</span>**P1** · Los webhooks externos deben validar firma HMAC obligatorio.</div>
  <div class="req-card req-prio-1"><span class="req-id">NFR-S-05</span>**P1** · Los secrets (API keys, DB passwords) NUNCA en código · solo env vars + secret manager.</div>
  <div class="req-card req-prio-2"><span class="req-id">NFR-S-06</span>**P2** · El sistema debe registrar audit log de toda mutación financiera (asientos, DTE, pagos).</div>
  <div class="req-card req-prio-2"><span class="req-id">NFR-S-07</span>**P2** · El sistema debe rotar tokens MeLi/MP automáticamente (cron) antes de expirar.</div>
  <div class="req-card req-prio-2"><span class="req-id">NFR-S-08</span>**P2** · El sistema debe ofrecer 2FA para login operador.</div>
  <div class="req-card req-prio-3"><span class="req-id">NFR-S-09</span>**P3** · El sistema debe permitir export GDPR-style de toda la data de un cliente (B2B/D2C).</div>

# 09 · No funcionales · Escalabilidad

<div class="req-card req-prio-1"><span class="req-id">NFR-SC-01</span>**P1** · La arquitectura debe ser multi-tenant nativo · soportar N tenants en misma BD con aislamiento RLS.</div>
  <div class="req-card req-prio-1"><span class="req-id">NFR-SC-02</span>**P1** · Cada canal debe ser un adapter independiente · agregar canal nuevo no debe requerir tocar core.</div>
  <div class="req-card req-prio-2"><span class="req-id">NFR-SC-03</span>**P2** · El sistema debe soportar 100 órdenes/hora por tenant sin degradación (MVP).</div>
  <div class="req-card req-prio-2"><span class="req-id">NFR-SC-04</span>**P2** · El sistema debe soportar 100K SKUs por tenant (catálogo grande).</div>
  <div class="req-card req-prio-3"><span class="req-id">NFR-SC-05</span>**P3** · El sistema debe soportar 1.000 órdenes/hora por tenant (escalado fase 3).</div>
  <div class="req-card req-prio-3"><span class="req-id">NFR-SC-06</span>**P3** · El sistema debe ser desplegable en regiones distintas para latencia local.</div>
  <div class="req-card req-prio-2"><span class="req-id">NFR-SC-07</span>**P2** · La BD debe estar en Supabase (Postgres) · permite escalar vertical hasta 10K órdenes/hora antes de necesitar partition.</div>

# 10 · No funcionales · Compliance Chile

<div class="req-card req-prio-1"><span class="req-id">NFR-C-01</span>**P1** · El sistema debe respetar Ley 19.628 (protección datos personales Chile).</div>
  <div class="req-card req-prio-1"><span class="req-id">NFR-C-02</span>**P1** · El sistema debe emitir DTE válidos SII (estructura XML según normativa).</div>
  <div class="req-card req-prio-1"><span class="req-id">NFR-C-03</span>**P1** · El sistema debe mantener libro IVA digital (ventas + compras) según Resolución SII.</div>
  <div class="req-card req-prio-2"><span class="req-id">NFR-C-04</span>**P2** · El sistema debe permitir inventario anual (Resolución 73 SII).</div>
  <div class="req-card req-prio-2"><span class="req-id">NFR-C-05</span>**P2** · El sistema debe alertar vencimientos: F30 · F30-1 · garantías bancarias · vigencia ChileProveedores.</div>
  <div class="req-card req-prio-2"><span class="req-id">NFR-C-06</span>**P2** · El sistema debe soportar Régimen 14D N°3 Pro-PYME General (cálculo automático).</div>
  <div class="req-card req-prio-3"><span class="req-id">NFR-C-07</span>**P3** · El sistema debe pre-generar F22 anual con saldos contables del año.</div>
  <div class="req-card req-prio-3"><span class="req-id">NFR-C-08</span>**P3** · El sistema debe gestionar accesos auditados (quién vio qué · quién modificó qué).</div>
