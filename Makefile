============================================

MAKEFILE PRO

Projet Python — Structure Premium

============================================

PYTHON := python3
PIP := $(PYTHON) -m pip

--------------------------------------------

Installation des dépendances

--------------------------------------------

install:
	$(PIP) install -r requirements/base.txt

install-dev:
	$(PIP) install -r requirements/dev.txt

install-test:
	$(PIP) install -r requirements/test.txt

install-docs:
	$(PIP) install -r requirements/docs.txt

install-all:
	$(PIP) install -r requirements/all.txt

--------------------------------------------

Qualité du code

--------------------------------------------

lint:
	flake8 src/

format:
	black src/
	isort src/

check:
	black --check src/
	isort --check-only src/
	flake8 src/

--------------------------------------------

Tests

--------------------------------------------

test:
	pytest -q

test-cov:
	pytest --cov=src --cov-report=term-missing

--------------------------------------------

Exécution

--------------------------------------------

run:
	$(PYTHON) src/main.py

--------------------------------------------

Documentation

--------------------------------------------

docs:
	mkdocs serve

docs-build:
	mkdocs build

--------------------------------------------

Nettoyage

--------------------------------------------

clean:
	find . -type d -name "pycache" -exec rm -r {} +
	rm -rf .pytest_cache
	rm -rf .mypy_cache

clean-all: clean
	rm -rf dist build

--------------------------------------------

Publication / Distribution

--------------------------------------------

build:
	$(PYTHON) -m build

publish:
	$(PYTHON) -m twine upload dist/*

--------------------------------------------

Aide

--------------------------------------------

help:
	@echo "Commandes disponibles :"
	@echo "  install        - Installe les dépendances de base"
	@echo "  install-dev    - Installe les dépendances de développement"
	@echo "  install-test   - Installe les dépendances de test"
	@echo "  install-docs   - Installe les dépendances de documentation"
	@echo "  install-all    - Installe toutes les dépendances"
	@echo "  lint           - Analyse le code"
	@echo "  format         - Formate le code"
	@echo "  check          - Vérifie le formatage"
	@echo "  test           - Lance les tests"
	@echo "  test-cov       - Tests avec couverture"
	@echo "  run            - Exécute le projet"
	@echo "  docs           - Lance la doc en local"
	@echo "  docs-build     - Compile la documentation"
	@echo "  clean          - Nettoie les fichiers temporaires"
	@echo "  clean-all      - Nettoyage complet"
	@echo "  build          - Construit le package"
	@echo "  publish        - Publie sur PyPI"
`

---

🎯 Pourquoi ce Makefile est premium

- Modulaire : installation séparée (base, dev, test, docs, all)  
- Pro : commandes pour build, publish, docs, tests, lint  
- Élégant : structure claire, sections bien définies  
- Prêt pour GitHub Actions : parfait pour CI/CD  
- Aligné avec ton style : propre, lisible, efficace  

---
