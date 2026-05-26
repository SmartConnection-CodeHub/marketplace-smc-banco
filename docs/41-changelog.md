---
number: 41
id: changelog
title: Changelog
subtitle: "Historial público de cambios Marketplace SMC · features · fixes · breaking changes por release."
block: Operaciones
author: PM
version: 1.0
date: 2026-05-26
status: 🟢 Activo
prev: 40-glosario.html
next: index.html
---

# 01 · Convenciones

Seguimos [Keep a Changelog](https://keepachangelog.com) y SemVer.

- **MAJOR** (X.0.0) · breaking changes (rompen API · contratos)
- **MINOR** (0.X.0) · features nuevas backwards-compatible
- **PATCH** (0.0.X) · bug fixes · sin nuevas features

Categorías por release:

- ✨ Added · features nuevas
- 🔧 Changed · cambios a algo existente
- 🐛 Fixed · bugs resueltos
- ❌ Removed · removido o deprecated
- 🔒 Security · vulns parchadas

# 02 · Unreleased

Cosas en main que aún no salieron a prod.

- ✨ Added: docs banco completo 41 documentos
- 🔧 Changed: personas reformuladas como agentes SMC (Cerebro · Comercial · Fiori · Controller · Supply-Chain)
- 🔧 Changed: founders correctos (Camila · Javier · Guillermo)
- 🔒 Security: PIN gate hoku · drawer nav cross-doc

# 03 · v0.5.0 · 2026-05-26 · Banco de documentos

Hito mayor: banco público con 41 docs branded + PIN gate.

- ✨ Added: 41 documentos blueprint completos
- ✨ Added: Auth gate ligero PIN "hoku" (SHA-256)
- ✨ Added: Drawer navigation premium cross-docs
- ✨ Added: ADR-0001 Opportunities Architecture sync con tags idempotentes
- ✨ Added: Scripts `build.py` + `apply_adr.py` + `create_doc.py`
- ✨ Added: Config tokens (`config.json` · 28 variables)
- 🔧 Changed: Migrada arquitectura Opportunities sin LLM (free Chilean APIs)
- 🔧 Changed: Personas usan agentes SMC (no nombres ficticios)

# 04 · v0.4.0 · 2026-05-15 · Cerebro IA

- ✨ Added: Endpoint `/api/cerebro/chat` con SSE streaming
- ✨ Added: Fallback chain Groq → Gemini → DeepSeek
- ✨ Added: Logger central `mkt_api_logs` (antes vacío)
- 🐛 Fixed: Cookie-first OAuth proxy MeLi (era env var stale)

# 05 · v0.3.0 · 2026-05-01 · Smart Cache

- ✨ Added: Smart Cache Hot/Warm/Cold (TTL 6h · 12h · delete 7d)
- ✨ Added: Cron refresh MeLi tokens cada 6h
- 🔧 Changed: Max 1000 rows en cache (anti-bloat)

# 06 · v0.2.0 · 2026-04-15 · Multi-canal foundation

- ✨ Added: Channel Adapter Pattern (MeLi · D2C · MP · B2B)
- ✨ Added: RLS Postgres por tenant_id
- ✨ Added: Page Settings con conexión MeLi OAuth
- 🐛 Fixed: 401/403 MeLi proxy lectura cookies httpOnly

# 07 · v0.1.0 · 2026-04-01 · MVP inicial

Primer despliegue público.

- ✨ Added: Dashboard con métricas básicas
- ✨ Added: Login Supabase Auth
- ✨ Added: Búsqueda productos MeLi (proxy)
- ✨ Added: Deploy AWS Amplify auto desde push a main

# 08 · v0.0.1 · 2026-03-15 · Setup repo

- ✨ Added: Next.js 16 · TypeScript · Tailwind v4
- ✨ Added: Supabase project + RLS templates
- ✨ Added: GitHub Actions CI básico
- ✨ Added: Estructura monorepo (apps · packages)

# 09 · Breaking changes futuras (planificadas)

Cuando lleguen estas versiones tendrán migración guide:

- **v1.0.0**: nueva URL base `api.marketplace.smconnection.cl` · endpoints versionados `/v1/...`
- **v2.0.0**: SDK JS oficial · auth via API keys además de JWT
- **v3.0.0**: webhooks firmados HMAC · evento `product.synced` consolidado

> [!info] Cómo se anuncian breaking changes
> 90 días antes en este changelog · email a todos los clientes activos · banner in-app · migration guide específico.
