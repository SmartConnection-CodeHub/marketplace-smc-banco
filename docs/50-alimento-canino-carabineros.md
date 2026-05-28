---
number: 50
id: alimento-canino-carabineros
title: Alimento Canino Carabineros
subtitle: "Proyecto B2G · SMC adjudica licitación ChileCompra · InfoPet provee productos con su know-how de proveedores caninos."
block: Proyectos
author: Javier Bianchi
version: 0.3
date: 2026-05-28
status: 🟡 En evaluación
prev: 41-changelog.html
next: 41-changelog.html
---

# 01 · Descripción del Proyecto

Provisión de alimento canino (croquetas y húmedo) a **Carabineros de Chile** para sus unidades K9 de trabajo y perreras institucionales. El canal es **ChileCompra** (Mercado Público), modalidad licitación pública.

**Smart Connection SpA** actúa como contratista B2G: adjudica la licitación, gestiona el contrato con el Estado y factura a Carabineros. **InfoPet** actúa como proveedor interno: abastece los productos aprovechando su red de proveedores caninos y conocimiento del mercado.

> [!premise] 🎯 Modelo de negocio
> SMC tiene la estructura legal y comercial para operar en ChileCompra · InfoPet tiene el know-how de productos, proveedores y logística canina. La unión de ambos crea una ventaja competitiva que ninguna distribuidora genérica puede replicar fácilmente.

---

# 02 · Flujo Operativo

El proyecto opera en **3 capas** con roles claramente separados:

```
┌──────────────────────────────────────────────────────────────┐
│  CAPA 1 · ESTADO                                             │
│  Carabineros de Chile · Dirección de Logística               │
│  Publica licitación en ChileCompra → adjudica → paga factura │
└──────────────────┬───────────────────────────────────────────┘
                   │ Contrato + Factura (precio gobierno)
                   ▼
┌──────────────────────────────────────────────────────────────┐
│  CAPA 2 · CONTRATISTA B2G                                    │
│  Smart Connection SpA (RUT 76.811.863-9)                     │
│  Se inscribe en ChileProveedores · presenta oferta ·         │
│  gestiona contrato · coordina entrega · factura al Estado    │
└──────────────────┬───────────────────────────────────────────┘
                   │ Orden de compra (precio proveedor + margen SMC)
                   ▼
┌──────────────────────────────────────────────────────────────┐
│  CAPA 3 · PROVEEDOR INTERNO                                  │
│  InfoPet (know-how productos + red de proveedores caninos)   │
│  Selecciona productos · gestiona stock · coordina entrega    │
│  Proveedores: TopK9 · otros distribuidores caninos           │
└──────────────────────────────────────────────────────────────┘
```

> [!info] 💡 Por qué este modelo funciona
> InfoPet ya opera con TopK9 y otros proveedores caninos premium · tiene experiencia comprando volumen · conoce qué productos funcionan para perros de trabajo. SMC aporta la estructura jurídica y comercial para operar en el Estado. Juntos compiten contra distribuidoras genéricas que no tienen ese know-how específico.

---

# 03 · Márgenes del Flujo

El modelo genera margen en **dos puntos**:

| Capa | Actor | Precio referencia | Margen estimado |
|------|-------|-------------------|-----------------|
| Compra a proveedor | InfoPet → TopK9/otros | Costo neto proveedor | — |
| Venta interna | SMC → InfoPet (precio transfer) | Costo + margen InfoPet | ~15–25% |
| Venta al Estado | SMC → Carabineros | Precio licitación | ~20–30% sobre transfer |
| **Margen total cadena** | | | **~35–55% sobre costo** |

> [!warning] ⚠️ Variables que comprimen margen
> Boleta de seriedad de oferta · garantía de fiel cumplimiento (5–10% del contrato) · logística y despacho a cuarteles · plazo de pago Estado 30–60 días hábiles · IVA diferido. El margen real neto puede ser menor al estimado sin estos costos.

---

# 04 · Contexto B2G

**Canal:** ChileCompra · Mercado Público (www.mercadopublico.cl)

**Organismo comprador:** Carabineros de Chile · Dirección de Logística

**Tipo de compra esperada:**

| Modalidad | Monto estimado | Plazo proceso |
|-----------|----------------|---------------|
| Trato directo | < $30M CLP | Rápido · menos requisitos |
| Licitación pública L1 | < $100M CLP | 20 días hábiles |
| Licitación pública LE | $100M–$1.000M CLP | 30 días hábiles |

> [!decision] 📌 Estrategia de entrada
> Arrancar con **trato directo** o **L1** para construir historial como proveedor del Estado antes de competir en licitaciones LE grandes. El historial de contratos cumplidos es un factor de evaluación en futuras licitaciones.

---

