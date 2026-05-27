---
number: 19
id: uat
title: UAT · User Acceptance Testing
subtitle: "Plan integral de pruebas · 24 casos por CU · 5 escenarios end-to-end · criterios sign-off por fase."
block: Producto Técnico
author: User-QAS + Architect + Cerebro
version: 1.0
date: 2026-05-27
status: 🟡 Draft · evoluciona durante construcción
prev: 18-plan-ejecucion.html
next: 21-business-comercio.html
---

# 01 · Premisa

Doc 19 define el **plan integral de pruebas** que valida que Marketplace SMC cumple lo especificado en Doc 11 Funcional + Doc 13 Técnica antes de cierre de cada fase del Doc 18 Plan Ejecución.

> [!info] UAT vs unit tests vs E2E
> Unit + integration tests viven en el repo (Vitest · 70%+ cobertura) · UAT corre en QAS antes de promote a PROD · enfoque founder-side · valida workflows reales no funciones aisladas.

# 02 · Estrategia · 4 niveles de testing

| Nivel | Owner | Cuándo | Tool | Output |
|-------|-------|--------|------|--------|
| Unit | dev | en cada commit · pre-push | Vitest | Coverage report |
| Integration | dev + Pipeline | en CI · main | Vitest + Supabase test DB | Suite verde |
| E2E automation | User-QAS | nightly QAS | Playwright | Reporte HTML + screenshots |
| UAT (este doc) | 3 founders | fin de cada sprint | Manual + checklist | Sign-off sheet |

# 03 · Ambientes

| Ambiente | URL | Datos | Quién testea |
|----------|-----|-------|-------------|
| Local | localhost:3000 | seed minimal | Developer |
| QAS | qas.marketplace.smconnection.cl | mirror PROD - 30 días | Founders + auto Playwright |
| PROD | marketplace.smconnection.cl | datos reales | smoke test post-deploy |

# 04 · Criterios universales de cada CU (pre-flight)

Cada caso de prueba UAT debe verificar **antes** de marcar como pass:

| # | Criterio | Cómo verificar |
|---|----------|----------------|
| C-1 | Endpoint responde 200 · 4xx · 5xx según corresponda | Network tab DevTools |
| C-2 | Tiempo respuesta dentro de budget (Doc 13 §15) | DevTools timing |
| C-3 | DB tablas modificadas correctamente | Supabase SQL editor |
| C-4 | Auditoría INSERT en mkt_api_logs / mkt_audit_logs | Query verificación |
| C-5 | Sentry sin error nuevo · sin warnings | Sentry dashboard QAS |
| C-6 | PostHog event registrado si aplica | PostHog activity |
| C-7 | UI feedback visible (loading · success · error) | Visual inspection |
| C-8 | Mobile responsive 375px · 768px · 1280px+ | Chrome DevTools device toolbar |
| C-9 | Accesibilidad keyboard nav | Tab + Enter sin mouse |
| C-10 | RLS bloquea acceso cross-tenant | Cambiar JWT + reintentar |

# 05 · Casos UAT por CU · Fase 1 Reputación (Q4-26 → Q1-27)

## CU-01 · Onboarding founders + 2FA

| Test ID | Acción | Resultado esperado |
|---------|--------|---------------------|
| UAT-01-A | Camila crea cuenta con email + password fuerte | Email confirmación enviado · status='pending_2fa' |
| UAT-01-B | Camila completa verify TOTP con Authenticator | Status='active' · puede acceder dashboard |
| UAT-01-C | Camila intenta login sin 2FA | Bloqueo · prompt código TOTP |
| UAT-01-D | Reset password con email | Email link recibido en 30s · link expira 1h |
| UAT-01-E | 3 founders cuentas creadas + 2FA activo | Query: SELECT count(*) FROM auth.users WHERE mfa_enabled = true = 3 |

## CU-02 · Crear producto + foto pro propia

| Test ID | Acción | Resultado esperado |
|---------|--------|---------------------|
| UAT-02-A | Camila sube 1 producto · SKU · 1 foto profesional propia · precio | Producto guardado · validation BR-001 ok (foto >800px) |
| UAT-02-B | Intentar subir foto stock genérica de proveedor | BR-001 bloquea · mensaje claro |
| UAT-02-C | Editar precio · stock · descripción | UPDATE · pg_notify('inventory_changed') dispara |
| UAT-02-D | Eliminar producto sin ventas | DELETE soft (deleted_at) · queda en histórico |
| UAT-02-E | Eliminar producto con ventas históricas | Bloqueo · solo unpublish posible |

