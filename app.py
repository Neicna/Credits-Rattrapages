from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

# Configuration de la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///game.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- Modèle Character ---
class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    specialty = db.Column(db.String(80), nullable=False)
    level = db.Column(db.Integer, default=1)
    hp = db.Column(db.Integer, default=100)

# --- Route pour créer un personnage ---
@app.route("/api/character/create", methods=["POST"])
def create_character():
    data = request.json  # données envoyées depuis le frontend
    new_character = Character(
        name=data["name"],
        specialty=data["specialty"]
    )
    db.session.add(new_character)
    db.session.commit()
    return jsonify({"message": "Personnage créé", "id": new_character.id}), 201

# Route de test
@app.route("/")
def home():
    return jsonify({"message": "Bienvenue dans Crédits & Rattrapages !"})

if __name__ == "__main__":
    # Création des tables au démarrage (si pas déjà créées)
    with app.app_context():
        db.create_all()
    app.run(debug=True)