# 05 · Productos InfoPet para Carabineros

**Categoría ONU:** 10131500 (Animal feed)

**Productos objetivo a través de InfoPet:**

- Croquetas premium para razas medianas/grandes (perros de trabajo activos)
- Alimento húmedo para recuperación post-operatoria o perros mayores
- Suplementos articulares (glucosamina/condroitina) para K9 de alto rendimiento
- Snacks y premios para entrenamiento K9

**Proveedores de InfoPet que abastecen:**
- **TopK9** — proveedor principal · alimento y snacks caninos premium
- Otros distribuidores de la red InfoPet según disponibilidad y volumen

> [!success] ✅ Ventaja diferenciadora
> InfoPet conoce qué productos funcionan en perros de trabajo (alto desgaste energético · articulaciones · recuperación). Eso se traduce en una propuesta técnica más sólida que la de un distribuidor genérico que solo ofrece precio.

---

# 06 · Por Qué SMC y No InfoPet Directamente

InfoPet **no puede licitar** contratos de Carabineros de Chile por **conflicto de interés**: los socios de InfoPet son hijos de funcionarios de Carabineros, lo que les impide ser proveedores directos del organismo según la normativa de probidad y contratos públicos chilena (Ley 19.886, art. 4).

SMC SpA no tiene esa restricción y opera con total independencia legal respecto de Carabineros.

> [!premise] 🤝 Modelo de ayuda mutua — no de maximización de margen
> SMC no busca el mayor margen posible en esta operación. El % que captura es bajo y acordado entre founders. El valor para SMC es otro: **facturas de ventas reales** a un organismo del Estado, que aumentan la credibilidad financiera de la empresa ante bancos, inversionistas y proveedores. Para InfoPet es la única forma de participar de esta oportunidad sin exponer a sus socios a sanciones legales.

**Beneficios concretos por actor:**

| Actor | Beneficio directo |
|-------|-------------------|
| **SMC SpA** | Historial de ventas B2G · credibilidad financiera · facturación real · puntaje ChileProveedores |
| **InfoPet** | Acceso a un canal B2G que no puede operar directamente · margen sobre sus productos a volumen |
| **Founders** | Sinergia entre empresas del grupo · sin competencia interna · flujo de caja coordinado |

---

# 07 · Flujo de IVA Optimizado

El modelo de 3 capas permite que cada actor pague IVA **solo sobre su margen**, minimizando el IVA total de la cadena.

```
PROVEEDOR (TopK9 u otro)
  Factura a InfoPet: $100 neto + $19 IVA = $119 total
  IVA emitido: $19

        ↓

INFOPET
  Crédito fiscal IVA: $19 (factura TopK9)
  Factura a SMC: $130 neto + $24,7 IVA = $154,7 total
  IVA a pagar InfoPet: $24,7 − $19 = $5,7 (solo sobre margen $30)

        ↓

SMC SpA
  Crédito fiscal IVA: $24,7 (factura InfoPet)
  Factura a Carabineros: $160 neto + $30,4 IVA = $190,4 total
  IVA a pagar SMC: $30,4 − $24,7 = $5,7 (solo sobre margen $30)

        ↓

CARABINEROS (Estado)
  Paga $190,4 total · recupera IVA vía crédito fiscal institucional
```

> [!success] ✅ Resultado del flujo IVA
> IVA total pagado por la cadena privada: **$11,4** sobre $60 de margen combinado (tasa efectiva 19% solo sobre valor agregado real). Sin este esquema de facturación encadenada, la carga tributaria sería mayor. El Estado recupera su IVA, la cadena privada paga solo lo que corresponde.

> [!info] 💡 Precio gobierno vs. precio costo
> Los números del ejemplo son ilustrativos. Los márgenes reales se definen al momento de armar la oferta licitatoria: InfoPet fija su precio transfer a SMC con suficiente margen para cubrir operación + IVA diferido · SMC arma el precio oferta considerando garantías + logística + su margen acordado.

---

# 08 · Próximos Pasos

**SMC (Javier / Guillermo):**
- [ ] Inscribir Smart Connection SpA en ChileProveedores (RUT 76.811.863-9)
- [ ] Buscar licitaciones históricas de Carabineros en Mercado Público (rubro: alimento animal)
- [ ] Preparar ficha de proveedor y documentación requerida por ChileCompra
- [ ] Definir monto objetivo de primera adjudicación (recomendado: trato directo < $30M)

**InfoPet (Javier):**
- [ ] Solicitar cotización de volumen B2G a TopK9
- [ ] Levantar catálogo de productos con resolución SAG para licitaciones
- [ ] Calcular precio transfer InfoPet → SMC para distintos volúmenes
- [ ] Confirmar capacidad logística para despacho a cuarteles de Carabineros
