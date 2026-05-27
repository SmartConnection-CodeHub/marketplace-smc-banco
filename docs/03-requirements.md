---
number: 03
id: requirements
title: Requirements
subtitle: "Funcionales agrupados por fase Y1 + no funcionales cross · alineado con Doc 17 Estrategia Y1."
block: Marketplace SMC
author: PM + Architect + Functional-Lead + Cerebro
version: 2.0
date: 2026-05-27
status: 🟢 Activo · rediseño v2 por fase
prev: index.html
next: index.html
---

# 01 · Sistema de priorización

<div class="box box-premise">
    <div class="box-title">🎯 Hilo conductor · Estrategia Y1 Reputation First</div>

Toda priorización Y1 sigue la **Estrategia Y1 · Reputation First** (ver [Doc 17](17-estrategia-y1.html)). Features se agrupan por la fase Y1 que habilitan. Features que NO mueven el hito de fase actual son P3-P4.

- **Q4 2026 → Q1 2027 · Fase 1 Reputación** · publicar fotos pro · reputación verde · 10 ventas verdes
- **Q1 2027 → Q2 2027 · Fase 2 Escala MeLi** · ads · Full Fulfillment · escalado volumen
- **Q2 2027 → Q3 2027 · Fase 3 Diversificación** · D2C · MP · B2B · dropshipping
- **Q3 2027+ · Fase 4 Consolidación** · analytics · conciliación · break-even

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

# 02 · FR-Y1F1 · Fase 1 Reputación (Q4-26 → Q1-27)

Hito fase: **10 ventas verdes MeLi** · reputación verde mantenida · 3 founders confiando en el sistema.

<div class="req-card req-prio-1"><span class="req-id">FR-Y1F1-01</span>**P1** · El sistema debe permitir crear producto con SKU master + fotos propias profesionales (BR-001 valida >800px · no fotos stock).</div>
<div class="req-card req-prio-1"><span class="req-id">FR-Y1F1-02</span>**P1** · El sistema debe mantener inventario físico real-time con stock_real + stock_reserved.</div>
<div class="req-card req-prio-1"><span class="req-id">FR-Y1F1-03</span>**P1** · El sistema debe publicar SKU a MeLi vía OAuth 2.0 PKCE · token storage seguro · refresh 6h.</div>
<div class="req-card req-prio-1"><span class="req-id">FR-Y1F1-04</span>**P1** · El sistema debe procesar webhooks MeLi con HMAC SHA-256 + idempotency UUID v7 (TTL 24h).</div>
<div class="req-card req-prio-1"><span class="req-id">FR-Y1F1-05</span>**P1** · El sistema debe descontar stock con SELECT FOR UPDATE para evitar oversell concurrente.</div>
<div class="req-card req-prio-1"><span class="req-id">FR-Y1F1-06</span>**P1** · El sistema debe emitir DTE 39 (boleta) o 33 (factura RUT empresa) vía Open Factura con retry exponencial 5x.</div>
<div class="req-card req-prio-1"><span class="req-id">FR-Y1F1-07</span>**P1** · El sistema debe cotizar courier (Chilexpress · Starken) y generar etiqueta PDF descargable.</div>
<div class="req-card req-prio-1"><span class="req-id">FR-Y1F1-08</span>**P1** · El sistema debe enviar email tracking al comprador vía Resend.</div>
<div class="req-card req-prio-1"><span class="req-id">FR-Y1F1-09</span>**P1** · El sistema debe trackear reputación MeLi (score · medalla · alertas amarillo/rojo) vía cron 1h refresh.</div>
<div class="req-card req-prio-2"><span class="req-id">FR-Y1F1-10</span>**P2** · El sistema debe ofrecer chat Cerebro con SSE streaming (&lt;600ms first token) · rate limit 60 msg/día/founder.</div>

# 03 · FR-Y1F2 · Fase 2 Escala MeLi (Q1-27 → Q2-27)

Hito fase: **50 ventas/mes** · costo CAC controlado · Full Fulfillment activo o evaluado.

