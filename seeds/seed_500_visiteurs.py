import random
from pymongo import MongoClient
from datetime import datetime, timezone, timedelta

client = MongoClient("mongodb://localhost:27017")
db = client["visiteurs"]

db.visiteurs.drop()
print("🗑️  Collection vidée")

now = datetime.now(timezone.utc)
random.seed(42)

# ─── Données de référence ───────────────────────────────────────────────────

FORMATIONS_INTERESSEE = [
    "BUT GACO",
    "BUT Infocom",
    "BUT Informatique",
    "BUT QLIO",
]

FORMATIONS_ORIGINE = [
    {"type": "bac_general",  "libelle": "Baccalauréat Général"},
    {"type": "bac_techno",   "libelle": "Baccalauréat STMG"},
    {"type": "bac_techno",   "libelle": "Baccalauréat STI2D"},
    {"type": "bac_techno",   "libelle": "Baccalauréat ST2S"},
    {"type": "bac_techno",   "libelle": "Baccalauréat STHR"},
    {"type": "bac_pro",      "libelle": "Baccalauréat Pro SN"},
    {"type": "bac_pro",      "libelle": "Baccalauréat Pro MELEC"},
    {"type": "bac_pro",      "libelle": "Baccalauréat Pro MEI"},
    {"type": "bac_pro",      "libelle": "Baccalauréat Pro Logistique"},
    {"type": "bac_pro",      "libelle": "Baccalauréat Pro Commerce"},
    {"type": "bac_pro",      "libelle": "Baccalauréat Pro Vente"},
    {"type": "bac_pro",      "libelle": "Baccalauréat Pro TMSEC"},
    {"type": "bts",          "libelle": "BTS SIO"},
    {"type": "bts",          "libelle": "BTS NDRC"},
    {"type": "bts",          "libelle": "BTS Gestion de la PME"},
    {"type": "bts",          "libelle": "BTS Communication"},
    {"type": "bts",          "libelle": "BTS Supply Chain"},
    {"type": "licence",      "libelle": "Licence Informatique"},
    {"type": "licence",      "libelle": "Licence Économie-Gestion"},
    {"type": "licence",      "libelle": "Licence Sciences du Langage"},
    {"type": "licence",      "libelle": "Licence AES"},
    {"type": "master",       "libelle": "Master Informatique"},
    {"type": "master",       "libelle": "Master Marketing"},
    {"type": "master",       "libelle": "Master Management"},
    {"type": "master",       "libelle": "Master Sciences de l'Information"},
    {"type": "but",          "libelle": "BUT Informatique"},
    {"type": "but",          "libelle": "BUT en cours (autre)"},
    {"type": "prepa",        "libelle": "Classe Préparatoire"},
    {"type": "autre",        "libelle": "Autre formation"},
]

ETABLISSEMENTS = [
    ("Lycée Henri IV",                    "Paris"),
    ("Lycée Léonard de Vinci",            "Nantes"),
    ("Lycée des Métiers du Numérique",    "Rennes"),
    ("IUT de Grenoble",                   "Grenoble"),
    ("Lycée Gustave Eiffel",              "Dijon"),
    ("Lycée Voltaire",                    "Strasbourg"),
    ("Lycée Racine",                      "Paris"),
    ("Lycée Victor Hugo",                 "Besançon"),
    ("Lycée Jean-Baptiste Say",           "Lille"),
    ("Lycée Ampère",                      "Lyon"),
    ("Lycée des Métiers du Transport",    "Rouen"),
    ("Lycée Fermat",                      "Toulouse"),
    ("Lycée Louis Armand",                "Mulhouse"),
    ("Lycée Jean Perrin",                 "Saint-Étienne"),
    ("Lycée Montaigne",                   "Bordeaux"),
    ("Lycée Camus",                       "Marseille"),
    ("Lycée Descartes",                   "Tours"),
    ("Lycée Vauban",                      "Brest"),
    ("Lycée Blaise Pascal",               "Clermont-Ferrand"),
    ("Lycée Lamartine",                   "Mâcon"),
    ("Lycée Jules Ferry",                 "Nice"),
    ("IUT de Lyon",                       "Lyon"),
    ("IUT de Bordeaux",                   "Bordeaux"),
    ("IUT Paris Rives de Seine",          "Paris"),
    ("Université de Montpellier",         "Montpellier"),
    ("Université de Nantes",              "Nantes"),
    ("Université Paris-Saclay",           "Orsay"),
    ("Université de Strasbourg",          "Strasbourg"),
    ("Université Toulouse III",           "Toulouse"),
    ("Université de Rennes 1",            "Rennes"),
]

