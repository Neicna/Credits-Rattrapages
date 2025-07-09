# 🎓 Crédits & Rattrapages

**Crédits & Rattrapages** est un jeu de rôle textuel en ligne où vous incarnez un élève ingénieur luttant pour valider ses semestres. Affrontez des partiels redoutables, survivez aux projets de groupe, affinez votre spécialité et tentez de franchir l'épreuve ultime : les rattrapages.

## 🧠 Concept

Ce RPG parodique inspiré de *Donjons & Dragons* transpose les mécaniques classiques du jeu de rôle dans l’univers impitoyable des écoles d’ingénieurs.

- 🎲 Création de personnage avec spécialité (Informatique, Chimie, Mécanique, etc.)
- ⚔️ Combats au tour par tour contre des profs, bugs de code, ou crises existentielles
- 📜 Scénario scénarisé avec dialogues interactifs et événements aléatoires
- 🎒 Gestion d’inventaire et compétences
- 🗺️ Exploration de lieux comme le BDE, la BU, l’amphi A ou les enfers du moodle

## 🛠️ Stack technique

- **Frontend** : React  
- **Backend** : Flask (Python)  
- **Base de données** : SQLite  
- **API** : REST (JSON)

## 🚀 Lancer le projet en local

### Prérequis
- Python 3.10+
- Node.js (v18+ recommandé)
- npm ou yarn
- virtualenv (optionnel)

### Installation du backend (Flask)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate sous Windows
pip install -r requirements.txt
python app.py
