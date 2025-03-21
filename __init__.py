from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

key = Fernet.generate_key()
f = Fernet(key)

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str

# Nouvelle route pour décrypter la valeur fournie par l'utilisateur
@app.route('/decrypt/', methods=['POST'])
def decryptage():
    data = request.get_json()  # Récupère les données envoyées en JSON
    if 'valeur' not in data:
        return jsonify({"error": "Champ 'valeur' manquant"}), 400

    try:
        valeur_bytes = data['valeur'].encode()  # Conversion str -> bytes
        valeur_decryptee = f.decrypt(valeur_bytes).decode()  # Décryptage
        return jsonify({"valeur_decryptee": valeur_decryptee})
    except Exception as e:
        return jsonify({"error": "Échec du décryptage", "details": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
