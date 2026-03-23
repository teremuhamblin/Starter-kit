#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The MadDoG.tmdg — Cyber & Code Engineering Toolkit
CLI All‑In‑One : Branding + Menu + Sous-commandes + Modules.
"""

import sys
import argparse
import subprocess
from pathlib import Path


# ============================
#  ASCII BRANDING
# ============================

MAD_DOG_ASCII = r"""
███╗   ███╗ █████╗ ██████╗ ██████╗  ██████╗  ██████╗ 
████╗ ████║██╔══██╗██╔══██╗██╔══██╗██╔═══██╗██╔════╝ 
██╔████╔██║███████║██████╔╝██████╔╝██║   ██║██║  ███╗
██║╚██╔╝██║██╔══██║██╔══██╗██╔══██╗██║   ██║██║   ██║
██║ ╚═╝ ██║██║  ██║██║  ██║██║  ██║╚██████╔╝╚██████╔╝
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ 
"""


# ============================
#  MODULES INTERNES
# ============================

def run_command(cmd: str):
    """Exécute une commande shell proprement."""
    try:
        subprocess.run(cmd.split(), check=True)
    except Exception as e:
        print(f"❌ Erreur : {e}")


# --- Scan environnement ---
def cmd_scan(args):
    print("🔍 Scan de l’environnement…\n")
    print("Python :", sys.version)
    print("Chemin :", sys.executable)
    print("Répertoire :", Path.cwd())
    print("\n✔ Scan terminé.\n")


# --- Diagnostic complet ---
def cmd_doctor(args):
    print("🩺 Diagnostic complet…\n")

    tools = {
        "python": "python --version",
        "pip": "pip --version",
        "ruff": "ruff --version",
        "black": "black --version",
        "pytest": "pytest --version",
    }

    for name, cmd in tools.items():
        print(f"→ {name} :", end=" ")
        try:
            subprocess.run(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print("OK")
        except Exception:
            print("❌ Non trouvé")

    print("\n✔ Diagnostic terminé.\n")


# --- Build ---
def cmd_build(args):
    print("⚙️ Build du projet…\n")
    run_command("python -m build")
    print("✔ Build terminé.\n")


# --- Tests ---
def cmd_test(args):
    print("🧪 Lancement des tests…\n")
    run_command("pytest -q")
    print("✔ Tests terminés.\n")


# --- Format & Lint ---
def cmd_format(args):
    print("🎨 Formatage du code…\n")
    run_command("black src tests")
    run_command("ruff check src tests --fix")
    print("✔ Formatage terminé.\n")


def cmd_lint(args):
    print("🔎 Linting…\n")
    run_command("ruff check src tests")
    run_command("black --check src tests")
    print("✔ Lint terminé.\n")


# --- Infos Toolkit ---
def cmd_info(args):
    print("🧠 Informations The MadDoG\n")
    print("Nom : The MadDoG.tmdg")
    print("Type : Cyber & Code Engineering Toolkit")
    print("Version : 1.0.0")
    print("Auteur : Teremu")
    print("\nStructure du projet :")
    print(" - src/tmdg/")
    print(" - docs/")
    print(" - git/")
    print(" - assets/")
    print(" - tests/")
    print("\n✔ Informations affichées.\n")


# --- Branding ---
def cmd_banner(args):
    print(MAD_DOG_ASCII)
    print("🐺 The MadDoG.tmdg — Cyber & Code Engineering Toolkit\n")


# ============================
#  MENU INTERACTIF
# ============================

def interactive_menu():
    while True:
        print(MAD_DOG_ASCII)
        print("🐺  The Mad
