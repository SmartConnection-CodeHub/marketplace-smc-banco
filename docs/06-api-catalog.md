---
number: 06
id: api-catalog
title: API Catalog
subtitle: "Endpoints REST internos · estilo OpenAPI/Swagger · 30+ rutas + schemas · expandible clickeable."
block: Producto Técnico
author: Backend
version: 2.0
date: 2026-05-26
status: 🟢 Activo
prev: 05-data-model.html
next: 07-architecture.html
---

# 01 · Listado completo · 30 endpoints

| # | Método | Path | Tag | Auth | Descripción |
|---|--------|------|-----|------|-------------|
| 1 | POST | `/api/auth/login` | Auth | público | Login email + password · genera JWT |
| 2 | POST | `/api/auth/refresh` | Auth | refresh token | Renueva access_token |
| 3 | POST | `/api/auth/logout` | Auth | JWT | Cierra sesión · limpia cookies |
| 4 | GET | `/api/products` | Products | JWT | Lista productos con filtros |
| 5 | POST | `/api/products` | Products | JWT | Crea producto en catálogo maestro |
| 6 | GET | `/api/products/:id` | Products | JWT | Detalle + listings cross-canal |
| 7 | PATCH | `/api/products/:id` | Products | JWT | Patch parcial · dispara sync canales |
| 8 | DELETE | `/api/products/:id` | Products | JWT | Soft delete · status=archived |
| 9 | GET | `/api/inventory` | Inventory | JWT | Stock real-time · filtro low_stock |
| 10 | PATCH | `/api/inventory/:product_id` | Inventory | JWT | Ajusta stock · pg_notify cross-canal |
| 11 | GET | `/api/orders` | Orders | JWT | Lista órdenes filtros status/channel |
| 12 | GET | `/api/orders/:id` | Orders | JWT | Detalle + items + payments + invoice |
| 13 | POST | `/api/orders/:id/accept` | Orders | JWT | Acepta orden · reserva stock |
| 14 | POST | `/api/orders/:id/ship` | Orders | JWT | Genera etiqueta + tracking |
| 15 | POST | `/api/orders/:id/cancel` | Orders | JWT | Cancela · libera stock · refund |
| 16 | POST | `/api/payments` | Payments | JWT | Crea pago abstrayendo pasarela |
| 17 | POST | `/api/invoices/emit` | Payments | JWT | Emite DTE 33/39/61 en SII |
| 18 | POST | `/api/channels/meli/sync` | Channels | JWT | Sync MeLi stock + precios + listings |
| 19 | POST | `/api/channels/mp/sync` | Channels | JWT | Sync catálogo Mercado Público |
| 20 | GET | `/api/channels` | Channels | JWT | Canales activos + health |
| 21 | POST | `/api/cerebro/chat` | Cerebro IA | JWT | Chat IA · SSE streaming · fallback chain |
| 22 | GET | `/api/cerebro/opportunities` | Cerebro IA | JWT | Oportunidades scored sin LLM |
| 23 | POST | `/api/webhooks/meli` | Webhooks | HMAC | Recibe órdenes MeLi · firma SHA-256 |
| 24 | POST | `/api/webhooks/payment` | Webhooks | HMAC | Notif. pasarela · estado pago |
| 25 | POST | `/api/webhooks/courier` | Webhooks | HMAC | Tracking updates couriers |
| 26 | POST | `/api/cron/refresh-meli` | Cron | CRON_SECRET | Refresh tokens MeLi 6h |
| 27 | POST | `/api/cron/sync-mp` | Cron | CRON_SECRET | Sync licitaciones MP diario 8am |
| 28 | POST | `/api/cron/cache-cleanup` | Cron | CRON_SECRET | Limpia Smart Cache Cold 7d |
| 29 | GET | `/api/logs/api` | Logs | JWT founders | Logs centralizados LLMOps |
| 30 | GET | `/api/health` | Logs | público | Health check uptime |
| 31 | GET | `/api/suppliers` | Suppliers | JWT | Lista proveedores dropship activos |
| 32 | POST | `/api/suppliers` | Suppliers | JWT | Crea proveedor con auth_mode |
| 33 | PATCH | `/api/suppliers/:id` | Suppliers | JWT | Update credentials / payment_terms / status |
| 34 | POST | `/api/suppliers/:id/sync-catalog` | Suppliers | JWT | Sync catálogo proveedor → mkt_supplier_products |
| 35 | POST | `/api/suppliers/:id/purchase-orders` | Suppliers | JWT | Crea OC al proveedor (propagación dropship) |
| 36 | GET | `/api/suppliers/:id/purchase-orders/:po_id` | Suppliers | JWT | Estado + tracking OC |
| 37 | POST | `/api/webhooks/supplier/:supplier_code` | Webhooks | HMAC | Webhook proveedor (tracking · stock · cancellation) |
| 38 | GET | `/api/ads/accounts` | Ads | JWT | Cuentas publicitarias (Mercado/Meta/Google/TikTok) |
| 39 | POST | `/api/ads/accounts` | Ads | JWT | Conectar nueva cuenta con OAuth |
| 40 | GET | `/api/ads/campaigns` | Ads | JWT | Lista campañas con filtros + ROAS actual |
| 41 | POST | `/api/ads/campaigns` | Ads | JWT | Crea campaña multi-canal |
| 42 | PATCH | `/api/ads/campaigns/:id` | Ads | JWT | Pausar · ajustar presupuesto · status |
| 43 | GET | `/api/ads/metrics` | Ads | JWT | Time series spend/clicks/conv/roas por campaña |
| 44 | POST | `/api/ads/events` | Ads | JWT | Envía conversion event a Meta CAPI / Google EC / TikTok Events |
| 45 | POST | `/api/cron/ads-sync-metrics` | Cron | CRON_SECRET | Sync diario métricas desde providers |
| 46 | POST | `/api/cron/ads-events-batch` | Cron | CRON_SECRET | Envía conversion events pendientes batch 5min |

