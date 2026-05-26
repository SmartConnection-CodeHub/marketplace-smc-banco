---
number: 37
id: runbook-dr-plan
title: Runbook & DR Plan
subtitle: "Operación día a día Marketplace SMC + disaster recovery · RTO/RPO · escenarios típicos."
block: Operaciones
author: INFRA-OPS
version: 1.0
date: 2026-05-26
status: 🟢 Activo
prev: 36-stakeholder-map.html
next: 38-onboarding-dev.html
---

# 01 · Objetivos de recuperación

| Métrica | Target | Significado |
|---------|--------|-------------|
| RTO | &lt;4h | Tiempo máx restaurar servicio |
| RPO | &lt;1h | Datos máx que podemos perder |
| Disponibilidad | 99.5% | ~3.6h downtime/mes aceptable |
| MTTR SEV1 | &lt;1h | Tiempo medio resolver críticos |

# 02 · Operación diaria

```
DIARIO (cron 8am)
- Backup Supabase verify (alerta si falla)
- Sync Mercado Público últimas oportunidades
- Refresh MeLi tokens (cron expiran 6h)
- Review alertas overnight

SEMANAL (lunes)
- Review métricas dashboard (uptime · errores · latencia)
- Update dependencias menores (patch versions)
- Triage tickets soporte abiertos

MENSUAL
- Game day · simular SEV1 (rotar escenario)
- Review costos AWS · Supabase · ajustar
- Revisar Risk Register

TRIMESTRAL
- Rotación secretos (API keys · DB passwords)
- Restore drill (probar restore real desde backup)
- Audit accesos · revocar inactivos
```

# 03 · Escenarios DR interactivos

> [!pipeline] dr-scenarios
> Cada escenario DR con sus etapas y pasos clave. Click en cualquier paso ve el detalle (stack · errores comunes · acciones específicas). Cambiá de escenario con el selector arriba.

# 04 · Escenarios DR (referencia detallada)

## E1 · Supabase region down

- Probabilidad: Baja · Impacto: Total
- Detección: alertas Supabase + CloudWatch 5xx
- Acción:
  1. Verificar status.supabase.com
  2. Si confirmado: activar página estática mantención
  3. Notificar clientes en &lt;15 min
  4. Esperar resolución upstream (no hay self-hosted backup)
- Mejora futura: read-replica cross-region · daily snapshot a S3 propio

## E2 · Deploy malo en main

- Probabilidad: Media · Impacto: Alto
- Detección: alertas Sentry · spike 5xx · usuarios reportan
- Acción:
  1. Identificar commit (git -C path log)
  2. Rollback Amplify a build anterior
  3. Crear hotfix branch
  4. Postmortem en 48h

## E3 · DB corruption / migración mala

- Probabilidad: Baja · Impacto: Catastrófico
- Detección: queries fallan · data inconsistente
- Acción:
  1. Bloquear writes inmediato
  2. Identificar PITR timestamp seguro
  3. Restore a snapshot anterior (perdemos datos desde ese punto)
  4. Notificar clientes data afectada · ofrecer recuperar de fuentes (MeLi · MP)

## E4 · API key comprometida

- Probabilidad: Media · Impacto: Alto
- Detección: actividad anómala · spike costo · alerta proveedor
- Acción:
  1. Revocar key comprometida inmediato
  2. Generar nueva en proveedor
  3. Actualizar variable Amplify (sin restart manual)
  4. Audit logs · ver qué hizo el atacante
  5. Notificar clientes si data afectada

## E5 · MeLi PolicyAgent bloqueo cuenta

- Probabilidad: Alta · Impacto: Crítico (revenue)
- Detección: 403 sistemático en endpoints MeLi
- Acción:
  1. Abrir ticket MeLi developer support inmediato
  2. Mover features no-MeLi adelante (D2C · MP · B2B)
  3. Comunicar a clientes operadores afectados
  4. Plan B: integración pública no-DPP con scope limitado

# 04 · Test de restore (obligatorio trimestral)

- Crear environment QAS-DR aislado
- Restaurar último backup en QAS-DR
- Validar:
  - App levanta
  - Login funciona
  - Datos consistentes (sample 10 tenants)
  - Last backup &lt;1h antes del restore
- Documentar resultado · tiempo total · issues encontrados

# 05 · Contactos críticos

- AWS support: console.aws.amazon.com/support
- Supabase support: support@supabase.io
- MeLi developer: developers.mercadolibre.cl
- Status pages a monitorear: status.aws.amazon.com · status.supabase.com · status.mercadolibre.com.ar
