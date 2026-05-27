---
number: 13
id: especificacion-tecnica
title: Especificación Técnica
subtitle: "Cómo se construye granular · stack librería por librería · 5 ADRs · flujos detallados · monorepo · CI/CD · escalabilidad."
block: Producto Técnico
author: Architect + Hoku + Cerebro
version: 2.0
date: 2026-05-27
status: 🟡 Draft · pendiente review founders
prev: 11-especificacion-funcional.html
next: 14-founders-journey.html
---

# 01 · Premisa

Doc 13 detalla **cómo se construye** Marketplace SMC a nivel granular: librería específica por capa · cómo conversan entre sí · flujos técnicos detallados · ADRs registradas · cuándo refactorizar.

> [!info] No es repetición de Doc 07 Architecture
> Doc 07 muestra el HLA + 5 escenarios. Doc 13 detalla decisiones técnicas con librerías específicas · flujos request/response · event lifecycle · queries · CI/CD pipeline · cuándo aplica cada ADR.

# 02 · Stack completo · librería por librería

## 2.1 · Runtime + Framework

| Capa | Librería específica | Versión | Justificación |
|------|---------------------|---------|---------------|
| Runtime | Node.js | 22 LTS | Estable hasta 2027-04 |
| Framework | Next.js | 16.x App Router | RSC + Server Actions + ISR + middleware |
| TypeScript | TypeScript | 5.x strict mode | Type safety · catch en build |
| Build | Turbopack | (incluido Next.js 16) | Builds 10x más rápidos que webpack |

## 2.2 · UI + Frontend

| Capa | Librería específica | Versión | Rol |
|------|---------------------|---------|-----|
| CSS engine | Tailwind CSS | v4 | Utility-first · JIT compiler |
| Variants | Tailwind Variants (tv) | latest | Component variants + slots |
| Primitivas a11y | Radix UI | latest | Accesibilidad WAI-ARIA |
| Iconos | Lucide React | latest | Tree-shake · stroke 1.75 consistente |
| Motion | Framer Motion | 11.x | Animaciones + gestos |
| Forms | React Hook Form | 7.x | Performance · uncontrolled inputs |
| Validation | Zod | 3.x | Schema único client+server |
| State global Y1 | URL params + RSC | nativo | Sin Zustand/Redux Y1 · YAGNI |
| Data fetching client | TanStack Query | 5.x | Solo donde RSC no aplica |
| Charts | Recharts | latest | Si se necesitan dashboards complejos |
| Package interno | @smc/ui | propio | Abstracción Radix + tv + lucide |

## 2.3 · Backend + Data

| Capa | Librería específica | Versión | Rol |
|------|---------------------|---------|-----|
| ORM | Drizzle ORM | latest | Type-safe · zero runtime · migrations versionadas |
| DB driver | postgres.js (de Drizzle) | latest | Connection pooling para serverless |
| Auth | Supabase Auth + JWT | latest | Email/password + TOTP 2FA opcional |
| Auth SSR | @supabase/ssr | latest | Cookies httpOnly + refresh token rotation |
| Real-time | Supabase Realtime | latest | Only para subscribe específicos (Y2) |
| Storage | Supabase Storage | latest | Buckets con RLS · signed URLs |
| Rate limit | Upstash Redis + ratelimit | latest | 60 req/min/user · 600 req/min/IP |
| Idempotency | Custom middleware | propio | Tabla `mkt_idempotency` con TTL 24h |

## 2.4 · Integraciones externas