# 02 · Mapa de interacciones · quién llama a quién

> [!hla] api-interactions
> Cómo se conectan los 30 endpoints internamente. Click en cualquier bloque ve qué otros endpoints dispara o consume. Hover destaca la ruta end-to-end · filtros canal aíslan MeLi · MP · D2C · B2B.

# 03 · Detalle expandible · estilo Swagger interactivo

> [!swagger] api-spec
> Click en cualquier endpoint expande detalle · parámetros · request body · responses por código · curl ejemplo. **Login arriba** para activar el "▶ Probar" en cada endpoint · ejecuta requests reales contra la API.

# 02 · Convenciones del API

| Tema | Decisión |
|------|----------|
| Versionado | Path NO incluye `/v1/` Y1 · evaluar `/v2/` cuando haya breaking changes |
| Auth default | Bearer JWT (Supabase Auth) en header `Authorization` |
| Excepciones auth | Webhooks (HMAC firma) · Cron jobs (CRON_SECRET header) · `/health` público |
| Tenant aislamiento | `tenant_id` extraído del JWT · RLS Postgres aplica automático |
| Content-Type | `application/json` request y response |
| Errores | Estructura uniforme: `{ "error": "code", "message": "humano", "details": [...] }` |
| Rate limit | 60 req/min por user · 600 req/min por IP · headers `X-RateLimit-*` |
| Idempotency | Opcional via header `Idempotency-Key` (UUID) · obligatorio en POST /payments |

# 03 · Códigos de error estandarizados

| Code | Significado | Acción |
|------|-------------|--------|
| 200 | OK | — |
| 201 | Created | — |
| 400 | Bad Request | Revisar query params o body |
| 401 | Unauthorized | Token vencido · refresh o re-login |
| 403 | Forbidden | RLS o role insuficiente |
| 404 | Not Found | Recurso no existe en tenant actual |
| 409 | Conflict | Duplicate · stock insuficiente · idempotency repetida |
| 422 | Unprocessable | Validación Zod falló |
| 429 | Too Many Requests | Rate limit · esperar `Retry-After` |
| 500 | Internal Error | Reportar con `request-id` del header |
| 502 | Bad Gateway | Servicio externo down (SII · MeLi) · retry exponencial |
| 503 | Service Unavailable | Health degraded |

# 04 · Authentication flow

```
1. POST /api/auth/login  → access_token (1h) + refresh_token (30d) cookies httpOnly
2. Cualquier request    → header Authorization: Bearer <access_token>
3. Token vencido         → 401 → POST /api/auth/refresh con cookie refresh_token
4. Refresh vencido       → re-login obligatorio
5. POST /api/auth/logout → limpia cookies httpOnly · invalida refresh_token en DB
```

# 05 · Anti-patrones reportados

> [!anti] Evitar al consumir el API
> - Pasar tokens en query string · usar SIEMPRE header Authorization
> - Hardcodear `tenant_id` en cliente · viene del JWT
> - Reintentar 4xx · solo 5xx con backoff exponencial
> - Hacer requests en loop sin idempotency key (especialmente /payments)
> - Asumir orden de respuesta en streaming SSE (eventos no garantizan orden estricto)

# 06 · Versionado y breaking changes

- v1.0.0 actual · sin path versioning explícito
- v2.0.0 futuro: agregar `/v1/` prefix antes de cualquier breaking change
- Anuncio breaking change: 90 días en Doc 41 Changelog + email a founders
- Endpoints deprecated: header `Sunset: <date>` + log warning del cliente

# 07 · Performance esperada

