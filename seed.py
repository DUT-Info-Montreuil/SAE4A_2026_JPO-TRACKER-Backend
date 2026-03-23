from pymongo import MongoClient
from datetime import datetime, timezone

client = MongoClient("mongodb://localhost:27017")
db = client["jpo-tracker"]

# Vider la collection avant d'insérer
db.visiteurs.drop()
print("🗑️  Collection vidée")

now = datetime.now(timezone.utc)

visiteurs = [
    {
        "nom": "Dupont",
        "prenom": "Alice",
        "email": "alice.dupont@example.com",
        "telephone": "0612345678",
        "date_de_naissance": datetime(2005, 6, 15),
        "formation_origine": {"type": "bac_general", "libelle": "Baccalauréat Général"},
        "établisement_d'origine": {"nom": "Lycée Victor Hugo", "ville": "Paris"},
        "adresse": {"ville": "Paris", "code_postal": "75001"},
        "formation_interessee": "BUT Informatique",
        "evenement": {"type": "JPO", "date_visite": datetime(2026, 3, 9, 10, 30)},
        "immersion": {"souhaite_participer": True, "statut": "en_attente"},
        "rgpd": {
            "information_affichee": True,
            "consentement_collecte": True,
            "consentement_contact": False,
            "date_consentement": now
        },
        "meta": {
            "source_saisie": "tablette",
            "annee_campagne": 2026,
            "statut": "actif",
            "created_at": now,
            "updated_at": now
        }
    },
    {
        "nom": "Martin",
        "prenom": "Bob",
        "email": "bob.martin@example.com",
        "telephone": "0698765432",
        "date_de_naissance": datetime(2006, 3, 22),
        "formation_origine": {"type": "bac_techno", "libelle": "Baccalauréat STI2D"},
        "établisement_d'origine": {"nom": "Lycée Pasteur", "ville": "Lyon"},
        "adresse": {"ville": "Lyon", "code_postal": "69001"},
        "formation_interessee": "BUT Réseaux & Télécoms",
        "evenement": {"type": "JPO", "date_visite": datetime(2026, 3, 9, 14, 0)},
        "immersion": {"souhaite_participer": False, "statut": "non_demande"},
        "rgpd": {
            "information_affichee": True,
            "consentement_collecte": True,
            "consentement_contact": True,
            "date_consentement": now
        },
        "meta": {
            "source_saisie": "ordinateur",
            "annee_campagne": 2026,
            "statut": "actif",
            "created_at": now,
            "updated_at": now
        }
    },
    {
        "nom": "Leroy",
        "prenom": "Clara",
        "email": "clara.leroy@example.com",
        "telephone": "",
        "date_de_naissance": None,
        "formation_origine": {"type": "bac_pro", "libelle": "Baccalauréat Pro SN"},
        "établisement_d'origine": {"nom": "Lycée Curie", "ville": "Marseille"},
        "adresse": {"ville": "Marseille", "code_postal": "13001"},
        "formation_interessee": "LP Cybersécurité",
        "evenement": {"type": "portes_ouvertes", "date_visite": datetime(2026, 3, 15, 9, 0)},
        "immersion": {"souhaite_participer": True, "statut": "confirme"},
        "rgpd": {
            "information_affichee": True,
            "consentement_collecte": True,
            "consentement_contact": False,
            "date_consentement": now
        },
        "meta": {
            "source_saisie": "tablette",
            "annee_campagne": 2026,
            "statut": "inactif",
            "created_at": now,
            "updated_at": now
        }
    },
    {
        "nom": "Bernard",
        "prenom": "David",
        "email": "david.bernard@example.com",
        "telephone": "0756789012",
        "date_de_naissance": datetime(2004, 11, 8),
        "formation_origine": {"type": "bac_general", "libelle": "Baccalauréat Général"},
        "établisement_d'origine": {"nom": "Lycée Montaigne", "ville": "Bordeaux"},
        "adresse": {"ville": "Bordeaux", "code_postal": "33000"},
        "formation_interessee": "BUT MMI",
        "evenement": {"type": "JPO", "date_visite": datetime(2026, 3, 9, 11, 0)},
        "immersion": {"souhaite_participer": False, "statut": "non_demande"},
        "rgpd": {
            "information_affichee": False,
            "consentement_collecte": False,
            "consentement_contact": False,
            "date_consentement": now
        },
        "meta": {
            "source_saisie": "smartphone",
            "annee_campagne": 2026,
            "statut": "actif",
            "created_at": now,
            "updated_at": now
        }
    },
    {
        "nom": "Petit",
        "prenom": "Emma",
        "email": "emma.petit@example.com",
        "telephone": "0634567890",
        "date_de_naissance": datetime(2005, 9, 30),
        "formation_origine": {"type": "bac_techno", "libelle": "Baccalauréat STMG"},
        "établisement_d'origine": {"nom": "Lycée Molière", "ville": "Toulouse"},
        "adresse": {"ville": "Toulouse", "code_postal": "31000"},
        "formation_interessee": "BUT GEA",
        "evenement": {"type": "portes_ouvertes", "date_visite": datetime(2026, 3, 15, 10, 30)},
        "immersion": {"souhaite_participer": True, "statut": "en_attente"},
        "rgpd": {
            "information_affichee": True,
            "consentement_collecte": True,
            "consentement_contact": True,
            "date_consentement": now
        },
        "meta": {
            "source_saisie": "tablette",
            "annee_campagne": 2026,
            "statut": "actif",
            "created_at": now,
            "updated_at": now
        }
    }
]

result = db.visiteurs.insert_many(visiteurs)

print(f"\n✅ {len(result.inserted_ids)} visiteurs insérés :\n")
for i, (oid, v) in enumerate(zip(result.inserted_ids, visiteurs)):
    print(f"  [{i+1}] {v['prenom']} {v['nom']:<10} | {v['formation_interessee']:<25} | statut: {v['meta']['statut']}")
    print(f"       _id: {oid}")

print(f"\n💡 Copiez un _id ci-dessus pour tester GET /visiteurs/<id>")
