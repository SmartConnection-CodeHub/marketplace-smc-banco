---
number: 11
id: especificacion-funcional
title: Especificación Funcional
subtitle: "Qué hace el sistema · herramientas concretas · flujos detallados · interacciones granulares · maquetas."
block: Producto Técnico
author: Functional-Lead + PM + Cerebro
version: 2.0
date: 2026-05-27
status: 🟡 Draft · pendiente review founders
prev: 10-assessment.html
next: 13-especificacion-tecnica.html
---

# 01 · Premisa

Doc 11 detalla **qué hace el sistema** a nivel granular: qué herramienta específica toma cada decisión · cómo conversan entre sí · qué disparadores activan cada flujo · qué endpoints toca · qué tablas DB · qué UI screen.

> [!info] No es repetición de Doc 02 BBP
> Doc 02 muestra los 14 procesos. Doc 11 detalla cómo CADA proceso se ejecuta en herramientas concretas con disparadores · datos · APIs · UI. Doc 13 es el espejo técnico (cómo se construye).

# 02 · Mapa funcional de herramientas

> [!hla] funcional-tools-map
> Cada bloque = herramienta concreta del stack. Click ve qué casos de uso la usan + cómo conversa con las demás. Filtros por modo (local · Nexport · dropship).

# 03 · Catálogo de herramientas externas (granular)

| Herramienta | Categoría | Rol Y1 | Auth method | Frecuencia |
|-------------|-----------|--------|-------------|-----------|
| **SoloTodo API** (Plan B activo) | Source pricing + catálogo MeLi | Análisis competencia · scoring oportunidades · 58K productos MeLi Chile indexados | Pública sin auth · sin costo | Pricing update 6-12h |
| **Mercado Libre API v2** (objetivo) | Canal | Publicar listings · sync stock · recibir órdenes | OAuth 2.0 PKCE + cookies httpOnly | Webhooks real-time + cron 6h refresh |
| **Mercado Ads** | Canal · publicidad | Campaigns · ROAS tracking · pausing | Token OAuth ML | Diaria (auto-tune) |
| **Mercado Público (ChileCompra)** | Canal B2G | Sync licitaciones · postular · adjudicar | Ticket auth (env var) | Cron 8am diario |
| **B2B Portal propio** | Canal B2B | RFQ · cotización · firma HMAC | API keys por cliente | Real-time |
| **Transferencia bancaria** (default Y1) | Pago | Cobros D2C · upload comprobante · verify manual founder | Sin auth · UI propia | 1-24h verify |
| **MercadoPago** (opcional dual) | Pasarela | Cobros activables por SKU · MeLi auto + D2C opt-in | OAuth + webhook firmado HMAC | Webhook real-time |
| **WebPay Plus** (deferido Y2) | Pasarela | Si volumen justifica setup | Certificado + commerce code | Y2 |
| **Open Factura** | DTE SII | Emitir DTE 33/39/61 | API key + cert digital | Real-time post-venta |
| **Chilexpress API** | Logística | Cotizar + etiqueta + tracking | API key | Real-time |
| **Starken API** | Logística | Cotizar + etiqueta + tracking | API key | Real-time |
| **Groq Llama 3.3 70B** | IA primary | Cerebro chat · scoring | API key OpenRouter | Real-time SSE |
| **Gemini Flash 2.0** | IA fallback 1 | Cuando Groq excede TPM | API key OpenRouter | Fallback |
| **DeepSeek V3** | IA fallback 2 | Cuando Gemini falla | API key OpenRouter | Fallback |
| **OpenRouter** | IA router | Routing automatic + cost cap | API key | Capa sobre Groq/Gemini/DS |
<!-- SoloTodo movido al top como Plan B activo · entry duplicada eliminada -->
| **Open Food Facts** | Source data | Productos alimentación + nutrición | Pública sin auth | Cron diario |
| **Banco Central API** | Source FX | USD/CLP tipo cambio | Pública sin auth | Cron diario 9am |
| **Supabase Auth** | Auth users | JWT founders · 2FA opcional TOTP | Email/password | Login persistente 30d |
| **Supabase Postgres** | DB principal | Source of truth · RLS multi-tenant ready | service_role solo backend | Real-time todos reads/writes |
| **Supabase Storage** | Blob storage | Fotos productos · PDFs DTE · attachments | Signed URLs | On demand |
| **AWS Amplify** | Hosting + CDN | Deploy Next.js · CloudFront edge | GitHub PAT + AWS IAM | Push to main → deploy |
| **GitHub Actions** | CI/CD | Lint · type-check · tests · build · tag | GITHUB_TOKEN write | Push to main |
| **Sentry** | Errors | Error tracking + alerts | DSN | Real-time |
| **PostHog** | Product analytics | Funnels · feature flags · events | Project API key | Real-time |
| **CloudWatch** | Infra metrics | Lambda timing · API Gateway · cost | AWS IAM | Real-time + 14d retention |
| **Gmail API** (default Y1) | Email transaccional | Confirmaciones · tracking · password reset · alertas founders | OAuth Workspace SMC | On event · batch 5min |
| **Vercel Cron** | Scheduler | Refresh MeLi 6h · sync MP 8am · cleanup 7d | CRON_SECRET header | Programado |
| **pg_cron + pg_notify** | DB triggers | Stock cross-canal · events internos | Solo Postgres | Real-time |

