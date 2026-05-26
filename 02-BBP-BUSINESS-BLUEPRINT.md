# 02 · BUSINESS BLUEPRINT (BBP) · 12 procesos end-to-end
**Marketplace SMC · cómo opera el negocio · NO cómo se construye el software**

> Documento 2 de 9 · base funcional del sistema
> Versión: 1.0 · 2026-05-25 · autor: Functional-Lead + Cerebro
> Status: 🟢 ACTIVO

---

## Cómo leer este documento

Cada proceso describe:
1. **Actor(es)** · quién lo ejecuta
2. **Trigger** · qué lo inicia
3. **Pasos** · secuencia de actividades (notación BPMN simplificada)
4. **Inputs / Outputs**
5. **Eventos generados** · qué dispara hacia otros módulos
6. **Excepciones** · qué puede salir mal
7. **KPIs** · qué se mide

---

## Mapa de los 12 procesos

```
                ┌──────────────────────────────────┐
                │  CICLO ALTO NIVEL                 │
                └──────────────────────────────────┘

   [1] Sourcing               →   [2] Compra a Nexport
        ↓                              ↓
   [3] Recepción bodega       →   [4] Publicación cross-canal
        ↓                              ↓
        ↓                          ┌───┴───┬───────┬─────────┬─────────┐
        ↓                          ↓       ↓       ↓         ↓         ↓
        ↓                       [5] MeLi [6] D2C [7] B2G   [8] B2B  (futuros)
        ↓                          ↓       ↓       ↓         ↓
        └─────── [9] Fulfillment / Despacho ◄──────┴─────────┘
                          ↓
                      [10] Devolución (opcional)
                          ↓
                      [11] Facturación
                          ↓
                      [12] Cobranza
                          ↓
                      → Asiento contable automático (transversal a todos)
```

---

## Proceso 1 · SOURCING (búsqueda de productos)

**Actor:** Guillermo (operador) + IA Cerebro (sugerencias)
**Trigger:** Decisión de ampliar catálogo · alerta de stock bajo · oportunidad detectada

**Pasos:**
1. Operador define categoría/nicho a explorar (ej: "audífonos bluetooth")
2. Sistema consulta histórico de rotación de SKUs similares (si los hay)
3. IA sugiere: keywords trending MeLi, precios competencia, márgenes esperados
4. Operador filtra: 3-5 candidatos
5. Sistema arma "Brief Sourcing" con specs (descripción, precio target, MOQ esperado)
6. Brief queda en `/sourcing/briefs/{id}`
7. Pasa al proceso 2 (Compra a Nexport)

**Inputs:** keyword, presupuesto target, márgenes mínimos
**Outputs:** Brief de Sourcing (PDF + registro DB)
**Eventos generados:** `sourcing.brief.created`
**Excepciones:** ninguna oportunidad supera margen mínimo → brief descartado · alerta
**KPIs:** time-to-brief, % briefs que llegan a compra

---

## Proceso 2 · COMPRA A NEXPORT (intermediario importador)

**Actor:** Operador + Nexport (proveedor)
**Trigger:** Brief de Sourcing aprobado

**Pasos:**
1. Operador envía Brief a Nexport vía WhatsApp/email/portal Nexport
2. Nexport cotiza · entrega cotización en CLP+IVA + lead time
3. Operador registra cotización en `/sourcing/quotes/{id}`
4. Si OK · Operador emite Orden de Compra (OC) en Hub
5. Hub registra: OC + términos pago (ej: 50% adelanto · 50% B/L)
6. Operador transfiere primer pago (registro CxP)
7. Nexport confirma · envía tracking estimado
8. Hub crea registro shipment `/sourcing/shipments/{id}` con ETA

**Inputs:** Brief aprobado
**Outputs:** OC emitida · pago registrado · shipment en tránsito
**Eventos generados:** `purchase.po.created`, `purchase.payment.made`, `purchase.shipment.in-transit`
**Excepciones:** Nexport sin stock → buscar proveedor alternativo · Nexport cambia precio → renegociar
**KPIs:** time-to-PO, % OC entregadas en plazo, variación precio cotizado vs final

