---
number: 23
id: financial-model
title: Financial Model 3y
subtitle: "P&amp;L proyectado · cash flow · capital needs · break-even mensual."
block: Negocio
author: Controller + Founders
version: 1.0
date: 2026-05-26
status: 🟢 Activo
prev: 22-tam-sam-som.html
next: 24-unit-economics.html
---

# 01 · Proyección financiera 3 años

> [!chart-line] financial-line
> Revenue · Costos · Cash balance trimestre a trimestre. Break-even Q3 2027 · cash floor Q1-Q2 2027 sin reinyección.

# 02 · Supuestos clave

- Capital inicial autofinanciado: **$50M CLP** (founders)
- Pricing promedio: Pro $180K/mes (mix 70% Pro · 20% Business · 10% Starter)
- Churn promedio: 25% Y1 · 22% Y2 · 20% Y3
- Founders sin sueldo Y1 (equity vesting compensa)
- Infra costo: 30% revenue Y1 · 22% Y2 · 18% Y3 (economías escala)
- IA usage: cap $300K/mes Y1 con fallback chain

# 03 · Sensibilidad

| Escenario | Trigger | Acción |
|-----------|---------|--------|
| **Cash floor** | &lt;$10M en Q1-27 | Pausar contrataciones · reducir ADS |
| **Crecimiento &lt; plan** | &lt;15 Pro a Q2-27 | Pivot canales · double-down referidos |
| **Crecimiento &gt; plan** | &gt;40 Pro a Q2-27 | Acelerar hire Backend Q3 |
| **Churn &gt; 30%** | 3 meses seguidos | Pause onboarding · fix retención antes que adquirir |

# 04 · Capital needs y rondas

- **Y1 (Q4-26 → Q3-27)**: bootstrap · capital inicial $50M alcanza
- **Y2 (Q4-27 → Q3-28)**: opcional ronda semilla USD 500K si PMF claro (30+ Pro consistentes)
- **Y3 (Q4-28 → Q3-29)**: opcional Serie A si Y2 ARR &gt; USD 1M

# 05 · Break-even

Mes break-even target: **mes 11** (Q3-27). Si llegamos al mes 14 sin break-even → reevaluación profunda modelo.

# 06 · Flujo mensual típico Y1 Q2

```
Revenue:    +$12M  (18 Pro × $180K + 4 Starter + 2 Business)
─────────────────
Infra:      -$2.5M
IA usage:   -$1.5M
Marketing:  -$2M
Adm:        -$1M
Founders:   $0
─────────────────
EBITDA:     +$5M
```

> [!info] Decisión founders
> Sin sueldo Y1 = ahorro $36M/año (estimación 3 founders × $1M/mes). Compensa con equity vesting 4 años cliff 1.