# 04 · Workflows por modo · paso a paso

## 4.1 · Modo stock propio compra local Chile (Y1 prioridad)

> [!pipeline] flow-stock-local
> Venta end-to-end · 3 escenarios paralelos (MeLi · D2C storefront · MP) · cada etapa con herramientas · disparadores · DB · tiempo target. Click box ve detalle granular.

**3 canales del mismo modo stock propio**:

| Canal | Margen | Comisión | Volumen Y1 esperado |
|-------|--------|----------|---------------------|
| **MELI** (default visible) | 28% | Fee MeLi 13-17% + MP 2.9% | 80% Y1 |
| **D2C storefront** | 40%+ | Solo pasarela 2.9% | 5-10% Y1 · crece Y2 |
| **MP B2G** | 22-30% | 0% (pago directo institución 30-60d) | Fase 3 |

## 4.2 · Modo dropshipping (paralelo)

> [!pipeline] flow-dropshipping
> Venta sin stock propio · 7 etapas · OC propagada al proveedor · despacho directo al cliente final.

## 4.3 · Modo Nexport importación (Fase 2 · Y2+)

Same flow que 4.1 más sub-proceso importación previo (ciclo 30-90 días USD). Documentado en Doc 02 BBP P02b.

# 05 · 24 casos de uso · detalle granular

Cada CU tiene 6 atributos: **Trigger · Tools · Endpoint · Tablas · UI screen · Output**.

## Fase 1 · Reputación Q4-26 (CU-001 → CU-006)

### CU-001 · Crear producto en catálogo maestro

| Atributo | Detalle |
|----------|---------|
| Trigger | Founder click "Nuevo producto" en `/dashboard/productos` |
| Tools | Supabase Postgres (insert) · Supabase Storage (upload fotos) |
| Endpoint | `POST /api/products` (validación Zod · service_role insert) |
| Tablas | `products` (insert) · `product_images` (jsonb embedded) |
| UI screen | `/dashboard/productos/nuevo` · formulario 12 campos · drag-drop fotos |
| Output | producto con `id` UUID · `status='active'` · ready para publicar |
| Tiempo target | &lt; 3 min input founder · &lt; 500ms response API |

### CU-002 · Configurar listing MeLi

| Atributo | Detalle |
|----------|---------|
| Trigger | Founder click "Publicar en MeLi" en producto existente |
| Tools | MeLi API v2 (`POST /items`) · Channel Adapter pattern |
| Endpoint | `POST /api/channels/meli/publish/:product_id` |
| Tablas | `channel_listings` (insert) · `products` (update `external_ids`) |
| UI screen | Modal con campos MeLi-specific (categoría · attrs requeridos) |
| Output | listing live en MeLi · `mlc_id` guardado en DB |
| Tiempo target | &lt; 5s API call MeLi + 2s db write |

