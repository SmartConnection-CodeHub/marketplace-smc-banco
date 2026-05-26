---
number: 38
id: onboarding-dev
title: Onboarding Dev Guide
subtitle: "Cómo arrancar como dev en Marketplace SMC en menos de 1 día · setup · stack · convenciones · primer PR."
block: Operaciones
author: TechLead
version: 1.0
date: 2026-05-26
status: 🟢 Activo
prev: 37-runbook-dr-plan.html
next: 39-api-sdk-postman.html
---

# 01 · Bienvenida

Si estás leyendo esto sos parte de Marketplace SMC. Esta guía te lleva de 0 al primer PR mergeado en &lt;1 día.

# 02 · Setup

```
1. Hardware
   - Mac con M1+ o Linux ARM/x64
   - Mínimo 16GB RAM · 100GB libre

2. Cuentas necesarias
   - GitHub (te invitamos a la org)
   - Google Workspace @smconnection.cl
   - Supabase (acceso lectura QAS)
   - AWS Console (rol IAM dev)

3. Software base
   - Node 22.x LTS · pnpm o npm
   - Git con SSH key generada
   - VS Code o JetBrains · cualquiera
   - Claude Code (CLI) recomendado

4. Clonar repos
   git -C ~/projects clone git@github.com:SmartConnection-CodeHub/smartconnection-marketplace.git
   cd smartconnection-marketplace
   npm install
   cp .env.example .env.local
```

# 03 · Variables de entorno

Pedile a Guillermo o INFRA-OPS las variables para `.env.local`. NUNCA commitearlas.

Variables críticas mínimas:

```
NEXT_PUBLIC_SUPABASE_URL=
NEXT_PUBLIC_SUPABASE_ANON_KEY=
SUPABASE_SERVICE_ROLE_KEY=
MELI_CLIENT_ID=
MELI_CLIENT_SECRET=
MELI_ACCESS_TOKEN=
MERCADOPUBLICO_TICKET=
GROQ_API_KEY=
```

# 04 · Stack en 1 pantalla

```
Next.js 16 (App Router · Server Components default)
   ↓
TypeScript 5.x estricto
   ↓
Tailwind v4 · Radix · @smc/ui
   ↓
Supabase (Postgres + Auth + RLS)
   ↓
AWS Amplify (deploy push a main)
```

# 05 · Convenciones código

- **Edit siempre · Write solo si &gt;80% archivo cambia**
- Server Components por defecto · `use client` solo nodos hoja
- Validación: Zod schemas compartidos client + server
- Estilos: tokens CSS · jamás colores hex inline
- Importar UI: solo desde `@smc/ui` · nunca Radix directo
- Custom hooks: `_hooks/useFeatureX.ts` por feature
- Test: vitest · 1 test por ruta crítica mínimo

# 06 · Workflow Git

```
1. Crear branch desde main
   git -C path checkout -b feat/nombre-corto

2. Commits descriptivos en español
   git -C path commit -m "feat: agrega filtro por canal en dashboard"

3. Push y abrir PR
   git -C path push -u origin feat/nombre-corto
   gh pr create --title "..." --body "..."

4. Esperar review (1 approver mínimo)
5. CI debe estar verde (lint · type-check · tests · build)
6. Merge squash a main → auto-deploy Amplify QAS
7. Promover a PRD: PR de release-X.Y desde main
```

# 07 · Primer PR sugerido

Pickeá del board uno de estos para arrancar:

- Bug fix &lt;30min (etiqueta `good-first-issue`)
- Mejorar mensaje error en un endpoint específico
- Agregar test faltante para una función de utilidad
- Mejorar docstring de un componente

NO arrancar con: feature completa · refactor · cambio arquitectural.

# 08 · Quién pregunta qué

| Tema | Preguntar a |
|------|-------------|
| Stack · arquitectura | Architect |
| Frontend · UI · componentes | Fiori |
| Backend · DB · APIs | Backend |
| IA · prompts · agentes | Hoku |
| Deploy · infra · costos | Pipeline · INFRA-OPS |
| Seguridad · vulns | Security |
| Producto · features · roadmap | PM |
| Cliente · onboarding · soporte | Comercial |
| Bug raro inexplicable | Cerebro (orquesta) |

# 09 · Recursos

- `/Users/guillermogonzalezleon/CLAUDE.md` · operating system SMC
- Banco completo: https://smartconnection-codehub.github.io/marketplace-smc-banco/
- Memorias compartidas: `~/.claude/projects/-Users-guillermogonzalezleon/memory/`
- Skills: `~/.claude/skills/`

# 10 · Checklist primer día

- [ ] Acceso GitHub org · Supabase · AWS confirmados
- [ ] Repo clonado · npm install OK · dev server arriba
- [ ] Pude conectar a Supabase QAS
- [ ] Conocí los agentes SMC OS · entendí flujo
- [ ] Leí docs 01-Vision · 06-API · 07-Arquitectura del banco
- [ ] Primer PR creado (puede ser bug fix mínimo)
- [ ] Sesión 1:1 con Guillermo y/o TechLead