| Servicio | SDK / método | Auth | Estado Sprint 2 |
|----------|--------------|------|-----------------|
| **SoloTodo** (Plan B activo) | fetch directo | Sin auth · API pública gratis | ✅ Conectado · 58K productos MeLi indexados |
| Mercado Libre (objetivo) | fetch directo · sin SDK oficial | OAuth 2.0 PKCE | 🟡 App pendiente aprobación PolicyAgent |
| Mercado Público | fetch directo | Ticket env var | ⏭️ Fase 3 |
| Open Factura | fetch directo + cert digital | API key + cert | ⏭️ Sprint 4 |
| **Transferencia bancaria Kanki-style** (default Y1) | UI propia + upload comprobante | Sin auth · verify manual founder | ⏭️ Sprint 5 D2C |
| MercadoPago (opcional dual) | mercadopago oficial SDK | OAuth + webhook firmado | ⏭️ Sprint 5 D2C |
| WebPay Plus (deferido Y2) | @transbank/webpay-plus | Cert + commerce code | ⏭️ Y2 |
| Chilexpress | fetch directo | API key | ⏭️ Sprint 4 |
| Starken | fetch directo | API key | ⏭️ Sprint 4 |
| OpenRouter | openai SDK (compatible API) | API key | ✅ Hoku fallback chain |
| **Gmail API** (default Y1) | googleapis SDK | OAuth 2.0 cuenta SMC | ⏭️ Sprint 4 |
| Resend (deferido Y2) | resend SDK | API key | ⏭️ Y2 si Gmail no escala |
| Sentry | @sentry/nextjs | DSN | ✅ Configurado |
| PostHog | posthog-node + posthog-js | Project API key | ⏭️ Sprint 3 |

> [!info] SoloTodo es Plan B oficial mientras MeLi aprueba app
> MeLi bloquea endpoints públicos (403 sin OAuth desde servidores) · app SmartConnection-Marketplace en revisión PolicyAgent en developers.mercadolibre.cl. Mientras tanto · **SoloTodo** (api.solotodo.com · store_id 260) entrega 58K+ productos MeLi Chile indexados · precios actualizados 6-12h · URLs reales · sin auth · sin costo. Sirve para: análisis competencia · scoring oportunidades · benchmarks precio. Cuando MeLi apruebe → SoloTodo se mantiene como caché/fallback · NO se elimina (redundancia + costo cero).

## 2.5 · DevOps + Observability

| Capa | Tool | Rol |
|------|------|-----|
| Hosting | AWS Amplify | Next.js auto-deploy push to main |
| CDN | CloudFront (incluido Amplify) | Edge caching + WAF |
| Cert | ACM | Auto-renovado |
| DNS | Route 53 | smconnection.cl + subdomains |
| Cron | Vercel Cron (proxy via Amplify) | Schedule jobs |
| CI/CD | GitHub Actions | Lint · type-check · tests · build · tag |
| Monitoring infra | CloudWatch | Lambda · API Gateway · cost |
| Monitoring errors | Sentry | Frontend + backend |
| Analytics product | PostHog Cloud | Funnels · feature flags · events |
| LLMOps | Tabla `mkt_ai_logs` + dashboards Postgres | Cost · latency · quality |
| Logs aggregator | CloudWatch + filter Sentry | Structured JSON logs |

# 03 · Arquitectura de capas

> [!hla] arquitectura-capas
> Mapa técnico detallado · cada capa con librería · cómo intercambia datos con la siguiente · request/response paths.

# 04 · Request lifecycle · de browser a DB y vuelta

```
Browser (founder) hace acción
     ↓
Next.js Middleware (auth · rate limit · idempotency check)
     ↓
Route Handler (/api/X) o Server Action
     ↓
Zod schema validation (input)
     ↓
Business logic layer (services/ folder)
     ↓
Drizzle ORM (type-safe queries · transactions)
     ↓
Supabase Postgres (RLS apply by tenant_id)
     ↓
[opcional] pg_notify si data afecta otros canales
     ↓
[opcional] Side effects (call MeLi · Open Factura · etc)
     ↓
Zod schema validation (output)
     ↓
Response al browser (JSON o RSC stream)
     ↓
Sentry log si error · PostHog event si feature usage
     ↓
mkt_api_logs row append-only para audit
```

