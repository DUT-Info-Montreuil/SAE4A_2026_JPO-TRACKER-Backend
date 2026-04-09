class VisiteurLongDTO:
    def __init__(self, data: dict):
        self.id = data.get("id")
        self.nom = data.get("nom")
        self.prenom = data.get("prenom")
        self.email = data.get("email")
        self.telephone = data.get("telephone")
        self.date_de_naissance = data.get("date_de_naissance")
        self.situation_particulier = data.get("situation_particulier")
        self.formation_origine = data.get("formation_origine", {})
        self.etablissement_origine = data.get("etablissement_origine", {})
        self.adresse = data.get("adresse", {})
        self.formation_interessee = data.get("formation_interessee")
        self.evenement = data.get("evenement", {})
        self.immersion = data.get("immersion", {})
        self.rgpd = data.get("rgpd", {})
        self.meta = data.get("meta", {})

    def to_dict(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "prenom": self.prenom,
            "email": self.email,
            "telephone": self.telephone,
            "date_de_naissance": self.date_de_naissance,
            "situation_particulier": self.situation_particulier,
            "formation_origine": self.formation_origine,
            "etablissement_origine": self.etablissement_origine,
            "adresse": self.adresse,
            "formation_interessee": self.formation_interessee,
            "evenement": self.evenement,
            "immersion": self.immersion,
            "rgpd": self.rgpd,
            "meta": self.meta
        }
class VisiteurShortDTO:
    def __init__(self, id, nom, prenom, email, formation_interessee, evenement, statut, adresse, formation_origine):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.formation_interessee = formation_interessee
        self.adresse = adresse
        self.formation_origine = formation_origine
        self.evenement = evenement
        self.statut = statut

    def to_dict(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "prenom": self.prenom,
            "email": self.email,
            "formation_interessee": self.formation_interessee,
            "adresse": self.adresse,
            "formation_origine": self.formation_origine,
            "evenement": self.evenement,
            "statut": self.statut
        }