## CU-03 · Publicar a Mercado Libre

| Test ID | Acción | Resultado esperado |
|---------|--------|---------------------|
| UAT-03-A | Producto creado · click "Publicar a MeLi" | POST /items a MeLi · external_id guardado |
| UAT-03-B | Verificar listado aparece en cuenta MeLi del founder | mercadolibre.cl muestra producto |
| UAT-03-C | Cambiar stock localmente · verificar sync | MeLi muestra nuevo stock en &lt;30s |
| UAT-03-D | OAuth token expira · refresh automático | Cron 6h refresca · sin intervención founder |
| UAT-03-E | MeLi rechaza publicación (categoría inválida) | Error UI claro · sugerencia corrección |

## CU-04 · Recibir venta MeLi + procesar

| Test ID | Acción | Resultado esperado |
|---------|--------|---------------------|
| UAT-04-A | Webhook MeLi POST /api/webhooks/meli (orden nueva) | HMAC verify OK · INSERT mkt_orders |
| UAT-04-B | Reservar stock · UPDATE inventory.reserved | SELECT FOR UPDATE evita oversell |
| UAT-04-C | Webhook duplicado (idempotency key igual) | Return cached · NO segundo insert |
| UAT-04-D | Listar órdenes en dashboard | UI muestra 1 orden · status 'created' |
| UAT-04-E | Aceptar orden · cambia status a 'accepted' | UPDATE + audit_log |

## CU-05 · Emitir DTE + label courier + despachar

| Test ID | Acción | Resultado esperado |
|---------|--------|---------------------|
| UAT-05-A | Orden 'accepted' → click "Emitir factura" | Open Factura API · DTE 39 generado · folio SII guardado |
| UAT-05-B | Orden con RUT empresa (B2B) → DTE 33 (factura) | DTE 33 con timbre electrónico SII |
| UAT-05-C | Cotizar courier · 3 opciones (Chilexpress · Starken · ambos) | Mostrar precio + ETA por opción |
| UAT-05-D | Generar etiqueta PDF · descargable | PDF >0 bytes · QR escaneable |
| UAT-05-E | Webhook courier "in_transit" · "delivered" | UPDATE status + email comprador |

## CU-06 · Cerebro chat · primer mensaje

| Test ID | Acción | Resultado esperado |
|---------|--------|---------------------|
| UAT-06-A | Camila escribe "¿cuánto vendí esta semana?" | SSE stream &lt;600ms first token · respuesta basada en data real |
| UAT-06-B | Pregunta sin contexto suficiente | Cerebro pide aclaración · NO inventa |
| UAT-06-C | Founder #61 mensaje del día (rate limit) | Bloqueo · mensaje "límite diario alcanzado" |
| UAT-06-D | Provider Groq cae · fallback Gemini | Respuesta sigue · log mkt_ai_logs.fallback_used=true |
| UAT-06-E | 3 founders consultan simultáneo | Sin colisión · responses correlated por user_id |

# 06 · Casos UAT · Fase 2 Escala (Q1-27 → Q2-27)

## CU-07 · Sistema Oportunidades (v5 sin LLM)

| Test ID | Acción | Resultado esperado |
|---------|--------|---------------------|
| UAT-07-A | Cron diario 6am · scoring oportunidades | INSERT mkt_opportunities con score 1-100 |
| UAT-07-B | Camila ve top 10 ordenadas score DESC | UI lista clara · filtros por canal |
| UAT-07-C | Click oportunidad → ve 6 señales detail | Modal con breakdown de cada señal |
| UAT-07-D | Descartar oportunidad | Status='dismissed' · NO aparece más |
| UAT-07-E | Convertir oportunidad → acción (publicar SKU sugerido) | Producto pre-poblado · UI siguiente paso |

## CU-08 · Storefront D2C (Y2)

| Test ID | Acción | Resultado esperado |
|---------|--------|---------------------|
| UAT-08-A | Cliente externo navega marketplace.smconnection.cl | LCP &lt;2.5s · catálogo cargado ISR |
| UAT-08-B | Agregar al carrito + checkout WebPay | Pago exitoso · DTE emitido · email confirmación |
| UAT-08-C | Stock=0 cuando intenta comprar | Bloqueo · mensaje "agotado" |

## CU-09 · Ads multicanal automation

