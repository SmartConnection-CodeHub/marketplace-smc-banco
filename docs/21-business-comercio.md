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

SMC SpA opera **tres modos en paralelo** según rotación · capital disponible · velocidad de escalado:

1. **Stock propio · compra local Chile (Y1 prioridad)**: compra a proveedores nacionales → recibe en bodega → vende multi-canal · ciclo 3-7 días · pago CLP · margen 28-45%
2. **Stock propio · importación Nexport (Fase 2 · Y2+)**: cuando el volumen justifique · LCL/FCL en USD · ciclo 30-90 días · margen significativamente mayor pero capital atado más tiempo
3. **Dropshipping**: vender sin stock propio · proveedor (chileno o internacional) despacha directo al cliente · margen 10-25% sin capital atado · escalado catálogo rápido

Margen blended objetivo: 28-38% considerando mix de los 3 modos.

# 02 · Diagrama del flujo de dinero

**Modo 1 · Stock propio compra LOCAL Chile (Y1 prioridad):**

```
Capital inicial 50M CLP
      ↓
Compra a proveedor local Chile (CLP · 3-7 días)
      ↓
Recepción bodega · QA · ingreso inventario
      ↓
Publicación cross-canal (MeLi + MP + B2B)
      ↓
        ┌────────┴────────┐
    Venta MeLi  Venta B2G  Venta B2B
        └────────┬────────┘
                 ↓
       Cobro · DTE · Reinversión
```

**Modo 2 · Stock propio IMPORTACIÓN Nexport (Fase 2 · Y2+):**

```
Capital ampliado (línea crédito · reinversión Y1)
      ↓
RFQ a Nexport (USD · LCL/FCL · 30-90 días)
      ↓
Tránsito + aduana + IVA importación
      ↓
Recepción bodega Chile (igual P03)
      ↓
[Mismo flujo Modo 1 desde acá]
```

**Modo 3 · Dropshipping (sin stock propio · escalado rápido):**

```
Catálogo proveedor dropship sincronizado
      ↓
Publicación cross-canal con flag is_dropship=true
      ↓
            Venta llega
                 ↓
   OC propagada al proveedor (Supplier Adapter)
                 ↓
   Proveedor despacha DIRECTO al cliente final
                 ↓
       Cobro nuestro · DTE nuestro · margen retenido (10-25%)
                 ↓
       Liquidación al proveedor 7-15 días post-venta
```

# 03 · Streams de revenue

| Canal | % Y1 | Margen stock local | Margen Nexport (Y2+) | Margen dropship | Plazo cobro |
|-------|------|---------------------|----------------------|-----------------|-------------|
| Mercado Libre (B2C) | 50% | 28% | 35% | 12-18% | 14-28 días |
| Mercado Público (B2G) | 30% | 38% | 45% | 20-25% | 30-60 días |
| B2B empresa privada | 15% | 42% | 50% | 22-28% | 30-60 días |
| D2C storefront (Y2+) | 5% Y1 · 30% Y3 | 50% | 58% | 25-30% | inmediato |

Blend Y1 estimado: 28-33% margen bruto (predominante stock local + dropshipping) antes de costos operativos.

# 03b · Cuándo usar cada modo

| Producto / situación | Modo recomendado |
|----------------------|------------------|
| SKU validado · alta rotación · proveedor local disponible | Stock local Y1 |
| SKU nuevo · sin validar demanda · sin querer arriesgar capital | Dropshipping |
| Producto premium · margen 40%+ · volumen alto sostenido | Stock local Y1 (luego Nexport Y2) |
| Catálogo amplio para explorar (long-tail) | Dropshipping |
| Producto bulky/caro · rotación lenta | Dropshipping (no atar capital) |
| Producto exclusivo · ventaja diferencial | Stock propio (local o importado) |
| Volumen mensual sostenido > USD 5K mismo SKU | Migrar de dropship → stock local |
| Volumen sostenido > USD 30K mensual mismo SKU | Migrar de stock local → Nexport (Fase 2) |
| SLA crítico despacho cliente final · marca premium | Stock propio (control total) |
| Test de mercado producto importado antes de Nexport | Dropshipping desde importador chileno |

# 03c · Estrategia de migración entre modos

```
Producto nuevo → ARRANCA dropshipping (test demanda · sin capital)
                ↓
        ¿Vende >USD 5K/mes sostenido 2 meses?
                ↓ SÍ
        MIGRA a stock local Chile (margen sube 15-25 pp)
                ↓
        ¿Vende >USD 30K/mes sostenido 6 meses?
                ↓ SÍ
        EVALÚA Nexport importación Fase 2 (margen sube 5-10 pp más)
```

Esta progresión protege el capital · cada upgrade requiere validación real de volumen.

# 03d · Tácticas Y1 validadas por referentes chilenos

Aprendizajes del ecosistema e-commerce chileno aplicables Y1 SMC:

**Reputación primero (fase 1 · primeros 3 meses):**
- Primeras 10 ventas MeLi a precio costo o regalando · NO buscar utilidad
- Envío gratis siempre · sacrifica margen inicial · gana reputación
- Fotografía profesional propia · jamás usar fotos del proveedor

**Escala con base sólida (fase 2 · post 10 ventas verdes):**
- Activar Mercado Ads · ANTES de reputación es gastar sin convertir
- Migrar a Full Fulfillment MeLi (stock en sus almacenes) si producto rota
- Optimizar logística antes de ampliar catálogo

**Marca SMC mínima viable:**
- Empaque con sticker propio (nombre + logo)
- Mensaje post-venta personalizado (agradecimiento + invitación reseña)
- Paleta visual consistente cross-canal
- Diferenciarse · no competir solo en precio

**Anti-patrones a evitar:**
- Esperar dinero rápido o tratar como part-time
- Fotos del proveedor (= identificarse genérico)
- Sin estrategia de escalado post primeras ventas
- Mercado Ads sin reputación
- Vender SKU idéntico a competencia con misma foto y título

Referencia: e-commerce chileno escalado validó este path 2020-2025 con resultados USD 4M/año.

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
