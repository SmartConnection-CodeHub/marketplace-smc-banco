---
number: 16
id: comparativa-tools
title: Comparativa Tools
subtitle: "Qué herramientas alternativas existen · por qué construimos propio · cuándo cambiaríamos."
block: Founders Operation
author: Founders + RADAR
version: 2.0
date: 2026-05-26
status: 🟢 Activo
prev: 15-value-internal.html
next: 21-business-comercio.html
---

# 01 · El paisaje de herramientas

Para operar comercio multi-canal en Chile hoy hay 3 mundos:

- **ERP nacional**: Bling · Defontana · Softland (NO multi-canal nativo · NO IA)
- **Marketplace tools internacional**: BeezUp · ChannelEngine · Sellbrite (NO Chile · sin MP · sin Open Factura)
- **Sistemas custom**: lo que hacemos nosotros y otros comerciantes que tomaron este camino

# 02 · Comparativa por capacidad

| Capacidad | Bling | Sellbrite | Marketplace SMC propio |
|-----------|-------|-----------|------------------------|
| MeLi sync stock/precios | ✓ | ✓ | ✓ |
| Mercado Público (B2G) | ✗ | ✗ | ✓ |
| DTE SII auto-emisión | ✓ (limitado) | ✗ | ✓ |
| B2B propio (RFQ · API) | ✗ | ✓ (limitado) | ✓ |
| Cerebro IA scoring | ✗ | ✗ | ✓ |
| Cron refresh tokens auto | ✓ | ✓ | ✓ |
| Costo Y1 CLP | ~$1.4M | ~$2.6M (USD) | $0 software |
| Datos en nuestras manos | ✗ | ✗ | ✓ |
| Customización 100% | ✗ | ✗ | ✓ |

# 03 · Por qué construimos propio (decisión 2026-04)

- **MP cobertura**: ninguna alternativa cubre Mercado Público B2G integrado
- **DTE Chile**: ninguna alternativa internacional opera SII Chile nativo
- **Cerebro IA**: scoring oportunidades es ventaja diferencial
- **Costo**: $0 software vs $1.4M+ anual licencias
- **Datos**: control total · sin lock-in a vendor externo

# 04 · Riesgos de construir propio

> [!warning] Lo que asumimos
> - Tiempo de Guillermo · ~1.000 horas Y1 (compensadas con equity)
> - Mantención continua · si MeLi cambia API somos nosotros los que arreglamos
> - Sin soporte 24/7 · si se cae es Guillermo a las 3am
> - Sin comunidad/foros · estamos solos con docs internas

# 05 · Cuándo cambiaría la decisión

Re-evaluación trimestral. Triggers para considerar migrar a SaaS:

- Aparece un SaaS chileno que cubre MP + DTE + multi-canal por &lt; $80K/mes
- Tiempo Guillermo mantención excede 20h/semana sostenido
- Founder Guillermo se retira y nadie reemplaza skills técnicos
- Volumen crece tanto que sistema no escala (requiere re-arquitectura mayor)

# 06 · Lo que NO comparamos

> [!info] Out of scope
> No nos comparamos con Shopify · WooCommerce · Magento. Esas son plataformas D2C · no operación multi-canal. Si agregamos D2C storefront propio (Y2) · puede que la herramienta D2C SÍ sea SaaS (Shopify) y solo lo conectemos al sistema interno.

# 07 · Updates de paisaje

Quien mantiene este doc actualizado: **Guillermo** (check trimestral con RADAR).

Última revisión: 2026-05-26. Próxima: 2026-08.
