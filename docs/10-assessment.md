---
number: 10
id: assessment
title: Assessment v1 → v2
subtitle: "Auditoría honesta del banco v3.0.0 · qué funciona · qué falta · qué rediseñar · ruta a v4.0.0."
block: Producto Técnico
author: Cerebro + Founders
version: 1.0
date: 2026-05-27
status: 🟡 Draft · pendiente review founders
prev: 09-opportunities-system.html
next: 11-especificacion-funcional.html
---

# 01 · Premisa del assessment

Después de 3 versiones (v1 SaaS · v2 uso interno · v3 Reputation First) el banco tiene 32 documentos vivos. Antes de seguir construyendo · alto y pregunto: **¿qué está bien · qué falta · qué hay que rediseñar?**

> [!premise] Filosofía v4
> NO se borra nada de v3. Todo lo trabajado sirve como base. v4 trabaja SOBRE v3 · agrega lo que falta · rediseña lo que no encaja con el modelo más amplio · mantiene navegable v3 vía git tags. Versionado paralelo.

# 02 · Alcance del assessment (16 de 32 docs)

```
📦 PRODUCTO TÉCNICO (8)         👥 FOUNDERS OPERATION (4)
   01 Vision                       12 Roles
   02 BBP                          14 Journey
   03 Requirements                 15 Valor Interno
   04 RFP                          16 Comparativa Tools
   05 Data Model
   06 API Catalog               💼 ESTRATEGIA (1)
   07 Architecture                 17 ⭐ Reputation First Y1
   08 Roadmap

👔 GOBERNANZA selectiva (3)    ⛔ FUERA DE SCOPE
   38 Onboarding Dev              25·26·27 Marca · 30 Legal
   39 API SDK Postman             31·32 Seguridad
   41 Changelog                   21·23·24 Negocio · resto gobernanza
```

# 03 · Evaluación por documento

| # | Doc | Veredicto | Acción v4 |
|---|-----|-----------|-----------|
| 01 | Vision | 🟢 Funciona | Mantener · agregar 1 sección "Cómo leer este banco" al inicio |
| 02 | BBP | 🟡 Falta proceso publicidad/ADS | Agregar P14 ADS multicanal (Meta/Google/TikTok) |
| 03 | Requirements | 🔵 Rediseñar | Priorización Y1 OK pero falta FR/NFR por fase · matrix actual confusa |
| 04 | RFP | 🟢 Funciona | Mantener · revisar montos post-pivot (CLP no USD) |
| 05 | Data Model | 🟡 Falta tablas supplier | Agregar tablas: `suppliers`, `supplier_products`, `ads_campaigns`, `ads_pixels`, `marketing_events` |
| 06 | API Catalog | 🟡 Falta endpoints supplier + ADS | Sección nueva: `/api/suppliers/*` y `/api/ads/*` (Meta/Google) |
| 07 | Architecture | 🔵 Rediseñar parcial | HLA bien · falta zoom sobre Supplier Adapter Pattern · falta zona ADS pixels |
| 08 | Roadmap | 🟢 Funciona post-fix | 2 dimensiones OK · agregar Doc 18 Plan ejecución detallado |
| 12 | Roles Founders | 🟢 Funciona | Mantener · agregar sección "Decisiones que tomó cada uno" (registro histórico) |
| 14 | Founders Journey | 🟡 Falta journey error | Agregar escenario "cuando algo se rompe Y1" (qué hace cada uno) |
| 15 | Valor Interno | 🟢 Funciona | Mantener |
| 16 | Comparativa Tools | 🟢 Funciona | Mantener · update trimestral (próximo 2026-08) |
| 17 | ⭐ Estrategia Y1 | 🔵 Rediseñar levemente | Doc central · agregar "Cómo medimos el avance semanal" + "Qué hacer si fase no llega a hito" |
| 38 | Onboarding Dev | 🟡 Falta onboarding founders no-dev | Agregar onboarding para Camila y Javier (operación · NO técnico) |
| 39 | API SDK Postman | 🟢 Funciona | Mantener · ampliar cuando se construya supplier adapter |
| 41 | Changelog | 🟢 Funciona | Mantener · agregar entrada por cada release v4.x |

# 04 · Lo que FUNCIONA · se mantiene tal cual (8 docs)

🟢 **Verde · cero cambios**:

- Doc 01 Vision (premisa Reputation First clara)
- Doc 04 RFP (especificación contractual sólida)
- Doc 08 Roadmap (post-fix de 2 dimensiones)
- Doc 12 Roles Founders (cross-funcional explícito)
- Doc 15 Valor Interno (ROI cuantificable bien argumentado)
- Doc 16 Comparativa Tools (referente operativo)
- Doc 39 API SDK Postman (consistente · funcional)
- Doc 41 Changelog (formato Keep a Changelog · OK)