Target end-to-end: API lectura p95 &lt;350ms · mutación p95 &lt;600ms.

# 05 · Data flow cross-canal · venta MeLi

```
1. MeLi POST webhook a /api/webhooks/meli
2. Middleware verifica HMAC SHA-256 firma
3. Middleware verifica idempotency_key contra mkt_idempotency
4. Si new event: INSERT mkt_orders (status='created')
5. Trigger Postgres: UPDATE mkt_inventory.reserved += qty
   (con SELECT FOR UPDATE para evitar concurrency oversell)
6. Trigger Postgres: pg_notify('inventory_changed', product_id)
7. Listener Node.js subscriber recibe notify
8. Listener llama channels-sync API por cada adapter activo:
   · Adapter D2C → actualiza ISR revalidate
   · Adapter MP → actualiza stock en MP API
   · Adapter B2B → invalida cache portal
9. Mientras tanto · evento order.created dispara:
   · Side effect: emit DTE 39 vía Open Factura
   · Side effect: generate label vía Chilexpress
   · Side effect: send email comprador vía Resend
10. Cada side effect → row en mkt_api_logs (audit)
11. Sentry breadcrumbs en cada paso · si error → alerta
```

# 06 · Event-driven architecture

```
EVENTOS INTERNOS (pg_notify · solo Postgres)
─────────────────────────────────────────────────────
inventory_changed      → channels-sync · ISR revalidate
order_completed        → emit DTE · email comprador
opportunity_detected   → push notification UI
ads_roas_low           → alerta founder (sugerencia pausa)
licitacion_match       → notification Javier
threshold_phase_met    → email cierre fase

EVENTOS EXTERNOS (webhooks inbound · HMAC verificado)
─────────────────────────────────────────────────────
POST /webhooks/meli           → order events MeLi
POST /webhooks/payment        → pasarelas (MP · WebPay)
POST /webhooks/courier        → tracking updates
POST /webhooks/mp             → adjudicación MP
POST /webhooks/supplier/:id   → dropship suppliers

EVENTOS PROGRAMADOS (Vercel Cron)
─────────────────────────────────────────────────────
POST /cron/refresh-meli       6h · refresh OAuth tokens
POST /cron/sync-mp            8am · sync licitaciones diarias
POST /cron/cache-cleanup      7d · eliminar Smart Cache Cold
POST /cron/scoring-daily      6am · Cerebro scoring oportunidades
POST /cron/conciliacion       1ro mes · matching pagos vs DTE
POST /cron/reputation-tracker 1h · refresh materialized view
```

# 07 · Channel Adapter Pattern · interface + 4 impl

## Interface

```typescript
interface ChannelAdapter {
  readonly channelId: 'meli' | 'd2c' | 'mp' | 'b2b';
  readonly displayName: string;

  // Catalog
  publishProduct(product: Product, listing: ChannelListing): Promise<{ externalId: string }>;
  updateProduct(externalId: string, changes: Partial<Product>): Promise<void>;
  unpublishProduct(externalId: string): Promise<void>;
  syncStock(externalId: string, qty: number): Promise<void>;

  // Orders
  fetchOrders(since: Date): Promise<Order[]>;
  acceptOrder(externalOrderId: string): Promise<void>;
  shipOrder(externalOrderId: string, tracking: string): Promise<void>;
  cancelOrder(externalOrderId: string, reason: string): Promise<void>;

  // Auth
  refreshAuth(): Promise<void>;
  isAuthValid(): Promise<boolean>;

  // Health
  ping(): Promise<{ ok: boolean; latency_ms: number }>;
}
```

## 4 Implementaciones

