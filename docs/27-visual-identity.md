---
number: 27
id: visual-identity
title: Visual Identity
subtitle: "Logo · paleta · tipografía · iconografía · grid · ejemplos de uso · do/don't visuales."
block: Marca
author: Functional-Lead
version: 1.0
date: 2026-05-26
status: 🟢 Activo
prev: 26-tone-of-voice.html
next: 28-terms-of-service.html
---

# 01 · Logo

El logo de Marketplace SMC se construye sobre el wordmark **Smart Connection** con un punto teal (◆) como signo distintivo del holding.

- Versión principal: wordmark blanco sobre fondo dark (`#0F172A`)
- Versión secundaria: wordmark teal sobre fondo claro (`#FFFFFF`)
- Iso: solo el diamante ◆ teal · para favicons · avatars · packaging chico
- Lockup vertical: wordmark arriba · "Marketplace" abajo en JetBrains Mono
- Lockup horizontal: wordmark · separador vertical · "Marketplace"

> [!warning] Espacio de respiro
> Mínimo `1x` (donde `x` = altura de la M de Smart) alrededor del logo. NUNCA pegarlo a borde · texto · imagen.

# 02 · Paleta visual interactiva

> [!swatch] paleta-smc
> Click en cualquier swatch copia el hex al portapapeles · cada token mapea a una variable CSS oficial usada en todo el banco y la app.

# 03 · Reglas de uso de la paleta

- Mobile-first: contraste WCAG AA mínimo en cuerpo de texto (4.5:1)
- Dark surfaces (`smc-ink-900` · `smc-ink-700`) NO usar como fondo de párrafos largos
- Teal (`smc-primary` `#00C1C1`) es accent · NO fondo full · sobre fondo claro
- Semánticos (success/warning/danger/info) solo para señalización · jamás decoración
- Colores de bloque (com/biz/marca/legal/sec/gov) solo en marcadores del banco

# 04 · Tipografía

| Rol | Familia | Pesos | Cuándo |
|-----|---------|-------|--------|
| Display · Titulares | Inter | 800 · 700 | Cover · h1 · números KPI |
| Body | Inter | 400 · 500 · 600 | Párrafos · listas · tablas |
| Mono · Código | JetBrains Mono | 400 · 600 | Code blocks · slugs · IDs |

Escala tipográfica (rem, mobile-first):

- Display XL: 5.5rem (88px) · cover hero · letter-spacing -3px
- Display L: 2.0rem (32px) · section titles · letter-spacing -1px
- H1: 1.625rem (26px) · doc body
- H2: 1.25rem (20px)
- Body: 0.9375rem (15px) · line-height 1.6
- Caption: 0.75rem (12px) · letter-spacing 1.5px uppercase

# 05 · Iconografía

- Set primario: Lucide React (consistente · tree-shake · OSS)
- Tamaños canónicos: 16px · 20px · 24px · 32px
- Stroke width: 1.75 (estándar Lucide)
- Color: hereda del texto contenedor (`currentColor`)
- NO mezclar Lucide con Material/Heroicons · pick one

> [!info] Iconos custom
> Si se necesita icono no disponible en Lucide · diseñar en SVG con stroke 1.75 · viewBox 24x24 · path optimizado · sin fills.

# 06 · Grid y espaciado

Sistema 8pt:

- Base unit: 8px
- Espaciados permitidos: 4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 80 px
- Container max-width: 1200px desktop · padding lateral 72px
- Mobile: padding lateral 24px · 4 columnas
- Tablet: padding lateral 48px · 8 columnas
- Desktop: 12 columnas · gutter 24px

# 07 · Componentes branded

| Componente | Estilo SMC |
|------------|------------|
| Hero | Gradient `#0F172A → #0F766E → #00C1C1` · radial overlay |
| Cards | Border-top 4px color bloque · radius 14px · hover lift -2px |
| Botones primary | Bg `#00C1C1` · texto blanco · radius 10px · hover dark |
| Botones secondary | Outline `#00C1C1` · texto teal · transparente |
| Badges | Pill radius · 11px caps · letter-spacing 1.5px |
| Boxes premise/anti | Borde 4px lateral · bg leve color · padding 24px |

# 08 · Do · Don't

Do:

- Usar la paleta exacta · jamás colores aproximados
- Mantener jerarquía clara: Display → H1 → H2 → Body
- Espacio en blanco generoso · respira > rellena
- Teal (`#00C1C1`) como accent · NO como fondo full

Don't:

- Mezclar logos antiguos de SMC con el nuevo
- Aplicar drop shadows fuertes (lift sutil OK)
- Texto sobre fotos sin overlay legibilidad
- Usar comic sans · papyrus · ni broma

# 09 · Ejemplos de uso

| Material | Composición |
|----------|-------------|
| Email comercial | Header teal · CTA `#00C1C1` · footer con disclaimers |
| Pitch deck slide | Bg dark · titular Display L · 1 KPI grande accent |
| Doc legal (este banco) | Cover dark · cuerpo light · acento por bloque |
| Banner LinkedIn | Iso ◆ teal · wordmark blanco · gradient diagonal |
| Producto app | Sidebar dark · canvas light · CTA teal |
