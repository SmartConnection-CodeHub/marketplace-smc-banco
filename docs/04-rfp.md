---
number: 04
id: rfp
title: RFP
subtitle: "Request for Proposal · especificación contractual para construcción interna o vendor externo."
block: Marketplace SMC
author: PM + Cerebro
version: 1.0
date: 2026-05-25
status: 🟢 Activo
prev: 03-requirements.html
next: 05-data-model.html
---

# 01 · Contexto y motivación

Smart Connection SpA (futuro Marketplace SMC SpA) requiere construir una **plataforma operativa unificada multi-canal** que permita gestionar desde un solo lugar: compra, inventario, venta cross-canal (MeLi · D2C · Mercado Público · B2B), fulfillment, facturación electrónica chilena y contabilidad automática.

  
## Situación actual

  
- Operación dispersa en 4-5 herramientas (MeLi Seller Center · Excel · Shopify · ChileCompra portal · contabilidad externa)
- Conciliación manual mensual · alto error · alto costo en horas operativas
- Sin visibilidad cross-canal real · decisiones basadas en feeling
- Sin escalabilidad para sumar marcas/tenants futuros (marcas propias adicionales)

  
## Visión post-implementación

  
- 1 inventario master · 1 base clientes · 1 plan de cuentas · N canales como adapters
- Asientos contables automáticos por cada evento operativo
- Decisiones basadas en margen real cross-canal en tiempo real
- Arquitectura multi-tenant escalable a múltiples marcas

# 02 · Alcance del proyecto

## In-scope

  <table>
    <thead><tr><th>Módulo</th><th>Funcionalidad clave</th></tr></thead>
    <tbody>
      <tr><td>Inventory</td><td>SKU master · stock real-time · ajustes · multi-ubicación</td></tr>
      <tr><td>Sourcing</td><td>Proveedores · órdenes compra · landed cost · recepción</td></tr>
      <tr><td>Channels</td><td>4 canales nativos: MeLi · D2C · Mercado Público · B2B (Adapter pattern)</td></tr>
      <tr><td>Fulfillment</td><td>Picking · packing · couriers (Chilexpress · Starken)</td></tr>
      <tr><td>Finance</td><td>DTE · CxC · CxP · margen real · pre-F29</td></tr>
      <tr><td>Cerebro IA</td><td>Chat insights · alertas proactivas · cross-data</td></tr>
      <tr><td>Analytics</td><td>Dashboard consolidado · drill-down · KPIs</td></tr>
    </tbody>
  </table>

  
## Out-of-scope (no incluido en esta versión)

  
- POS físico para tienda con mesón
- Conciliación bancaria automática (manual via export)
- F22 anual completo (solo soporte parcial · contador lo cierra)
- Manejo de RRHH / sueldos / Previred
- Comercio exterior directo (Nexport es intermediario)

# 03 · Entregables esperados

<table>
    <thead><tr><th>#</th><th>Entregable</th><th>Formato</th></tr></thead>
    <tbody>
      <tr><td>1</td><td>Código fuente completo (frontend + backend + IaC)</td><td>Repositorio Git privado</td></tr>
      <tr><td>2</td><td>App desplegada en ambiente productivo</td><td>URL marketplace.smconnection.cl</td></tr>
      <tr><td>3</td><td>Ambiente staging/QA</td><td>URL qas.marketplace.smconnection.cl</td></tr>
      <tr><td>4</td><td>Documentación técnica (architecture · ADRs · README)</td><td>Markdown en repo</td></tr>
      <tr><td>5</td><td>Documentación de usuario (guías operador)</td><td>HTML + PDF</td></tr>
      <tr><td>6</td><td>Suite de tests (unit + integration + e2e)</td><td>En repo · cobertura &gt;60%</td></tr>
      <tr><td>7</td><td>Pipeline CI/CD funcional</td><td>GitHub Actions</td></tr>
      <tr><td>8</td><td>Migration scripts BD versionadas</td><td>SQL en repo</td></tr>
      <tr><td>9</td><td>Adapters de 4 canales funcionales</td><td>Código + tests + docs</td></tr>
      <tr><td>10</td><td>Soporte post-lanzamiento (3 meses)</td><td>SLA según contrato</td></tr>
    </tbody>
  </table>

# 04 · Stack técnico recomendado

