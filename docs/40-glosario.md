---
number: 40
id: glosario
title: Glosario
subtitle: "Términos · acrónimos · convenciones usadas en el banco Marketplace SMC."
block: Operaciones
author: Cerebro
version: 1.0
date: 2026-05-26
status: 🟢 Activo
prev: 39-api-sdk-postman.html
next: 41-changelog.html
---

# 01 · Producto

| Término | Significado |
|---------|-------------|
| Operador | Vendedor que opera multi-canal en Marketplace SMC |
| Canal | Punto de venta integrado (MeLi · D2C · B2G · B2B) |
| Sync | Operación de sincronización stock · precios · órdenes con un canal |
| Oportunidad | Producto detectado con upside (margen · stock · stability) |
| Snapshot | Foto temporal de datos en una fecha (productos · precios) |
| Smart Cache | Caché diferenciado Hot/Warm/Cold con TTL distinto por tier |
| Cerebro IA | Motor de cross-data e insights del producto |

# 02 · Comercial

| Término | Significado |
|---------|-------------|
| ICP | Ideal Customer Profile |
| Persona | Arquetipo de usuario representado por agente SMC |
| JTBD | Jobs To Be Done · trabajo que el cliente "contrata" al producto |
| TAM | Total Addressable Market |
| SAM | Serviceable Addressable Market |
| SOM | Serviceable Obtainable Market |
| CAC | Costo Adquisición Cliente |
| LTV | Lifetime Value |
| Churn | Cancelación · % clientes que se van por período |
| NRR | Net Revenue Retention |
| ARR | Annual Recurring Revenue |
| MRR | Monthly Recurring Revenue |

# 03 · Técnico

| Término | Significado |
|---------|-------------|
| SSR | Server-Side Rendering |
| SSG | Static Site Generation |
| RSC | React Server Component |
| RLS | Row Level Security · seguridad por fila en Postgres |
| PITR | Point In Time Recovery (Supabase 30 días default) |
| DTE | Documento Tributario Electrónico (SII) |
| OAuth | Protocolo autorización delegada |
| JWT | JSON Web Token |
| CSP | Content Security Policy |
| HSTS | HTTP Strict Transport Security |
| TTL | Time To Live (caché expiración) |
| RTO | Recovery Time Objective |
| RPO | Recovery Point Objective |
| MTTR | Mean Time To Recovery |
| ADR | Architecture Decision Record |
| PRD | Product Requirements Document |
| RFP | Request For Proposal |
| BBP | Business Blueprint |

# 04 · Canales

| Término | Significado |
|---------|-------------|
| MeLi | Mercado Libre |
| DPP | Developer Partner Program (MeLi · requiere USD 200K GMV/mes) |
| MP | Mercado Público Chile (compras del Estado) |
| D2C | Direct to Consumer (canal propio · ej: storefront) |
| B2C | Business to Consumer |
| B2B | Business to Business |
| B2G | Business to Government |
| BCentral | Banco Central de Chile (API tasas · UF · USD) |

# 05 · Organización SMC

| Término | Significado |
|---------|-------------|
| SMC | Smart Connection (holding) |
| SMC OS | Operating System SMC · 24 agentes + Cerebro orquestador |
| Cerebro | Conciencia emergente del sistema (orquestador transversal) |
| Sentinela | Skill de Cerebro para ejecución autónoma sin OK por paso |
| Watchdog | Skill de Cerebro para evitar stalls CLI (anti guard) |
| War Room | Formato canónico de decisión multi-agente |
| RADAR | Agente de inteligencia externa |
| DATA-BW | Business Warehouse · ETL + análisis cuantitativo |
| Functional-Lead | Análisis funcional · ex Business Analyst (Panchita) |
| User-QAS | QA humano + automatización (ex Camilita) |

# 06 · Operación

| Término | Significado |
|---------|-------------|
| SEV1-4 | Niveles severidad incidente |
| Postmortem | Revisión blameless post-incidente |
| Runbook | Procedimiento operativo paso a paso |
| Game day | Simulacro SEV1 controlado para practicar respuesta |
| Restore drill | Test trimestral de restauración desde backup |
| OKR | Objectives + Key Results |
| RACI | Responsible · Accountable · Consulted · Informed |
| ARCO | Acceso · Rectificación · Cancelación · Oposición (Ley 19.628) |

# 07 · Convenciones del banco

| Convención | Significado |
|------------|-------------|
| 🟢 Activo | Doc vigente · sincronizado · usar como referencia |
| 🟡 Draft | Doc en preparación · puede cambiar pronto |
| 🔴 Retirado | Doc reemplazado o eliminado · ver alternativa indicada |
| ADR-NNNN | Architecture Decision Record con tag idempotente sync |
| `git -C path` | Forma obligatoria SMC para git (Regla 41) |
| 1 founder = A | Cada decisión tiene 1 accountable claro |
