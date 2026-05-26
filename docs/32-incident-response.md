---
number: 32
id: incident-response
title: Incident Response Plan
subtitle: "Cómo respondemos cuando algo se rompe · severidades · roles · runbook genérico · postmortem."
block: Operaciones
author: Security
version: 1.0
date: 2026-05-26
status: 🟢 Activo
prev: 31-security-policy.html
next: 33-prd-template.html
---

# 01 · Severidades

| Sev | Definición | Tiempo respuesta | Ejemplo |
|-----|-----------|------------------|---------|
| SEV1 | App caída · usuarios no entran · data corruption | &lt;15 min | Supabase down · 500 prod en login |
| SEV2 | Feature crítica rota · workaround posible | &lt;1h | Checkout falla en 1 canal · sync MeLi roto |
| SEV3 | Bug visible · sin impacto crítico | &lt;1 día | Tipo en email · gráfico no carga |
| SEV4 | Bug menor · cosmético | &lt;1 semana | Espaciado mal · color off |

# 02 · Roles durante incidente

- **Commander**: lidera · decide · es el único que habla a clientes
- **Operator**: ejecuta · hace rollback · revisa logs
- **Communicator**: actualiza status page · responde tickets
- **Scribe**: anota timeline · acciones · evidencias para postmortem

Para Marketplace SMC inicial: 1 persona puede llevar 2-3 roles · ideal 1 persona = 1 rol.

# 03 · Runbook genérico

```
1. DETECTAR
   - Alerta (CloudWatch · Sentry · status page)
   - Reporte usuario en soporte
   - Detección proactiva monitoring

2. TRIAGE
   - Asignar severidad (tabla 01)
   - Activar Commander
   - Si SEV1/SEV2: notificar equipo en canal #incidents

3. CONTENER
   - Rollback si deploy reciente (último merge a main)
   - Disable feature flag si feature específica
   - Aislar tenant si data corruption (RLS)

4. INVESTIGAR
   - Logs Amplify · Supabase · Sentry
   - Reproducir en QAS si posible
   - Identificar root cause

5. REMEDIAR
   - Patch + deploy
   - Verificar fix en prod
   - Anunciar resolución

6. POSTMORTEM
   - &lt;48h después
   - Blameless: foco en sistema · no personas
   - Acciones de prevención con dueño y fecha
```

# 04 · Comunicación durante SEV1/SEV2

- Status page actualizado &lt;5 min
- Email a clientes afectados &lt;15 min
- Updates cada 30 min hasta resolver
- Post-resolución: email confirmando + ETA postmortem

> [!info] Tone honesto
> "Estamos investigando" es mejor que silencio. NUNCA prometer ETA que no se va a cumplir.

# 05 · Template postmortem

```
# Postmortem · [Incidente] · [Fecha]

## Resumen ejecutivo
- Severidad: SEV?
- Duración total: ?h ?min
- Clientes afectados: ?
- Impacto: pérdida ventas · downtime · data loss

## Timeline (UTC-3 Santiago)
- 14:00 · Deploy v1.2.3
- 14:15 · Alerta CloudWatch 5xx
- ...

## Root cause
[análisis técnico claro · sin asignar culpa]

## Lo que salió bien
- [3 cosas mínimo]

## Lo que salió mal
- [no más de 5 · accionables]

## Acciones (cada una con dueño + fecha)
- [ ] Acción 1 · @owner · 2026-MM-DD
- [ ] Acción 2 · @owner · 2026-MM-DD
```

# 06 · Práctica continua

- Game day cada 2 meses: simular SEV1 · cronometrar respuesta
- Chaos engineering ligero · matar 1 servicio en QAS
- Review trimestral del playbook · actualizar contactos · runbooks
