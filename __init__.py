from cryptography.fernet import Fernet
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Bienvenue sur l'API de cryptage et décryptage !"

# Route pour chiffrer avec une clé donnée par l'utilisateur
@app.route('/encrypt/<string:key>/<string:valeur>')
def encryptage(key, valeur):
    try:
        key_bytes = key.encode()  # Conversion de la clé en bytes
        f = Fernet(key_bytes)  # Création de l'objet Fernet avec la clé fournie
        valeur_bytes = valeur.encode()  # Conversion de la valeur en bytes
        token = f.encrypt(valeur_bytes)  # Encryptage
        return f"Valeur encryptée : {token.decode()}"  # Retourne la valeur encryptée
    except Exception as e:
        return f"Erreur : {str(e)}", 400  # Gestion des erreurs

# Route pour déchiffrer avec une clé donnée par l'utilisateur
@app.route('/decrypt/<string:key>/<string:valeur>')
def decryptage(key, valeur):
    try:
        key_bytes = key.encode()  # Conversion de la clé en bytes
        f = Fernet(key_bytes)  # Création de l'objet Fernet avec la clé fournie
        valeur_decryptee = f.decrypt(valeur.encode()).decode()  # Décryptage
        return f"Valeur décryptée : {valeur_decryptee}"  # Retourne la valeur décryptée
    except Exception as e:
        return f"Erreur lors du décryptage : {str(e)}", 400  # Gestion des erreurs

# Route pour générer une clé unique
@app.route('/generate_key/')
def generate_key():
    key = Fernet.generate_key().decode()  # Génération et conversion en string
    return f"Clé générée : {key}"

if __name__ == "__main__":
    app.run(debug=True)