**Notas legales:**
- Factura llega de Nexport (proveedor chileno · CLP + IVA 19%)
- IVA crédito se acumula en F29 mes correspondiente
- NO hay tipo de cambio · NO hay aduana de tu lado

---

## Proceso 3 · RECEPCIÓN EN BODEGA

**Actor:** Operador (o bodeguero futuro)
**Trigger:** Llegada física de mercadería de Nexport

**Pasos:**
1. Bodeguero recibe paquete · verifica embalaje
2. Abre Hub → /warehouse/recepcion → escanea código OC (QR generado en proceso 2)
3. Hub muestra lista esperada (SKU · cantidad · descripción)
4. Bodeguero cuenta físicamente · marca cada SKU como recibido
5. Si discrepancia (cantidad menor · daños) → registra "novedad" + foto
6. Asigna ubicación física a cada SKU (rack · pasillo · bin)
7. Sistema actualiza `inventory.physical_stock` · genera etiquetas barcode
8. Genera "Acta de Recepción" PDF (firmable digital)

**Inputs:** Mercadería física · OC referenciada
**Outputs:** Stock disponible en inventario · acta firmada
**Eventos generados:** `inventory.received`, `inventory.discrepancy` (si aplica)
**Excepciones:** OC no encontrada · cantidad >>esperada · producto distinto al pedido
**KPIs:** time-to-receive, % discrepancias, ratio merma/recepción

**Nota crítica:** este proceso DISPARA el asiento contable automático:
```
DEBE: Mercadería (existencia) por valor neto compra
HABER: Proveedores (Nexport) por valor compra
+ asiento separado IVA crédito si aplica
```

---

## Proceso 4 · PUBLICACIÓN CROSS-CANAL

**Actor:** Operador + Sistema (auto-publish)
**Trigger:** Producto nuevo en inventario · o decisión publicar producto existente en canal nuevo

**Pasos:**
1. Operador entra a `/inventory/sku/{id}` · selecciona "Publicar en canales"
2. Hub muestra checklist: MeLi · D2C · Mercado Público · B2B · Falabella (si están conectados)
3. Operador marca canales destino
4. Hub aplica `price-rules` por canal (landed cost + markup canal + comisión + IVA)
5. Operador revisa precio sugerido por canal · ajusta si quiere
6. Para cada canal marcado · Hub llama al adapter correspondiente:
   - MeLi adapter → API /items POST
   - D2C adapter → INSERT en tabla storefront-products
   - MP adapter → preparar borrador catálogo CM
   - B2B adapter → agregar a catálogo mayorista
7. Cada adapter responde OK/error
8. Hub registra estado publicación por canal en `inventory.channel_sync_status`

**Inputs:** SKU + canales destino + precios
**Outputs:** Producto publicado en N canales con status individual
**Eventos generados:** `inventory.published`, `channel.publish.success`, `channel.publish.error`
**Excepciones:** adapter falla (token expirado · MeLi rechaza) → reintentar + alerta
**KPIs:** time-to-publish, % éxito por canal, productos sin sincronizar

**Premisa core:** **publicar en N canales = 1 click. No 4 forms.**

---

## Proceso 5 · VENTA EN MELI (B2C marketplace ajeno)

**Actor:** Comprador externo MeLi · Hub recibe webhook
**Trigger:** Cliente paga en MeLi

**Pasos:**
1. MeLi envía webhook a `/api/webhooks/meli` con orden nueva
2. Hub valida HMAC · crea registro `orders` con `channel='meli'`
3. Hub reserva stock (`inventory.reservations` +1, `physical_stock` no cambia aún)
4. Cliente queda como `customers` con flag `is_meli_anonymous=true`
5. Hub crea task de fulfillment automática → entra a cola `/fulfillment/pendientes`
6. Operador (o sistema futuro) gestiona despacho (ver proceso 9)
7. Cuando MeLi confirma pago liberado (14-21 días) → registro `payments` con status=paid
8. CxC contra MeLi se actualiza