<div class="req-card req-prio-1"><span class="req-id">FR-Y1F2-01</span>**P1** · El sistema debe gestionar campañas Mercado Ads (mismo OAuth MeLi) · presupuesto · creatividades · ROAS tracking.</div>
<div class="req-card req-prio-1"><span class="req-id">FR-Y1F2-02</span>**P1** · El sistema debe alertar ROAS &lt;1.5 por 7 días con sugerencia pausa automática.</div>
<div class="req-card req-prio-2"><span class="req-id">FR-Y1F2-03</span>**P2** · El sistema debe evaluar y/o gestionar Full Fulfillment MeLi (envío de stock a bodega MeLi · sincronización stock).</div>
<div class="req-card req-prio-2"><span class="req-id">FR-Y1F2-04</span>**P2** · El sistema debe sugerir top SKUs a re-comprar según rotación (Cerebro analytics sin LLM).</div>
<div class="req-card req-prio-2"><span class="req-id">FR-Y1F2-05</span>**P2** · El sistema debe gestionar medallas MeLi (Mercado Líder Gold/Platinum) con tracker.</div>

# 04 · FR-Y1F3 · Fase 3 Diversificación (Q2-27 → Q3-27)

Hito fase: **≥30% revenue fuera de MeLi** · 1 adjudicación MP + 1 cliente B2B real + D2C operativo.

<div class="req-card req-prio-1"><span class="req-id">FR-Y1F3-01</span>**P1** · El sistema debe operar D2C storefront propio en marketplace.smconnection.cl con checkout WebPay Plus o MercadoPago.</div>
<div class="req-card req-prio-1"><span class="req-id">FR-Y1F3-02</span>**P1** · El sistema debe sincronizar Mercado Público diariamente 8am (cron) con licitaciones afines vía pg_trgm fuzzy match.</div>
<div class="req-card req-prio-1"><span class="req-id">FR-Y1F3-03</span>**P1** · El sistema debe ofrecer portal B2B con RFQ workflow + cotización custom + aprobación HMAC.</div>
<div class="req-card req-prio-1"><span class="req-id">FR-Y1F3-04</span>**P1** · El sistema debe operar modo dropshipping (Supplier Adapter Pattern · ADR-0003) propagando OC al proveedor.</div>
<div class="req-card req-prio-1"><span class="req-id">FR-Y1F3-05</span>**P1** · El sistema debe detectar trigger migración dropship → stock local (SKU >$5K/mes sostenido 2 meses).</div>
<div class="req-card req-prio-2"><span class="req-id">FR-Y1F3-06</span>**P2** · El sistema debe emitir DTE 33 (factura) y DTE 52 (guía electrónica) para clientes institucionales MP.</div>

# 05 · FR-Y1F4 · Fase 4 Consolidación (Q3-27+)

Hito fase: **break-even operacional** · F22 anual proyectado positivo · 3 founders &lt;30h/sem cada uno en operación.

<div class="req-card req-prio-1"><span class="req-id">FR-Y1F4-01</span>**P1** · El sistema debe correr conciliación financiera mensual (cron 1ro mes) matching pagos vs DTE.</div>
<div class="req-card req-prio-1"><span class="req-id">FR-Y1F4-02</span>**P1** · El sistema debe generar resumen F29 mensual (ventas afectas + IVA débito + IVA crédito) listo upload SII.</div>
<div class="req-card req-prio-2"><span class="req-id">FR-Y1F4-03</span>**P2** · El sistema debe forecastear flujo de caja 30/60/90 días.</div>
<div class="req-card req-prio-2"><span class="req-id">FR-Y1F4-04</span>**P2** · El sistema debe pre-generar F22 anual con saldos contables del año.</div>
<div class="req-card req-prio-2"><span class="req-id">FR-Y1F4-05</span>**P2** · El sistema debe calcular margen real por SKU = Precio − Landed − Comisión canal − Logística − IVA débito.</div>
<div class="req-card req-prio-2"><span class="req-id">FR-Y1F4-06</span>**P2** · El sistema debe mostrar dashboard consolidado: revenue · margen · órdenes · split por canal + drill-down.</div>

# 06 · FR-CROSS · Cross-cutting (todas las fases)

Foundations que habilitan TODAS las fases · no asociadas a una fase específica.

## Auth + tenancy

