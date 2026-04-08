import bcrypt
mdp = input("Mot de passe : ")
print(bcrypt.hashpw(mdp.encode(), bcrypt.gensalt()).decode())