### CU-003 · Primera venta (regalo o costo)

| Atributo | Detalle |
|----------|---------|
| Trigger | Comprador hace pedido en MeLi · MeLi dispara webhook |
| Tools | Webhook receiver · DB insert · Open Factura DTE 39 · Chilexpress label |
| Endpoint | `POST /api/webhooks/meli` (HMAC + idempotency) |
| Tablas | `orders` (insert · status=accepted) · `order_items` (insert) · `inventory` (decrement · SELECT FOR UPDATE) |
| UI screen | Toast "Nueva venta MeLi" · `/dashboard/ordenes/:id` |
| Output | Orden cerrada · DTE emitido · etiqueta · email comprador |
| Tiempo target | Webhook → DTE emitido &lt; 30s end-to-end |

### CU-004 · Recibir orden vía webhook (genérico)

| Atributo | Detalle |
|----------|---------|
| Trigger | MeLi POST webhook con order_id |
| Tools | Next.js Route Handler · HMAC SHA-256 verify · Idempotency key check |
| Endpoint | `POST /api/webhooks/meli` |
| Tablas | `webhook_events` (append-only audit) · `orders` (insert si nueva) |
| UI screen | N/A · server-side |
| Output | Order procesada · stock reservado · pg_notify event |
| Reglas BR | BR-005 (stock real-time) · BR-006 (SELECT FOR UPDATE) · BR-009 (DTE auto) |

### CU-005 · Emitir DTE 39 boleta

| Atributo | Detalle |
|----------|---------|
| Trigger | Evento `order.completed` · pg_notify dispara worker |
| Tools | Open Factura API · Supabase Storage (PDF) · Gmail API (email) |
| Endpoint | `POST /api/invoices/emit/:order_id` (internal) |
| Tablas | `invoices` (insert con `folio_sii` · `pdf_url`) |
| UI screen | Indicador en `/dashboard/ordenes/:id` con badge DTE estado |
| Output | DTE 39 con folio SII oficial · PDF en Storage · email al comprador |
| Reglas BR | BR-010 (39 default · 33 si RUT empresa) · BR-011 (retry 5x) |

### CU-006 · Tracker reputación · 10 ventas verdes

| Atributo | Detalle |
|----------|---------|
| Trigger | Cada orden completada dispara recálculo |
| Tools | Postgres materialized view + pg_cron refresh 1h |
| Endpoint | `GET /api/metrics/reputation` |
| Tablas | `orders` JOIN `order_reputation_signals` (view) |
| UI screen | Widget hero `/dashboard` · progress bar 0/10 · color sem |
| Output | Indicador real-time hito Fase 1 |

## Fase 2 · Escala MeLi Q1-27 (CU-007 → CU-012)

### CU-007 · Configurar Mercado Ads campaign

| Atributo | Detalle |
|----------|---------|
| Trigger | Founder click "Crear campaña" en producto con reputación verde |
| Tools | MeLi Ads API · validation `reputation_color=green` antes submit |
| Endpoint | `POST /api/channels/meli/ads/campaign` |
| Tablas | `ads_campaigns` (insert) · `ads_pixels` (mapping product → pixel) |
| UI screen | Wizard 3 pasos: producto · presupuesto · validación BR-003 |
| Output | Campaña activa · tracking ROAS panel |

### CU-008 · Monitor ROAS · pausar si &lt;1.5x

| Atributo | Detalle |
|----------|---------|
| Trigger | Cron diario 7am calcula ROAS últimas 7d por campaña |
| Tools | Cerebro IA sugiere · founder decide en UI |
| Endpoint | `GET /api/channels/meli/ads/roas` · `POST .../pause/:id` |
| Tablas | `ads_metrics_daily` (insert) · `ads_campaigns` (update status) |
| UI screen | Dashboard `/ads` tabla ROAS · botón pausar · sugerencia Cerebro |
| Output | Campañas con ROAS &lt;1.5x sugeridas para pausa · founder valida |

