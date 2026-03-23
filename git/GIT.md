🚀 Git Starter Kit — The MadDoG.tmdg Edition
Un ensemble cohérent, professionnel et élégant pour structurer ton dépôt Git.

📦 Contenu du pack
- .gitignore — Spécifique à ton stack  
- .gitattributes — Optimisé Python + scripts + branding  
- .gitmessage — Template premium pour commits  
- .git-blame-ignore-revs — Pour ignorer les commits de formatage  
- .mailmap — Normalisation des auteurs  
- .editorconfig — Cohérence multi‑éditeur  
- Hooks Git (optionnels)  
  - pre-commit  
  - prepare-commit-msg  

---

🧱 1. .gitignore — Teremu Stack

`gitignore

Python
pycache/
*.pyc
*.pyo
*.pyd
*.egg-info/
.env
.venv/
venv/

Virtual environments
.env/
.venv/
venv/

Tools
.mypy_cache/
.ruff_cache/
.pytest_cache/
.coverage
htmlcov/

Logs
*.log

IDE
.vscode/
.idea/

OS
.DS_Store
Thumbs.db

Build
dist/
build/

Branding & assets
assets/
branding/generated/

Secrets
secrets/
*.key
*.pem
`

---

🧭 2. .gitattributes — Version optimisée pour ton starter kit

`gitattributes
* text=auto eol=lf

Python & scripts
*.py      text eol=lf diff=python
*.sh      text eol=lf
*.ps1     text eol=lf
*.bash    text eol=lf
*.zsh     text eol=lf

Config
*.json    text diff=json
*.yml     text diff=yaml
*.yaml    text diff=yaml
*.toml    text diff=toml
*.ini     text
*.cfg     text

Docs & branding
*.md      text diff=markdown
*.ascii   text
*.palette text

Assets
*.svg     text
*.png     binary
*.jpg     binary
*.jpeg    binary
*.gif     binary
*.webp    binary
*.ico     binary

Archives
*.zip     binary
*.tar     binary
*.gz      binary
*.7z      binary

Secrets
secrets/* -diff -merge
`

---

📝 3. .gitmessage — Template premium pour commits

`text

🧿 Commit Message — Teremu Edition

Ligne 1 : Résumé clair (max 72 chars)

Ligne 2 : Vide

Ligne 3+ : Détails, contexte, motivations, notes techniques

[TAG] Résumé du changement

Contexte :
- Pourquoi ce changement ?
- Quel problème est résolu ?

Détails :
- Ce qui a été modifié
- Impacts potentiels

Notes :
- Tests effectués
- TODO éventuels
`

---

🕶️ 4. .git-blame-ignore-revs — Pour ignorer les commits de formatage

`text

Commits à ignorer dans git blame (formatage, refactor global)

Exemple :

1234567890abcdef1234567890abcdef12345678
`

Tu ajouteras ici les commits de type :  
style: format with black  
refactor: restructure project  

---

👤 5. .mailmap — Normalisation des auteurs

`text

Format :

Nom Correct <email@correct> Nom Ancien <email@ancien>

Teremu <contact@teremu.dev> Teremu <teremu@oldmail.com>
`

---

🧩 6. .editorconfig — Cohérence multi‑éditeur

`editorconfig
root = true

[*]
charset = utf-8
indent_style = space
indent_size = 4
endofline = lf
insertfinalnewline = true
trimtrailingwhitespace = true

[*.md]
trimtrailingwhitespace = false
`

---

🪝 7. Hooks Git (optionnels mais puissants)

pre-commit — Lint + format + sécurité

`bash

!/usr/bin/env bash
echo "🔍 Running pre-commit checks..."

Python formatting
if command -v ruff >/dev/null 2>&1; then
    ruff check .
fi

Python formatting
if command -v black >/dev/null 2>&1; then
    black --check .
fi

Secrets scanning (optionnel)
if command -v detect-secrets >/dev/null 2>&1; then
    detect-secrets scan > /dev/null
fi

echo "✔ Pre-commit checks completed."
`

prepare-commit-msg — Pré-remplissage branding

`bash

!/usr/bin/env bash
TEMPLATE=".gitmessage"

if [ -f "$TEMPLATE" ]; then
    cat "$TEMPLATE" > "$1"
fi
`

---
