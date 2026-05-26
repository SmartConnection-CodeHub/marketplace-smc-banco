---
number: 21
id: business-comercio
title: Modelo Comercio
subtitle: "Cómo SMC SpA genera dinero · ciclo compra-venta multi-canal · sin SaaS · sin suscripciones."
block: Negocio
author: Founders + Controller
version: 2.0
date: 2026-05-26
status: 🟢 Activo
prev: 16-comparativa-tools.html
next: 23-financial-comercio.html
---

# 01 · Modelo de negocio en 1 línea

SMC SpA compra productos a Nexport (importador) y los vende en 3 canales (Mercado Libre · Mercado Público · B2B empresas). Margen blend objetivo: 35-45%.

# 02 · Diagrama del flujo de dinero

```
Capital inicial 50M CLP
      ↓
Compra a Nexport (LCL/FCL · 30-60 días)
      ↓
Recepción bodega · QA · ingreso inventario
      ↓
Publicación cross-canal (MeLi + MP + B2B)
      ↓
                ┌────────┴────────┐
            Venta MeLi       Venta B2G        Venta B2B
       (B2C alto vol.)  (institucional)  (empresa privada)
                └────────┬────────┘
                         ↓
              Cobro (pasarela · transferencia)
                         ↓
              DTE emitido (SII · Open Factura)
                         ↓
              Reinversión + reserva impuestos
```

# 03 · Streams de revenue

| Canal | % esperado Y1 | Margen típico | Plazo cobro |
|-------|---------------|---------------|-------------|
| Mercado Libre (B2C) | 50% | 28% (post comisión MeLi) | 14-28 días |
| Mercado Público (B2G) | 30% | 38% | 30-60 días |
| B2B empresa privada | 15% | 42% | 30-60 días |
| D2C storefront (Y2+) | 5% Y1 · 30% Y3 | 50% | inmediato |

Blend Y1 estimado: 35% margen bruto antes de costos operativos.

# 04 · Estructura de costos

- **COGS**: precio Nexport + logística importación + bodegaje
- **Comisiones canal**: MeLi 12-18% · pasarelas 2-3% · MP solo si gana
- **Operación**: bodega · couriers (cobro a cliente) · DTE · IA usage
- **Founders**: $0 sueldo Y1 · compensación equity · utilidades Y2+

# 05 · Lo que NO cobramos

> [!info] Claridad de modelo
> NO cobramos suscripción · NO cobramos por uso del sistema · NO cobramos a terceros. SMC SpA gana plata vendiendo productos físicos · la plataforma es una herramienta interna no un producto comercializable.

# 06 · Reglas de inversión

- 50% del margen mes 1-6 va a reposición stock (rotación)
- 20% reserva impuestos (IVA · IDPC · F22)
- 10% reserva contingencia (devoluciones · merma · disputas)
- 20% disponible para evaluación: nuevos SKUs · ampliar bodega · contratación

# 07 · Cuándo evaluar pivote

> [!warning] Triggers para reevaluación profunda
> - Margen blended Y1 &lt; 25%: revisar sourcing y mix canales
> - Inventario stuck &gt; 90 días: revisar pricing o liquidar
> - Cualquier canal acaba de revenue Y3 &gt; 80%: dependencia · diversificar
