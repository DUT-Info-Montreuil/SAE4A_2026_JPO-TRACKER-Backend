from pymongo import MongoClient
from datetime import datetime, timezone

client = MongoClient("mongodb://localhost:27017")
db = client["jpo-tracker"]

# Vider la collection avant d'insérer
db.visiteurs.drop()
print("🗑️  Collection vidée")

now = datetime.now(timezone.utc)

visiteurs = [

    # ─────────────────────────────────────────────
    # 🖥️  DÉPARTEMENT INFORMATIQUE
    # ─────────────────────────────────────────────

    # Cas 1 – Bac général, JPO, consentement total, immersion en attente, tablette
    {
        "nom": "Fontaine",
        "prenom": "Lucas",
        "email": "lucas.fontaine@example.com",
        "telephone": "0611223344",
        "date_de_naissance": datetime(2005, 4, 12),
        "formation_origine": {"type": "bac_general", "libelle": "Baccalauréat Général"},
        "établisement_d'origine": {"nom": "Lycée Henri IV", "ville": "Paris"},
        "adresse": {"ville": "Paris", "code_postal": "75005"},
        "formation_interessee": "BUT Informatique",
        "evenement": {"type": "JPO", "date_visite": datetime(2026, 3, 9, 9, 0)},
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
    },

    # Cas 2 – Bac STI2D, JPO, sans consentement contact, immersion confirmée, ordinateur
    {
        "nom": "Chevalier",
        "prenom": "Inès",
        "email": "ines.chevalier@example.com",
        "telephone": "0699887766",
        "date_de_naissance": datetime(2006, 1, 28),
        "formation_origine": {"type": "bac_techno", "libelle": "Baccalauréat STI2D"},
        "établisement_d'origine": {"nom": "Lycée Léonard de Vinci", "ville": "Nantes"},
        "adresse": {"ville": "Nantes", "code_postal": "44000"},
        "formation_interessee": "BUT Informatique",
        "evenement": {"type": "JPO", "date_visite": datetime(2026, 3, 9, 14, 30)},
        "immersion": {"souhaite_participer": True, "statut": "confirme"},
        "rgpd": {
            "information_affichee": True,
            "consentement_collecte": True,
            "consentement_contact": False,
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

    # Cas 3 – Bac Pro SN, Portes ouvertes, aucun consentement, téléphone manquant, inactif
    {
        "nom": "Rousseau",
        "prenom": "Théo",
        "email": "theo.rousseau@example.com",
        "telephone": "",
        "date_de_naissance": datetime(2006, 7, 3),
        "formation_origine": {"type": "bac_pro", "libelle": "Baccalauréat Pro SN"},
        "établisement_d'origine": {"nom": "Lycée des Métiers du Numérique", "ville": "Rennes"},
        "adresse": {"ville": "Rennes", "code_postal": "35000"},
        "formation_interessee": "BUT Informatique",
        "evenement": {"type": "portes_ouvertes", "date_visite": datetime(2026, 3, 15, 10, 0)},
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
            "statut": "inactif",
            "created_at": now,
            "updated_at": now
        }
    },

    # Cas 4 – Déjà en BUT1 (réorientation), date de naissance None, salon virtuel, immersion refusée
    {
        "nom": "Morel",
        "prenom": "Axel",
        "email": "axel.morel@example.com",
        "telephone": "0745678901",
        "date_de_naissance": None,
        "formation_origine": {"type": "bac_general", "libelle": "Baccalauréat Général"},
        "établisement_d'origine": {"nom": "IUT de Grenoble", "ville": "Grenoble"},
        "adresse": {"ville": "Grenoble", "code_postal": "38000"},
        "formation_interessee": "BUT Informatique",
        "evenement": {"type": "salon_virtuel", "date_visite": datetime(2026, 2, 20, 16, 0)},
        "immersion": {"souhaite_participer": False, "statut": "refuse"},
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

    # Cas 5 – Bac Pro MELEC, portes ouvertes, email invalide (test robustesse), smartphone, immersion en_attente
    {
        "nom": "Garnier",
        "prenom": "Noémie",
        "email": "noemie.garnier_INVALID",
        "telephone": "0623456789",
        "date_de_naissance": datetime(2005, 11, 19),
        "formation_origine": {"type": "bac_pro", "libelle": "Baccalauréat Pro MELEC"},
        "établisement_d'origine": {"nom": "Lycée Gustave Eiffel", "ville": "Dijon"},
        "adresse": {"ville": "Dijon", "code_postal": "21000"},
        "formation_interessee": "BUT Informatique",
        "evenement": {"type": "portes_ouvertes", "date_visite": datetime(2026, 3, 15, 11, 0)},
        "immersion": {"souhaite_participer": True, "statut": "en_attente"},
        "rgpd": {
            "information_affichee": True,
            "consentement_collecte": True,
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

    # ─────────────────────────────────────────────
    # 📣  DÉPARTEMENT GACO / INFOCOM
    # ─────────────────────────────────────────────

    # Cas 6 – Bac STMG, JPO, consentement total, immersion confirmée, tablette
    {
        "nom": "Laurent",
        "prenom": "Camille",
        "email": "camille.laurent@example.com",
        "telephone": "0656789012",
        "date_de_naissance": datetime(2005, 8, 5),
        "formation_origine": {"type": "bac_techno", "libelle": "Baccalauréat STMG"},
        "établisement_d'origine": {"nom": "Lycée Voltaire", "ville": "Strasbourg"},
        "adresse": {"ville": "Strasbourg", "code_postal": "67000"},
        "formation_interessee": "BUT GACO",
        "evenement": {"type": "JPO", "date_visite": datetime(2026, 3, 9, 10, 0)},
        "immersion": {"souhaite_participer": True, "statut": "confirme"},
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
    },

    # Cas 7 – Bac Général, Portes ouvertes, sans consentement collecte, inactif, sans immersion
    {
        "nom": "Simon",
        "prenom": "Jade",
        "email": "jade.simon@example.com",
        "telephone": "0712345678",
        "date_de_naissance": datetime(2006, 2, 14),
        "formation_origine": {"type": "bac_general", "libelle": "Baccalauréat Général"},
        "établisement_d'origine": {"nom": "Lycée Racine", "ville": "Paris"},
        "adresse": {"ville": "Paris", "code_postal": "75008"},
        "formation_interessee": "BUT Infocom",
        "evenement": {"type": "portes_ouvertes", "date_visite": datetime(2026, 3, 15, 14, 0)},
        "immersion": {"souhaite_participer": False, "statut": "non_demande"},
        "rgpd": {
            "information_affichee": True,
            "consentement_collecte": False,
            "consentement_contact": False,
            "date_consentement": now
        },
        "meta": {
            "source_saisie": "ordinateur",
            "annee_campagne": 2026,
            "statut": "inactif",
            "created_at": now,
            "updated_at": now
        }
    },

    # Cas 8 – Bac Pro Commerce, JPO, téléphone + email, immersion en attente, smartphone
    {
        "nom": "Michel",
        "prenom": "Romain",
        "email": "romain.michel@example.com",
        "telephone": "0667890123",
        "date_de_naissance": datetime(2004, 5, 25),
        "formation_origine": {"type": "bac_pro", "libelle": "Baccalauréat Pro Commerce"},
        "établisement_d'origine": {"nom": "Lycée Jean Moulin", "ville": "Clermont-Ferrand"},
        "adresse": {"ville": "Clermont-Ferrand", "code_postal": "63000"},
        "formation_interessee": "BUT GACO",
        "evenement": {"type": "JPO", "date_visite": datetime(2026, 3, 9, 13, 0)},
        "immersion": {"souhaite_participer": True, "statut": "en_attente"},
        "rgpd": {
            "information_affichee": True,
            "consentement_collecte": True,
            "consentement_contact": True,
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

    # Cas 9 – Bac STD2A, salon virtuel, date de naissance None, email manquant, immersion refusée
    {
        "nom": "Thomas",
        "prenom": "Léa",
        "email": "",
        "telephone": "0789012345",
        "date_de_naissance": None,
        "formation_origine": {"type": "bac_techno", "libelle": "Baccalauréat STD2A"},
        "établisement_d'origine": {"nom": "Lycée des Arts", "ville": "Montpellier"},
        "adresse": {"ville": "Montpellier", "code_postal": "34000"},
        "formation_interessee": "BUT Infocom",
        "evenement": {"type": "salon_virtuel", "date_visite": datetime(2026, 2, 25, 15, 30)},
        "immersion": {"souhaite_participer": False, "statut": "refuse"},
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

    # Cas 10 – Bac Pro Vente, portes ouvertes, aucun consentement, téléphone None, inactif
    {
        "nom": "Richard",
        "prenom": "Hugo",
        "email": "hugo.richard@example.com",
        "telephone": None,
        "date_de_naissance": datetime(2005, 12, 1),
        "formation_origine": {"type": "bac_pro", "libelle": "Baccalauréat Pro Vente"},
        "établisement_d'origine": {"nom": "Lycée Jean-Baptiste Say", "ville": "Lille"},
        "adresse": {"ville": "Lille", "code_postal": "59000"},
        "formation_interessee": "BUT GACO",
        "evenement": {"type": "portes_ouvertes", "date_visite": datetime(2026, 3, 15, 9, 30)},
        "immersion": {"souhaite_participer": False, "statut": "non_demande"},
        "rgpd": {
            "information_affichee": False,
            "consentement_collecte": False,
            "consentement_contact": False,
            "date_consentement": now
        },
        "meta": {
            "source_saisie": "ordinateur",
            "annee_campagne": 2026,
            "statut": "inactif",
            "created_at": now,
            "updated_at": now
        }
    },

    # ─────────────────────────────────────────────
    # 📦  DÉPARTEMENT QLIO
    # ─────────────────────────────────────────────

    # Cas 11 – Bac STI2D, JPO, consentement total, immersion confirmée, tablette, actif
    {
        "nom": "Dupuis",
        "prenom": "Mathis",
        "email": "mathis.dupuis@example.com",
        "telephone": "0645678901",
        "date_de_naissance": datetime(2005, 3, 17),
        "formation_origine": {"type": "bac_techno", "libelle": "Baccalauréat STI2D"},
        "établisement_d'origine": {"nom": "Lycée Ampère", "ville": "Lyon"},
        "adresse": {"ville": "Lyon", "code_postal": "69003"},
        "formation_interessee": "BUT QLIO",
        "evenement": {"type": "JPO", "date_visite": datetime(2026, 3, 9, 11, 30)},
        "immersion": {"souhaite_participer": True, "statut": "confirme"},
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
    },

    # Cas 12 – Bac Pro Logistique, portes ouvertes, sans consentement contact, immersion en attente, smartphone
    {
        "nom": "Blanc",
        "prenom": "Sarah",
        "email": "sarah.blanc@example.com",
        "telephone": "0734567890",
        "date_de_naissance": datetime(2006, 6, 9),
        "formation_origine": {"type": "bac_pro", "libelle": "Baccalauréat Pro Logistique"},
        "établisement_d'origine": {"nom": "Lycée des Métiers du Transport", "ville": "Rouen"},
        "adresse": {"ville": "Rouen", "code_postal": "76000"},
        "formation_interessee": "BUT QLIO",
        "evenement": {"type": "portes_ouvertes", "date_visite": datetime(2026, 3, 15, 13, 30)},
        "immersion": {"souhaite_participer": True, "statut": "en_attente"},
        "rgpd": {
            "information_affichee": True,
            "consentement_collecte": True,
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

    # Cas 13 – Bac Général, JPO, aucun consentement, ni téléphone ni date de naissance, inactif
    {
        "nom": "Gilles",
        "prenom": "Clément",
        "email": "clement.gilles@example.com",
        "telephone": "",
        "date_de_naissance": None,
        "formation_origine": {"type": "bac_general", "libelle": "Baccalauréat Général"},
        "établisement_d'origine": {"nom": "Lycée Fermat", "ville": "Toulouse"},
        "adresse": {"ville": "Toulouse", "code_postal": "31400"},
        "formation_interessee": "BUT QLIO",
        "evenement": {"type": "JPO", "date_visite": datetime(2026, 3, 9, 16, 0)},
        "immersion": {"souhaite_participer": False, "statut": "non_demande"},
        "rgpd": {
            "information_affichee": False,
            "consentement_collecte": False,
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

    # Cas 14 – Bac Pro MEI, salon virtuel, consentement partiel, immersion refusée, ordinateur
    {
        "nom": "Bonnet",
        "prenom": "Élodie",
        "email": "elodie.bonnet@example.com",
        "telephone": "0778901234",
        "date_de_naissance": datetime(2005, 10, 22),
        "formation_origine": {"type": "bac_pro", "libelle": "Baccalauréat Pro MEI"},
        "établisement_d'origine": {"nom": "Lycée Louis Armand", "ville": "Mulhouse"},
        "adresse": {"ville": "Mulhouse", "code_postal": "68100"},
        "formation_interessee": "BUT QLIO",
        "evenement": {"type": "salon_virtuel", "date_visite": datetime(2026, 2, 18, 11, 0)},
        "immersion": {"souhaite_participer": False, "statut": "refuse"},
        "rgpd": {
            "information_affichee": True,
            "consentement_collecte": True,
            "consentement_contact": False,
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

    # Cas 15 – Bac Pro TMSEC (sécurité), JPO, consentement total, immersion confirmée, smartphone, double formation d'intérêt
    {
        "nom": "Renard",
        "prenom": "Antoine",
        "email": "antoine.renard@example.com",
        "telephone": "0612987654",
        "date_de_naissance": datetime(2004, 8, 30),
        "formation_origine": {"type": "bac_pro", "libelle": "Baccalauréat Pro TMSEC"},
        "établisement_d'origine": {"nom": "Lycée Jean Perrin", "ville": "Saint-Étienne"},
        "adresse": {"ville": "Saint-Étienne", "code_postal": "42000"},
        "formation_interessee": "BUT QLIO",
        "formations_secondaires": ["BUT Informatique"],
        "evenement": {"type": "JPO", "date_visite": datetime(2026, 3, 9, 15, 0)},
        "immersion": {"souhaite_participer": True, "statut": "confirme"},
        "rgpd": {
            "information_affichee": True,
            "consentement_collecte": True,
            "consentement_contact": True,
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

]

result = db.visiteurs.insert_many(visiteurs)

print(f"\n✅ {len(result.inserted_ids)} visiteurs insérés :\n")

departements = {
    "BUT Informatique": "🖥️  Informatique",
    "BUT GACO":         "📣  GACO",
    "BUT Infocom":      "📣  Infocom",
    "BUT QLIO":         "📦  QLIO",
}

for i, (oid, v) in enumerate(zip(result.inserted_ids, visiteurs)):
    dept = departements.get(v["formation_interessee"], "❓ Autre")
    print(f"  [{i+1:02d}] {v['prenom']} {v['nom']:<12} | {dept:<20} | {v['formation_interessee']:<18} | statut: {v['meta']['statut']}")
    print(f"       _id: {oid}")

print(f"\n💡 Copiez un _id ci-dessus pour tester GET /visiteurs/<id>")
print(f"\n📊 Résumé :")
for dept_key, dept_label in departements.items():
    count = sum(1 for v in visiteurs if v["formation_interessee"] == dept_key)
    print(f"   {dept_label} : {count} visiteur(s)")