<table>
    <thead><tr><th>Capa</th><th>Tecnología</th><th>Justificación</th></tr></thead>
    <tbody>
      <tr><td>Frontend</td><td>Next.js 16 + React 19 + TypeScript</td><td>Stack actual SMC · server components · SSR</td></tr>
      <tr><td>Estilo</td><td>Tailwind v4 + Radix UI</td><td>Stack actual @smc/ui</td></tr>
      <tr><td>Backend</td><td>Next.js API Routes + Server Actions</td><td>Misma stack · monorepo simple</td></tr>
      <tr><td>BD</td><td>Supabase Postgres + RLS</td><td>Multi-tenant nativo · pgvector para IA</td></tr>
      <tr><td>Auth</td><td>Supabase Auth (email + OAuth)</td><td>JWT integrado · roles</td></tr>
      <tr><td>Storage</td><td>Supabase Storage (imágenes · adjuntos)</td><td>Integrado · CDN</td></tr>
      <tr><td>IA</td><td>Groq (Llama 3.3 70B) + OpenRouter fallback</td><td>Cerebro IA · barato · rápido</td></tr>
      <tr><td>Facturación</td><td>Open Factura API (DTE Chile)</td><td>SII compliance turnkey</td></tr>
      <tr><td>Pasarela pagos</td><td>MercadoPago + WebPay Plus</td><td>Coverage Chile máximo</td></tr>
      <tr><td>Couriers</td><td>Chilexpress API + Starken API</td><td>Cobertura nacional</td></tr>
      <tr><td>Deploy</td><td>AWS Amplify (Next.js auto-deploy)</td><td>Stack actual SMC</td></tr>
      <tr><td>Observabilidad</td><td>Sentry + Supabase Logs + LLMOps custom</td><td>Errors + perf + IA tracking</td></tr>
      <tr><td>Testing</td><td>Vitest + Playwright</td><td>Stack actual</td></tr>
      <tr><td>CI/CD</td><td>GitHub Actions</td><td>Estándar SMC</td></tr>
    </tbody>
  </table>

# 05 · Integraciones requeridas

<table>
    <thead><tr><th>Sistema externo</th><th>API</th><th>Uso</th></tr></thead>
    <tbody>
      <tr><td>MercadoLibre Chile</td><td>REST + Webhooks</td><td>Catálogo · órdenes · stock · reputación</td></tr>
      <tr><td>Mercado Público</td><td>REST público</td><td>Licitaciones · ofertas · adjudicaciones</td></tr>
      <tr><td>Open Factura</td><td>REST</td><td>Emisión DTE válidos SII</td></tr>
      <tr><td>SII MIPYME</td><td>REST</td><td>Libro IVA digital · folios</td></tr>
      <tr><td>MercadoPago</td><td>REST + Webhooks</td><td>Pagos D2C · split</td></tr>
      <tr><td>WebPay Plus (Transbank)</td><td>REST</td><td>Pagos D2C tarjetas</td></tr>
      <tr><td>Chilexpress</td><td>REST</td><td>Etiquetas envío · tracking</td></tr>
      <tr><td>Starken</td><td>REST</td><td>Etiquetas envío · tracking</td></tr>
      <tr><td>Groq</td><td>REST</td><td>IA Cerebro · insights · chat</td></tr>
      <tr><td>OpenRouter</td><td>REST</td><td>Fallback IA multi-provider</td></tr>
      <tr><td>Nexport</td><td>Manual/email</td><td>Proveedor (sin API)</td></tr>
    </tbody>
  </table>

# 06 · Criterios de aceptación

<div class="box box-premise">
    <div class="box-title">✅ Para que cada módulo se considere "Done"</div>
    <ul style="margin:0">
      <li>Funcionalidad demostrable en ambiente staging</li>
      <li>Tests automatizados (unit + integration) con cobertura ≥60% del módulo</li>
      <li>Documentación de uso (markdown en repo)</li>
      <li>Sin bugs P1 abiertos · &lt;3 bugs P2 abiertos</li>
      <li>Performance dentro de targets NFR (Doc 03)</li>
      <li>Code review aprobado por al menos 1 dev senior</li>
      <li>Deploy automatizado (CI passing en main)</li>
    </ul>
  </div>

  
## Criterios end-to-end (MVP completo)

  
- Crear SKU master desde 0 · publicar en 2 canales · vender en cada uno · descontar stock cross-canal · emitir DTE · cobrar · generar asiento contable
- Cerrar mes contable con resumen pre-F29 sin Excel paralelo
- Onboarding nuevo operador en &lt;2 horas con doc usuario
- 0 oversell en 100 ventas de prueba simuladas concurrentes

# 07 · Timeline y fases

<table>
    <thead><tr><th>Fase</th><th>Duración</th><th>Entregable</th></tr></thead>
    <tbody>
      <tr><td>F0 · Discovery + Spec final</td><td>2 semanas</td><td>Refinamiento blueprint · ADRs · setup repo</td></tr>
      <tr><td>F1 · Core (Inventory + Auth + Tenants)</td><td>4 semanas</td><td>Catálogo + RLS multi-tenant + login operador</td></tr>
      <tr><td>F2 · Canal MeLi + DTE</td><td>4 semanas</td><td>Primer canal funcional end-to-end</td></tr>
      <tr><td>F3 · Canal D2C + Pagos</td><td>3 semanas</td><td>Storefront propio operativo</td></tr>
      <tr><td>F4 · Canal Mercado Público</td><td>4 semanas</td><td>B2G búsqueda + oferta + adjudicación</td></tr>
      <tr><td>F5 · Canal B2B + Quote</td><td>3 semanas</td><td>CRM ligero + cotizador</td></tr>
      <tr><td>F6 · Finanzas + Contabilidad</td><td>4 semanas</td><td>CxC · CxP · asientos · pre-F29</td></tr>
      <tr><td>F7 · Cerebro IA + Analytics</td><td>3 semanas</td><td>Chat insights · dashboards</td></tr>
      <tr><td>F8 · Hardening + UAT</td><td>3 semanas</td><td>Testing carga · seguridad · UAT operador</td></tr>
      <tr><td>F9 · Soporte post-lanzamiento</td><td>12 semanas</td><td>SLA bug fixing + iteración</td></tr>
    </tbody>
  </table>
  
