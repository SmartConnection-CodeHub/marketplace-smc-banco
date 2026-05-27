---
number: 18
id: plan-ejecucion
title: Plan Ejecución v4
subtitle: "Gantt detallado · agentes SMC OS asignados · costo por entrega · roadmap operacional ejecutable."
block: Founders Operation
author: PM + Cerebro
version: 1.0
date: 2026-05-27
status: 🟡 Draft · pendiente OK founders
prev: 17-estrategia-y1.html
next: 21-business-comercio.html
---

# 01 · Premisa

Doc 17 dice **qué hacer** (estrategia). Doc 10 dice **qué hace** el sistema (funcional). Doc 11 dice **cómo** se construye (técnico). Este doc dice **cuándo · con quién · cuánto**.

> [!info] Hilo conductor del banco
> 17 Estrategia → 10 Funcional → 11 Técnico → 18 Ejecución → 19 UAT
> Cada doc responde una pregunta distinta · juntos cubren el ciclo completo.

# 02 · Gantt Q4-26 → Q3-27 (Y1 completo)

> [!gantt] plan-ejecucion-gantt
> Roadmap operacional · cada barra = entregable concreto · color por agente owner.

# 03 · Catálogo de agentes SMC OS (asignación recursos)

Los agentes son skills de Claude Code · NO personas. Cada agente tiene tarifa horaria equivalente (= horas humanas que ahorra · proxy de valor).

| Agente | Capacidad | Tarifa equivalente CLP/h | Uso en Y1 |
|--------|-----------|--------------------------|-----------|
| 🧠 Cerebro | Síntesis · planning · orquestación | $25K/h | Decisiones estratégicas · refactor docs |
| 🐾 Hoku | AI dev · prompts · RAG · agentes | $35K/h | Cerebro IA · scoring · chat SSE |
| 🔧 Backend | APIs · DB · auth · integraciones | $30K/h | Channel Adapter · Supplier Adapter · DTE |
| 🎨 Fiori | Frontend · CSS · @smc/ui · accesibilidad | $25K/h | Dashboard · listings · D2C storefront |
| 🐕 Functional-Lead | Maquetas · UX · BPMN · specs | $25K/h | Wireframes · workflows · onboarding |
| 🔍 Architect | Estándares · ADRs · integraciones | $30K/h | Decisiones técnicas · code review |
| 👩 User-QAS | QA · smoke · Playwright | $20K/h | Pre-release validation · regression |
| 🛠️ Pipeline | DevOps · CI/CD · Amplify | $20K/h | Deploys · monitoring · alertas |
| 💰 Comercial | Onboarding · pricing · retención | $25K/h | NO aplica Y1 (uso interno · sin clientes) |
| 🧮 Controller | Tributario · F29 · F22 · galvarez | $30K/h | DTE setup · conciliación · reportes SII |

# 04 · Entregables Y1 · costo por agente + monto total

## Q4-26 · Fase 1 Reputación (12 semanas)

| Entregable | Agente owner | Horas | Costo CLP |
|------------|-------------|-------|-----------|
| Setup repo + Amplify + Supabase | 🔧 Backend + 🛠️ Pipeline | 16h | $480K |
| Auth + tenant_id JWT + RLS | 🔧 Backend + 🔍 Architect | 12h | $400K |
| Channel Adapter MeLi · OAuth + tokens cookies | 🔧 Backend | 24h | $720K |
| Webhook receiver MeLi · validación HMAC | 🔧 Backend | 8h | $240K |
| DTE Open Factura integration · DTE 39 | 🔧 Backend + 🧮 Controller | 12h | $400K |
| Dashboard founder · listings + orders | 🎨 Fiori | 32h | $800K |
| Cerebro chat MVP · SSE + fallback chain | 🐾 Hoku | 20h | $700K |
| Wireframes flujo onboarding founder | 🐕 Functional-Lead | 8h | $200K |
| **Q4-26 subtotal** | | **132h** | **$3.94M CLP** |

## Q1-27 · Fase 2 Escala MeLi (12 semanas)

