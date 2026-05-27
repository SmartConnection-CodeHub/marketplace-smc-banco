---
number: 11
id: especificacion-funcional
title: Especificación Funcional
subtitle: "Qué hace el sistema · casos de uso · reglas de negocio · criterios de aceptación."
block: Producto Técnico
author: Functional-Lead + Cerebro
version: 1.0
date: 2026-05-27
status: 🟡 Draft · pendiente review founders
prev: 10-assessment.html
next: 13-especificacion-tecnica.html
---

# 01 · Premisa

Este documento define **qué hace** Marketplace SMC desde la perspectiva del usuario (los 3 founders). NO habla de cómo se construye técnicamente (eso es Doc 11). NO habla de cuándo se construye (eso es Doc 18).

> [!info] Relación con otros docs
> Doc 17 · estrategia (norte estratégico Y1)
> Doc 10 (este) · qué hace el sistema (casos de uso)
> Doc 11 · cómo se construye (arquitectura + ADRs)
> Doc 18 · cuándo · con qué agentes · cuánto cuesta

# 02 · Personas (3 founders)

| Persona | Foco operativo | Rol primario en el sistema |
|---------|----------------|----------------------------|
| Camila Bianchi | Logística + Comercial | Operadora bodega + listings MeLi/MP |
| Javier Bianchi | Logística + Comercial + Sourcing | Sourcing + cotizaciones MP + B2B |
| Guillermo González León | Técnica + Contabilidad + Operativa backup | Mantenimiento sistema + DTE + Cerebro IA |

Cross-funcional: cualquiera de los 3 puede operar logística + comercial (rotación). Guillermo único en técnica + contabilidad.

# 03 · Casos de uso (CU-001 → CU-024)

Agrupados por fase Y1 del Doc 17 Estrategia Reputation First.

## Fase 1 · Reputación (Q4-26 · CU-001 a CU-006)

| CU | Caso de uso | Actor | Hito |
|----|-------------|-------|------|
| CU-001 | Subir primer producto al catálogo maestro con fotos pro propias | Cualquier founder | 5 productos en cuenta MeLi |
| CU-002 | Configurar listing MeLi con título · descripción · categoría correcta | Cualquier founder | Listing aprobado por MeLi |
| CU-003 | Vender primera unidad a costo (regalo a contacto) · activar termómetro | Cualquier founder | Termómetro vendedor activo |
| CU-004 | Recibir orden vía webhook MeLi · aceptar manualmente · despachar | Cualquier founder | Venta confirmada |
| CU-005 | Emitir DTE 39 (boleta) automático al cierre de la orden | Sistema · Open Factura | DTE emitido con folio SII |
| CU-006 | Lograr 10 ventas con reputación verde MeLi | Sistema mide · founders ejecutan | Hito Fase 1 cerrado |

## Fase 2 · Escala MeLi (Q1-27 · CU-007 a CU-012)

| CU | Caso de uso | Actor | Hito |
|----|-------------|-------|------|
| CU-007 | Configurar Mercado Ads · campaign por SKU ganador | Cualquier founder | ADS activo |
| CU-008 | Monitorear ROI de campaign · pausar si <1.5x | Cerebro IA sugiere · founder decide | Decisión semanal |
| CU-009 | Migrar SKU rotado a Full Fulfillment MeLi | Cualquier founder | Stock en almacenes MeLi |
| CU-010 | Subir reputación a Medalla Plata · 30+ ventas/mes sostenidas | Sistema mide | Plata alcanzada |
| CU-011 | Recibir alertas Cerebro IA sobre oportunidades cross-categoría | Cerebro background | Sugerencia diaria |
| CU-012 | Cerrar 30 órdenes/mes sostenidas 2 meses · cerrar Fase 2 | Sistema mide | Hito Fase 2 cerrado |

## Fase 3 · Diversificación (Q2-27 · CU-013 a CU-018)

| CU | Caso de uso | Actor | Hito |
|----|-------------|-------|------|
| CU-013 | Sync diario licitaciones Mercado Público (cron 8am) | Sistema | Licitaciones nuevas en DB |
| CU-014 | Cerebro filtra licitaciones afines + scoring | Cerebro IA | Top 5 sugeridas/día |
| CU-015 | Postular a licitación · oferta generada · review · submit | Javier típicamente | Oferta enviada MP |
| CU-016 | Recibir webhook adjudicación · ejecutar despacho institucional | Cualquier founder | Primera adjudicación B2G |
| CU-017 | Cliente B2B envía RFQ vía portal · generar cotización | Javier típicamente | Primera venta B2B |
| CU-018 | Cerrar 1 adjudicación MP + 1 venta B2B + MeLi sostenido | Sistema mide | Hito Fase 3 cerrado |

## Fase 4 · Consolidación (Q3-27 · CU-019 a CU-024)

| CU | Caso de uso | Actor | Hito |
|----|-------------|-------|------|
| CU-019 | Cierre mensual con conciliación pagos vs DTE | Guillermo + sistema | Reporte galvarez.cl mensual |
| CU-020 | Evaluación Nexport (importación) si SKU > USD 30K/mes sostenido | Los 3 founders | Decisión Y2 Nexport sí/no |
| CU-021 | Preparar D2C storefront para Y2 launch | Frontend (Y2) | D2C MVP listo |
| CU-022 | Setup dropshipping con proveedores chilenos (modo on-demand) | Backend + Javier | 1+ proveedor dropship activo |
| CU-023 | Review trimestral Risk Register · ajustar | Los 3 founders | Risks actualizados |
| CU-024 | Cierre Y1 · $5M+ revenue mensual sostenido 2 meses · break-even | Sistema mide | Hito Y1 cerrado |