VILLES_CP = [
    ("Paris",            "75001"),
    ("Lyon",             "69001"),
    ("Marseille",        "13001"),
    ("Toulouse",         "31000"),
    ("Bordeaux",         "33000"),
    ("Nantes",           "44000"),
    ("Strasbourg",       "67000"),
    ("Lille",            "59000"),
    ("Rennes",           "35000"),
    ("Grenoble",         "38000"),
    ("Dijon",            "21000"),
    ("Rouen",            "76000"),
    ("Mulhouse",         "68100"),
    ("Saint-Étienne",    "42000"),
    ("Besançon",         "25000"),
    ("Brest",            "29200"),
    ("Clermont-Ferrand", "63000"),
    ("Nice",             "06000"),
    ("Tours",            "37000"),
    ("Metz",             "57000"),
    ("Caen",             "14000"),
    ("Nancy",            "54000"),
    ("Angers",           "49000"),
    ("Amiens",           "80000"),
    ("Limoges",          "87000"),
]

EVENEMENTS = [
    ("JPO",            [datetime(2026, 3, 9,  9,  0), datetime(2026, 3, 9, 10, 0),
                        datetime(2026, 3, 9, 11, 30), datetime(2026, 3, 9, 14, 0),
                        datetime(2026, 3, 9, 15, 0),  datetime(2026, 3, 9, 16, 0)]),
    ("portes_ouvertes",[datetime(2026, 3, 15, 9, 30), datetime(2026, 3, 15, 10, 0),
                        datetime(2026, 3, 15, 11, 0), datetime(2026, 3, 15, 13, 30),
                        datetime(2026, 3, 15, 14, 0), datetime(2026, 3, 15, 15, 0)]),
    ("salon_virtuel",  [datetime(2026, 2, 18, 10, 0), datetime(2026, 2, 18, 11, 0),
                        datetime(2026, 2, 20, 14, 0), datetime(2026, 2, 20, 16, 0)]),
    ("salon",          [datetime(2026, 1, 22, 10, 0), datetime(2026, 1, 22, 14, 0),
                        datetime(2026, 1, 23, 9,  0), datetime(2026, 1, 23, 15, 0)]),
    ("evenement",      [datetime(2026, 4,  5, 10, 0), datetime(2026, 4,  5, 14, 0),
                        datetime(2026, 4, 12, 11, 0), datetime(2026, 4, 12, 16, 0)]),
]

SOURCES_SAISIE  = ["tablette", "ordinateur", "smartphone"]
STATUTS_IMMERSION = ["en_attente", "confirme", "refuse", "non_demande"]

NOMS = [
    "Fontaine","Chevalier","Rousseau","Morel","Garnier","Laurent","Simon","Petit","Richard",
    "Dupuis","Blanc","Gilles","Bonnet","Renard","Martin","Bernard","Thomas","Dubois","Robert",
    "Leroy","Moreau","Simon","Michel","Lefebvre","Lefevre","Leroux","Roux","David","Bertrand",
    "Morin","Fournier","Girard","Bonnet","Dupont","Lambert","Fontaine","Roussel","Vincent",
    "Muller","Lecomte","Marchand","Durand","Perrin","Robin","Boyer","Francois","Colin","Henry",
    "Masson","Renault","Schmitt","Brun","Leclercq","Vidal","Dufour","Lucas","Benoit","Joly",
    "Mathieu","Meyer","Barbier","Gautier","Clement","Gauthier","Perez","Arnaud","Giraud",
    "Rey","Leclerc","Pierre","Mercier","Laurent","Blanchard","Guillot","Poirier","Royer",
    "Aubert","Noel","Picard","Bourgeois","Denis","Carpentier","Faure","Guerin","Nguyen","Adam",
    "Laporte","Poulain","Leger","Charrier","Remy","Baudry","Collin","Pages","Fleury","Germain",
]

PRENOMS = [
    "Lucas","Inès","Théo","Axel","Noémie","Camille","Jade","Antoine","Hugo","Mathis",
    "Sarah","Clément","Élodie","Julien","Léa","Maxime","Chloé","Thomas","Emma","Nicolas",
    "Alice","Manon","Baptiste","Lucie","Pierre","Anaïs","Romain","Clara","Quentin","Laura",
    "Simon","Marie","Alexandre","Julie","Florian","Pauline","Adrien","Sophie","Damien","Amandine",
    "Kevin","Margot","Dylan","Charlotte","Alexis","Océane","Tristan","Juliette","Ethan","Zoé",
    "Nathan","Elise","Robin","Lena","Mathieu","Audrey","Sébastien","Marion","Corentin","Laure",
    "Benjamin","Justine","Anthony","Aurore","Jeremy","Virginie","Thibault","Sandrine","Valentin",
    "Isabelle","Arthur","Nathalie","Raphaël","Stéphanie","Louis","Patricia","Gabriel","Valérie",
    "Hugo","Céline","Charles","Christine","Enzo","Sylvie","Tom","Monique","Liam","Brigitte",
    "Ilias","Amira","Youssef","Fatima","Mehdi","Yasmine","Karim","Nadia","Sofiane","Samira",
]