| Tipo | p50 | p95 |
|------|-----|-----|
| Auth | 80 ms | 200 ms |
| Lista paginada | 120 ms | 350 ms |
| Detail endpoint | 90 ms | 220 ms |
| Mutaciones (POST/PATCH) | 200 ms | 600 ms |
| Sync canales (POST /channels/*/sync) | 1-3 s | 8 s |
| Cerebro SSE chat | 200 ms first token | 600 ms first token |
| Suppliers sync-catalog | 5-15 s | 30 s |
| Ads metrics fetch | 1-3 s | 8 s |
| Ads events POST (CAPI) | 80 ms | 200 ms |

# 08 · Detalle endpoints Suppliers (Doc 13 §08 · ADR-0003)

## POST /api/suppliers

Crea un proveedor dropship. Soporta 4 auth modes: api_key · oauth · email_automated · whatsapp_business.

```json
// Request
{
  "supplier_code": "proveedor-x",
  "display_name": "Proveedor X SpA",
  "rut": "76.123.456-7",
  "auth_mode": "api_key",
  "credentials": { "api_key": "..." },
  "contact_email": "ventas@proveedor.cl",
  "payment_terms": "7d post-venta · transferencia CLP"
}

// Response 201
{
  "id": "uuid",
  "supplier_code": "proveedor-x",
  "status": "active"
}
```

Validation Zod: `supplier_code` slug · `auth_mode` enum · `credentials` matches schema según auth_mode.

## POST /api/suppliers/:id/sync-catalog

Dispara `SupplierAdapter.syncCatalog()` · upsert en `mkt_supplier_products`.

```json
// Response 200
{
  "synced_count": 342,
  "new_count": 28,
  "updated_count": 314,
  "deactivated_count": 0,
  "duration_ms": 8432
}
```

## POST /api/suppliers/:id/purchase-orders

Crea OC dropship (uso interno desde flujo orden) o manual desde dashboard.

```json
// Request
{
  "items": [{ "supplier_sku": "SKU-X-001", "qty": 2 }],
  "ship_to": {
    "full_name": "Juan Pérez",
    "rut": "12.345.678-9",
    "street": "Av. Providencia 1234",
    "city": "Santiago",
    "region": "RM",
    "phone": "+56912345678"
  },
  "order_id": "uuid-orden-marketplace"  // opcional · NULL si manual
}

// Response 201
{
  "id": "uuid-po",
  "external_po_id": "PROV-X-99887",
  "status": "created",
  "total_clp": 45000,
  "expected_shipped_at": "2026-05-30T00:00:00Z"
}
```

## POST /api/webhooks/supplier/:supplier_code

Recibe webhook de proveedor (HMAC firmado). Eventos: shipped · delivered · cancelled · stock_changed.

```json
// Request (firma en header X-Supplier-Signature)
{
  "event_type": "shipped",
  "external_po_id": "PROV-X-99887",
  "tracking_number": "CHX-12345",
  "courier": "Chilexpress",
  "occurred_at": "2026-05-28T14:23:00Z"
}

// Response 200
{ "ok": true, "event_id": "uuid" }
```

# 09 · Detalle endpoints Ads (Doc 02 BBP P14)

## POST /api/ads/accounts

Conecta cuenta publicitaria con OAuth. Tokens cifrados en Supabase Vault.

```json
// Request
{
  "provider": "mercado_ads",   // o "meta" | "google_ads" | "tiktok"
  "oauth_code": "...",          // recibido del flow OAuth callback
  "display_name": "SMC SpA · Mercado Ads",
  "monthly_budget_clp": 500000
}

// Response 201
{
  "id": "uuid",
  "provider": "mercado_ads",
  "external_account_id": "MLA123456",
  "is_active": true
}
```

## POST /api/ads/campaigns

Crea campaña en provider remoto + sincroniza row local.

```json
// Request
{
  "account_id": "uuid",
  "name": "Black Friday 2026",
  "product_ids": ["uuid-sku-1", "uuid-sku-2"],
  "budget_clp": 100000,
  "start_date": "2026-11-25",
  "end_date": "2026-11-30"
}

// Response 201
{
  "id": "uuid",
  "external_campaign_id": "ADS-99887",
  "status": "active"
}
```

## GET /api/ads/metrics

Time series spend/clicks/conv/roas. Filtro por campaign_id · date_range.

```bash
GET /api/ads/metrics?campaign_id=uuid&date_from=2026-05-01&date_to=2026-05-27
```

```json
// Response 200
{
  "campaign_id": "uuid",
  "rows": [
    { "date": "2026-05-27", "impressions": 4523, "clicks": 89, "conversions": 7, "spend_clp": 12000, "revenue_clp": 84000, "roas": 7.0 }
  ],
  "summary": {
    "total_spend": 240000,
    "total_revenue": 1820000,
    "average_roas": 7.58,
    "alerts": []
  }
}
```

Si ROAS &lt;1.5 últimos 7 días · `summary.alerts` incluye `{ "type": "low_roas", "suggestion": "pausar o cambiar creatividad" }`.

## POST /api/ads/events

Envía conversion event server-side (Meta CAPI · Google Enhanced Conversions · TikTok Events). Hashed PII según provider spec.

```json
// Request
{
  "provider": "meta_capi",
  "event_type": "purchase",
  "event_id": "uuid-order-1",   // idempotency
  "user_data": {
    "em": "sha256-hash-email",
    "ph": "sha256-hash-phone"
  },
  "custom_data": {
    "value": 45000,
    "currency": "CLP",
    "content_ids": ["sku-1"]
  }
}

// Response 200
{ "ok": true, "queued_for_provider": true }
```

Cron `/api/cron/ads-events-batch` (5min) envía batch pendientes a cada provider.
