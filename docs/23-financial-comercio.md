---
number: 23
id: financial-comercio
title: Financial Model · Comercio
subtitle: "P&amp;L 3 años · cash flow operación comercio multi-canal · sin revenue SaaS."
block: Negocio
author: Controller + Founders
version: 2.0
date: 2026-05-26
status: 🟢 Activo
prev: 21-business-comercio.html
next: 24-margen-canal.html
---

# 01 · Proyección 3 años · operación comercio

> [!chart-line] financial-comercio
> Revenue ventas · COGS · Margen bruto · Cash balance. Break-even operativo target: mes 8-10.

# 02 · Supuestos clave

- Capital inicial: $50M CLP (founders · sin sueldo Y1)
- Mix canales Y1: 50% MeLi · 30% MP · 15% B2B · 5% D2C
- Mix de modos Y1: 70% stock propio · 30% on-demand (sin capital atado)
- Margen blended: 30-35% Y1 · 35-40% Y2 · 40-45% Y3
- Rotación stock propio objetivo: 60-90 días
- Reinversión: 50% margen → reposición · 20% impuestos · 10% contingencia · 20% disponible

# 02b · COGS diferencial por modo

| Concepto | Stock propio | On-demand |
|----------|--------------|-----------|
| Pago al proveedor | Anticipado (30-60 días antes) | Post-venta (cuando llega cobro cliente) |
| Capital atado | Alto · todo el inventario | Cero |
| Costos logística | Importación + bodegaje + courier salida | Solo courier (proveedor paga o se carga al cliente) |
| Riesgo merma | Sí (obsolescencia · daño · robo) | Cero (no es nuestro stock) |
| Margen típico | 28-50% | 10-25% |
| Velocidad escalado catálogo | Lento (limitado por capital) | Rápido (catálogo del proveedor) |

# 03 · Métricas a monitorear mensual

| Métrica | Target Y1 | Trigger alarma |
|---------|-----------|----------------|
| Revenue mensual | $5-15M Q4-26 → Q3-27 | &lt; $3M sostenido 2 meses |
| Margen blended | &gt; 30% | &lt; 25% trimestre |
| Stock turnover | 60-90 días | &gt; 120 días |
| Cash balance | &gt; $10M floor | &lt; $5M alerta máxima |
| Devoluciones | &lt; 3% órdenes | &gt; 5% sostenido |

# 04 · Capital y rondas

- **Y1**: $50M autofinanciado · sin ronda
- **Y2-Y3**: si comercio funciona · evaluar línea crédito (BancoEstado PyME) para fondear inventario
- **NO se busca inversión equity**: Marketplace NO es producto SaaS · no aplica VC

# 05 · Cuándo evaluar pivote

> [!warning] Re-evaluación profunda
> - Cash floor &lt; $5M Q1-27 sostenido: reducir inventario · pausar canal débil
> - Margen blended &lt; 25% trimestre: revisar sourcing y mix
> - 1 canal &gt; 80% revenue: dependencia · diversificar antes
> - Inventario stuck &gt; 120 días: liquidar al costo · liberar capital

# 06 · Distribución utilidades

- Y1: 0 distribución · reinversión 100%
- Y2: 50% reinversión · 50% retiros founders (post-impuestos)
- Y3+: política definida con CPA · ratios objetivos
- Reglas en pacto socios · ROFR para retiro extraordinario

# 07 · Reportería contable

- Cierre mensual interno: Guillermo + cron sistema
- Reporte galvarez.cl: 1ro mes (F29 IVA · libro mayor)
- Anual F22 SII: marzo año siguiente · galvarez.cl coordina
- Auditoría externa: NO Y1-Y2 · evaluar Y3 si volumen lo justifica
