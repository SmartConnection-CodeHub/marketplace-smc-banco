# Onboarding · Editar el Banco Marketplace SMC

Guía rápida para Javier · cómo editar y crear documentos del banco usando markdown + Python.

---

## 1. Qué es el banco

`marketplace-smc-banco` es un repo público con ~37 documentos del proyecto Marketplace SMC. Cada doc es un **HTML branded** generado a partir de un **markdown editable** (`docs/*.md`). El HTML se publica automático en GitHub Pages:
```
https://smartconnection-codehub.github.io/marketplace-smc-banco/
```

**Idea clave:** vos NO editás HTML. Editás el `.md` con texto plano · corrés el script Python · se regenera el HTML.

---

## 2. Setup una sola vez

```bash
# Clonar el repo
git clone https://github.com/SmartConnection-CodeHub/marketplace-smc-banco
cd marketplace-smc-banco

# Verificar Python 3 instalado (debería estar en Mac/Linux)
python3 --version

# Verificar git funciona
git status
```

Editor recomendado: **VS Code** (cualquier editor de texto sirve).

---

## 3. Estructura de un .md

Cada doc tiene 2 partes: **frontmatter YAML** (metadata arriba) + **body markdown** (contenido abajo).

```markdown
---
number: 17
id: estrategia-y1
title: Estrategia Y1
subtitle: "Reputation First · 4 fases · hito 10 ventas verdes."
block: Estrategia
author: Founders + Cerebro
version: 1.0
date: 2026-05-27
status: 🟢 Activo
prev: 16-comparativa-tools.html
next: 18-onboarding.html
---

# 01 · Primera sección

Texto markdown normal. **Negrita** con `**texto**` · *itálica* con `*texto*`.

# 02 · Otra sección

- Lista con guion
- Otro item
- Tercer item

| Columna 1 | Columna 2 |
|-----------|-----------|
| Dato A    | Dato B    |
| Dato C    | Dato D    |

> [!info] Bloque destacado
> Esto se renderiza como caja informativa azul.

> [!warning] Advertencia
> Caja amarilla atención.
```

Cada `# NN · Título` se vuelve una **sección/página** del documento HTML.

---

## 4. Editar un doc existente

```bash
# 1. Sincronizar con remoto
git pull origin main

# 2. Abrir el .md a editar (ejemplo: doc 17)
code docs/17-estrategia-y1.md  # o vim · nano · TextEdit

# 3. Editar texto · guardar

# 4. Regenerar el HTML
python3 create_doc.py docs/17-estrategia-y1.md --apply

# 5. Ver localmente (opcional)
open 17-estrategia-y1.html  # Mac

# 6. Si está OK, subir
git add docs/17-estrategia-y1.md 17-estrategia-y1.html
git commit -m "docs(17): ajuste hito Fase 1"
git push origin main
```

En **~1 minuto** GitHub Pages publica los cambios.

---

## 5. Crear un doc nuevo

```bash
# 1. Copiar uno existente como template
cp docs/17-estrategia-y1.md docs/42-mi-nuevo-doc.md

# 2. Editar frontmatter (número 42 · id · title · etc.)
code docs/42-mi-nuevo-doc.md

# 3. Reescribir body completo

# 4. Generar HTML
python3 create_doc.py docs/42-mi-nuevo-doc.md --apply

# 5. Editar index.html para agregar card al nuevo doc

# 6. Commit + push
```

---

## 6. Bloques especiales (callouts)

Sintaxis: `> [!tipo] título` · líneas siguientes con `>`.

```markdown
> [!premise] 🎯 Premisa clave
> Texto premisa. Se renderiza con icono y borde resaltado.

> [!anti] ⛔ Lo que NO hacemos
> Lista de no-objetivos.

> [!info] 💡 Insight
> Caja azul informativa.

> [!warning] ⚠️ Cuidado
> Caja amarilla advertencia.

> [!success] ✅ Logrado
> Caja verde de éxito.

> [!decision] 📌 Decisión tomada
> Caja para decisiones formales (ADRs).
```

---

## 7. Diagramas interactivos (avanzado)

Para diagramas (gantt · pipeline · heatmap · etc.) se usa **sidecar JSON**. Ver ejemplos en `docs/14-founders-journey/` o `docs/35-risk-register/`. Por ahora **NO te preocupes** · arrancá con markdown puro · cuando necesites un diagrama avisás a Guillermo.

---

## 8. Workflow git diario

```bash
# Al empezar a editar
git pull origin main          # traer cambios de Guillermo/Camila

# Editar lo que necesites
# ... editor ...

# Al terminar
python3 create_doc.py docs/NN-mi-doc.md --apply
git add docs/NN-mi-doc.md NN-mi-doc.html
git commit -m "docs(NN): qué cambié"
git push origin main
```

**Conflictos:** si `git push` rechaza · `git pull --rebase origin main` resuelve casi todo automático.

---

## 9. Validar antes de push

Antes de pushear · siempre:

```bash
# Audit general del banco · detecta links rotos · numeración inconsistente · etc.
python3 audit_banco.py

# Si dice "0 issues" o solo cosas menores · safe push
# Si dice errores en TU archivo · arreglar primero
```

---

## 10. FAQ

**P: ¿Puedo editar el HTML directamente?**
R: NO. Si editás el HTML, la próxima vez que alguien regenere desde el .md, perdés tu cambio. Editá siempre el `.md`.

**P: ¿Puedo poner HTML inline dentro del markdown?**
R: Sí, pero el script lo envuelve en `<p>` y rompe tablas/SVGs. Para tablas complejas o diagramas, usar sintaxis pipe (`| col |`) o sidecar JSON.

**P: ¿Cómo veo el doc renderizado sin pushear?**
R: Después de `python3 create_doc.py docs/X.md --apply` · doble click al `.html` generado · abre en el navegador.

**P: ¿Y si rompo algo grave?**
R: Todo está versionado en git. `git log` ve el historial · `git revert <commit-id>` deshace · `git checkout main -- archivo.html` recupera la versión del remoto.

**P: ¿Markdown tiene más sintaxis?**
R: Sí. Para más: <https://www.markdownguide.org/cheat-sheet/> · pero con lo de esta guía cubrís 90% de los casos.

---

## 11. Comandos copy-paste cheatsheet

```bash
# Sincronizar
git pull origin main

# Regenerar UN doc
python3 create_doc.py docs/NN-mi-doc.md --apply

# Regenerar TODOS los docs (sirve después de cambiar el script o estilos)
python3 create_doc.py docs/*.md --apply

# Audit del banco
python3 audit_banco.py

# Subir cambios
git add .
git commit -m "docs: descripción"
git push origin main
```

---

## 12. Ayuda

- Cualquier duda · preguntar a Guillermo (canal #marketplace-smc)
- Si Python o git tira error raro · pegar el error en el chat
- Si querés agregar diagramas (gantt · pipeline) · Guillermo te explica el sidecar JSON
