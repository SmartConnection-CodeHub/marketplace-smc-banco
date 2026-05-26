---
number: 36
id: stakeholder-map
title: Stakeholder Map
subtitle: "Mapa de stakeholders Marketplace SMC + matriz RACI · quién decide · quién aprueba · quién consulta."
block: Producto
author: PM
version: 1.0
date: 2026-05-26
status: 🟢 Activo
prev: 35-risk-register.html
next: 37-runbook-dr-plan.html
---

# 01 · Lista de stakeholders

| ID | Stakeholder | Tipo | Nivel interés | Nivel poder |
|----|-------------|------|---------------|-------------|
| S1 | Camila Bianchi | Founder | Alto | Alto |
| S2 | Javier Bianchi | Founder | Alto | Alto |
| S3 | Guillermo González León | Founder | Alto | Alto |
| S4 | Operadores Pro (5 primeros) | Cliente | Alto | Medio |
| S5 | Mercado Libre (canal) | Partner | Medio | Alto |
| S6 | Mercado Público (canal) | Partner | Medio | Medio |
| S7 | Supabase · AWS · Groq | Proveedor crítico | Medio | Alto |
| S8 | Contadores galvarez.cl | Proveedor servicio | Bajo | Medio |
| S9 | SII Chile | Regulador | Medio | Alto |
| S10 | Eventual inversor Año 2 | Potencial | Bajo (hoy) | Alto (futuro) |

# 02 · Estrategia por cuadrante

- **Alto interés + Alto poder** (S1-S3 · S5 · S7 · S9): manage closely · reuniones regulares
- **Alto interés + Bajo poder** (S4 · S8): keep informed · newsletter · check-ins
- **Bajo interés + Alto poder** (S10): keep satisfied · materiales preparados por si activa
- **Bajo interés + Bajo poder**: monitor · revisar trimestralmente

# 03 · Matriz RACI · decisiones clave

Convenciones:
- R = Responsible (ejecuta)
- A = Accountable (responde por resultado · solo 1)
- C = Consulted (consultado antes de decidir)
- I = Informed (informado después)

| Decisión | Camila | Javier | Guillermo | TechLead | Comercial | Operadores |
|----------|--------|--------|-----------|----------|-----------|------------|
| Pricing y planes | C | C | A | I | R | C |
| Roadmap trimestral | C | C | A | R | C | C |
| Cambios arquitectura | I | I | C | A/R | I | - |
| Constitución SMC SpA Marketplace | A | A | A | - | C | - |
| Equity split founders | A | A | A | - | - | - |
| Onboarding cliente nuevo | I | I | I | C | A/R | - |
| Postmortem incidente SEV1 | I | I | A | R | I | I |
| Cambio Terms of Service | C | C | A | I | I | I |
| Aceptar oferta inversor | A | A | A | C | C | - |

# 04 · Cadencia comunicación

| Stakeholder | Frecuencia | Formato |
|-------------|-----------|---------|
| Founders (S1-S3) | Semanal | Standup lunes 9am + Slack continuo |
| Operadores Pro (S4) | Cada 2 semanas | Email update + Loom demo nuevos features |
| Proveedores críticos (S5-S7) | Mensual | Email status + ticket cuando aplica |
| SII (S9) | Por evento | Cuando hay obligación · F29 mensual · F22 anual |
| Inversor potencial (S10) | Semestral o on-demand | Update deck + métricas clave |

# 05 · Reglas oro

> [!info] Decisiones founder
> Las decisiones marcadas A en founder requieren acuerdo &gt;= 2 de 3 founders salvo veto explícito en pacto socios.

> [!warning] Single accountability
> Cada decisión tiene UN A · si dos personas son A · nadie es A. Revisar si pasa.
