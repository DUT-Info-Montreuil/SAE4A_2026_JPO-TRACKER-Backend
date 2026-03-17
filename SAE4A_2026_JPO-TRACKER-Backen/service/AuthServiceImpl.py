from database import db
import bcrypt

class AuthServiceImpl:

    def register(self, data):
        email = data.get("email")
        password = data.get("password")

        if db.users.find_one({"email": email}):
            return {"error": "Utilisateur déjà existant"}

        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        db.users.insert_one({
            "email": email,
            "password": hashed_pw
        })

        return {"message": "Compte créé"}

    def login(self, data):
        email = data.get("email")
        password = data.get("password")

        user = db.users.find_one({"email": email})

        if not user:
            return {"error": "Utilisateur introuvable"}

        if not bcrypt.checkpw(password.encode('utf-8'), user["password"]):
            return {"error": "Mot de passe incorrect"}

        return {"message": "Connexion réussie"}