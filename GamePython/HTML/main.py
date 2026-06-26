#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Application GamePython - Fenêtre avec boutons ouvrant des liens HTML
Point d'entrée principal de l'application (Terminal caché)
"""

import tkinter as tk
import sys
from gui import GamePythonGUI


def main():
    """Fonction principale pour lancer l'application"""
    root = tk.Tk()
    app = GamePythonGUI(root)
    
    # Masquer le terminal Windows APRÈS la création de la fenêtre
    if sys.platform == "win32":
        try:
            import ctypes
            hwnd = ctypes.windll.kernel32.GetConsoleWindow()
            if hwnd != 0:
                root.after(200, lambda: ctypes.windll.user32.ShowWindow(hwnd, 0))
        except:
            pass
    
    root.mainloop()


if __name__ == "__main__":
    main()
