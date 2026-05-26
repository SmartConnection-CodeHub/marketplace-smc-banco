# 01 · VISION & PROSPECT DEFINITION
**Marketplace SMC · plataforma operativa unificada multi-canal**

> Documento 1 de 9 · base del blueprint · debe leerse PRIMERO
> Versión: 1.0 · 2026-05-25 · autor: Cerebro + PRM + War Room SMC
> Status: 🟢 ACTIVO

---

## 1. ¿Qué es Marketplace SMC?

**Marketplace SMC es UNA SOLA plataforma operativa que centraliza compra, inventario, venta multi-canal, fulfillment, contabilidad y analytics para un vendedor que opera en Chile a través de canales B2C, B2G y B2B simultáneamente.**

No es:
- ❌ NO es un ERP genérico tipo Defontana o Bsale
- ❌ NO es un marketplace público (no se cobra a vendedores terceros)
- ❌ NO es un single-channel manager (no es Helium 10 ni Channable)
- ❌ NO es una tienda online individual (no es Kanki standalone)

Es:
- ✅ Cockpit operativo del vendedor · todo bajo un mismo techo
- ✅ Plataforma multi-tenant que puede operar N marcas/canales sobre la misma base
- ✅ Source-of-truth único de inventario, clientes, pedidos, asientos contables
- ✅ Orquestador de adapters por canal (MeLi · Mercado Público · D2C · B2B · futuros)

---

## 2. North Star Metric

**% de ingresos del usuario que se gestionan dentro de la plataforma (vs fuera de ella).**

Si el usuario factura $10M/mes y solo $2M pasan por SMC Marketplace → North Star = 20%. Si todos los $10M pasan → North Star = 100%.

Esta métrica obliga a que la plataforma sea ÚTIL para TODOS los canales del usuario, no solo el más fácil.

---

## 3. ¿Para quién? · Stakeholders

### Stakeholder principal · "el operador"
- **Vendedor PYME chileno** que opera 2+ canales simultáneamente
- Factura entre $5M y $200M CLP/mes
- Hoy usa Excel + 4-5 herramientas separadas (MeLi seller center + tienda Shopify + carpeta Excel + ChileCompra + Defontana)
- Pierde tiempo conciliando data · no tiene visibilidad cross-canal
- Caso primario · Guillermo (Smart Connection SpA → futuro Marketplace SMC SpA)

### Stakeholder secundario · "los socios"
- Co-founder potencial (Javier · equity TBD)
- Contadora externa (galvarez.cl) que necesita exportar data para F29/F22
- Operador de bodega (futuro · cuando exista bodega física)

### Stakeholder terciario · "los integradores"
- APIs externas: MeLi, Mercado Público, Open Factura, MercadoPago, couriers, Groq IA
- La plataforma debe ser AMIGABLE para integrar nuevas APIs sin refactor

### Anti-stakeholders (NO son nuestro usuario)
- Vendedores grandes (>$500M/mes) · ellos usan Oracle / SAP B1 / Microsoft Dynamics
- Vendedores de un solo canal · ellos no necesitan unificación
- Personas naturales sin SII activo · no podemos atenderlos legalmente

---

## 4. ¿Qué problema resolvemos?

### Problema 1 · "Excel paralelo"
El vendedor lleva 3-5 sistemas de inventario distintos (uno por canal). Cuando vende en MeLi tiene que recordar bajar manual el stock de su tienda Shopify. Resultado: oversell, descontento clientes, multas plataformas.

### Problema 2 · "ceguera cross-canal"
No sabe cuál canal vende más, dónde gana más margen, qué SKU rota mejor por canal. Decide a ciegas dónde invertir publicidad.

### Problema 3 · "facturación rota"
Vende en 4 canales · factura en 1 sistema · concilia mensual a mano · F29 mal · multas SII. Contadora cobra extra por desorden.

### Problema 4 · "publicación duplicada"
Crear el mismo producto en MeLi + Shopify + Mercado Público requiere subir título, fotos, precio, stock 4 veces. Si cambia precio, hay que actualizar en 4 lados.

### Problema 5 · "cobranza ciega"
No sabe cuánto le debe MeLi, ChileCompra, sus clientes B2B. Cada plataforma tiene su propio reporte. Cash flow es adivinanza.

### Problema 6 · "supply chain a ciegas"
No sabe cuándo le llega el próximo lote de Nexport · cuánto stock real tiene · cuándo va a quedar sin SKU X. Decide compras por feeling.

---

## 5. Modelo de negocio

### Fase 1 · uso interno (2026 Q2-Q3)
- Marketplace SMC = herramienta interna del propio Guillermo
- Operada bajo SMC SpA (ampliando giro) o bajo Marketplace SMC SpA (cuando se constituya en Q4)
- Sin facturación · sin clientes externos