# 05 · Lo que FALTA agregar al banco v4 (secciones nuevas)

🟡 **Amarillo · construir**:

| Sección nueva | Dónde | Por qué |
|---------------|-------|---------|
| **P14 Publicidad / ADS multicanal** | Doc 02 BBP escenario nuevo | Meta + Google + TikTok pixels · escalado D2C Y2 |
| **Tablas suppliers + ads** | Doc 05 Data Model · sidecar ERD ampliado | Supplier Adapter Pattern + ADS analytics necesitan estos |
| **Endpoints /api/suppliers + /api/ads** | Doc 06 API Catalog · Swagger ampliado | Que el API soporte modo on-demand + ADS automation |
| **Zoom Supplier Adapter Pattern** | Doc 07 Architecture · diagrama secundario | Hoy solo se menciona · falta diagramar |
| **"Cómo leer este banco"** | Doc 01 Vision · sección 0 | Reduce fricción · navegación clara desde el primer doc |
| **"Decisiones founder históricas"** | Doc 12 Roles · sección nueva | Registro · evitar re-discutir lo ya decidido |
| **"Journey cuando algo se rompe"** | Doc 14 Founders Journey · escenario nuevo | Resiliencia Y1 · qué hace cada uno en SEV1 |
| **"Cómo medir avance semanal"** | Doc 17 Estrategia · sección nueva | Operacionalizar · de estrategia a acción concreta |
| **"Onboarding no-dev Camila y Javier"** | Doc 38 Onboarding · sección nueva | Hoy es solo para Guillermo técnico |
| **🆕 Doc 10 Especificación Funcional** | Bloque Producto Técnico | Casos de uso + reglas negocio + criterios aceptación |
| **🆕 Doc 11 Especificación Técnica** | Bloque Producto Técnico | Decisiones arquitecturales + ADRs + performance budgets |
| **🆕 Doc 18 Plan Ejecución Gantt** | Bloque Founders Operation | Gantt detallado + agentes SMC OS asignados + costos |
| **🆕 Doc 19 UAT pruebas integrales** | Bloque Producto Técnico | Validación end-to-end · post-build |

# 06 · Lo que REDISEÑAR profundo (4 docs)

🔵 **Azul · rework**:

```
Doc 03 Requirements · rediseño
─────────────────────────────────────────────────────
Actual: tabla genérica FR/NFR sin agrupación clara.
Propuesta v4:
  · FR-Y1F1 (features Fase 1 Reputación)
  · FR-Y1F2 (features Fase 2 Escala MeLi)
  · FR-Y1F3 (features Fase 3 Diversificación)
  · FR-Y1F4 (features Fase 4 Consolidación)
  · FR-CROSS (cross-cutting: auth · DB · adapter · cerebro)
  · NFR-Y1 (performance · seguridad · uptime targets Y1)

Doc 07 Architecture · rediseño parcial
─────────────────────────────────────────────────────
Actual: HLA muy bueno · 5 escenarios pipeline · ADRs.
Falta:
  · Sub-diagrama Supplier Adapter Pattern (paralelo a Channel)
  · Zona ADS pixels (Meta Conversions API · Google Ads · TikTok Events)
  · ADR-0002 Supplier Adapter Pattern formal
  · ADR-0003 ADS automation strategy

Doc 17 Estrategia Y1 · rediseño leve
─────────────────────────────────────────────────────
Actual: 4 fases + tácticas + KPIs · sólido.
Agregar:
  · Sección "Avance semanal" (review lunes · qué medimos)
  · Sección "Qué hacer si fase no llega a hito" (decisión tree)
  · Sección "Cómo se relaciona con Doc 18 Plan Ejecución"

Doc 14 Founders Journey · rediseño leve
─────────────────────────────────────────────────────
Actual: 3 scenarios (ONBOARDING · MP_FIRST · EVOLVE).
Agregar:
  · Scenario "BREAKDOWN" · cuando algo se rompe (orden duplicada · stock 0 · SII rechaza DTE · etc) · quién toma qué decisión
```

# 07 · Navegación propuesta v4

Hoy hay un index plano con 7 bloques. **v4 propone navegación por intención del lector**:

