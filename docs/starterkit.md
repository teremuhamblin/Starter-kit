Starter Kit Complet
- Cohérent, modulaire, premium, et aligné avec ton identité technique + artistique.  
- Pack structuré, pensé comme une fondation professionnelle pour n’importe quel projet que tu vas lancer.

Ce kit inclut :

- Git (ignore, attributes, hooks, message templates)  
- Structure de projet  
- Makefile  
- Invoke tasks  
- Documentation (README, templates, branding)  
- Sécurité (secrets, scans, conventions)  
- Automation (scripts, linters, formatters)  
- Edition : propre, élégant, modulaire, extensible.

---

🌐 Starter Kit Complet — Teremu Edition

📁 1. Structure de projet recommandée

`text
project/
│
├── src/
│   └── project_name/
│       ├── init.py
│       ├── core/
│       ├── utils/
│       └── cli.py
│
├── tests/
│   └── test_basic.py
│
├── tasks.py              # Invoke tasks
├── Makefile              # Automation
├── pyproject.toml        # Config Python (ruff, black, pytest…)
├── requirements.txt
│
├── .gitignore
├── .gitattributes
├── .gitmessage
├── .git-blame-ignore-revs
├── .editorconfig
│
├── branding/
│   ├── logo.svg
│   ├── palette.palette
│   └── ascii/
│       └── banner.ascii
│
├── assets/
│   └── images/
│
├── secrets/
│   └── .gitkeep
│
└── README.md
`

---

⚙️ 2. Makefile — Automation Premium

`makefile

============================

The MadDoG.tmdg Starter Kit Makefile

============================

.PHONY: install format lint test clean

install:
	pip install -r requirements.txt
	pip install -e .

format:
	black src tests
	ruff check src tests --fix

lint:
	ruff check src tests
	black --check src tests

test:
	pytest -q

clean:
	find . -type d -name "pycache" -exec rm -rf {} +
	rm -rf .pytest_cache
`

---

🧰 3. tasks.py — Invoke Automation

`python
from invoke import task

@task
def format(c):
    c.run("black src tests")
    c.run("ruff check src tests --fix")

@task
def lint(c):
    c.run("ruff check src tests")
    c.run("black --check src tests")

@task
def test(c):
    c.run("pytest -q")

@task
def build(c):
    c.run("python -m build")

@task
def clean(c):
    c.run("rm -rf dist build .pytestcache /pycache_")
`

---

🧪 4. pyproject.toml — Config Python complète

`toml
[tool.black]
line-length = 88
target-version = ["py310"]

[tool.ruff]
line-length = 88
select = ["E", "F", "W", "I"]
ignore = ["E501"]

[tool.pytest.ini_options]
pythonpath = ["src"]
addopts = "-q"
`

---

🧿 5. README.md — Version Starter Kit Premium

`markdown

🧿 Project Name — The MadDoG.tmdg Starter Kit

Un starter kit premium, modulaire et élégant, conçu pour des projets Python modernes avec automatisation, branding et structure professionnelle.

🚀 Features
- Structure Python propre et modulaire
- Makefile + Invoke pour automatisation
- Linting & formatting (Ruff + Black)
- Tests intégrés (pytest)
- Branding (ASCII, palette, logo)
- Git Starter Pack complet

📦 Installation
`bash
make install
`

🧪 Tests
`bash
make test
`

🧰 Automatisation
`bash
make format
make lint
make clean
`

🧱 Structure
Voir project/ pour la structure complète.
`

---

🎨 6. Branding — ASCII + Palette

branding/ascii/banner.ascii

`
████████╗███████╗██████╗ ███████╗███╗   ███╗██╗   ██╗
╚══██╔══╝██╔════╝██╔══██╗██╔════╝████╗ ████║╚██╗ ██╔╝
   ██║   █████╗  ██████╔╝█████╗  ██╔████╔██║ ╚████╔╝ 
   ██║   ██╔══╝  ██╔══██╗██╔══╝  ██║╚██╔╝██║  ╚██╔╝  
   ██║   ███████╗██║  ██║███████╗██║ ╚═╝ ██║   ██║   
   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝   ╚═╝   
`

branding/palette.palette

`

Teremu Premium Palette
primary: #4C00FF
secondary: #00E0FF
accent: #FF00A8
dark: #0A0A0A
light: #F5F5F5
`

---

🔐 7. Sécurité — dossier secrets/

`text
secrets/
└── .gitkeep
`

.gitattributes protège déjà ce dossier contre les diffs.

---

🧪 8. Scripts utilitaires (optionnels)

scripts/doctor.sh — Vérification du setup

`bash

!/usr/bin/env bash
echo "🔍 Checking environment..."

python3 --version
pip --version
ruff --version
black --version
pytest --version

echo "✔ Environment OK"
`

---

🎁 Bonus

Tu eux étendre ton starter kit vers :

🔧 Version DevOps
- Dockerfile  
- docker-compose  
- CI/CD GitHub Actions  
- Release automation  

🌐 Version Web
- FastAPI / Flask  
- Frontend minimal (Vite, Tailwind)  

🛡️ Version Sécurité
- Scans secrets  
- Hardening  
- Pre-commit hooks avancés  

🧬 Version Branding Ultime
- Templates README  
- Templates CHANGELOG  
- Templates release notes  
- ASCII art dynamiques  

---