### CU-009 · Migrar SKU a Full Fulfillment MeLi

| Atributo | Detalle |
|----------|---------|
| Trigger | Producto vende &gt;5 unidades/sem sostenido 4 sem |
| Tools | MeLi FF API · workflow migración stock físico |
| Endpoint | `POST /api/channels/meli/fulfillment/migrate/:product_id` |
| Tablas | `products` (update `fulfillment_mode='full'`) · `inventory_transfers` |
| UI screen | `/dashboard/productos/:id/fulfillment` con CTA migrar |
| Output | Stock en almacenes MeLi · mayor visibilidad algoritmo |

### CU-010 · Subir a Medalla Plata

| Atributo | Detalle |
|----------|---------|
| Trigger | Sistema cumple criterios MeLi (auto-tracked poll diario) |
| Tools | MeLi seller reputation API · poll daily |
| Endpoint | `GET /api/channels/meli/reputation/level` |
| Tablas | `seller_reputation_history` (insert) |
| UI screen | Badge dashboard · animación al subir |
| Output | Medalla Plata visible públicamente |

### CU-011 · Cerebro IA alertas oportunidades

| Atributo | Detalle |
|----------|---------|
| Trigger | Cron diario 6am · scoring 6 señales sin LLM |
| Tools | Cerebro scoring algorithm · Postgres queries · SoloTodo |
| Endpoint | `GET /api/cerebro/opportunities?min_score=70` |
| Tablas | `opportunities` (insert/update con `score`) · `opportunity_signals` (jsonb) |
| UI screen | Panel `/dashboard/oportunidades` · top 10 sorted by score |
| Output | Top 10 del día · cero costo IA por scoring |

### CU-012 · Cerrar Fase 2 (30 órdenes/mes sostenidas)

| Atributo | Detalle |
|----------|---------|
| Trigger | Cron mensual día 1 · si threshold 2x consecutivo · hito cerrado |
| Tools | Postgres analytics query · pg_cron · email founders |
| Endpoint | `GET /api/metrics/phase-2-progress` |
| Tablas | `phase_milestones` (update) |
| UI screen | Hero dashboard "Fase 2 cerrada · pasamos a Fase 3" |
| Output | Notificación email + sistema migra lógica a Fase 3 |

## Fase 3 · Diversificación Q2-27 (CU-013 → CU-018)

### CU-013 · Sync diario licitaciones Mercado Público

| Atributo | Detalle |
|----------|---------|
| Trigger | Vercel cron 8am · header `CRON_SECRET` valida |
| Tools | Mercado Público API REST · ticket auth · Cerebro filter |
| Endpoint | `POST /api/cron/sync-mp` |
| Tablas | `mp_licitaciones` (insert/update) · `mp_categorias_match` (insert) |
| UI screen | N/A server · visible en `/dashboard/mercado-publico` |
| Output | Licitaciones nuevas del día filtradas + scored |

### CU-014 · Cerebro filter + scoring licitaciones

| Atributo | Detalle |
|----------|---------|
| Trigger | post CU-013 · pg_notify event `mp_synced` |
| Tools | Cerebro scoring + matching catálogo (pg_trgm fuzzy) |
| Endpoint | `GET /api/cerebro/mp-suggestions?date=today` |
| Tablas | `mp_licitaciones` JOIN `products` ON fuzzy SKU |
| UI screen | Panel B2G con top 5 sugeridas + score |
| Output | Top 5 licitaciones afines + scoring del día |

### CU-015 · Postular a licitación MP

| Atributo | Detalle |
|----------|---------|
| Trigger | Javier click "Postular" en sugerencia |
| Tools | MP API POST oferta · template Cerebro genera · founder valida |
| Endpoint | `POST /api/channels/mp/postular/:licitacion_id` |
| Tablas | `mp_postulaciones` (insert) · `mp_ofertas_pdf` (Storage) |
| UI screen | Wizard 4 pasos: validar items · pricing · template · submit |
| Output | Oferta enviada · pending hasta apertura |

