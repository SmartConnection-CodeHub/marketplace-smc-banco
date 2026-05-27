---
number: 35
id: risk-register
title: Risk Register
subtitle: "Registro vivo de riesgos Marketplace SMC · probabilidad × impacto · plan de mitigación por cada uno."
block: Producto
author: PM
version: 1.0
date: 2026-05-26
status: 🟢 Activo
prev: 34-okrs-framework.html
next: 36-stakeholder-map.html
---

# 01 · Cómo se usa

Este registro lo revisamos trimestral en sesión de 1h.

- Cada riesgo tiene dueño · NO "el equipo" (responsabilidad difusa = no se mueve)
- Probabilidad: Baja (1) · Media (2) · Alta (3)
- Impacto: Bajo (1) · Medio (2) · Alto (3)
- Score = P × I (rango 1-9)
- Acción según score: 1-2 monitor · 3-4 mitigar trimestre · 6-9 acción inmediata

# 02 · Riesgos comerciales

| ID | Riesgo | P | I | Score | Mitigación | Dueño |
|----|--------|---|---|-------|-----------|-------|
| C1 | **No llegar a 10 ventas verdes Q4 (Fase 1 estancada)** | 2 | 3 | 6 | Regalar a contactos primeras 5 · ajustar precio agresivo · ver Doc 17 | Founders |
| C2 | **Reputación MeLi roja por reclamo en cuenta nueva** | 2 | 3 | 6 | Atender cliente final con cuidado extremo Y1 · responder &lt;2h | Founders |
| C3 | **Activar Mercado Ads sin reputación = quemar plata** | 3 | 2 | 6 | Regla no transable: ADS OFF hasta 10 ventas verdes · Doc 24 sección 04b | Founders |
| C4 | Bloqueo MeLi PolicyAgent | 1 | 3 | 3 | Plan B v5 Opportunities sin DPP · diversificar canales | Founders |
| C5 | No conseguir adjudicar primera licitación MP Q2 (Fase 3) | 2 | 2 | 4 | Postular agresivo · Cerebro asistido · 3-5/semana | Founders |
| C6 | Competidor copia fotos/listings | 2 | 2 | 4 | Foto pro propia + marca SMC visible · diferenciar | Founders |

# 03 · Riesgos técnicos

| ID | Riesgo | P | I | Score | Mitigación | Dueño |
|----|--------|---|---|-------|-----------|-------|
| T1 | API de canal externo cambia sin aviso | 3 | 2 | 6 | Adapter Pattern + alertas changelog · degradación graceful | TechLead |
| T2 | Supabase down extendido | 1 | 3 | 3 | PITR backups · documentar manual failover · status page | INFRA-OPS |
| T3 | Costo IA escala más rápido que revenue | 2 | 2 | 4 | Fallback chain Groq → Gemini · cache de prompts comunes | Hoku |
| T4 | Tech debt acumulado paraliza features | 2 | 3 | 6 | 20% capacidad cada sprint a deuda · score B mínimo en core | Architect |

# 04 · Riesgos legales y compliance

| ID | Riesgo | P | I | Score | Mitigación | Dueño |
|----|--------|---|---|-------|-----------|-------|
| L1 | SMC SpA pierde rectificación giro | 2 | 3 | 6 | Plan B: constituir Marketplace SMC SpA dedicada Q4 | Compliance |
| L2 | Cliente reclama por data breach | 1 | 3 | 3 | Security policy · 2FA admins · audit logs | Security |
| L3 | SII rechaza facturas DTE | 2 | 2 | 4 | Doble validador (Open Factura + Acepta) · monitoring | Controller |

# 05 · Riesgos de equipo

| ID | Riesgo | P | I | Score | Mitigación | Dueño |
|----|--------|---|---|-------|-----------|-------|
| E1 | Founder se va antes vesting | 2 | 3 | 6 | Vesting 4 años con cliff 1 año en pacto socios | Compliance |
| E2 | Falta capacidad técnica (1 dev a tiempo parcial) | 3 | 3 | 9 | Contratar dev Q2 · usar más agentes IA · scope realista | Founders |
| E3 | Conflicto Javier-InfoPet vs Marketplace | 2 | 2 | 4 | Declaración explícita en pacto socios · review trimestral | Compliance |

# 06 · Heatmap visual P×I

> [!heatmap] risk-heatmap
> Cada riesgo posicionado en su cuadrante. Click revela detalle. Los rojos (score 9 · cuadrante superior derecho) son los críticos a mover ya.

# 07 · Top riesgos para mover este trimestre (score &gt;= 6)

1. C1 · MeLi DPP no aprueba (9)
2. E2 · Falta capacidad técnica (9)
3. C2 · Churn primeros meses (6)
4. C3 · No conseguir 5 Pro Q4 (6)
5. T1 · API canal cambia (6)
6. T4 · Tech debt paraliza (6)
7. L1 · Rectificación SMC SpA (6)
8. E1 · Founder se va (6)

# 07 · Revisión trimestral

- Sesión 1h con los 3 founders + Cerebro
- Cada dueño reporta status su riesgo (verde · amarillo · rojo)
- Riesgos resueltos → archivo histórico
- Riesgos nuevos → agregar con dueño
- Reordenar prioridades por scoring actual