| Entregable | Agente owner | Horas | Costo CLP |
|------------|-------------|-------|-----------|
| Mercado Ads integration · campaigns + ROI tracking | 🔧 Backend + 🐾 Hoku | 28h | $880K |
| Full Fulfillment MeLi migration flow | 🔧 Backend | 12h | $360K |
| Cerebro scoring oportunidades v5 (sin LLM · 6 señales) | 🐾 Hoku | 32h | $1.12M |
| Panel oportunidades UI | 🎨 Fiori | 16h | $400K |
| pg_notify cross-canal sync | 🔧 Backend | 16h | $480K |
| Smart Cache Hot/Warm/Cold | 🔧 Backend | 12h | $360K |
| Cron jobs (refresh MeLi 6h · cleanup 7d) | 🔧 Backend + 🛠️ Pipeline | 8h | $250K |
| Tests integración Channel Adapter MeLi | 👩 User-QAS | 12h | $240K |
| **Q1-27 subtotal** | | **136h** | **$4.09M CLP** |

## Q2-27 · Fase 3 Diversificación (12 semanas)

| Entregable | Agente owner | Horas | Costo CLP |
|------------|-------------|-------|-----------|
| Channel Adapter Mercado Público · Ticket auth | 🔧 Backend | 24h | $720K |
| Cerebro postulación licitaciones · template + AI | 🐾 Hoku | 24h | $840K |
| Panel B2G dashboard · licitaciones + ofertas | 🎨 Fiori | 20h | $500K |
| Channel Adapter B2B custom · portal RFQ | 🔧 Backend + 🎨 Fiori | 32h | $880K |
| Pricing engine B2B · descuentos volumen | 🔧 Backend | 16h | $480K |
| Supplier Adapter Pattern · 1er proveedor dropship | 🔧 Backend + 🔍 Architect | 28h | $880K |
| Workflow on-demand orden → OC proveedor | 🔧 Backend | 16h | $480K |
| Tests integración multi-canal | 👩 User-QAS | 16h | $320K |
| **Q2-27 subtotal** | | **176h** | **$5.10M CLP** |

## Q3-27 · Fase 4 Consolidación (12 semanas)

| Entregable | Agente owner | Horas | Costo CLP |
|------------|-------------|-------|-----------|
| D2C storefront MVP (Y2 prep) | 🎨 Fiori + 🔧 Backend | 40h | $1.20M |
| Conciliación pagos vs DTE automática | 🔧 Backend + 🧮 Controller | 16h | $480K |
| Reporte mensual galvarez.cl auto | 🧮 Controller + 🔧 Backend | 8h | $240K |
| Observabilidad LLMOps · dashboards | 🐾 Hoku + 🛠️ Pipeline | 12h | $360K |
| Performance audit + budget alinear | 🎨 Fiori + 🔍 Architect | 16h | $480K |
| Security audit checklist SR-1 a SR-12 | 🔍 Architect | 8h | $240K |
| Evaluación Nexport (decisión Y2 sí/no) | Los 3 founders | 4h | $100K |
| Cierre Y1 · postmortem · plan Y2 | 🧠 Cerebro + Founders | 8h | $200K |
| **Q3-27 subtotal** | | **112h** | **$3.30M CLP** |

# 05 · Resumen económico Y1

| Concepto | CLP | USD aprox |
|----------|-----|-----------|
| Total horas equivalentes IA · 4 trimestres | 556h | — |
| Total costo agentes (proxy valor) | **$16.43M CLP** | ~$18.5K |
| Costo real cash · solo Guillermo dev | $0 (founder · sin sueldo Y1) | $0 |
| Costos cash externos (Amplify · Supabase · APIs IA · Open Factura) | $3-5M Y1 | $3.5-5.7K |
| Inversión inicial inventory stock local | $20M | $22.7K |
| **Cash out Y1 estimado** | **$23-25M CLP** | **~$26-28K USD** |