| Canal | Clase | Highlights |
|-------|-------|------------|
| **MeLi** | `MercadoLibreAdapter` | OAuth 2.0 PKCE · refresh 6h · webhook firmado · rate limit 1K req/min |
| **D2C** | `D2CStorefrontAdapter` | Next.js ISR revalidate · stock real-time UI · pasarelas internas (Y2) |
| **MP** | `MercadoPublicoAdapter` | Ticket auth · sync diario 8am · postular ofertas · webhook adjudicación |
| **B2B** | `B2BCustomAdapter` | API keys por cliente · RFQ workflow · firma HMAC aprobación |

Beneficio: agregar canal nuevo = 1 archivo nuevo. NO refactor del resto.

# 08 · Supplier Adapter Pattern

```typescript
interface SupplierAdapter {
  readonly supplierId: string;
  readonly displayName: string;
  readonly authMode: 'api_key' | 'oauth' | 'email_automated' | 'whatsapp_business';

  syncCatalog(): Promise<SupplierProduct[]>;
  checkStock(sku: string): Promise<{ available: number; updated_at: Date }>;
  createPurchaseOrder(items: OrderItem[], shipTo: Address): Promise<{ poId: string }>;
  cancelPurchaseOrder(poId: string, reason: string): Promise<void>;
  trackShipment(poId: string): Promise<{ status: string; eta: Date; tracking_number?: string }>;
  handleReturn(orderId: string, items: ReturnItem[]): Promise<{ rmaId: string }>;
  ping(): Promise<{ ok: boolean }>;
}
```

ADR-0003 formaliza este pattern para modo dropshipping Y1.

# 09 · Estructura monorepo

```
marketplace-smc/                       (repo principal · Next.js app)
├── app/
│   ├── (founders)/                   (route group · auth wall)
│   │   ├── dashboard/
│   │   ├── productos/
│   │   ├── ordenes/
│   │   ├── cerebro/
│   │   ├── oportunidades/
│   │   ├── ads/
│   │   ├── mercado-publico/
│   │   ├── b2b/
│   │   └── settings/
│   ├── (public)/                     (route group · sin auth)
│   │   ├── d2c/                      (storefront Y2)
│   │   └── b2b/rfq/                  (portal cliente B2B)
│   └── api/
│       ├── auth/
│       ├── products/
│       ├── orders/
│       ├── channels/{meli|d2c|mp|b2b}/
│       ├── suppliers/
│       ├── ads/
│       ├── cerebro/
│       ├── webhooks/{meli|payment|courier|mp|supplier}/
│       └── cron/
├── lib/
│   ├── db/                           (Drizzle schema + migrations)
│   ├── adapters/
│   │   ├── channels/{meli,d2c,mp,b2b}.ts
│   │   └── suppliers/{xxx}.ts
│   ├── cerebro/                      (scoring · chat SSE · cache)
│   ├── auth/                         (Supabase Auth helpers SSR)
│   ├── validators/                   (Zod schemas)
│   └── utils/
├── packages/
│   ├── ui/                           (@smc/ui · componentes atómicos)
│   ├── shared/                       (@smc/shared · tipos cross-canal)
│   └── prompts/                      (@smc/prompts · versionados IA)
├── supabase/
│   ├── migrations/                   (SQL versionado)
│   └── seed.sql
├── .github/workflows/
│   ├── ci.yml                        (lint + type + test + build + tag)
│   └── e2e.yml                       (Playwright nightly · Y2)
└── public/
```

# 10 · Integración BD · cómo se conecta

```
Next.js Server Components / Route Handlers
     ↓
import { db } from '@/lib/db'         (singleton client)
     ↓
Drizzle ORM (type-safe queries)
     ↓
postgres.js (driver con connection pooling)
     ↓
Supabase Postgres (RLS enforced)
     ↓
Si tenant_id en JWT no matches → 0 rows (RLS bloquea)
```

## Patrones obligatorios