| Test ID | Acción | Resultado esperado |
|---------|--------|---------------------|
| UAT-09-A | Activar campaña Mercado Ads · presupuesto $10K | POST a MeLi Ads · campaign activa |
| UAT-09-B | ROAS &lt;1.5 por 7 días · alerta auto | Notification founder · sugerencia pausa |
| UAT-09-C | Pausar campaña · verificar gasto detiene | MeLi API confirma status='paused' |

# 07 · Casos UAT · Fase 3 Diversificación (Q2-27 → Q3-27)

## CU-10 · Mercado Público B2G

| Test ID | Acción | Resultado esperado |
|---------|--------|---------------------|
| UAT-10-A | Cron 8am · sync licitaciones MP | INSERT mkt_mp_licitaciones · filtradas por categoría |
| UAT-10-B | Cerebro sugiere top 5 afines catálogo SMC | Lista con scoring + razones |
| UAT-10-C | Javier postula con template Cerebro generado | PDF + JSON enviado a MP API · ticket auth |
| UAT-10-D | Webhook adjudicación recibido | UPDATE + workflow despacho institucional |
| UAT-10-E | DTE 33 emitido a institución pública | Folio SII · pago 30-60 días tracked |

## CU-11 · B2B portal RFQ

| Test ID | Acción | Resultado esperado |
|---------|--------|---------------------|
| UAT-11-A | Cliente B2B crea cuenta con API key invitada | Cuenta + portal acceso restringido |
| UAT-11-B | Crear RFQ con 10 SKUs · cantidades | INSERT mkt_b2b_rfq · founder recibe alerta |
| UAT-11-C | Founder responde cotización custom | Cliente recibe email · puede aprobar/rechazar |
| UAT-11-D | Aprobar cotización · firma HMAC | Workflow despacho dispara |

## CU-12 · Dropshipping flow completo

| Test ID | Acción | Resultado esperado |
|---------|--------|---------------------|
| UAT-12-A | Sync catálogo proveedor dropship | INSERT productos con is_dropship=true |
| UAT-12-B | Cliente compra SKU dropship en MeLi | OC propagada al proveedor automáticamente |
| UAT-12-C | Proveedor stock=0 cuando llega OC | Refund automático + email comprador |
| UAT-12-D | Proveedor despacha · webhook tracking | UPDATE order + email comprador |
| UAT-12-E | SKU dropship vende >$5K/mes 2 meses | Cerebro alerta · sugiere migrar a stock local |

# 08 · Casos UAT · Fase 4 Consolidación (Q3-27+)

## CU-13 · Conciliación financiera mensual

| Test ID | Acción | Resultado esperado |
|---------|--------|---------------------|
| UAT-13-A | Cron 1ro mes · POST /api/cron/conciliacion | Matching pagos vs DTE · diferencias detectadas |
| UAT-13-B | Reporte enviado a CONTROLLER + 3 founders | Email con tabla discrepancias |
| UAT-13-C | F29 prep mensual · datos compatibles SII | Export JSON listo upload |

## CU-14 · Multi-tenant readiness (Y3 anticipación)

| Test ID | Acción | Resultado esperado |
|---------|--------|---------------------|
| UAT-14-A | Crear tenant test_b · verificar isolation RLS | Founder tenant_a NO ve data tenant_b |
| UAT-14-B | Crear órdenes en ambos tenants paralelo | Postgres separado lógicamente · query con JWT correcto |

# 09 · Escenarios end-to-end · 5 happy paths

> [!hla] funnel-uat
> Mapa visual de los 5 escenarios E2E críticos · cada uno con sus CU encadenados.

## E2E-1 · Venta MeLi (stock local) ciclo completo
CU-02 → CU-03 → CU-04 → CU-05 · 3 días · target: founder click 5 veces total

## E2E-2 · Venta dropshipping ciclo completo
CU-12-A → CU-12-B → CU-12-D · 5-7 días · target: 0 intervención manual

## E2E-3 · Adjudicación Mercado Público
CU-10-A → CU-10-B → CU-10-C → CU-10-D → CU-10-E · 7-30 días según licitación

## E2E-4 · Cliente B2B RFQ → pedido
CU-11-A → CU-11-B → CU-11-C → CU-11-D · 1-3 días

## E2E-5 · Storefront D2C compra externa
CU-08-A → CU-08-B · 5 minutos cliente externo

# 10 · Performance + load testing

| Test | Tool | Target | Trigger fail |
|------|------|--------|--------------|
| API products list 1K items | k6 | p95 &lt;350ms | &gt;800ms |
| 100 órdenes concurrentes MeLi webhook | k6 | sin oversell · sin duplicate | 1+ oversell |
| Cerebro chat 50 sesiones simultáneas | k6 + manual | first token &lt;600ms p95 | &gt;2s |
| RSC streaming 100 founders dashboard | Lighthouse CI | LCP &lt;2.5s | &gt;4s |