### CU-016 · Webhook adjudicación MP

| Atributo | Detalle |
|----------|---------|
| Trigger | MP envía webhook POST resultado |
| Tools | Mercado Público webhook receiver · HMAC validation |
| Endpoint | `POST /api/webhooks/mp` |
| Tablas | `mp_postulaciones` (update status) · `orders` (insert si ganada) |
| UI screen | Notificación + workflow despacho institucional |
| Output | Primera adjudicación B2G · workflow despacho activo |

### CU-017 · Cliente B2B envía RFQ

| Atributo | Detalle |
|----------|---------|
| Trigger | Cliente B2B POST form portal `/b2b/rfq` |
| Tools | Form Next.js + Zod validation · API key del cliente |
| Endpoint | `POST /api/b2b/rfq` |
| Tablas | `b2b_rfqs` (insert) · `b2b_companies` (lookup/insert) |
| UI screen | Notification founder · `/dashboard/b2b/rfq/:id` |
| Output | RFQ recibida · founder genera cotización |

### CU-018 · Cierre Fase 3

Threshold: 1+ adjudicación MP + 1+ B2B + MeLi 30+/mes sostenidos.

## Fase 4 · Consolidación Q3-27 (CU-019 → CU-024)

CU-019 conciliación pagos vs DTE · CU-020 evaluación Nexport · CU-021 D2C prep · CU-022 setup primer supplier dropship · CU-023 risk review · CU-024 cierre Y1 con break-even.

Detalle por CU sigue mismo formato 6 atributos.

# 06 · 18 reglas de negocio · ejemplo concreto cada una

Cada BR ahora con implementación específica:

```
BR-001 · Fotos pro propias siempre
  Implementación:
  · Validation Zod en POST /api/products requiere >= 3 images
  · Cada imagen pasa por detector "is_provider_default" (perceptual hash
    contra base fotos típicas proveedores Chile)
  · Si match > 80% similarity → bloquear publish con error
    "Esta foto es del proveedor · subí foto propia · ver Doc 17 Estrategia Fase 1"

BR-005 · pg_notify cross-canal stock < 1s
  Implementación:
  · Trigger Postgres ON UPDATE OF inventory.stock_real
  · NOTIFY 'inventory_changed' con product_id payload
  · Listener Node.js suscrito · llama channels-sync API por adapter
  · Timeout máx 1s · si excede → alerta CloudWatch

BR-010 · DTE 39 boleta default · 33 si RUT empresa
  Implementación:
  · POST /api/invoices/emit valida campo customer_rut
  · Si rut termina en -K o letra después número → empresa → DTE 33
  · Sino → DTE 39 (boleta persona natural)
  · Edge case: RUT 60-66M (entidades públicas) → DTE 33 forzado

BR-016 · Fallback chain IA · NUNCA Claude
  Implementación:
  · OpenRouter routing con preferences order:
    1. groq/llama-3.3-70b-versatile (primary · rate 12K TPM)
    2. google/gemini-2.0-flash-001 (fallback · free tier)
    3. deepseek/deepseek-chat (fallback 2 · cheap)
  · Claude excluido explícitamente en config preferences
  · Si los 3 fallan → retornar mensaje "IA temporalmente no disponible · reintentando..."
```

(13 BRs restantes con tratamiento similar granular)

# 07 · Maquetas mínimas Y1 · qué construir