```typescript
// ✅ Server-side · createServerClient (RLS aplicada)
import { createServerClient } from '@/lib/supabase/server';

export async function getProducts() {
  const supabase = await createServerClient();
  const { data } = await supabase.from('products').select('*');
  return data;
}

// ❌ NUNCA queries con service_role en código client-side

// ✅ Server Action con Zod validation
'use server';
import { z } from 'zod';
import { createServerClient } from '@/lib/supabase/server';

const schema = z.object({
  sku: z.string().min(3),
  name: z.string().min(1),
  base_price: z.number().int().positive(),
});

export async function createProduct(input: unknown) {
  const parsed = schema.parse(input);
  const supabase = await createServerClient();
  const { data, error } = await supabase.from('products').insert(parsed).select().single();
  if (error) throw new Error(error.message);
  return data;
}
```

# 11 · Orquestación · cuando entra una orden

```
ORDEN ENTRA → orchestrator decide qué hacer
     ↓
1. Identify channel (meli · mp · d2c · b2b)
2. Call ChannelAdapter[channel].acceptOrder()
3. Postgres transaction:
   · INSERT mkt_orders
   · UPDATE mkt_inventory (reserve)
   · INSERT mkt_order_items
4. If is_dropship product → SupplierAdapter[supplier_id].createPurchaseOrder()
5. Trigger pg_notify('order_completed')
6. Side effect listener:
   · emit DTE
   · generate label (si stock propio)
   · send email comprador
7. PostHog event 'order.completed'
8. Sentry breadcrumb success
```

# 12 · Deploy · ambientes · CI/CD

## Ambientes

| Ambiente | URL | Auto-deploy | Branch |
|----------|-----|-------------|--------|
| Development local | localhost:3000 | manual · `npm run dev` | feature branches |
| QAS (futuro Y2) | qas.marketplace.smconnection.cl | push develop | develop |
| Production | marketplace.smconnection.cl | push main + tests verdes | main |

## Pipeline CI · GitHub Actions

```yaml
name: CI — Marketplace
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  ci:
    permissions:
      contents: write  # para push tag

    steps:
      - Checkout
      - Setup Node 22
      - npm ci
      - npm test (Vitest)
      - npx tsc --noEmit (type-check)
      - npm run build (Next.js production build)
      - if main + tests OK → git tag deploy-marketplace-YYYY.MM.DD-XXX
      - if main → AWS Amplify auto-deploy hook
      - smoke test post-deploy (curl marketplace.smconnection.cl status 200)
      - if smoke fail → rollback automático + alerta Sentry
```

## Rollback strategy

- AWS Amplify mantiene últimos 25 builds
- Rollback en 1 click vía console O CLI
- Tag deploys permite git checkout fácil
- Si rollback dispara → notification founders + Sentry incident

# 13 · Escalabilidad técnica · cuándo refactorizar

```
SEÑAL                                          ACCIÓN
─────────────────────────────────────────────────────
Build time > 5min                              Turbopack tuning · code splitting
Bundle client > 500KB                          Dynamic imports · server components
API p95 > 800ms                                Add caching · index DB · query review
DB connections agotadas                        Pool tuning · pgBouncer
1 canal > 80% revenue                          Acelerar diversificación (BR-driven)
Founder > 8h/día sistema                       Automatizar más · agentes IA bg
Tests > 5min                                   Parallelizar · test sharding
Costo IA > $300K CLP/mes                       Cache prompts comunes · downgrade modelos
Tabla Postgres > 1M rows                       Indexar correctamente · particionar
Tenant count > 5                               Migrar de tenant_id implicit a explicit
                                               sharding (Y3+)
```

## Cuándo NO refactorizar

- ❌ "Para hacer el código más limpio" sin métrica concreta
- ❌ "Para usar la tecnología nueva X" sin caso de uso real
- ❌ "Porque siempre quise" — guardarse para hobbies personales

> [!info] Regla de oro
> Refactor cuando hay número concreto que dispara · NO porque "se ve mejor". Rule of three: 3 violaciones repetidas → abstraer. NO refactorizar 1 vez.

# 14 · ADRs registradas · 6 decisiones

