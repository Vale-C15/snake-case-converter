# `snake_case`  ⋆｡°✩

<p align="center">
  <samp>
  ˚　　　　✦　　　　　.　　　　✧<br/>
  <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;╭───────────────╮<br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;│ &nbsp; text → code &nbsp; │<br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;╰───────────────╯<br/>
  <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;hello, beautiful world<br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↓<br/>
  &nbsp;&nbsp;&nbsp;&nbsp;hello_beautiful_world<br/>
  <br/>
  ✧　　　　.　　　　　⋆　　　　✦
  </samp>
</p>

<p align="center">
  A small Python tool for turning everyday text into clean <code>snake_case</code>.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-9B8AC4?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/No_dependencies-♡-B6A0D2?style=flat-square"/>
</p>

---

### ✧ what it does

Takes your text and gives it a little makeover:

- lowercase everything
- remove accents and diacritics
- replace spaces and special characters with `_`
- clean up unnecessary underscores
- convert multiple texts in one session

### ⋆ try it

```bash
git clone https://github.com/YOUR_USERNAME/snake-case-converter.git
cd snake-case-converter
python snake_case.py
```

**Requirements:** Python 3.8+ · No external dependencies.

### ✦ before → after

| before | after |
|:--|:--|
| `Hello World` | `hello_world` |
| `Código de Área` | `codigo_de_area` |
| `Mi Primer Proyecto` | `mi_primer_proyecto` |
| `User Profile (Admin)` | `user_profile_admin` |

### ☾ little peek

```text
=== CONVERSOR A SNAKE_CASE ===

Ingresa el texto: Gestión de Proyectos

Resultado: gestion_de_proyectos

Ingresa el texto: salir

¡Hasta luego!
```

### ⌘ under the hood

Built with Python's standard library:

- `re` — pattern matching
- `unicodedata` — Unicode normalization

---

<p align="center">
  <samp>
  made with Python & a little curiosity ♡<br/>
  <br/>
  AI-assisted development · built and refined by me<br/>
  <br/>
  ⋆｡°✩　thanks for stopping by　✩°｡⋆
  </samp>
</p>