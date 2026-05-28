---
number: 50
id: alimento-canino-carabineros
title: Alimento Canino Carabineros
subtitle: "Proyecto B2G · SMC adjudica licitación ChileCompra · InfoPet provee productos con su know-how de proveedores caninos."
block: Proyectos
author: Javier Bianchi
version: 0.2
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

# 06 · Próximos Pasos

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