| Maqueta | Estado | Ref banco-diseño v8 | Detalle granular |
|---------|--------|---------------------|------------------|
| `/dashboard` home | 🆕 diseñar | sección home | Hero con hito fase actual + 4 widgets (ventas hoy · órdenes pending · alertas · oportunidades) |
| `/dashboard/productos` lista | 🆕 diseñar | sección catálogo | Grid masonry · filtros canal+status · search · CTA nuevo |
| `/dashboard/productos/:id` detalle | 🆕 diseñar | sección detail | Tabs General · Listings · Inventory · Sales history |
| `/dashboard/productos/nuevo` form | 🆕 diseñar | form pattern | 12 fields · drag-drop fotos · category picker · validation inline |
| `/dashboard/ordenes` lista | 🆕 diseñar | sección órdenes | Filter status/canal/fecha · row click → detail |
| `/dashboard/ordenes/:id` detalle | 🆕 diseñar | — | Timeline horizontal · items + payment + invoice + tracking |
| `/dashboard/cerebro` chat | 🆕 diseñar | sección IA | SSE streaming · sidebar history · suggested prompts |
| `/dashboard/oportunidades` | 🆕 diseñar | sección scoring | Top 10 cards con score breakdown (6 señales) · CTA agregar al catálogo |
| `/dashboard/mercado-publico` Q2 | 🆕 diseñar | — | Licitaciones día · top sugeridas Cerebro · workflow postular |
| `/dashboard/ads` Mercado Ads Q1 | 🆕 diseñar | — | Campaigns table · ROAS chart · pausar/activar |
| `/dashboard/b2b` portal Q2 | 🆕 diseñar | — | RFQs recibidas · cotizaciones · aprobaciones |
| `/dashboard/settings` | 🆕 diseñar | settings | Conectar canales · cron status · usuarios |

# 08 · Criterios aceptación medibles con SQL

```sql
-- Fase 1 cerrada · 10 ventas verdes
SELECT COUNT(*) >= 10 AS phase_1_closed
FROM orders
WHERE channel='meli'
  AND status='delivered'
  AND reputation_color='green'
  AND completed_at > NOW() - INTERVAL '60 days';

-- Fase 2 · 2 meses consecutivos 30+ órdenes
SELECT COUNT(*) >= 2 AS phase_2_closed
FROM (
  SELECT DATE_TRUNC('month', completed_at) AS month,
         COUNT(*) AS orders_count
  FROM orders
  WHERE channel='meli' AND status='delivered'
  GROUP BY month
  HAVING COUNT(*) >= 30
) recent_months
WHERE month >= NOW() - INTERVAL '3 months';

-- Margen blended mensual
SELECT
  DATE_TRUNC('month', completed_at) AS month,
  SUM(total) AS revenue,
  SUM(cogs) AS cogs,
  ROUND(((SUM(total) - SUM(cogs))::float / NULLIF(SUM(total), 0) * 100)::numeric, 2) AS margin_pct
FROM orders
WHERE status='delivered'
GROUP BY month
ORDER BY month DESC LIMIT 12;

-- ROAS Mercado Ads por campaña últimas 7d
SELECT
  c.name,
  c.product_id,
  SUM(m.revenue) AS revenue_7d,
  SUM(m.spend) AS spend_7d,
  CASE WHEN SUM(m.spend) > 0
    THEN ROUND((SUM(m.revenue) / SUM(m.spend))::numeric, 2)
    ELSE NULL
  END AS roas
FROM ads_campaigns c
JOIN ads_metrics_daily m ON m.campaign_id = c.id
WHERE m.date > NOW() - INTERVAL '7 days'
GROUP BY c.id, c.name, c.product_id
ORDER BY roas ASC NULLS LAST;
```

# 09 · Out of scope explícito Y1

❌ NO hace Y1:
- App mobile (web responsive es suficiente · pwa Y2)
- Multi-tenant entre marcas (1 tenant = SMC SpA · multi-tenant Y3+)
- Multi-moneda (CLP único · USD solo Nexport Fase 2)
- Garantías / seguros productos (Y2)
- Programa fidelidad clientes (Y2)
- Marketplace interno (no vendemos a otros vendedores)
- Operación fuera Chile (territorialmente Chile-only)
- Pago directo sistema (siempre vía pasarela externa)
- Voice / audio interface (Y3+ si vale)

# 10 · Próximos pasos

1. ✅ Doc 11 v2 · granular · herramientas + flujos detallados
2. ⏭️ Doc 13 v2 · Espec Técnica granular alineada con Doc 07 Architecture
3. ⏭️ Tu OK para empezar maquetas (Doc 18 detalla qué construir)
4. ⏭️ Doc 19 UAT post-construcción
