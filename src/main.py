#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The MadDoG.tmdg — Cyber & Code Engineering Toolkit
Main launcher for the framework.
"""

import sys
import argparse
from pathlib import Path

# Import interne (selon ta structure)
try:
    from tmdg.core import system
    from tmdg.utils import banner
except Exception:
    # Mode fallback si lancé hors package
    pass


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
#  MENU PRINCIPAL
# ============================

def show_menu():
    print(MAD_DOG_ASCII)
    print("🐺  The MadDoG.tmdg — Cyber & Code Engineering Toolkit\n")
    print("Sélectionne une action :\n")
    print("  1) Scanner l’environnement")
    print("  2) Lancer les outils internes")
    print("  3) Afficher les informations système")
    print("  4) Documentation")
    print("  5) Quitter\n")

    choice = input("👉 Choix : ").strip()
    return choice


# ============================
#  ACTIONS
# ============================

def action_environment():
    print("\n🔍 Vérification de l’environnement…\n")
    print("Python :", sys.version)
    print("Chemin :", sys.executable)
    print("\n✔ Environnement analysé.\n")


def action_tools():
    print("\n🧰 Outils disponibles :\n")
    print(" - Formatter (Black)")
    print(" - Linter (Ruff)")
    print(" - Tests (pytest)")
    print(" - Build (Invoke)\n")
    print("Utilise `make` ou `invoke` pour les lancer.\n")


def action_system_info():
    print("\n🖥 Informations système :\n")
    print("Plateforme :", sys.platform)
    print("Version Python :", sys.version)
    print("Répertoire courant :", Path.cwd())
    print("\n✔ Informations récupérées.\n")


def action_docs():
    print("\n📚 Documentation :\n")
    print(" - README.md")
    print(" - STARTER-KIT.md")
    print(" - Wiki GitHub")
    print(" - docs/\n")


# ============================
#  MAIN
# ============================

def main():
    parser = argparse.ArgumentParser(
        description="The MadDoG.tmdg — Cyber & Code Engineering Toolkit"
    )
    parser.add_argument(
        "--cli",
        action="store_true",
        help="Lancer directement le menu interactif"
    )

    args = parser.parse_args()

    if args.cli:
        while True:
            choice = show_menu()

            if choice == "1":
                action_environment()
            elif choice == "2":
                action_tools()
            elif choice == "3":
                action_system_info()
            elif choice == "4":
                action_docs()
            elif choice == "5":
                print("\n🐺 À bientôt, MadDoG.\n")
                break
            else:
                print("\n❌ Choix invalide.\n")

    else:
        print(MAD_DOG_ASCII)
        print("Utilise `python main.py --cli` pour lancer le menu interactif.")


if __name__ == "__main__":
    main()
