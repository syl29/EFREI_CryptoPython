from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify

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

@app.route('/decrypt/<string:valeur>')
def decryptage(valeur):
    try:
        valeur_decryptee = f.decrypt(valeur.encode()).decode()  # Décryptage
        return f"Valeur décryptée : {valeur_decryptee}"  # Retourne la valeur décryptée
    except Exception as e:
        return f"Erreur lors du décryptage : {str(e)}", 400  # Gestion des erreurs

if __name__ == "__main__":
    app.run(debug=True)

