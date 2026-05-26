---
number: 29
id: privacy-policy
title: Privacy Policy
subtitle: "Política de privacidad y cookies · Ley 19.628 Chile · GDPR-friendly."
block: Legal
author: Compliance
version: 1.0
date: 2026-05-26
status: 🟢 Activo
prev: 28-terms-of-service.html
next: 30-templates-legal.html
---

# 01 · Datos que recolectamos

Recolectamos solo lo necesario para prestar el servicio:

| Categoría | Ejemplos | Por qué |
|-----------|----------|---------|
| Identificación | RUT · razón social · email · teléfono | Crear cuenta · facturar |
| Comerciales | Productos · órdenes · clientes B2B/B2G | Operar plataforma |
| Financieros | Cuentas bancarias · facturas · pagos | Cobranza · contabilidad |
| Técnicos | IP · user-agent · cookies · logs | Seguridad · análisis |
| Comunicaciones | Emails enviados · soporte chat | Atención cliente |

# 02 · Bases legales (Ley 19.628)

- **Consentimiento** · datos voluntariamente provistos al registrarse
- **Contrato** · datos necesarios para prestar servicio acordado
- **Obligación legal** · datos requeridos por SII · Banco Central
- **Interés legítimo** · seguridad · prevención fraude

# 03 · Compartir con terceros

NUNCA vendemos tus datos. Compartimos SOLO con proveedores estrictamente necesarios:

- Supabase (base de datos · región sa-east-1)
- AWS Amplify (hosting app)
- Open Factura (emisión DTE)
- MercadoPago / WebPay (pasarelas pago)
- Groq (IA · sin datos sensibles · solo prompts agregados)
- Chilexpress / Starken (logística · solo dirección entrega)

# 04 · Cookies

Usamos cookies para:

- **Sesión**: mantenerte logueado (necesaria)
- **Preferencias**: idioma · zona horaria
- **Analytics**: PostHog · uso anonimizado del producto
- NO usamos cookies de tracking publicitario terceros

> [!info] Banner cookies
> Al ingresar primera vez · banner pide consentimiento · podés rechazar cookies no esenciales y la plataforma sigue funcionando.

# 05 · Tus derechos (ARCO + Habeas Data)

- **Acceso**: pedir copia de tus datos en JSON · entrega &lt;30 días
- **Rectificación**: corregir datos incorrectos
- **Cancelación**: pedir eliminación · respetando obligaciones SII (8 años custodia tributaria)
- **Oposición**: bloquear ciertos usos (ej: marketing)

Ejercer derechos: email a privacy@smconnection.cl con tu RUT.

# 06 · Retención de datos

| Tipo | Retención |
|------|-----------|
| Cuenta activa | Mientras dure relación contractual |
| Facturas y DTE | 8 años (obligación SII) |
| Logs técnicos | 90 días |
| Backups | 30 días point-in-time recovery |
| Datos eliminados a pedido | Borrado en 30 días salvo retención legal obligatoria |

# 07 · Seguridad

- Cifrado en tránsito (TLS 1.3) y at rest (AES-256)
- Row Level Security (RLS) Postgres por tenant
- 2FA disponible para operadores
- Logs de acceso auditados

> [!warning] Limitaciones honestas
> Ningún sistema es 100% seguro. Hacemos best-effort y notificamos breaches dentro de 72h según Ley 19.628.
