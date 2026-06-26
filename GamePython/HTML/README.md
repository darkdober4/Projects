# 🎮 GamePython - Fenêtre HTML Links

Application Python avec une interface graphique (tkinter) contenant des boutons cliquables qui ouvrent des liens HTML.

## 📁 Structure du projet

```
GamePython/HTML/
├── main.py          # Point d'entrée principal
├── gui.py           # Interface graphique (classe GamePythonGUI)
├── config.py        # Configuration des boutons et des liens
└── README.md        # Ce fichier
```

## 🚀 Comment démarrer

### Prérequis
- Python 3.6 ou supérieur
- Aucune dépendance externe (utilise tkinter qui est inclus avec Python)

### Lancer l'application

1. Ouvrez un terminal/PowerShell
2. Naviguez vers le dossier du projet:
   ```bash
   cd "C:\Users\cassa\OneDrive\Bureau\GamePython\HTML"
   ```
3. Lancez l'application:
   ```bash
   python main.py
   ```

## ⚙️ Configuration des liens

Pour ajouter vos liens HTML:

1. Ouvrez le fichier `config.py`
2. Trouvez la section `BUTTONS_CONFIG`
3. Remplacez `"INSERT HTML LINK HERE"` par vos vrais liens

Exemple:
```python
BUTTONS_CONFIG = [
    {
        "name": "Google",
        "url": "https://www.google.com"  # ← Remplacez par votre lien
    },
    {
        "name": "GitHub",
        "url": "https://www.github.com"   # ← Remplacez par votre lien
    },
    # ... autres boutons
]
```

## 📚 Comment ajouter un nouveau bouton

1. Allez dans `config.py`
2. Ajoutez une nouvelle entrée dans la liste `BUTTONS_CONFIG`:
   ```python
   {
       "name": "Mon Bouton",
       "url": "https://mon-lien.com"
   }
   ```

## 🎨 Personnaliser l'interface

Vous pouvez modifier les paramètres dans `config.py`:

- **WINDOW_WIDTH**: Largeur de la fenêtre (pixels)
- **WINDOW_HEIGHT**: Hauteur de la fenêtre (pixels)
- **BUTTON_WIDTH**: Largeur des boutons
- **BUTTON_COLOR_BG**: Couleur de fond des boutons
- **BUTTON_COLOR_FG**: Couleur du texte des boutons
- **BUTTON_HOVER_COLOR**: Couleur au survol

## 🔧 Fichiers

### main.py
- Point d'entrée de l'application
- Initialise tkinter et lance l'interface

### gui.py
- Contient la classe `GamePythonGUI` qui gère l'interface
- Contient la classe `ButtonHoverEffect` pour les effets visuels
- Gère l'ouverture des liens avec `webbrowser`

### config.py
- Configuration centralisée des boutons et des liens
- Configuration visuelle de l'interface

## 💡 Conseils

- Les liens doivent commencer par `http://` ou `https://`
- Les emojis peuvent être utilisés dans les noms des boutons
- Les liens s'ouvriront dans votre navigateur par défaut

## 🐛 Dépannage

**Le lien ne s'ouvre pas:**
- Vérifiez que le lien commence par `http://` ou `https://`
- Vérifiez l'orthographe du lien

**La fenêtre ne s'affiche pas correctement:**
- Ajustez WINDOW_WIDTH et WINDOW_HEIGHT dans config.py
- Redémarrez l'application

## 📝 Notes

- L'application utilise `webbrowser` pour ouvrir les liens (navigateur par défaut du système)
- L'interface est responsive et s'adapte à la taille de la fenêtre
- Les boutons ont un effet de survol (changement de couleur)

Amusez-vous! 🎮
