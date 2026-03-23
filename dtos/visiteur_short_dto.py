class VisiteurShortDTO:
    def __init__(self, id, nom, prenom, email, formation_interessee, evenement, statut):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.formation_interessee = formation_interessee
        self.evenement = evenement
        self.statut = statut

    def to_dict(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "prenom": self.prenom,
            "email": self.email,
            "formation_interessee": self.formation_interessee,
            "evenement": self.evenement,
            "statut": self.statut
        }