<div class="req-card req-prio-1"><span class="req-id">FR-X-AUTH-01</span>**P1** · El sistema debe autenticar founders con Supabase Auth + JWT con tenant_id implícito.</div>
<div class="req-card req-prio-1"><span class="req-id">FR-X-AUTH-02</span>**P1** · El sistema debe exigir 2FA TOTP para todos los admins.</div>
<div class="req-card req-prio-2"><span class="req-id">FR-X-AUTH-03</span>**P2** · El sistema debe rotar tokens OAuth (MeLi · MP) automáticamente antes de expirar.</div>

## DB + persistencia

<div class="req-card req-prio-1"><span class="req-id">FR-X-DB-01</span>**P1** · El sistema debe implementar RLS Postgres en TODAS las tablas con tenant_id.</div>
<div class="req-card req-prio-1"><span class="req-id">FR-X-DB-02</span>**P1** · El sistema debe registrar audit log append-only de toda mutación crítica (financiera · DTE · cambios stock).</div>
<div class="req-card req-prio-1"><span class="req-id">FR-X-DB-03</span>**P1** · El sistema debe correr pg_notify para sync cross-canal cuando inventory cambia.</div>

## Adapter patterns

<div class="req-card req-prio-1"><span class="req-id">FR-X-ADP-01</span>**P1** · El sistema debe implementar Channel Adapter Pattern (ADR-0002) · 4 canales con interface única.</div>
<div class="req-card req-prio-1"><span class="req-id">FR-X-ADP-02</span>**P1** · El sistema debe implementar Supplier Adapter Pattern (ADR-0003) para dropshipping.</div>
<div class="req-card req-prio-2"><span class="req-id">FR-X-ADP-03</span>**P2** · Agregar canal o proveedor nuevo debe requerir solo 1 archivo nuevo (NO refactor core).</div>

## Cerebro IA

<div class="req-card req-prio-2"><span class="req-id">FR-X-AI-01</span>**P2** · El sistema debe usar fallback chain Groq → Gemini → DeepSeek vía OpenRouter (NUNCA Claude).</div>
<div class="req-card req-prio-2"><span class="req-id">FR-X-AI-02</span>**P2** · El sistema debe loggear cada llamada IA en mkt_ai_logs (provider · tokens · cost · latency · cache_hit).</div>
<div class="req-card req-prio-2"><span class="req-id">FR-X-AI-03</span>**P2** · El sistema debe auto-throttle si cost IA diario &gt;80% budget.</div>

## Webhooks + integraciones

<div class="req-card req-prio-1"><span class="req-id">FR-X-WH-01</span>**P1** · El sistema debe recibir webhooks de canales externos con HMAC SHA-256 obligatorio (timingSafeEqual).</div>
<div class="req-card req-prio-1"><span class="req-id">FR-X-WH-02</span>**P1</span>** · El sistema debe rechazar requests sin idempotency_key en POSTs críticos.</div>

# 07 · NFR-Y1 · No funcionales cross

## Performance budgets

<table>
    <thead><tr><th>ID</th><th>Métrica</th><th>Target Y1</th><th>Prio</th></tr></thead>
    <tbody>
      <tr><td>NFR-Y1-P-01</td><td>API GET p95</td><td>&lt; 350ms</td><td><span class="badge badge-blocked">P1</span></td></tr>
      <tr><td>NFR-Y1-P-02</td><td>API POST p95</td><td>&lt; 600ms</td><td><span class="badge badge-blocked">P1</span></td></tr>
      <tr><td>NFR-Y1-P-03</td><td>LCP Dashboard founder</td><td>&lt; 2.5s</td><td><span class="badge badge-blocked">P1</span></td></tr>
      <tr><td>NFR-Y1-P-04</td><td>INP Dashboard</td><td>&lt; 200ms</td><td><span class="badge badge-pending">P2</span></td></tr>
      <tr><td>NFR-Y1-P-05</td><td>Webhook MeLi ack</td><td>&lt; 500ms</td><td><span class="badge badge-blocked">P1</span></td></tr>
      <tr><td>NFR-Y1-P-06</td><td>Sync inventory cross-canal</td><td>&lt; 30s</td><td><span class="badge badge-blocked">P1</span></td></tr>
      <tr><td>NFR-Y1-P-07</td><td>Cerebro first token SSE</td><td>&lt; 600ms</td><td><span class="badge badge-pending">P2</span></td></tr>
      <tr><td>NFR-Y1-P-08</td><td>Build CI</td><td>&lt; 3 min</td><td><span class="badge badge-future">P3</span></td></tr>
      <tr><td>NFR-Y1-P-09</td><td>Bundle client gzipped</td><td>&lt; 250KB</td><td><span class="badge badge-pending">P2</span></td></tr>
    </tbody>
  </table>