> [!info] Lectura
> $16.43M es valor entregado (horas IA · si las hiciera humano costaría eso). Cash out real es ~$23-25M (mayoritariamente inventory). Recupero esperado vía revenue Y1: $20-50M según mix MeLi+MP+B2B.

# 06 · Dependencias críticas (orden ineludible)

```
Setup repo + Auth + DB
  ↓ (bloquea todo)
Channel Adapter MeLi + DTE
  ↓ (sin esto · Fase 1 imposible)
Dashboard founder + webhook handling
  ↓ (sin esto · operación manual eterna)
Cerebro chat MVP
  ↓ (sin esto · cero diferencial vs competencia)
Mercado Ads integration
  ↓ (Fase 2 requiere reputación previa)
Scoring oportunidades sin LLM
  ↓ (lo que vende SMC vs solo MeLi)
Mercado Público + B2B
  ↓ (Fase 3 · diversificación)
Supplier Adapter Pattern
  ↓ (dropshipping habilitado)
D2C storefront prep
  ↓ (Y2 launch ready)
Consolidación + postmortem Y1
```

# 07 · Hitos cuantificables (lo que se mide)

| Mes | Hito | Métrica |
|-----|------|---------|
| M1 (Q4-26 Oct) | Repo + Amplify + Supabase live | URL responde 200 · auth funcional |
| M2 (Q4-26 Nov) | Primera publicación MeLi · 5 SKUs | 5 listings activos en MeLi |
| M3 (Q4-26 Dic) | 10 ventas verdes MeLi · cierre Fase 1 | `count(orders) ≥ 10 AND reputation=green` |
| M4 (Q1-27 Ene) | Mercado Ads activo · ROI &gt; 1.5 | ROAS mensual ≥ 1.5x |
| M6 (Q1-27 Mar) | 30 órdenes/mes sostenidas | Threshold mensual 2x consecutivo |
| M7 (Q2-27 Abr) | 1ra adjudicación Mercado Público | Evento adjudicación en DB |
| M9 (Q2-27 Jun) | 1ra venta B2B | Evento ventas B2B en DB |
| M10 (Q3-27 Jul) | Supplier Adapter activo · 1+ dropship | Producto vendido vía supplier |
| M12 (Q3-27 Sep) | $5M+/mes sostenido 2 meses · break-even Y1 | Revenue mensual + cash flow |

# 08 · Riesgos de ejecución + plan B

| Riesgo | P × I | Mitigación |
|--------|-------|-----------|
| Guillermo capacidad técnica saturada (E2 Risk Register) | 9 | Scope realista · 20% buffer por trimestre · contratar dev Y2 |
| Fase 1 no llega a 10 ventas (C1) | 6 | Acelerar primeras ventas regalando · revisar fotos · escalado MeLi |
| Sub-estimación horas por entregable | 6 | +25% buffer cada estimate · review semanal real vs plan |
| Dependencia bloqueante 1 agente saturado | 4 | Paralelizar · agentes IA pueden hacer múltiples streams simultáneos |
| Build/deploy issues bloquean entregable | 4 | CI obligatorio · rollback rápido · canary deploys |

# 09 · Cadencia operativa de seguimiento

```
Lunes 9am · standup 15min
  · Qué entregó cada agente semana pasada
  · Qué entrega esta semana
  · Bloqueos
  · Decisiones rápidas pendientes

Viernes último mes · cierre mensual
  · Hito mes alcanzado sí/no
  · Costo real vs plan
  · Ajustes mes siguiente
  · Update Doc 41 Changelog

Trimestral · cierre fase
  · Hito fase alcanzado sí/no
  · Postmortem fase
  · Risk register review
  · Ajuste plan trimestre siguiente
```

# 10 · Próximos pasos inmediatos

1. ✅ Doc 18 creado (este doc)
2. ⏭️ Tu OK final del plan (assessment + 10 + 11 + 18)
3. ⏭️ Empezar ejecución Q4-26 · primer entregable: Setup repo + Amplify + Supabase
4. ⏭️ Doc 19 UAT en paralelo (criterios validación cuando empiece a haber qué validar)
