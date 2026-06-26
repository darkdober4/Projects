#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Application GamePython - Fenêtre avec boutons ouvrant des liens HTML
Lanceur sans terminal (fichier .pyw)
"""

import tkinter as tk
from gui import GamePythonGUI


def main():
    """Fonction principale pour lancer l'application"""
    root = tk.Tk()
    app = GamePythonGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