### Fase 2 · marca propia única (Kanki como primer tenant · 2026 Q4-2027 Q1)
- Migrar back-office de Kanki al Hub (sin cambiar el front kanki.smconnection.cl)
- Validar arquitectura multi-tenant con caso real

### Fase 3 · 2-3 marcas internas (2027)
- Operar Marketplace SMC con Kanki + otra marca propia + caso vertical X
- Validar plug-and-play de nuevos canales

### Fase 4 · plataforma SaaS para PYMEs (2028+)
- Si las fases 1-3 demuestran que funciona · ofrecer a otros vendedores PYME
- Modelo subscription tipo $100-300K CLP/mes por tenant
- Foco vendedores 2-canal+ que hoy usan Excel paralelo

**Nota:** la fase 4 es opcional. La plataforma puede vivir feliz solo como uso interno de Marketplace SMC SpA. No se condiciona el diseño a que se convierta en SaaS · pero la arquitectura multi-tenant permite hacerlo sin refactor.

---

## 6. Valores de diseño · qué NO transamos

```
1. SINGLE SOURCE OF TRUTH
   1 inventario · 1 catálogo de clientes · 1 catálogo de productos · 1 catálogo
   de proveedores · 1 chart of accounts. Cualquier duplicación = anti-patrón.

2. CHANNEL ADAPTER PATTERN
   Cada canal externo (MeLi, MP, etc.) se conecta vía adapter que implementa
   interfaz estándar. Agregar canal nuevo = escribir 1 adapter · no tocar core.

3. EVENT-DRIVEN ACCOUNTING
   Cada operación (venta, compra, devolución) emite evento que el módulo
   contable consume automático. NO existe "registro manual de asiento".

4. MULTI-TENANT DESDE DÍA 1
   tenant_id en TODAS las tablas. Aunque hoy haya 1 solo tenant · arquitectura
   soporta N. Permite migrar Kanki + agregar marcas sin refactor.

5. HONESTIDAD UI
   Si una pantalla muestra data MOCK · etiqueta visible "mock". Si un cron
   pendiente · etiqueta "pendiente". Cero teatro. Cero Math.random.

6. ESCALABLE GRADUALMENTE
   Empezar simple (1 bodega · 1 marca · 2 canales) pero SIN cementar
   decisiones que impidan crecer (multi-bodega · multi-marca · N canales).

7. COMPLIANCE CHILE NATIVO
   F29 · F22 · DTE · libro IVA · F30 · F30-1 · todo respetando normativa
   SII desde el primer día. Sin parches "cuando crezca lo agrego".
```

---

## 7. Decisiones que NO se toman en este documento (se difieren a docs siguientes)

| Decisión | Va en |
|----------|-------|
| Cuáles 12 procesos exactos | Doc 02 · BBP |
| Qué tablas exactas | Doc 05 · Data Model |
| Qué stack técnico (Next? Rails? Django?) | Doc 07 · Architecture |
| Cuándo se construye qué | Doc 08 · Roadmap |
| Cómo se ve cada pantalla | Doc 09 · Maquetas |
| Pricing del SaaS futuro | Documento aparte cuando se decida fase 4 |

---

## 8. Criterios de éxito (cómo sabemos que la plataforma sirve)

```
Fase 1 (uso interno SMC)
   • Cierre mensual F29 desde Hub sin Excel paralelo
   • >80% órdenes cross-canal vistas en 1 dashboard
   • 0 oversell por desync de inventario
   • Tiempo conciliación mensual reducido 70% vs hoy

Fase 2 (Kanki migrado)
   • Kanki opera 100% desde el Hub · solo storefront vive aparte
   • Stock unificado · venta en Kanki descuenta de inventario maestro
   • Cierre contable Kanki + SMC mismo balance

Fase 3 (2-3 marcas)
   • Plug nuevo tenant en <1 día (no semanas)
   • Plug nuevo canal externo en <1 sprint
   • Métricas por marca + consolidadas (drill-down)

Fase 4 (SaaS)
   • Onboarding cliente PYME en <2 horas (no consulting)
   • Churn <5% anual · CAC < 3 meses de MRR
```

---

## 9. Lo que este documento NO promete

- NO promete que será SaaS comercial (es opcional)
- NO promete reemplazar al contador (asiste pero no decide tributario)
- NO promete vender por canales que no tienen API (Cencosud · supplier portals)
- NO promete construirse en 1 mes (es proyecto enterprise · ver Doc 08 Roadmap)

---

## 10. Una analogía para alinear

```
Marketplace SMC es el "Stripe del vendedor multi-canal chileno":

   Stripe unifica el cobro: cualquier integración, una sola API.
   Marketplace SMC unifica la operación: cualquier canal, una sola plataforma.

   Stripe escondió la complejidad de Visa/Mastercard/Amex bajo /charge.
   Marketplace SMC esconde MeLi/MP/B2B/D2C bajo /sell.
```

---

**Next:** Doc 02 · Business Blueprint · los 12 procesos end-to-end.