**Inputs:** Webhook MeLi order_created
**Outputs:** Orden registrada · stock reservado · task fulfillment
**Eventos generados:** `order.created`, `inventory.reserved`, `fulfillment.queued`
**Excepciones:** webhook duplicado (idempotency check) · stock insuficiente (oversell · alerta crítica)
**KPIs:** orders/día por canal · oversell rate (debe ser 0)

---

## Proceso 6 · VENTA EN D2C (storefront propio)

**Actor:** Comprador externo · Hub procesa checkout
**Trigger:** Cliente completa checkout en kanki.smconnection.cl (u otro storefront tenant)

**Pasos:**
1. Cliente en storefront agrega productos al carrito
2. Checkout: ingresa datos + paga (WebPay/MercadoPago/transferencia)
3. Hub recibe orden via API directa (no webhook · es nuestro propio storefront)
4. Mismo flow que MeLi: orden + reserva stock + customer + task fulfillment
5. Cliente queda como `customers` con datos completos
6. Boleta/factura electrónica se emite automático
7. Pago se acredita (depende pasarela · WebPay 24h · transferencia manual)

**Inputs:** Checkout completo · pago confirmado
**Outputs:** Orden · DTE emitido · cliente registrado · fulfillment en cola
**Eventos generados:** `order.created`, `dte.issued`, `payment.received`
**Excepciones:** pasarela rechaza · cliente abandona checkout · stock cambió entre carrito y pago
**KPIs:** conversion rate · ticket promedio · abandono carrito

---

## Proceso 7 · VENTA B2G (Mercado Público · Estado)

**Actor:** Operador + Hub + Mercado Público API
**Trigger:** Licitación publicada que matchea filtros · o compra ágil dirigida

**Pasos:**
1. Hub monitorea API Mercado Público diariamente
2. Filtra licitaciones por: categorías propias · región · monto
3. Operador revisa "Bandeja Oportunidades" `/channels/mp/licitaciones-abiertas`
4. Decide ofertar → click "Preparar oferta"
5. Hub pre-llena form con productos del catálogo CM + precio sugerido + plazo entrega
6. Operador adjunta: certificados · garantía bancaria si aplica
7. Hub envía oferta via API MP (o exporta XML para upload manual)
8. Si adjudican → MP notifica · Hub registra orden con `channel='mp'`
9. Operador entrega físicamente · genera acta recepción Estado
10. Hub emite factura electrónica → carga en sistema MP
11. Estado paga 30-90 días después · Hub trackea CxC

**Inputs:** Licitación detectada · oferta operador
**Outputs:** Oferta enviada · orden adjudicada · factura · pago futuro
**Eventos generados:** `mp.tender.detected`, `mp.offer.sent`, `mp.tender.won`, `order.created`
**Excepciones:** licitación se cae · oferta rechazada · Estado tarda más de 90 días pagar
**KPIs:** tasa adjudicación · tiempo pago promedio Estado · ROI por organismo público

---

## Proceso 8 · VENTA B2B (empresa privada)

**Actor:** Operador + Cliente empresa
**Trigger:** Empresa pide cotización (email · WhatsApp · llamada)

**Pasos:**
1. Operador crea/busca cliente en `/channels/b2b/clientes`
2. Click "Nueva cotización" → arma quote (pickea SKUs + cantidades + precio mayorista)
3. Hub genera PDF cotización · envía email automático al cliente
4. Cliente aprueba (responde email o click link aprobación)
5. Hub convierte cotización en orden · reserva stock · crea task fulfillment
6. Hub emite factura electrónica
7. Operador despacha
8. Cliente paga (según términos · normalmente 15-30 días)
9. Hub trackea CxC