**Total construcción: ~30 semanas (~7 meses) · soporte 3 meses adicionales.**

# 08 · Presupuesto referencial

<table>
    <thead><tr><th>Concepto</th><th>Modelo</th><th>Referencial CLP</th></tr></thead>
    <tbody>
      <tr><td>Construcción interna (1 dev senior · 7 meses)</td><td>Salario</td><td>$25-35M total</td></tr>
      <tr><td>Construcción vendor externo (equipo 2-3 personas)</td><td>Proyecto fijo</td><td>$50-100M total</td></tr>
      <tr><td>Costo SaaS equivalente como alternativa</td><td>Mensual</td><td>$330K-500K/mes</td></tr>
      <tr><td>Hosting AWS Amplify</td><td>Mensual</td><td>$50-150K/mes</td></tr>
      <tr><td>Supabase Pro</td><td>Mensual</td><td>$25K/mes</td></tr>
      <tr><td>Open Factura (DTE)</td><td>Mensual</td><td>$30K/mes</td></tr>
      <tr><td>Groq IA + OpenRouter</td><td>Variable</td><td>$10-50K/mes</td></tr>
      <tr><td>Domain · SSL · CDN</td><td>Anual</td><td>$50K/año</td></tr>
      <tr><td>**Operación recurrente total**</td><td>Mensual</td><td>**~$140-280K/mes**</td></tr>
    </tbody>
  </table>
  <div class="box box-info">
    <div class="box-title">💡 Comparativa honesta</div>
    <p style="margin:0">Construir custom cuesta más al inicio pero ~50% menos al año 2-3 vs SaaS estilo Defontana+Bsale+Channable+Open Factura ($330K+/mes). Punto de equilibrio: ~12-18 meses.</p>
  </div>

# 09 · Riesgos y mitigaciones

<table>
    <thead><tr><th>Riesgo</th><th>Probabilidad</th><th>Impacto</th><th>Mitigación</th></tr></thead>
    <tbody>
      <tr><td>MeLi app no aprobada en producción</td><td>Alta</td><td>Alto</td><td>Construir canales B2G + B2B primero · MeLi en F2 ya con app aprobada</td></tr>
      <tr><td>Cambio política API MeLi / MP</td><td>Media</td><td>Alto</td><td>Adapter pattern · cambio aislado · regression tests</td></tr>
      <tr><td>Dependencia Nexport (proveedor único)</td><td>Media</td><td>Medio</td><td>Catálogo CRM permite agregar proveedores alternativos rápido</td></tr>
      <tr><td>Carga regulatoria SII cambia</td><td>Baja</td><td>Alto</td><td>Open Factura absorbe cambios · monitoreo trimestral</td></tr>
      <tr><td>Cambio régimen Marketplace SMC SpA</td><td>Alta</td><td>Medio</td><td>App neutra a entidad legal · solo cambia razón social en facturas</td></tr>
      <tr><td>Bugs financieros en producción</td><td>Media</td><td>Crítico</td><td>Tests integración estrictos · audit log · rollback DB versionado</td></tr>
      <tr><td>Equipo dev con knowledge loss</td><td>Media</td><td>Alto</td><td>Documentación obligatoria · pair programming · code review</td></tr>
    </tbody>
  </table>

# 10 · Términos y condiciones

## Propiedad intelectual

  
Todo código, documentación y assets producidos son propiedad exclusiva de Smart Connection SpA (futuro Marketplace SMC SpA). Vendor externo (si aplica) cede derechos completos al pago final.

  
## Confidencialidad

  
Equipo de desarrollo y vendor (si aplica) firman NDA antes de acceder a credenciales o data operativa.

  
## SLA producción

  
- Uptime objetivo: 99.5% mensual (excluye mantenimientos programados)
- Bug P1 (sistema caído · pérdida data · facturación rota): respuesta &lt;2h · resolución &lt;8h
- Bug P2 (módulo crítico afectado): respuesta &lt;1 día · resolución &lt;3 días
- Bug P3-P4: respuesta &lt;1 semana

  
## Términos de pago (si vendor externo)

  
- Hito 1 (cierre F0): 10%
- Hito 2 (cierre F1 Core): 20%
- Hitos 3-7 (cierre cada canal/módulo): 10% c/u (50% total)
- Hito 8 (cierre F8 hardening + UAT): 15%
- Hito 9 (cierre F9 soporte): 5%

  
## Garantía

  
3 meses post-lanzamiento · vendor corrige bugs P1-P2 sin costo adicional · garantía contra defectos.
