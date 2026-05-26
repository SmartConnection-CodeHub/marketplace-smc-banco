# 🎨 SMC Diagram Kit · v1.0.0

Kit reusable de diagramas interactivos para bancos de documentos SMC. Originado en este repo (`marketplace-smc-banco`) · aplicable cross-proyectos del holding.

## Archivos del kit

```
_diagram-kit.css     · estilos branded · 13 componentes · responsive · print · a11y
_diagram-kit.js      · 13 renderers + SMCDiagram.boot()
inject_diagram.py    · helper HTMLs manuales
create_doc.py        · generador markdown → HTML branded
```

## 13 renderers

| Kind | Cuándo |
|------|--------|
| `hla` / `erd` | Arquitecturas · ERDs · mapas de sistemas |
| `pipeline` | Procesos con escenarios (CEM-style) |
| `swatch` | Brand book paleta |
| `heatmap` | Matriz P×I · 2D priorización |
| `funnel` | Sales · TAM/SAM/SOM |
| `gantt` | Roadmap trimestral |
| `canvas9` | Business Model Strategyzer |
| `slides` | Pitch deck |
| `pi-matrix` | Stakeholder power × interest |
| `chart-line` / `chart-bar` | Financial · unit economics |
| `jtbd` | Jobs To Be Done |
| `value-prop` | Strategyzer Value Prop Canvas |

## Uso rápido en doc nuevo

```markdown
---
number: 99
id: mi-doc
title: Mi Documento
---

# 01 · Diagrama

> [!hla] mi-mapa
> Caption opcional

# 02 · Más texto
Texto normal · tablas · listas...
```

Con sidecar JSON en `docs/mi-doc/mi-mapa.json`:

```json
{
  "title": "Mi mapa",
  "blocks": {
    "block1": { "type": "...", "title": "...", "desc": "..." }
  },
  "connections": [
    { "from": "block1", "to": "block2" }
  ]
}
```

Generar:

```bash
python3 create_doc.py docs/mi-doc.md --apply
```

## Uso en HTML manual existente

```bash
python3 inject_diagram.py mi-doc.html hla mi-id mi-data.json \
  --after-id=intro \
  --title="Mapa interactivo" \
  --caption="Descripción..."
```

## Versión

**v1.0.0** · 2026-05-26 · estabilizado en `marketplace-smc-banco`.

## Aplicado en

- `marketplace-smc-banco` (origen · 22 docs visualmente ricos)
- `maquetas/infopet/_diagram-kit/` (kit disponible para uso)
- `maquetas/Kanki and Company/_diagram-kit/` (kit disponible para uso)
- `~/.claude/skills/smc-diagram-kit/` (versión canónica)

## Roadmap v1.1.0

- `swimlane` BPMN
- `kanban`
- `mindmap` radial
- Lazy-load condicional

## Mantenimiento

Cambios al kit en este repo se consideran upstream. Para sincronizar:

```bash
cp _diagram-kit.* inject_diagram.py create_doc.py ~/.claude/skills/smc-diagram-kit/
cp _diagram-kit.* inject_diagram.py create_doc.py /path/otro-proyecto/
```