## Security

<div class="req-card req-prio-1"><span class="req-id">NFR-Y1-S-01</span>**P1** · TLS 1.3 obligatorio + HSTS preload.</div>
<div class="req-card req-prio-1"><span class="req-id">NFR-Y1-S-02</span>**P1** · AES-256 at rest (Supabase default).</div>
<div class="req-card req-prio-1"><span class="req-id">NFR-Y1-S-03</span>**P1** · service_role solo en backend · NUNCA NEXT_PUBLIC_*.</div>
<div class="req-card req-prio-1"><span class="req-id">NFR-Y1-S-04</span>**P1** · Cookies httpOnly + SameSite=lax.</div>
<div class="req-card req-prio-1"><span class="req-id">NFR-Y1-S-05</span>**P1** · CSP headers estrictos + report-uri.</div>
<div class="req-card req-prio-1"><span class="req-id">NFR-Y1-S-06</span>**P1** · Rate limit 60 req/min/user · 600 req/min/IP vía Upstash Redis.</div>
<div class="req-card req-prio-2"><span class="req-id">NFR-Y1-S-07</span>**P2** · OWASP ZAP scan QAS sin high/medium vulnerabilities.</div>

## Escalabilidad

<div class="req-card req-prio-1"><span class="req-id">NFR-Y1-SC-01</span>**P1** · Multi-tenant nativo · RLS por tenant_id en TODAS las tablas (ready Y3+ sharding).</div>
<div class="req-card req-prio-1"><span class="req-id">NFR-Y1-SC-02</span>**P1** · Channel + Supplier Adapter Pattern · canal/proveedor nuevo = 1 archivo (no refactor).</div>
<div class="req-card req-prio-2"><span class="req-id">NFR-Y1-SC-03</span>**P2** · Soportar 100 órdenes/hora por tenant sin degradación.</div>
<div class="req-card req-prio-2"><span class="req-id">NFR-Y1-SC-04</span>**P2** · Soportar 10K SKUs por tenant.</div>

## Compliance Chile

<div class="req-card req-prio-1"><span class="req-id">NFR-Y1-C-01</span>**P1** · Ley 19.628 protección datos personales · consent management.</div>
<div class="req-card req-prio-1"><span class="req-id">NFR-Y1-C-02</span>**P1** · DTE válidos SII (XML según normativa Open Factura).</div>
<div class="req-card req-prio-1"><span class="req-id">NFR-Y1-C-03</span>**P1** · Libro IVA digital ventas + compras (Resolución SII).</div>
<div class="req-card req-prio-2"><span class="req-id">NFR-Y1-C-04</span>**P2** · Régimen 14D N°3 Pro-PYME General (cálculo automático).</div>
<div class="req-card req-prio-2"><span class="req-id">NFR-Y1-C-05</span>**P2** · Alertas vencimientos: F30 · F30-1 · garantías · ChileProveedores.</div>
<div class="req-card req-prio-3"><span class="req-id">NFR-Y1-C-06</span>**P3** · Pre-generar F22 anual con saldos contables del año.</div>

# 08 · Mapping requirements → sprints (Doc 18)

| Fase Y1 | Sprints (Doc 18) | Requirements |
|---------|------------------|--------------|
| Cross foundations | Sprint 1-2 Q4-26 | FR-CROSS-* + NFR-Y1-S-* + NFR-Y1-SC-01/02 |
| Fase 1 Reputación | Sprint 2-4 Q4-26 → Q1-27 | FR-Y1F1-01 a FR-Y1F1-10 |
| Fase 2 Escala | Sprint 5-6 Q1-27 → Q2-27 | FR-Y1F2-01 a FR-Y1F2-05 |
| Fase 3 Diversificación | Sprint 7-9 Q2-27 → Q3-27 | FR-Y1F3-01 a FR-Y1F3-06 |
| Fase 4 Consolidación | Sprint 10+ Q3-27+ | FR-Y1F4-01 a FR-Y1F4-06 |
