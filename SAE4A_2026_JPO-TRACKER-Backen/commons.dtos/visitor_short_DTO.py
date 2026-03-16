class VisitorShortDTO:

    def __init__(self, id: str, nom: str, prenom: str):
        self.id = id
        self.nom = nom
        self.prenom = prenom

    def to_dict(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "prenom": self.prenom
        }