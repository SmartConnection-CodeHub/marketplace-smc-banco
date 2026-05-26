---
number: 39
id: api-sdk-postman
title: API SDK & Postman
subtitle: "Cómo consumir la API Marketplace SMC · ejemplos curl · SDK JS · colección Postman · autenticación."
block: Producto
author: Backend
version: 1.0
date: 2026-05-26
status: 🟢 Activo
prev: 38-onboarding-dev.html
next: 40-glosario.html
---

# 01 · Base URL

| Ambiente | URL |
|----------|-----|
| Producción | `https://marketplace.smconnection.cl/api` |
| QAS | `https://qas.marketplace.smconnection.cl/api` (futuro) |
| Local dev | `http://localhost:3000/api` |

# 02 · Autenticación

Toda llamada requiere bearer token JWT obtenido vía Supabase Auth.

```
curl -X POST https://marketplace.smconnection.cl/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"usuario@ejemplo.cl","password":"***"}'
```

Respuesta:

```
{
  "access_token": "eyJhbGc...",
  "refresh_token": "eyJhbGc...",
  "expires_in": 3600,
  "tenant_id": "uuid-tenant"
}
```

Usar token en headers de toda llamada posterior:

```
Authorization: Bearer eyJhbGc...
```

# 03 · Endpoints principales

## GET /api/products

Lista productos del tenant. Soporta filtros y paginación.

```
curl -H "Authorization: Bearer $TOKEN" \
  "https://marketplace.smconnection.cl/api/products?limit=20&offset=0"
```

Query params:

- `limit` (default 20 · max 100)
- `offset` (default 0)
- `channel` (meli · d2c · b2g · b2b · all)
- `category_id`
- `search` (busca en nombre · descripción)
- `order` (default `created_at.desc`)

## GET /api/opportunities

Devuelve oportunidades scored (sin LLM). Ver ADR-0001.

```
curl -H "Authorization: Bearer $TOKEN" \
  "https://marketplace.smconnection.cl/api/opportunities?min_score=70"
```

## POST /api/sync/meli

Dispara sincronización con MeLi (proxy OAuth).

```
curl -X POST -H "Authorization: Bearer $TOKEN" \
  https://marketplace.smconnection.cl/api/sync/meli
```

## GET /api/data

Endpoint genérico tabla. Cuidado con `order` por defecto.

> [!warning] Bug conocido
> Default `order=created_at.desc` falla en `mkt_products` (tiene `snapshot_at`). Pasar `order=snapshot_at.desc` explícito si la tabla no tiene `created_at`.

# 04 · Códigos error

| Code | Significado | Acción |
|------|-------------|--------|
| 200 | OK | - |
| 201 | Creado | - |
| 400 | Bad request | Revisar query params · body |
| 401 | No autorizado | Token vencido · re-login |
| 403 | Prohibido | RLS · este tenant no tiene acceso |
| 404 | No existe | Revisar id |
| 429 | Rate limit | Esperar · ver header `Retry-After` |
| 500 | Server error | Reportar a soporte con request-id |

# 05 · Rate limits

- 60 requests/minuto por usuario
- 600 requests/minuto por IP
- Headers de respuesta: `X-RateLimit-Limit` · `X-RateLimit-Remaining` · `X-RateLimit-Reset`

# 06 · SDK JS (futuro Q2 2027)

Por ahora sólo curl/fetch directo. SDK oficial en roadmap:

```
// borrador del SDK · NO existe aún
import { MarketplaceSMC } from '@smc/sdk-js'

const client = new MarketplaceSMC({ apiKey: '...' })

const products = await client.products.list({ limit: 20 })
const opps = await client.opportunities.list({ minScore: 70 })
await client.sync.meli()
```

# 07 · Colección Postman

Descargar colección curada con todos los endpoints:

```
https://marketplace.smconnection.cl/docs/postman/Marketplace-SMC.json
```

Importar en Postman:

1. File → Import → URL
2. Pegar URL
3. Configurar environment con `base_url` y `access_token`
4. Run collection completa para smoke test

# 08 · Webhooks (Q3 2027)

Suscribir a eventos asincrónicos:

- `product.synced`
- `order.created`
- `inventory.low_stock`
- `opportunity.detected`

Endpoint registro:

```
POST /api/webhooks/subscribe
{ "url": "https://tuapp.cl/hook", "events": ["order.created"] }
```

> [!info] Verificación
> Cada webhook llega firmado HMAC SHA-256 · validar header `X-SMC-Signature` antes de procesar.
