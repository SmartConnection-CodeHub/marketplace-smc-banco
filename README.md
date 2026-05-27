# Marketplace SMC · Banco de Documentos

Banco completo de documentos estratégicos · tácticos · operativos · técnicos · legales y comerciales del proyecto **Marketplace SMC SpA** (entidad legal futura del holding Smart Connection).

## Estructura

```
📦 PRODUCTO TÉCNICO (8 docs) · ✅ completo
   01 Vision · 02 BBP · 03 Requirements · 04 RFP
   05 Data Model · 06 API Catalog · 07 Architecture · 08 Roadmap

💰 COMERCIAL & PRODUCTO (11 docs) · en construcción
   10-20 · Prospect · ICP · Personas · JTBD · Journey · Value Prop ·
          Competitive · Pricing · GTM · Sales · Pitch

💼 NEGOCIO & FINANZAS (4 docs) · en construcción
   21-24 · BMC · TAM/SAM/SOM · Financial Model · Unit Economics

🎙️ MARCA & MARKETING (3 docs) · en construcción
   25-27 · Brand Book · Tone of Voice · Visual Identity

⚖️ LEGAL & COMPLIANCE (3 docs) · pendiente
   28-30 · ToS · Privacy · Templates legales

⛨ SEGURIDAD (2 docs) · pendiente
   31-32 · Security Policy · Incident Response

👔 GOBERNANZA & OPS (9 docs) · pendiente
   33-41 · PRDs · OKRs · Risks · RACI · Runbook · Onboarding · SDK · Glosario · Changelog
```

## Cómo usar

1. Abrir `index.html` en cualquier navegador
2. Click en card del documento de interés
3. Print → PDF con `Cmd+P` si necesitás versión imprimible

## Editar documentos · workflow escalable

```
┌─────────────────────────────────────────────────────────────────┐
│ DOCS NUEVOS (markdown-first · 100% escalable)                  │
│   1. Crear docs/NN-slug.md con frontmatter YAML + markdown puro │
│   2. Usar tablas pipe (| col |) + callouts > [!tipo] + sidecars │
│   3. python3 create_doc.py docs/NN-slug.md --apply              │
│   4. HTML se regenera fielmente desde el .md                    │
│                                                                 │
│ DOCS LEGACY (HTML inline complejo · editar HTML directo)        │
│   - SVGs inline, tablas con clases custom, scripts JSON         │
│   - Editar el .html directamente · NO regenerar desde .md       │
│   - Tienen .md "sombra" solo como referencia documental         │
│                                                                 │
│ Generar .md sombra desde HTML legacy (referencia)               │
│   python3 html_to_md.py NN-slug.html                            │
│   ⚠️ Ese .md NO regenera HTML idéntico · es solo lectura       │
└─────────────────────────────────────────────────────────────────┘
```

### Limpieza cross-proyecto

Auditoría 2026-05-27: 19 menciones a Kanki (proyecto separado) eliminadas
de 6 HTMLs. InfoPet se mantiene porque es contexto real (conflicto interés
Javier declarado en pacto socios · doc 12 + 30 + 35).

## Versión

Versión 1.0 · 2026-05-26 · primera publicación

## Confidencialidad

🔒 **Repo privado · contenido confidencial.**
Contiene estrategia comercial · pricing · financial model · análisis competitivo.
Solo accesible para miembros autorizados de Smart Connection SpA.