```
Lector tipo A · "tengo 5 min · quiero entender SMC"
─────────────────────────────────────────────────────
  → Doc 01 Vision (5 min lectura)
  → Doc 17 ⭐ Estrategia Y1 (10 min · doc central)
  → STOP · tiene el panorama

Lector tipo B · "soy founder · necesito operar"
─────────────────────────────────────────────────────
  → Doc 12 Roles Founders (mi rol específico)
  → Doc 14 Founders Journey (qué hago día 1 al 90)
  → Doc 02 BBP (los procesos donde participo)
  → Doc 17 Estrategia (cómo se conecta a la estrategia anual)

Lector tipo C · "voy a construir tech"
─────────────────────────────────────────────────────
  → Doc 11 🆕 Especificación Técnica (norte arquitectural)
  → Doc 07 Architecture (HLA + escenarios)
  → Doc 05 Data Model (schema)
  → Doc 06 API Catalog (endpoints)
  → Doc 38 Onboarding Dev (setup · convenciones)

Lector tipo D · "necesito plan + plata"
─────────────────────────────────────────────────────
  → Doc 18 🆕 Plan Ejecución (gantt + agentes + montos)
  → Doc 23 Financial (cash flow esperado · ver bloque negocio)
  → Doc 41 Changelog (historial decisiones)
```

Implementación en index.html v4: tabs/filters por tipo de lector + recommended path visual.

# 08 · Versionado · cómo navegamos entre versiones

```
v3.0.0 (actual · stable)
  · Tag git congelado · navegable en repo
  · URL: github.com/SmartConnection-CodeHub/marketplace-smc-banco/tree/v3.0.0
  · No se borra · no se modifica

v4.0.0-rc1 (futuro · proceso)
  · Rama paralela: feature/v4-banco-extended
  · Build separado: banco-v4 dir en mismo repo
  · O subdomain: v4.marketplace.smconnection.cl
  · Vos navegás entre las dos vía link visible en header

Switcher UI (a construir):
  ┌─────────────────────────────────────────┐
  │ Marketplace SMC Banco          v3 [v4]  │
  │                                          │
  │ Estás viendo · v3.0.0 (stable)           │
  │ Hay versión nueva · v4.0.0-rc1 (preview) │
  │ [Probar v4]   [Quedarme en v3]           │
  └─────────────────────────────────────────┘
```

# 09 · Backlog priorizado para v4

| # | Item | Prioridad | Estado | Owner |
|---|------|-----------|--------|-------|
| 1 | Doc 11 Especificación Funcional | P1 | ✅ v2 granular (2026-05-27) | Cerebro + Functional-Lead |
| 2 | Doc 13 Especificación Técnica | P1 | ✅ v2 granular (2026-05-27) | Cerebro + Architect |
| 3 | Doc 18 Plan Ejecución Gantt | P1 | ✅ Gantt + agentes + monto | Cerebro + PM |
| 4 | Doc 19 UAT | P1 | ✅ v1 · 24 CU + 5 E2E (2026-05-27) | User-QAS |
| 5 | Rediseño Doc 17 (3 secciones nuevas) | P2 | ✅ §10 review semanal + §11 breakdown + §12 conexión Doc 18 | Cerebro + Founders |
| 6 | Doc 14 scenario BREAKDOWN | P2 | ✅ §06 incidentes + escalación | Founders |
| 7 | Scaffolding code · adapters | P1 | ✅ ChannelAdapter + SupplierAdapter en repo (2026-05-27) | Backend |
| 8 | Rediseño Doc 03 Requirements | P2 | 🟡 pendiente · agrupar por fase | Functional-Lead |
| 9 | Sub-diagrama Supplier Adapter Doc 07 | P2 | 🟡 pendiente | Architect |
| 10 | Tablas supplier + ads Doc 05 | P2 | 🟡 pendiente | Backend |
| 11 | Endpoints /api/suppliers + /api/ads Doc 06 | P2 | 🟡 pendiente | Backend |
| 12 | P14 ADS process Doc 02 BBP | P3 | 🟡 pendiente | Business Dev |
| 13 | Onboarding Camila/Javier Doc 38 | P3 | 🟡 pendiente | HR + Founders |
| 14 | Switcher UI v3 / v4 navegación | P3 | 🟡 pendiente | Fiori |

P1 = bloquea v4 · P2 = roadmap v4 · P3 = nice-to-have · P4 = post-launch.

# 10 · Próximos pasos inmediatos (cola Sentinela)

1. ✅ Doc 10 Assessment creado
2. ✅ Doc 11 Especificación Funcional v2 (granular · 3 sidecars)
3. ✅ Doc 13 Especificación Técnica v2 (granular · 1 sidecar)
4. ✅ Doc 18 Plan Ejecución (Gantt + agentes + montos)
5. ✅ Doc 19 UAT v1 (24 CU · 5 E2E · sign-off por fase)
6. ✅ Scaffolding repo marketplace · adapters + Sprint 1
7. ✅ Doc 17 refinado (review semanal · breakdown · conexión Doc 18)
8. ✅ Doc 14 refinado (scenario BREAKDOWN)
9. ⏭️ Sprint 2 Q4-26 · empezar implementación real (MeLi OAuth + dashboard)
10. ⏭️ Resto backlog P2-P3 según prioridad founders

Status v4: **70% completado** · pendiente Sprint 2-10 ejecución técnica.
