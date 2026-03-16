class visitor_long_dto:

    def __init__(self, id: str, nom: str, prenom: str, email: str, bac: str, departement: str):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.bac = bac
        self.departement = departement

    def to_dict(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "prenom": self.prenom,
            "email": self.email,
            "bac": self.bac,
            "departement": self.departement
        }