| ADR | Título | Status | Dónde está el detalle |
|-----|--------|--------|-----------------------|
| ADR-0001 | v5 Opportunities sin LLM | ✅ Accepted | Doc 09 Sistema Oportunidades |
| ADR-0002 | Channel Adapter Pattern | ✅ Accepted | sección 07 |
| ADR-0003 | Supplier Adapter Pattern | 🟡 Proposed | sección 08 |
| ADR-0004 | ADS multicanal automation (Y2) | 🟡 Proposed | Doc 11 · sección Ads |
| ADR-0005 | Versionado banco v3 ↔ v4 | 🟡 Proposed | Doc 10 Assessment · sección 08 |
| ADR-0006 | SoloTodo como Plan B catálogo MeLi | ✅ Accepted | sección 14b · este doc |
| ADR-0007 | Gmail API en vez de Resend Y1 | ✅ Accepted | sección 14c · este doc |
| ADR-0008 | Pagos dual: transferencia Kanki-style + MercadoPago opt | ✅ Accepted | sección 14d · este doc |

## 14b · ADR-0006 · SoloTodo Plan B mientras MeLi aprueba app

**Status**: ✅ Accepted · 2026-05-27
**Context**: app SmartConnection-Marketplace en review PolicyAgent MeLi (developers.mercadolibre.cl). Mientras no esté aprobada · endpoints públicos MeLi devuelven 403 desde servidores (anti-scraping). Sin OAuth tampoco se puede leer catálogo.

**Decisión**: usar **SoloTodo API** (api.solotodo.com · MELI_STORE_ID=260) como fuente de catálogo MeLi Chile mientras MeLi aprueba.

**Por qué SoloTodo**:
- 58K+ productos MeLi Chile indexados (verificado live 2026-05-27)
- Precios actualizados cada 6-12h
- URLs reales del producto en MeLi (clickeables)
- Cross-store: agrupa precios MeLi vs Falabella · París · Ripley · etc
- API pública sin auth · sin costo
- Estable hace años (proyecto chileno consolidado)

**Trade-offs aceptados**:
- ❌ NO permite publicar ni vender · solo lectura
- ❌ NO entrega cuentas propias (es público · vemos competencia · no nuestras ventas)
- ❌ Latencia 6-12h vs real-time webhook MeLi
- ✅ Cubre 100% análisis competencia + scoring oportunidades
- ✅ Cero costo · cero riesgo policy
- ✅ Cuando MeLi apruebe → se mantiene como caché/fallback redundante

**Cómo se usa en código**:
- `lib/solotodo-client.ts` (329 líneas · client con tipos completos)
- `app/api/solotodo/test/route.ts` (health check)
- `app/dashboard/settings/page.tsx` (botón "Probar conexión SoloTodo")
- Sprint 3: integrar en Sistema Oportunidades como fuente de precios competencia

**Cuándo deprecate SoloTodo**:
- NUNCA · se mantiene siempre como fallback redundante
- Costo cero · no afecta cuotas MeLi · ayuda a validar consistencia precios

**Riesgo**: SoloTodo cambia API o sube paywall.
**Mitigación**: API pública desde 2014 · sin señales de cierre. Si pasa → seguimos con MeLi OAuth directo.

## 14c · ADR-0007 · Gmail API en vez de Resend Y1

**Status**: ✅ Accepted · 2026-05-27
**Context**: necesitamos enviar emails transaccionales (tracking · confirmación venta · post-venta · alertas founders). Sprint inicial sugirió Resend (servicio especializado · $0-20/mes). Founders ya tienen Google Workspace activo (smconnection.cl) con Gmail API funcional.

**Decisión**: usar **Gmail API** (cuenta `marketplace@smconnection.cl`) como motor de envío Y1.