# 11 · Security testing

| Test | Tool | Esperado |
|------|------|----------|
| OWASP ZAP scan QAS | ZAP CLI | 0 high · 0 medium |
| SQL injection en todos los endpoints | Manual + sqlmap | RLS bloquea · NO error 500 |
| Auth bypass tentado (manipular JWT) | jwt.io + manual | 401 siempre |
| Rate limit honrado | k6 burst 100 req/min | 429 después de 60 |
| CORS origins restrictivos | curl + headers | Sin Access-Control-Allow-Origin: * |
| Secrets en client bundle | npm run build + grep | 0 service_role · 0 API keys |

# 12 · Accesibilidad WCAG 2.2 AA

| Test | Tool | Esperado |
|------|------|----------|
| Lighthouse a11y score | Chrome DevTools | &gt;90 |
| Keyboard navigation completa | Manual | Tab cubre TODO · sin keyboard traps |
| Screen reader VoiceOver Mac | VoiceOver | Labels descriptivos · sin "button button" |
| Contraste color | axe-core | AA en todos los textos |
| Touch targets mobile | Manual 375px | Botones &gt;44px altura |

# 13 · Criterios sign-off por fase

## Fase 1 Reputación Q4-26 → Q1-27

✓ Sign-off cuando:
- 100% UAT-01 a UAT-06 verde
- E2E-1 pasa con 10 órdenes consecutivas
- Lighthouse a11y &gt;90
- 0 errores P0 abiertos en backlog
- Backup PITR confirmado funcional (test restore)
- 3 founders firmaron checklist

## Fase 2 Escala Q1-27 → Q2-27

✓ Sign-off cuando:
- UAT-07 + UAT-08 + UAT-09 verde
- Performance test 100 órdenes/hora sin degradación
- ROAS dashboard usable por Camila sin ayuda
- Backup + DR plan probado (Doc 37)

## Fase 3 Diversificación Q2-27 → Q3-27

✓ Sign-off cuando:
- UAT-10 + UAT-11 + UAT-12 verde
- 1 adjudicación MP real procesada end-to-end
- 1 cliente B2B real cerrado en portal
- Dropshipping con &gt;1 proveedor real funcionando

## Fase 4 Consolidación Q3-27+

✓ Sign-off cuando:
- UAT-13 + UAT-14 verde
- Conciliación mensual real cerrada sin diferencias inexplicadas
- Multi-tenant scaffold testeado (sin migrar aún)

# 14 · Defect lifecycle

```
DEFECTO DETECTADO durante UAT
     ↓
Founder reporta vía dashboard "Reportar issue"
     ↓
GitHub Issue creado auto · labels [bug · priority · area]
     ↓
Triage diario (Architect + dev asignado)
     ↓
Priority:
  P0 → blocker · fix HOY · QAS deploy nuevo
  P1 → fix sprint actual · QAS antes sign-off
  P2 → backlog · próximo sprint
  P3 → nice-to-have · evaluable
     ↓
PR + tests · approval Architect
     ↓
Re-test UAT específico
     ↓
Mark verde + close issue
```

# 15 · UAT regression suite (Y2+)

Cada vez que se cierra una fase · sus UAT pasan a Playwright nightly automation:
- Fase 1 → Playwright suite-fase-1.spec.ts (runs nightly QAS)
- Si falla → notification User-QAS + alerta Sentry incident
- Bloquea promote a PROD si suite roja

# 16 · Métricas UAT trackeadas

| Métrica | Cómo medir | Target |
|---------|-----------|--------|
| % UAT pass first try | Sign-off sheet | &gt;80% |
| Bugs P0 escaped a PROD | post-deploy 30d | &lt;2 por fase |
| Tiempo defecto reportado → fix | GitHub Issue timestamps | P0 &lt;24h · P1 &lt;1 semana |
| Cobertura UAT vs CU | matriz | 100% CU mapeados |
| Lighthouse score promedio | CI Lighthouse | &gt;90 a11y · &gt;85 performance |

# 17 · Próximos pasos

1. ✅ Doc 19 v1 · plan completo
2. ⏭️ Durante Sprint 1 Q4-26 · empezar a marcar UAT-01 a UAT-06
3. ⏭️ User-QAS prepara Playwright skeleton para automation Fase 2+
4. ⏭️ Cada cierre fase → sign-off sheet firmado por 3 founders
