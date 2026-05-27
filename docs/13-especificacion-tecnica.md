---
number: 13
id: especificacion-tecnica
title: Especificación Técnica
subtitle: "Cómo se construye · stack confirmado · ADRs · performance budgets · observabilidad."
block: Producto Técnico
author: Architect + Cerebro
version: 1.0
date: 2026-05-27
status: 🟡 Draft · pendiente review founders
prev: 11-especificacion-funcional.html
next: 14-founders-journey.html
---

# 01 · Premisa

Documento define **cómo se construye** Marketplace SMC. Complementa Doc 07 Architecture (HLA + escenarios) con detalle de decisiones técnicas + ADRs + performance budgets + observabilidad.

> [!info] Hilo conductor
> Doc 10 dice qué hace · Doc 11 dice cómo se construye · Doc 18 dice cuándo y con qué equipo. Los 3 son complementarios · NO redundantes.

# 02 · Stack confirmado

| Capa | Tecnología | Justificación |
|------|------------|---------------|
| Runtime | Node.js 22 LTS | Estable hasta 2027-04 · familiarity Guillermo |
| Framework | Next.js 16 (App Router) | SSR + RSC + Server Actions + ISR · DX excelente |
| TypeScript | 5.x strict | Type safety · catch bugs en build |
| UI | React 19 + Tailwind v4 + Radix + @smc/ui | Component-driven · accesible · branded |
| State Y1 | URL params + Server Components | Sin Zustand/Redux Y1 · YAGNI |
| DB | Supabase Postgres (sa-east-1) | RLS · pg_cron · pg_notify · backups PITR 30d |
| Auth | Supabase Auth + JWT con tenant_id | Single tenant Y1 · multi-tenant ready arch |
| ORM | Drizzle ORM | Type-safe · zero runtime · migrations versionadas |
| Validation | Zod (client + server) | Single source of truth schemas |
| Forms | React Hook Form + Zod resolver | Performance · UX · validación shared |
| Pagos | MercadoPago + WebPay Plus | MercadoPago para MeLi · WebPay para D2C Chile |
| Logística | Chilexpress + Starken APIs | Couriers locales Chile principales |
| DTE | Open Factura | DTE 33 · 39 · 61 · cumplimiento SII |
| IA | OpenRouter (chain) | Groq · Gemini · DeepSeek fallback · NUNCA Claude |
| Hosting | AWS Amplify | Auto-deploy push · CDN CloudFront · build optimizado |
| Domain | marketplace.smconnection.cl | Custom domain · cert ACM |
| Observabilidad | Sentry + PostHog + CloudWatch | Errores · funnels · infra · cost dashboards |
| Cron | Vercel Cron + pg_cron | Refresh MeLi 6h · sync MP diario · cache cleanup 7d |
| CI/CD | GitHub Actions | Lint · type-check · build · auto-tag deploy |

# 03 · Architectural Decision Records (ADRs)

## ADR-0001 · v5 Opportunities sin LLM (existente)

Status: ✅ Accepted (2026-05-15)
Context: MeLi DPP requiere USD 200K GMV · imposible Y1.
Decision: 6 capas Opportunities · scoring sin LLM · usar SoloTodo + Mercado Público + Open Food Facts + BCentral.
Consequences: Cero costo IA por scoring · sin dependencia DPP · catálogo amplio Chile.

## ADR-0002 · Channel Adapter Pattern (existente)

Status: ✅ Accepted (2026-05-10)
Context: 4+ canales (MeLi · MP · D2C · B2B) con APIs muy distintas. Sin abstracción se vuelve unmaintainable.
Decision: Interface uniforme `ChannelAdapter` con métodos `syncStock()`, `listOrders()`, `publishProduct()`. Cada canal implementa su adapter.
Consequences: Agregar canal nuevo = 1 archivo nuevo · NO refactor del resto.

## ADR-0003 · Supplier Adapter Pattern 🆕

Status: 🟡 Proposed (2026-05-27)
Context: Modo dropshipping (Doc 02 P13) requiere integración con proveedores externos. Cada proveedor tiene API/feed/método distinto. Sin abstracción = misma plaga que Channel.
Decision: Interface uniforme `SupplierAdapter` con métodos `syncCatalog()`, `checkStock(sku)`, `createPurchaseOrder(items)`, `trackShipment(po_id)`, `handleReturn(order_id)`. Cada proveedor implementa el suyo.
Consequences: Agregar proveedor dropship = 1 archivo · NO refactor.
Alternativas descartadas: webhooks ad-hoc por proveedor (mantenimiento caro · escalado lineal).

## ADR-0004 · ADS multicanal automation 🆕

Status: 🟡 Proposed (2026-05-27)
Context: D2C Y2+ requiere ADS (Meta + Google + TikTok). Sin automation · tiempo founder por campaign sale del presupuesto.
Decision: Construir AdsManager que abstrae las 3 plataformas. Métricas comunes (CTR · CPC · ROAS). Pixels server-side (Meta Conversions API + Google Ads Enhanced Conversions + TikTok Events API) para deprecation cookie-less.
Consequences: 1 panel · 3 plataformas. Server-side mejor measurement.
Alternativas descartadas: usar tool tercero (Triple Whale · Northbeam) · costo $300+/mes innecesario Y2.