**Por qué Gmail API**:
- Costo cero adicional (Workspace Business Starter ya pagado)
- Reputación dominio establecida (mejor deliverability que Resend nuevo)
- OAuth 2.0 SDK oficial googleapis
- 500-2000 emails/día por usuario Workspace (suficiente Y1)
- API SMC ya tiene credenciales (`reference_google_workspace.md`)

**Trade-offs**:
- ❌ No tiene templates fancy ni analytics builtin (debemos loggear nosotros)
- ❌ Limit 500-2000/día · si Marketplace explota (>2K órdenes/día) tendríamos que migrar
- ❌ Sin warming dominio automático
- ✅ Cero costo · cero proveedor nuevo
- ✅ Templates en código versionados @smc/prompts (regla Hoku)

**Cuándo migrar a Resend**:
- Volumen >1.5K emails/día sostenido (Y2 escalado)
- Necesitamos templates editables sin deploy
- Founders quieren métricas opens/clicks builtin

**Cómo se usa en código (Sprint 4)**:
- `lib/email/gmail-client.ts` · googleapis SDK
- `lib/email/templates/` · markdown templates versionados
- Cron 5min batch envíos (evita rate limit)
- Logging en `mkt_email_logs` (similar a mkt_ai_logs)

## 14d · ADR-0008 · Pagos dual: transferencia Kanki-style + MercadoPago opt

**Status**: ✅ Accepted · 2026-05-27
**Context**: necesitamos cobrar en D2C storefront. Sprint inicial sugirió MercadoPago + WebPay Plus. Founders recién partiendo · sin volumen para justificar setup pasarelas. Kanki Street (proyecto hermano SMC) opera con transferencia bancaria manual exitosamente.

**Decisión**: ofrecer **transferencia bancaria Kanki-style como default Y1** + **MercadoPago opcional** activable por SKU/cliente. WebPay Plus deferido Y2.

**Por qué dual**:

| Aspecto | Transferencia Kanki-style | MercadoPago opcional |
|---------|--------------------------|---------------------|
| Fee | 0% | 2.9-4.5% por transacción |
| Setup | Configurar cuenta bancaria · listo | OAuth + cert + webhook + reconciliación |
| Cliente | Sube comprobante en UI | Checkout directo |
| Founder | Verifica manual (5 min/día) | Auto |
| Tiempo orden | 1-24h (espera comprobante) | Real-time |
| Confianza cliente | Alta en Chile (común) | Más alta (instantánea) |
| Volumen sostenible | <50 órdenes/día | Ilimitado |

**Flow transferencia Kanki-style**:
1. Cliente hace checkout · ve datos transferencia (cuenta · RUT · monto · referencia)
2. Cliente sube comprobante PDF/imagen en UI
3. Sistema crea orden status=`payment_pending`
4. Founder recibe alerta · revisa comprobante · marca `payment_verified`
5. Workflow normal sigue (DTE + label + despacho)

**Flow MercadoPago (cuando activado por SKU)**:
1. Cliente hace checkout · redirect MercadoPago
2. Pago real-time · webhook firmado → orden status=`paid` directo
3. Workflow normal sigue

**Tabla `mkt_orders.payment_method`**: `'transferencia' | 'mercadopago' | 'webpay'` (futuro)
**Tabla `mkt_payment_proofs`** (nueva Sprint 5): comprobantes uploaded con verify state

**Cuándo activar MercadoPago default**:
- >20 órdenes/día sostenido 30 días
- Founders confirman costo 2.9-4.5% es asumible vs tiempo manual
- Cliente B2B grande que exige instantáneo

**Costo evitado Y1**: ~2.9-4.5% × revenue total Y1. Con 50 órdenes/mes × $25K CLP × 12 meses = $15M CLP/año revenue · ahorro ~$435K-675K CLP.

# 15 · Performance budgets

