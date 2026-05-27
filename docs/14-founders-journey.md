---
number: 14
id: founders-journey
title: Founders Journey
subtitle: "Onboarding founders al sistema · primer mes · operación estable · evolución."
block: Founders Operation
author: Founders + Cerebro
version: 2.0
date: 2026-05-26
status: 🟢 Activo
prev: 12-roles-founders.html
next: 15-value-internal.html
---

# 01 · Journey interactivo · onboarding a operación

> [!pipeline] founders-journey
> Cómo los 3 founders adoptan el sistema · semana 1 → operación regular → mejora continua.

# 02 · Hito clave · primer ciclo completo

Día simbólico: primera orden que entra por webhook MeLi · se procesa · se factura · se despacha · todo automático sin intervención manual. Si llegamos a ese hito en mes 1 estamos OK. Si llegamos en mes 3 hay que revisar.

# 03 · Indicadores de adopción saludable

- Camila pasa a usar dashboard bodega &gt;= 5 veces/día (no Excel paralelo)
- Javier pasa a postular Mercado Público desde el sistema (no manual)
- Guillermo pasa a deploy &lt; 1 hora cuando cambia algo (no setup recurrente)
- Los 3 confiamos en el stock real-time sin verificar manual

# 04 · Anti-patrones detectables

> [!anti] Si vemos esto · pausamos y arreglamos antes de seguir
> - Sigue habiendo Excel paralelo de stock · síntoma de no confiar
> - Postulación MP sigue manual · el sistema no la facilita lo suficiente
> - Cualquier founder pasa &gt; 2h/día en operación manual repetitiva
> - Stock real vs stock sistema diverge &gt; 2% en cualquier momento

# 05 · Evolución esperada año por año

- **Y1**: foco aprender · ajustar · estabilizar 3 canales (MeLi · MP · B2B)
- **Y2**: agregar D2C storefront · automatizar lo que aún es manual
- **Y3**: evaluar si hay margen para escalar (más SKUs · más canales · más volumen) con o sin contratación externa

# 06 · Scenario BREAKDOWN · cuando algo se rompe

Realidad operativa: tarde o temprano algo va a fallar. Este journey define **quién decide qué** sin que el sistema se quede paralizado.

## Mapa de incidentes típicos

| Incidente | Detectado por | Primera acción (5 min) | Decision owner | Doc soporte |
|-----------|---------------|------------------------|----------------|-------------|
| Orden duplicada (idempotency falló) | Camila revisando dashboard | Pausar webhook + verificar mkt_idempotency | Guillermo | Doc 32 Incident |
| Stock 0 cuando ya vendí | Sistema (alert auto) | Refund inmediato + email comprador disculpa | Camila | Doc 21 Business |
| SII rechaza DTE | Open Factura retry agota 5x | Manual re-emit con corrección · escalar contador | Camila + Gladys | Doc 37 Runbook |
| Courier no recoge en 24h | Webhook timeout | Llamar courier · re-agendar · si persiste cambiar | Javier | Doc 02 BBP P09 |
| Reclamo MeLi cliente | Camila revisando inbox MeLi | Responder en &lt;2h · refund si error nuestro | Camila | Doc 21 Business |
| MeLi baja reputación a amarillo | Sistema (cron 1h) | Pausar ads inmediato · war room founders | los 3 | Doc 17 §11 |
| Build CI falla &gt;3 commits | Pipeline workflow | Fix forward o rollback · Sentry analiza root cause | Guillermo | Doc 32 Incident |
| Provider IA cae (Groq + Gemini) | Cerebro fallback chain log | Auto-fallback DeepSeek · si también cae mensaje UX | Guillermo | Doc 13 §17 |
| Supabase región sa-east-1 down | Sentry + Status page | Status page propio · esperar Supabase + comunicar | Guillermo | Doc 37 DR Plan |
| Founder enfermo &gt;3 días | los otros 2 | Backup roles temporal · doc 12 roles mapea | los 3 | Doc 12 Roles |

## Reglas anti-pánico

> [!info] No es emergencia salvo que sea P0
> P0 = sangrado de dinero o reputación AHORA (oversell · DTE rechazo · MeLi amarillo). Resto se prioriza en review semanal.

## Cuándo escalar entre founders

```
Acción afecta a 1 cliente   → resuelve el founder que detectó
Acción afecta > 5 clientes  → consulta a otros 2 antes de actuar
Acción irreversible         → SIEMPRE consulta · sin excepción
Acción legal/financiera     → siempre 3 firmas + Compliance/Controller
```

## Post-mortem cada incidente P0/P1

Después de cerrar un incidente P0 o P1 · sesión 30 min · formato:
- Qué pasó (timeline objetivo)
- Por qué (root cause · NO blame)
- Cómo lo detectamos
- Cómo se evita repetir (acción concreta · dueño · fecha)
- Cómo lo arreglaríamos más rápido la próxima vez

Output: row en `mkt_postmortems` + actualizar Doc 32 Incident Response si patrón nuevo.