**Inputs:** Solicitud cotización
**Outputs:** Cotización · orden · factura · CxC
**Eventos generados:** `b2b.quote.created`, `b2b.quote.approved`, `order.created`
**Excepciones:** cliente no responde 14 días → recordatorio · rechazo cotización → analytics
**KPIs:** conversion quote→orden · ticket promedio B2B · % cobrado en tiempo

---

## Proceso 9 · FULFILLMENT (despacho)

**Actor:** Operador (o equipo bodega futuro) + courier
**Trigger:** Orden con status=paid o status=approved en cola fulfillment

**Pasos:**
1. Operador entra a `/fulfillment/pendientes` · ve cola priorizada
2. Para cada orden: Hub genera picking list (qué SKU sacar de qué ubicación)
3. Operador hace picking físico · marca SKUs picked
4. Packing: arma paquete · pesa · mide
5. Hub elige courier según regla `/reglas-despacho` (MeLi → Chilexpress · B2B → Starken · etc)
6. Llama API courier · genera etiqueta envío
7. Operador pega etiqueta · entrega a retiro courier
8. Hub registra tracking number · monitorea estado
9. Cuando courier marca entregado → Hub actualiza orden status=delivered
10. Webhook al canal correspondiente (MeLi · MP · etc.) confirma entrega

**Inputs:** Orden paid · stock disponible
**Outputs:** Paquete entregado · tracking activo · costo logístico registrado
**Eventos generados:** `fulfillment.picked`, `fulfillment.shipped`, `fulfillment.delivered`
**Excepciones:** SKU no encontrado físicamente (stock fantasma) · courier no retira · entrega fallida
**KPIs:** time-to-ship · % entregado en plazo · % paquetes perdidos

**Asiento contable automático:** al shipped:
```
DEBE: Costo de venta (CMV) por landed cost
HABER: Mercadería (existencia) por landed cost
```

---

## Proceso 10 · DEVOLUCIÓN (opcional · sí pero ojalá poco)

**Actor:** Cliente · Operador
**Trigger:** Cliente pide devolución (motivo: defecto · arrepentimiento · diferente al esperado)

**Pasos:**
1. Cliente solicita por canal correspondiente (MeLi · email · WhatsApp)
2. Operador valida motivo · aprueba RMA
3. Hub crea ticket `/fulfillment/devoluciones/{id}`
4. Cliente envía producto de vuelta
5. Operador recibe · inspecciona estado
6. Si OK · stock vuelve a inventario (`inventory.adjustments` IN)
7. Hub emite Nota de Crédito Electrónica (NC 61) al canal de origen
8. Reembolsa pago al cliente (transferencia · WebPay reverse · etc.)

**Inputs:** Solicitud devolución · producto físico
**Outputs:** Stock recuperado · NC emitida · reembolso
**Eventos generados:** `return.requested`, `return.approved`, `return.received`, `dte.credit-note.issued`
**Excepciones:** producto llega dañado · cliente no envía · disputa MeLi (caso de fuerza)
**KPIs:** return rate · costo promedio devolución

---

## Proceso 11 · FACTURACIÓN (DTE Chile)

**Actor:** Sistema (automático)
**Trigger:** Venta confirmada · necesidad emitir DTE

**Pasos:**
1. Cuando orden status=approved (o paid en MeLi/D2C) · Hub trigger emisión DTE
2. Decide tipo documento según cliente:
   - Persona natural sin RUT → Boleta Electrónica (39)
   - Empresa con RUT → Factura Electrónica (33)
   - Cliente exento (algunas org públicas) → Factura Exenta (34)
3. Llama API Open Factura (o SII MIPYME directo)
4. Recibe folio + XML firmado + PDF
5. Guarda en `dte.documents`
6. Envía PDF al cliente por email
7. Reporta automático al SII (libro IVA digital)