| Métrica | Budget | Trigger alarma |
|---------|--------|----------------|
| LCP (Largest Contentful Paint) | &lt; 2.5s | &gt; 4s |
| INP (Interaction to Next Paint) | &lt; 200ms | &gt; 500ms |
| CLS (Cumulative Layout Shift) | &lt; 0.1 | &gt; 0.25 |
| API p50 lectura | &lt; 120ms | &gt; 300ms |
| API p95 lectura | &lt; 350ms | &gt; 800ms |
| API p95 mutación | &lt; 600ms | &gt; 1.5s |
| Cerebro first token SSE | &lt; 600ms | &gt; 2s |
| Sync MeLi p95 | &lt; 8s | &gt; 30s |
| Build CI | &lt; 3min | &gt; 8min |
| Bundle client | &lt; 250KB gzipped | &gt; 500KB |

# 16 · Security requirements · 12 items con implementación

| # | Requerimiento | Implementación |
|---|--------------|----------------|
| SR-1 | TLS 1.3 obligatorio | Amplify default + HSTS preload header |
| SR-2 | AES-256 at rest | Supabase default (Postgres + Storage) |
| SR-3 | RLS Postgres siempre activo | Policies por tabla + tenant_id implícito JWT |
| SR-4 | service_role solo backend | Variable env Amplify · NUNCA `NEXT_PUBLIC_*` |
| SR-5 | 2FA obligatorio admins | Supabase Auth TOTP enforcement |
| SR-6 | Cookies httpOnly + SameSite=lax | @supabase/ssr default + custom config |
| SR-7 | CSP headers estrictos | next.config.ts `headers()` + report-uri |
| SR-8 | Rate limit 60 req/min user | Upstash Redis middleware Next.js |
| SR-9 | Idempotency keys POST críticos | UUID v7 · tabla `mkt_idempotency` TTL 24h |
| SR-10 | Audit logs append-only | Tabla `audit_logs` con RLS read-only · only INSERT |
| SR-11 | Secrets en Amplify env vars | NUNCA en repo · rotación trimestral docs/security |
| SR-12 | HMAC SHA-256 webhooks | `crypto.timingSafeEqual` para evitar timing attacks |

# 17 · Observabilidad · LLMOps detallado

```
LOG estructurado JSON por evento
─────────────────────────────────────────────────────
{
  timestamp: "2026-10-15T14:23:11.234Z",
  level: "info|warn|error",
  request_id: "uuid-correlation",
  user_id: "uuid",
  tenant_id: "uuid",
  feature: "products.list",
  endpoint: "/api/products",
  method: "GET",
  status: 200,
  duration_ms: 124,
  error_msg: null,
  metadata: { /* feature-specific */ }
}

→ stdout (CloudWatch) + tabla mkt_api_logs (Postgres queryable)

LLMOps específico Cerebro
─────────────────────────────────────────────────────
{
  timestamp: "2026-10-15T14:23:15.123Z",
  feature: "cerebro.chat",
  provider: "groq",
  model: "llama-3.3-70b-versatile",
  prompt_version: "chat-v2.1",
  tokens_in: 1234,
  tokens_out: 456,
  cost_usd: 0.00021,
  latency_ms: 287,
  cache_hit: false,
  fallback_used: false,
  hallucination_flag: false
}

→ tabla mkt_ai_logs · dashboards costo/feature/día/founder

ALERTAS configuradas (CloudWatch + Sentry)
─────────────────────────────────────────────────────
- Error rate > 1% por 5 min          → email founders
- p95 API > 800ms por 10 min         → email
- Cost IA diario > 80% budget        → email + auto-throttle
- Sync canal fallido > 3 retries     → email + alert PostHog
- DTE SII rechazo                    → email INMEDIATO
- 401/403 spike > 10/min             → posible attack · email
```

# 18 · Próximos pasos técnicos

1. ✅ Doc 13 v2 · granular · librerías · flujos detallados
2. ⏭️ Tu OK plan
3. ⏭️ Empezar implementación Q4-26 según Doc 18 Plan Ejecución
4. ⏭️ Doc 19 UAT post-construcción
