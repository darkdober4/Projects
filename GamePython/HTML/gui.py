import tkinter as tk
from tkinter import ttk
import webbrowser
from config import BUTTONS_CONFIG, WINDOW_TITLE, WINDOW_WIDTH, WINDOW_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT


class ButtonHoverEffect:
    """Classe pour gérer l'effet de survol des boutons"""
    
    @staticmethod
    def on_enter(event, button, original_color, hover_color):
        button.config(bg=hover_color)
    
    @staticmethod
    def on_leave(event, button, original_color, hover_color):
        button.config(bg=original_color)


class GamePythonGUI:
    """Classe principale pour gérer l'interface graphique"""
    
    def __init__(self, root):
        self.root = root
        self.root.title(WINDOW_TITLE)
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.configure(bg="#34495e")
        
        # Centrer la fenêtre sur l'écran
        self.center_window()
        
        # Créer l'interface
        self.create_widgets()
    
    def center_window(self):
        """Centrer la fenêtre sur l'écran"""
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.update()
        
        # Obtenir les dimensions de l'écran
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Calculer la position
        x = (screen_width // 2) - (WINDOW_WIDTH // 2)
        y = (screen_height // 2) - (WINDOW_HEIGHT // 2)
        
        # S'assurer que la fenêtre n'est pas hors de l'écran
        if x < 0:
            x = 0
        if y < 0:
            y = 0
            
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}")
    
    def create_widgets(self):
        """Créer les éléments de l'interface graphique"""
        
        # Titre principal
        title_frame = tk.Frame(self.root, bg="#34495e")
        title_frame.pack(pady=20)
        
        title_label = tk.Label(
            title_frame,
            text="🎮 GamePython - Liens HTML",
            font=("Helvetica", 18, "bold"),
            bg="#34495e",
            fg="#ecf0f1"
        )
        title_label.pack()
        
        # Frame pour les boutons
        buttons_frame = tk.Frame(self.root, bg="#34495e")
        buttons_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        # Créer les boutons à partir de la configuration
        self.create_buttons(buttons_frame)
        
        # Bouton de fermeture en bas
        exit_frame = tk.Frame(self.root, bg="#34495e")
        exit_frame.pack(side=tk.BOTTOM, pady=15)
        
        exit_button = tk.Button(
            exit_frame,
            text="Quitter",
            command=self.root.quit,
            font=("Helvetica", 10, "bold"),
            bg="#e74c3c",
            fg="white",
            padx=20,
            pady=8,
            cursor="hand2",
            relief=tk.FLAT
        )
        exit_button.pack()
        
        # Effet hover sur le bouton Quitter
        exit_button.bind("<Enter>", lambda e: exit_button.config(bg="#c0392b"))
        exit_button.bind("<Leave>", lambda e: exit_button.config(bg="#e74c3c"))
    
    def create_buttons(self, parent):
        """Créer les boutons HTML à partir de la configuration"""
        
        for button_config in BUTTONS_CONFIG:
            button = tk.Button(
                parent,
                text=button_config["name"],
                command=lambda url=button_config["url"]: self.open_link(url),
                font=("Helvetica", 11, "bold"),
                bg="#2c3e50",
                fg="#ecf0f1",
                padx=15,
                pady=10,
                width=BUTTON_WIDTH,
                relief=tk.FLAT,
                cursor="hand2"
            )
            button.pack(pady=8, fill=tk.X)
            
            # Ajouter l'effet de survol
            button.bind(
                "<Enter>",
                lambda e, b=button, og="#2c3e50", hv="#3498db": 
                    ButtonHoverEffect.on_enter(e, b, og, hv)
            )
            button.bind(
                "<Leave>",
                lambda e, b=button, og="#2c3e50", hv="#3498db": 
                    ButtonHoverEffect.on_leave(e, b, og, hv)
            )
    
    def open_link(self, url):
        """Ouvrir le lien HTML dans le navigateur par défaut"""
        if url == "INSERT HTML LINK HERE":
            # Afficher un message d'avertissement si le lien n'est pas configuré
            print("⚠️  Le lien n'a pas été configuré. Veuillez modifier config.py")
        else:
            try:
                webbrowser.open(url)
                print(f"✅ Ouverture du lien: {url}")
            except Exception as e:
                print(f"❌ Erreur lors de l'ouverture du lien: {e}")