**Inputs:** Orden + cliente + items
**Outputs:** DTE válido · folio · PDF + XML
**Eventos generados:** `dte.issued`, `dte.send.failed`
**Excepciones:** folio agotado · cliente sin RUT cuando aplica · API Open Factura cae
**KPIs:** % DTE emitidos sin error · time-to-DTE

**Asiento contable automático:**
```
DEBE: Clientes (cuentas por cobrar) por total con IVA
HABER: Ventas afectas por neto
HABER: IVA débito por IVA
```

---

## Proceso 12 · COBRANZA

**Actor:** Sistema (monitoreo) + Operador (gestión cobros vencidos)
**Trigger:** Vencimiento próximo de factura

**Pasos:**
1. Hub monitorea diariamente CxC `/finanzas/cuentas-por-cobrar`
2. Calcula días restantes hasta vencimiento por cliente/canal
3. 5 días antes vencimiento → recordatorio automático cliente (email)
4. 0 días (vencimiento) → alerta operador
5. +7 días → segundo recordatorio + alerta amarilla
6. +15 días → llamada manual del operador
7. +30 días → escalamiento (gestión cobranza)
8. Cuando pago llega (transferencia · WebPay · acreditación canal) → conciliación
9. Hub matchea pago con factura · marca como `paid`
10. Genera asiento contable

**Inputs:** Facturas emitidas con vencimiento
**Outputs:** Pagos cobrados · alertas vencimientos · forecast flujo caja
**Eventos generados:** `payment.received`, `payment.overdue`, `customer.payment-late`
**Excepciones:** pago parcial · pago duplicado · cliente disputa monto
**KPIs:** DSO (Days Sales Outstanding) · % cobrado en plazo · cartera vencida

**Asiento contable automático:**
```
DEBE: Bancos (cuenta corriente) por monto recibido
HABER: Clientes (CxC) por monto recibido
```

---

## Procesos transversales (no son uno de los 12 pero corren siempre)

### T1 · CONTABILIDAD AUTOMÁTICA (event-driven)
Cada evento de los 12 procesos dispara asientos contables en plan de cuentas configurable. Generan F29 mensual automático + libro IVA + auxiliar de clientes/proveedores. Sin intervención humana salvo ajustes manuales.

### T2 · INVENTARIO REAL-TIME (single source of truth)
Cada venta/recepción/devolución/merma actualiza inventario inmediato. Cross-canal sincroniza stock vía webhook a cada adapter (MeLi push, D2C update, MP refresh catálogo CM).

### T3 · CEREBRO IA (sugerencias proactivas)
Analiza data de los 12 procesos · genera alertas: "stock bajo SKU X" · "MeLi vendiste 30% menos esta semana" · "comprá más del proveedor Y · su lead time mejoró".

### T4 · COMPLIANCE (vencimientos y validaciones)
F30/F30-1 (cotizaciones previsionales) · garantías bancarias · vigencia ChileProveedores · libro IVA digital · F22 anual. Alertas antes de vencer.

### T5 · ANALYTICS (cross-data)
Dashboards consolidados por canal · marca · vertical · producto. Permite tomar decisiones de pricing · canal · sourcing basadas en margen real (no asunciones).

---

## Resumen visual del flujo end-to-end

```
SOURCING (1) → COMPRA (2) → RECEPCIÓN (3) → PUBLICACIÓN (4)
                                                ↓
                          [VENTA] (5/6/7/8)
                                                ↓
                          FULFILLMENT (9) → DEVOLUCIÓN OPC (10)
                                                ↓
                          FACTURACIÓN (11) → COBRANZA (12)
                                                ↓
                          [transversales: contabilidad · inventario · IA · compliance · analytics]
```

---

## Premisa CORE recordada (no se transa)

```
NO duplicar esfuerzo · NO duplicar data · NO duplicar lógica.

1 inventario para los 12 procesos.
1 catálogo de clientes.
1 plan de cuentas.
1 tabla de órdenes (con channel como columna).
N adapters por canal externo.
```

---

**Next:** Doc 03 · Requirements funcional + no funcional