## ADR-0005 · Versionado banco v3 ↔ v4 🆕

Status: 🟡 Proposed (2026-05-27)
Context: v3.0.0 estable · v4 en construcción. Necesidad de navegar entre versiones (founders + tú quieres comparar).
Decision: 2 builds paralelos · `/v3` y `/v4` paths en mismo repo o subdomains separados. Switcher UI visible. NO se borra v3 cuando v4 sale.
Consequences: Mantenimiento 2 versiones temporal · OK. Cuando v4 estable · v3 archivado pero accesible.

# 04 · Performance budgets (targets Y1)

| Métrica | Budget | Trigger alarma |
|---------|--------|----------------|
| LCP (Largest Contentful Paint) | &lt; 2.5s | &gt; 4s |
| INP (Interaction to Next Paint) | &lt; 200ms | &gt; 500ms |
| CLS (Cumulative Layout Shift) | &lt; 0.1 | &gt; 0.25 |
| API p50 lectura | &lt; 120ms | &gt; 300ms |
| API p95 lectura | &lt; 350ms | &gt; 800ms |
| API p95 mutación | &lt; 600ms | &gt; 1.5s |
| Cerebro chat first token (SSE) | &lt; 600ms | &gt; 2s |
| Sync MeLi p95 | &lt; 8s | &gt; 30s |
| Build time CI | &lt; 3min | &gt; 8min |
| Bundle size cliente | &lt; 250KB gzipped | &gt; 500KB |

# 05 · Security requirements

| # | Requerimiento | Implementación |
|---|--------------|----------------|
| SR-1 | TLS 1.3 obligatorio | Amplify default + HSTS preload |
| SR-2 | AES-256 at rest | Supabase default |
| SR-3 | RLS Postgres siempre activo | tenant_id implícito desde JWT |
| SR-4 | service_role solo backend | NUNCA exposed a client |
| SR-5 | 2FA obligatorio admins | Supabase Auth TOTP |
| SR-6 | Cookies httpOnly + SameSite=lax | Default Next.js + custom config |
| SR-7 | CSP headers estrictos | next.config.ts headers() |
| SR-8 | Rate limit 60 req/min user | Middleware Next.js + Upstash Redis |
| SR-9 | Idempotency keys en POST críticos | UUIDs · tabla `mkt_idempotency` |
| SR-10 | Audit logs append-only | Tabla `audit_logs` + RLS |
| SR-11 | Secrets en Amplify env vars | NUNCA en repo · rotación trimestral |
| SR-12 | HMAC SHA-256 en webhooks | Validar firma antes de procesar |

# 06 · Observabilidad + LLMOps

```
LOGS estructurados (JSON) por evento
─────────────────────────────────────────────────────
{ timestamp · level · feature · user_id · tenant_id ·
  duration_ms · status · error_msg · metadata }

→ stdout (CloudWatch) + tabla mkt_api_logs (consultable)

LLMOps específico Cerebro
─────────────────────────────────────────────────────
{ provider · model · prompt_version · tokens_in · tokens_out ·
  cost_usd · latency_ms · cache_hit · feature · hallucination_flag }

→ tabla mkt_ai_logs · dashboards costo/feature/día

ALERTAS (CloudWatch + Sentry)
─────────────────────────────────────────────────────
- Error rate > 1% por 5 min → email founders
- p95 API > 800ms por 10 min → email
- Costo IA diario > 80% budget → email
- Sync canal fallido > 3 retries → email
- DTE SII rechazo → email inmediato
```

# 07 · Decisiones de implementación

> [!premise] Filosofía técnica
> Hacer lo mínimo que entregue valor · NO sobre-diseñar.

- **Sin tests E2E Y1**: foco unit + integration. E2E (Playwright) en Y2 si hay capacidad.
- **Sin GraphQL**: REST endpoints simples. GraphQL si complejidad data fetching lo justifica Y2.
- **Sin WebSockets Y1**: SSE para streaming Cerebro. WS solo si voz/colab requiere bidireccional Y2.
- **Sin micro-frontends**: single Next.js app. Split si equipo crece a 5+ devs.
- **Sin Kubernetes**: Amplify suficiente. K8s solo si self-hosting · NO el caso.
- **Sin Kafka / event streaming externo**: pg_notify suficiente Y1. RabbitMQ/Kafka si volumen >100K eventos/día.
- **Sin Sentry custom dashboards**: usar defaults. Custom solo si patrón específico emerge.

# 08 · Cosas que dejé fuera (por ahora)

- Schema completo DB → ver Doc 05 Data Model
- Endpoints detallados → ver Doc 06 API Catalog (Swagger live)
- HLA + 5 escenarios → ver Doc 07 Architecture
- Setup dev local · convenciones · workflow Git → ver Doc 38 Onboarding Dev
- Performance perfiles real → se construyen post-MVP con data real

# 09 · Próximos pasos técnicos

1. Implementar ADR-0003 Supplier Adapter Pattern (estimate: 16h)
2. Implementar ADR-0004 ADS Manager (estimate: 40h · Y2)
3. Setup observabilidad LLMOps tabla `mkt_ai_logs` (4h)
4. Performance audit Lighthouse · alinear a budgets (8h)
5. Audit security checklist 12 items SR-1 a SR-12 (4h)
