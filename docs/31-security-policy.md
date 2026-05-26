---
number: 31
id: security-policy
title: Security Policy
subtitle: "Política de seguridad Marketplace SMC · controles técnicos · procesos · disclosure responsable."
block: Operaciones
author: Security
version: 1.0
date: 2026-05-26
status: 🟢 Activo
prev: 30-templates-legal.html
next: 32-incident-response.html
---

# 01 · Principios

Aplicamos defensa en profundidad. Ningún control único nos cuida.

- **Menor privilegio** · cada rol accede solo a lo necesario
- **Zero trust** · nunca confiar en red interna · siempre validar
- **Fail-secure** · si algo falla · niega antes que permite
- **Auditable** · todo acceso queda logueado
- **Honest disclosure** · si hay breach · avisamos &lt;72h

# 02 · Controles técnicos

| Capa | Control |
|------|---------|
| Tránsito | TLS 1.3 obligatorio · HSTS · cert auto-renovado |
| Storage | AES-256 at rest (Supabase + S3) |
| DB | RLS Postgres por tenant_id · service_role solo servidor |
| Auth | Supabase Auth · JWT · 2FA opcional (obligatorio admins) |
| Secrets | Variables Amplify · NUNCA en repo · rotación trimestral |
| Headers | CSP · X-Frame-Options · X-Content-Type-Options |
| Rate limit | 60 req/min user · 600 req/min IP |
| Backups | PITR Supabase 30 días · daily snapshot S3 90 días |

# 03 · Gestión de accesos

- Onboarding: usuario invitado · MFA obligatorio · provisión por rol
- Offboarding: revocación &lt;1h tras anuncio salida
- Revisión trimestral: lista de usuarios activos · accesos
- Roles definidos: admin · operator · readonly · soporte
- Cuentas compartidas: PROHIBIDAS sin excepción

# 04 · SDLC seguro

- Code review obligatorio · 1 approver mínimo
- Dependabot activado · vulns altas se parchan &lt;7 días
- Pre-commit hooks: bloqueo de .env · secretos · keys
- Hook PreToolUse: bloqueo de rm -rf / · DROP TABLE
- CI: lint + type-check + tests antes de merge

# 05 · Disclosure responsable

Si encuentras una vulnerabilidad:

- Reporta a security@smconnection.cl
- NO la publiques antes de coordinar
- Respondemos &lt;48h · parche planificado por severidad
- Hall of Fame para reportantes (con permiso)
- Sin bug bounty monetario aún (futuro Year 2)

> [!warning] Si está en producción
> No probar sobre cuentas que no sean tuyas · respetar consentimiento · cumplir Ley 19.628.

# 06 · Compliance

- Ley 19.628 Chile (datos personales)
- DTE SII (facturación electrónica)
- Ley 21.521 (Fintec) si activamos pagos en futuro
- GDPR-ready desde diseño (sin certificación aún)
