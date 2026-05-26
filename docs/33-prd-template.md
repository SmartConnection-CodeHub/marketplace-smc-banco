---
number: 33
id: prd-template
title: PRD Template
subtitle: "Plantilla PRD para nuevas features Marketplace SMC · qué problema · qué solución · qué se mide."
block: Producto
author: PM
version: 1.0
date: 2026-05-26
status: 🟢 Activo
prev: 32-incident-response.html
next: 34-okrs-framework.html
---

# 01 · Cuándo usar este template

Usar PRD cuando:

- Feature mayor afecta 2+ áreas (frontend · backend · datos)
- Cambio impacta a más de 10 usuarios
- Implementación &gt;5 días
- Necesita decisión arquitectural o trade-off importante

NO usar para:

- Bug fixes
- Cambios cosméticos
- Refactor interno sin user impact
- Spikes &lt;1 día (usar nota corta · no PRD)

# 02 · Estructura del PRD

Toda PRD debe tener estas 8 secciones · si una está vacía justificar por qué.

## Sección 01 · One-liner

Una línea: qué problema resolvemos · para quién · qué cambia. Ejemplo:

> Permitir al operador ver oportunidades cross-canal en un solo lugar para no tener que abrir MeLi · SoloTodo · Mercado Público uno por uno.

## Sección 02 · Problema (motivación)

- ¿Qué dolor concreto observamos? (citas usuarios · métricas)
- ¿Por qué ahora? (urgencia · oportunidad)
- ¿Qué pasa si NO hacemos nada?

## Sección 03 · Usuario y casos de uso

- Persona afectada (Cerebro · Comercial · Fiori · etc.)
- Top 3 casos de uso priorizados
- Frecuencia de uso esperada (diario · semanal · mensual)

## Sección 04 · Solución propuesta

- Descripción funcional (qué hace el usuario)
- Flujo principal · pasos numerados
- Mockup HTML o wireframe (link a maqueta Business Analyst)
- Edge cases conocidos

## Sección 05 · Out of scope

- Qué NO incluye esta versión (explícito)
- Por qué se decidió postergarlo
- Bajo qué condiciones se incluiría futuro

## Sección 06 · Métricas de éxito

- 1 métrica primaria (la que decide si vale o no)
- 2-3 secundarias (sanity check)
- Baseline actual + target
- Cuándo se mide post-lanzamiento

## Sección 07 · Riesgos y dependencias

- ¿De qué APIs externas depende? (puede caer · changelog)
- ¿Qué se rompe si esto no llega a tiempo?
- ¿Cuál es el plan B?

## Sección 08 · Roadmap implementación

- Fases (MVP · v1 · v2)
- Estimación esfuerzo por fase
- Owner técnico

# 03 · Anti-patrones PRD

> [!anti] Evitar
> - Solución sin problema · "queremos hacer X" sin justificación
> - Métrica vaga · "mejorar UX" sin número
> - Scope creep en sección 05 ("incluye todo lo posible")
> - Sin alternativas evaluadas (¿por qué esta solución y no otra?)
> - Sin dueño técnico definido

# 04 · Aprobación

Antes de empezar implementación:

- PM da OK funcional (problema bien definido)
- TechLead da OK técnico (factible · sin tech debt nuevo)
- Founder da OK comercial (alineado con roadmap trimestral)