# 04 · Reglas de negocio (BR-001 → BR-018)

> [!info] Estructura
> Cada BR es regla NO transable que el sistema debe cumplir. Si una regla se rompe · es bug crítico.

## Reputación primero (Fase 1)

- **BR-001**: Las primeras 10 ventas se publican con foto pro propia · jamás del proveedor.
- **BR-002**: Envío gratis activado en Y1 fase 1 · sacrifica margen · gana reputación.
- **BR-003**: Mercado Ads NO se activa hasta tener termómetro verde sostenido 4 semanas.
- **BR-004**: Cuenta nueva NO atiende cliente con reclamo en primeros 30 días sin escalado a los 3 founders.

## Stock cross-canal (todas las fases)

- **BR-005**: Stock real-time único · pg_notify propaga cambio a todos los canales activos &lt;1s.
- **BR-006**: Reserva stock con SELECT FOR UPDATE · evita oversell por concurrencia.
- **BR-007**: Si producto tiene `is_on_demand=true` · stock refleja al proveedor (no propio).
- **BR-008**: Stock 0 → producto se despublica de canales automáticamente · no se vende lo que no hay.

## DTE / SII Chile

- **BR-009**: Todo cierre de orden con monto > 0 dispara emisión DTE automática.
- **BR-010**: DTE 39 (boleta) default · DTE 33 (factura) si cliente provee RUT empresa.
- **BR-011**: Si SII rechaza DTE · retry exponencial 5 veces · si todos fallan · alerta + queue manual.
- **BR-012**: NC (DTE 61) requiere autorización founder · NO auto-emisión por evento.

## Channels & Adapters

- **BR-013**: Channel Adapter Pattern uniforme · agregar canal nuevo NO requiere refactor.
- **BR-014**: Supplier Adapter Pattern análogo · agregar proveedor nuevo igual.
- **BR-015**: Cron refresh MeLi tokens cada 6h · si falla · alerta inmediata.

## Cerebro IA

- **BR-016**: Fallback chain Groq → Gemini → DeepSeek · NUNCA Claude (regla Hoku).
- **BR-017**: Scoring oportunidades = sin LLM (6 señales) · NO costo IA por scoring.
- **BR-018**: Chat Cerebro tiene rate limit 60 mensajes/día/founder · evita abuso.

# 05 · Workflows por modo de operación

Tres modos paralelos (Doc 21 Modelo Comercio):

## Modo 1 · Stock propio compra local Chile (Y1 prioridad)

```
Sourcing → Compra local (CLP · 3-7 días)
        → Recepción bodega · QA · ingreso inventory
        → Publicar cross-canal (foto pro)
        → Venta · webhook
        → Despacho directo
        → DTE emitido
        → Reinversión
```

## Modo 2 · Stock propio Nexport importación (Y2+)

```
Sourcing → RFQ Nexport (USD · 30-90 días)
        → Importación + aduana
        → Recepción bodega
        → [mismo flujo Modo 1 desde acá]
```

## Modo 3 · Dropshipping (sin stock propio)

```
Sync catálogo proveedor → Filter SKUs viables
                        → Publicar con flag is_dropship=true
                        → Venta · webhook
                        → OC propagada al proveedor (Supplier Adapter)
                        → Proveedor despacha al cliente final
                        → DTE emitido por SMC SpA
                        → Liquidar al proveedor 7-15 días
```

# 06 · Wireframes / Mockups (referencias)

Ya existentes en banco de diseño SMC:

- Dashboard founder (vista única operacional · todos los modos)
- Detalle producto (CRUD + multi-canal status)
- Lista órdenes (filter por canal · status · fecha)
- Detalle orden (timeline + items + payments + DTE + tracking)
- Cerebro chat (sidebar · SSE streaming)
- Panel oportunidades (top scored sin LLM)

Pendiente diseñar en v4:

- Panel ADS multicanal (Meta + Google + TikTok · campañas + ROI)
- Panel suppliers dropship (catálogos sync + comisión + liquidación)
- Switcher v3/v4 navegación banco
- Onboarding wizard no-dev (Camila + Javier paso a paso)

# 07 · Criterios de aceptación (resumen por hito)

| Hito | Criterio | Cómo se mide |
|------|----------|--------------|
| Cierre Fase 1 | 10 ventas verdes MeLi sostenidas 4 sem | `mkt_orders WHERE status=delivered AND channel=meli AND reputation_color=green` · count ≥ 10 |
| Cierre Fase 2 | 30 órdenes/mes sostenidas 2 meses | Query mensual con threshold |
| Cierre Fase 3 | 1+ adjudicación MP + 1+ B2B | Eventos específicos en `mkt_orders` |
| Cierre Fase 4 / Y1 | $5M+ revenue mensual sostenido 2 meses | Sum mensual revenue real |
| Margen blended | 30-35% Y1 | (Revenue - COGS) / Revenue por mes |
| Uptime sistema | 99.5% Y1 | Monitoring CloudWatch + Sentry |
| Tiempo founder operación manual | &lt;1h/sem cada uno | Self-report semanal + log sistema |

# 08 · Out of scope (explícito)

❌ Lo que **NO** hace el sistema (Y1):

- NO procesa pagos directamente (usa pasarelas externas)
- NO maneja inventario físico distribuido (1 bodega · simple)
- NO soporta multi-moneda (CLP único · USD solo en Nexport Fase 2)
- NO tiene app mobile (solo web responsive)
- NO maneja garantías / seguros productos (defer Y2)
- NO opera fuera de Chile (territorialmente Chile-only Y1)
- NO comparte tenant entre marcas (1 tenant = SMC SpA · multi-tenant es Y3+)