# ─── Génération des 500 visiteurs ───────────────────────────────────────────

def rand_phone():
    if random.random() < 0.05:
        return None
    if random.random() < 0.05:
        return ""
    prefixes = ["06", "07"]
    return random.choice(prefixes) + "".join([str(random.randint(0, 9)) for _ in range(8)])

def rand_email(prenom, nom, idx):
    if random.random() < 0.03:
        return f"{prenom.lower()}.{nom.lower()}_INVALID"
    domains = ["example.com", "gmail.com", "yahoo.fr", "outlook.com", "free.fr", "orange.fr"]
    return f"{prenom.lower().replace('é','e').replace('è','e').replace('ê','e').replace('ë','e').replace('à','a').replace('â','a').replace('î','i').replace('ô','o').replace('û','u').replace('ç','c')}.{nom.lower().replace('é','e').replace('è','e').replace('ê','e').replace('ë','e').replace('à','a').replace('â','a').replace('î','i').replace('ô','o').replace('û','u').replace('ç','c')}{idx}@{random.choice(domains)}"

def rand_dob():
    if random.random() < 0.04:
        return None
    year  = random.randint(2003, 2007)
    month = random.randint(1, 12)
    day   = random.randint(1, 28)
    return datetime(year, month, day)

def rand_evenement():
    evt_type, dates = random.choice(EVENEMENTS)
    return {"type": evt_type, "date_visite": random.choice(dates)}

def rand_immersion():
    souhaite = random.random() < 0.55
    if souhaite:
        statut = random.choice(["en_attente", "confirme"])
    else:
        statut = random.choice(["refuse", "non_demande"])
    return {"souhaite_participer": souhaite, "statut": statut}

def rand_rgpd():
    info    = random.random() < 0.90
    collecte = info and random.random() < 0.85
    contact  = collecte and random.random() < 0.75
    return {
        "information_affichee":  info,
        "consentement_collecte": collecte,
        "consentement_contact":  contact,
        "date_consentement":     now,
    }

visiteurs = []

for i in range(1, 501):
    nom    = random.choice(NOMS)
    prenom = random.choice(PRENOMS)
    etab   = random.choice(ETABLISSEMENTS)
    ville_cp = random.choice(VILLES_CP)
    fo     = random.choice(FORMATIONS_ORIGINE)
    fi     = random.choice(FORMATIONS_INTERESSEE)
    statut_meta = "actif" if random.random() < 0.82 else "inactif"
    situation_particuliere = random.random() < 0.15   # ~15 % ont une situation particulière

    v = {
        "id": i,
        "nom": nom,
        "prenom": prenom,
        "email": rand_email(prenom, nom, i),
        "telephone": rand_phone(),
        "date_de_naissance": rand_dob(),
        "situation_particuliere": situation_particuliere,
        "formation_origine": fo,
        "établisement_d'origine": {"nom": etab[0]},
        "adresse": {"ville": ville_cp[0], "code_postal": ville_cp[1]},
        "formation_interessee": fi,
        "evenement": rand_evenement(),
        "immersion": rand_immersion(),
        "rgpd": rand_rgpd(),
        "meta": {
            "source_saisie":  random.choice(SOURCES_SAISIE),
            "annee_campagne": 2026,
            "statut":         statut_meta,
            "created_at":     now,
            "updated_at":     now,
        },
    }


    visiteurs.append(v)

# ─── Insertion ──────────────────────────────────────────────────────────────

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
    sp   = "⚠️ SP" if v["situation_particuliere"] else "     "
    print(f"  [{i+1:03d}] {v['prenom']:<10} {v['nom']:<12} | {dept:<20} | {v['formation_interessee']:<18} | {sp} | statut: {v['meta']['statut']}")

print(f"\n📊 Résumé par formation :")
for dept_key, dept_label in departements.items():
    count = sum(1 for v in visiteurs if v["formation_interessee"] == dept_key)
    print(f"   {dept_label} : {count} visiteur(s)")

print(f"\n📊 Résumé par type de formation d'origine :")
types_fo = {}
for v in visiteurs:
    t = v["formation_origine"]["type"]
    types_fo[t] = types_fo.get(t, 0) + 1
for t, c in sorted(types_fo.items()):
    print(f"   {t:<15} : {c} visiteur(s)")

sp_count = sum(1 for v in visiteurs if v["situation_particuliere"])
print(f"\n⚠️  Situations particulières : {sp_count} visiteur(s)")

print(f"\n💡 Total inséré : {len(result.inserted_ids)} visiteurs")