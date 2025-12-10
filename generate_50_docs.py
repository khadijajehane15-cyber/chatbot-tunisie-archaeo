import os

print("=" * 70)
print("📚 GÉNÉRATEUR DE 50 DOCUMENTS - 10 SITES ARCHÉOLOGIQUES DE TUNISIE")
print("=" * 70)

# Créer le dossier data s'il n'existe pas
os.makedirs("data", exist_ok=True)

# CONTENU COMPLET POUR 10 SITES (50 DOCUMENTS)
SITES_COMPLET = {
    "carthage": {
        "general": """CARTHAGE - SITE ARCHÉOLOGIQUE

Localisation : Banlieue nord de Tunis, Gouvernorat de Tunis
Superficie : 500 hectares
Période : IXe siècle av. J.-C. - VIIe siècle ap. J.-C.
Statut UNESCO : Patrimoine mondial depuis 1979

Description :
Carthage, fondée par les Phéniciens vers 814 av. J.-C., fut la capitale de l'empire carthaginois.
Le site présente plusieurs couches archéologiques : phénicienne, punique, romaine, byzantine et arabe.

Principaux monuments :
- Ports puniques (commercial et militaire)
- Thermes d'Antonin (IIe siècle)
- Théâtre romain
- Colline de Byrsa avec musée
- Tophet (sanctuaire)

Le site témoigne de l'histoire méditerranéenne antique et des échanges culturels.""",

        "histoire": """HISTOIRE DE CARTHAGE

Chronologie :
- 814 av. J.-C. : Fondation par les Phéniciens de Tyr
- 650-146 av. J.-C. : Période punique, expansion commerciale
- 264-146 av. J.-C. : Guerres puniques contre Rome
- 146 av. J.-C. : Destruction par les Romains
- 29 av. J.-C. : Refondation par Auguste comme colonie romaine
- IIe-IIIe siècles : Âge d'or romain
- 439-533 : Royaume vandale
- 533-698 : Période byzantine
- 698 : Conquête arabe, déclin progressif

Personnages importants :
- Hannibal Barca (général carthaginois)
- Scipion l'Africain (général romain)
- Saint Cyprien (évêque de Carthage)""",

        "architecture": """ARCHITECTURE DE CARTHAGE

Caractéristiques puniques :
- Ports circulaires (cothon)
- Maisons à péristyle
- Tophet avec stèles
- Murs d'enceinte de 37 km

Architecture romaine :
- Thermes d'Antonin (35 000 m²)
- Théâtre de 5 000 places
- Villas avec mosaïques
- Aqueduc de Zaghouan (132 km)

Techniques :
- Opus africanum (murs à chaînage)
- Système d'égouts avancé
- Citernes pour l'eau""",

        "fouilles": """FOUILLES À CARTHAGE

Historique :
- 1856 : Premières fouilles par Charles Beulé
- 1874 : Début des fouilles systématiques
- 1972-1979 : Mission américaine
- Années 1990 : Fouilles tuniso-internationales

Découvertes majeures :
1. Ports puniques (confirmés en 1970)
2. Stèles du tophet
3. Mosaïques des villas romaines
4. Quartiers d'habitation punique""",

        "unesco": """UNESCO - CARTHAGE

Inscrit : 1979
Critères : (ii), (iii), (vi)
Superficie : 616 ha

Valeur exceptionnelle :
- Témoignage de la civilisation phénico-punique
- Exemple d'urbanisme romain en Afrique
- Lieu d'événements historiques majeurs

Protection : Monument historique classé depuis 1885"""
    },

    "dougga": {
        "general": """DOUGGA - SITE ARCHÉOLOGIQUE

Localisation : Gouvernorat de Béja, nord-ouest Tunisie
Altitude : 600 m
Superficie : 75 hectares
Statut UNESCO : Patrimoine mondial depuis 1997

Description :
Dougga, ancienne Thugga, est un site exceptionnellement bien conservé.
Perché sur une colline, il offre une vue panoramique et présente un mélange unique d'architecture numide et romaine.

Monuments principaux :
- Théâtre romain (3 500 places)
- Capitole (temple de Jupiter)
- Mausolée libyco-punique
- Temple de Saturne
- Thermes des Cyclopes""",

        "histoire": """HISTOIRE DE DOUGGA

Chronologie :
- IVe siècle av. J.-C. : Cité numide importante
- 46 av. J.-C. : Intégration à l'Empire romain
- IIe-IIIe siècles : Construction des principaux monuments
- 439-698 : Période byzantine
- Après 698 : Déclin et abandon

Particularité : Présence d'un mausolée pré-romain unique.""",

        "architecture": """ARCHITECTURE DE DOUGGA

Théâtre romain :
- Construit 168-169 ap. J.-C.
- 3 500 spectateurs
- Encore utilisé pour festivals

Capitole :
- Temple dédié à Jupiter, Junon, Minerve
- Façade à 6 colonnes corinthiennes

Mausolée libyco-punique :
- IIIe siècle av. J.-C.
- 21 m de haut
- Architecture numide pure""",

        "fouilles": """FOUILLES À DOUGGA

Début des fouilles : 1901
Mission française puis tunisienne
État de conservation : Exceptionnel

Découvertes :
- Inscriptions importantes
- Mosaïques bien préservées
- Système hydraulique complet""",

        "unesco": """UNESCO - DOUGGA

Inscrit : 1997
Critères : (ii), (iii)
Superficie : 70 ha

Valeur : Synthèse culturelle numide-romaine
Protection : Monument historique depuis 1891"""
    },

    "el_jem": {
        "general": """EL JEM - AMPHITHÉÂTRE ROMAIN

Localisation : Gouvernorat de Mahdia
Dimensions : 148 m × 122 m × 36 m
Capacité : 35 000 spectateurs
Statut UNESCO : Patrimoine mondial depuis 1979

Description :
Troisième plus grand amphithéâtre romain au monde.
Construit entièrement en pierre de taille au IIIe siècle ap. J.-C.

Particularités :
- Conservation exceptionnelle
- Hypogée (sous-sol) intact
- Pierre locale de qualité""",

        "histoire": """HISTOIRE EL JEM

Construction : vers 238 ap. J.-C.
Contexte : Ville prospère de Thysdrus (huile d'olive)
Événement : Révolte de Gordien en 238 ap. J.-C.

Utilisation :
- Combats de gladiateurs
- Chasses aux fauves
- Spectacles publics""",

        "architecture": """ARCHITECTURE EL JEM

Structure :
- 3 niveaux d'arcades
- 64 arcades au rez-de-chaussée
- Arène : 65 m × 39 m

Matériau : Calcaire local
Style : Sobre et monumental""",

        "fouilles": """FOUILLES EL JEM

Fouilles depuis 1904
Hypogée découvert dans les années 1970
Restaurations importantes pour l'UNESCO""",

        "unesco": """UNESCO - EL JEM

Inscrit : 1979
Critères : (iv), (vi)
Superficie : 2,8 ha

Valeur : Architecture romaine exceptionnelle en Afrique"""
    },

    "kerkouane": {
        "general": """KERKOUANE - VILLE PUNIQUE

Localisation : Péninsule du Cap Bon
Superficie : 12 hectares fouillés
Période : VIe-IIIe siècles av. J.-C.
Statut UNESCO : Patrimoine mondial depuis 1986

Description :
Site punique unique car jamais réoccupé après sa destruction.
Témoignage pur de l'urbanisme et de l'architecture carthaginoise.

Particularité : Plan urbain intact avec rues orthogonales.""",

        "histoire": """HISTOIRE KERKOUANE

Fondation : VIe siècle av. J.-C. par les Carthaginois
Apogée : IVe siècle av. J.-C.
Destruction : vers 250 av. J.-C. (probablement par les Romains)
Abandon : Jamais reconstruite

Importance : Site "fossile" de la civilisation punique.""",

        "architecture": """ARCHITECTURE KERKOUANE

Urbanisme :
- Plan orthogonal (rues à angle droit)
- Maisons avec bains privés
- Système d'égouts avancé

Découvertes :
- Ateliers de pourpre (teinture)
- Sanctuaires
- Nécropole""",

        "fouilles": """FOUILLES KERKOUANE

Découverte : 1952
Fouilles systématiques depuis les années 1970
État : Excellent (non perturbé par occupations ultérieures)""",

        "unesco": """UNESCO - KERKOUANE

Inscrit : 1986
Critères : (iii)
Superficie : 12 ha

Valeur : Témoignage unique de la civilisation punique"""
    },

    "bulla_regia": {
        "general": """BULLA REGIA - SITE ROMAIN

Localisation : Gouvernorat de Jendouba, nord-ouest
Particularité : Maisons souterraines
Période : Ier-IVe siècles ap. J.-C.

Description :
Site romain célèbre pour ses villas à étage souterrain (pour fuir la chaleur).

Monuments :
- Maison de la Pêche
- Maison d'Amphitrite
- Théâtre
- Capitole""",

        "histoire": """HISTOIRE BULLA REGIA

Origine : Ville numide
Romainisation : Ier siècle ap. J.-C.
Prospérité : IIe-IIIe siècles (production agricole)
Déclin : Après les invasions vandales""",

        "architecture": """ARCHITECTURE BULLA REGIA

Innovation : Architecture thermique
Villas avec :
- Étage souterrain pour l'été
- Étage supérieur pour l'hiver
- Système de ventilation naturel

Mosaïques : Exceptionnellement bien conservées""",

        "fouilles": """FOUILLES BULLA REGIA

Fouilles depuis le XIXe siècle
Découverte des villas souterraines dans les années 1960
Mosaïques restaurées in situ""",

        "unesco": """BULLA REGIA - IMPORTANCE

Non inscrite à l'UNESCO mais site majeur
Reconnue pour son architecture thermique unique
Patrimoine national tunisien"""
    },

    "sbeitla": {
        "general": """SBEITLA (SBEITLA) - SITE ROMAIN

Localisation : Gouvernorat de Kasserine, centre-ouest
Ancien nom : Sufetula
Particularité : Ensemble capitolin intact

Description :
Site romain bien conservé avec un ensemble capitolin unique en Afrique.

Monuments principaux :
- Arc de triomphe de Dioclétien
- Trois temples capitolin (Jupiter, Junon, Minerve)
- Théâtre
- Églises byzantines""",

        "histoire": """HISTOIRE SBEITLA

Fondation : Ier siècle ap. J.-C.
Apogée : IIIe-IVe siècles
Événement majeur : Bataille de Sufetula (647) marquant la conquête arabe
Période byzantine : Important centre chrétien""",

        "architecture": """ARCHITECTURE SBEITLA

Ensemble capitolin :
- Trois temples juxtaposés
- Accès par un escalier monumental
- Cour commune

Arc de Dioclétien :
- Porte d'entrée de la ville
- Dédié à la Tétrarchie""",

        "fouilles": """FOUILLES SBEITLA

Fouilles systématiques depuis 1900
Importantes découvertes byzantines
Restaurations du capitole dans les années 1970""",

        "unesco": """SBEITLA - PATRIMOINE

Candidature UNESCO en cours
Valeur : Ensemble capitolin exceptionnel
Conservation : Bon état général"""
    },

    "utique": {
        "general": """UTIQUE - ANCIEN PORT PUNIQUE

Localisation : Gouvernorat de Bizerte
Particularité : Plus ancienne fondation phénicienne en Tunisie
Fondation : 1101 av. J.-C.

Description :
Ancien port punique aujourd'hui à 10 km de la mer (ensablement).
Première capitale de la province d'Afrique romaine avant Carthage.

Monuments :
- Maisons romaines avec mosaïques
- Nécropoles puniques
- Thermes""",

        "histoire": """HISTOIRE UTIQUE

Fondation : 1101 av. J.-C. (selon Pline l'Ancien)
Rôle : Port principal avant Carthage
Guerres puniques : Base romaine
Ier siècle : Déclin au profit de Carthage
Cause : Ensablement du port""",

        "architecture": """ARCHITECTURE UTIQUE

Découvertes importantes :
- Mosaïques romaines (Maison de la Cascade)
- Habitat punique
- Installations portuaires

Problème : Site partiellement enfoui sous les alluvions""",

        "fouilles": """FOUILLES UTIQUE

Fouilles depuis le XIXe siècle
Découverte de riches demeures romaines
Problèmes : Niveau phréatique élevé""",

        "unesco": """UTIQUE - IMPORTANCE HISTORIQUE

Non inscrite à l'UNESCO
Importance : Plus ancien établissement phénicien
Site classé Monument Historique"""
    },

    "thuburbo_majus": {
        "general": """THUBURBO MAJUS - SITE ROMAIN

Localisation : Gouvernorat de Zaghouan
Période : Ier-IVe siècles ap. J.-C.
Particularité : Ville de garnison puis centre agricole

Description :
Cité romaine prospère grâce à la fertilité de la région.
Monuments bien conservés dans un cadre rural.

Principaux édifices :
- Capitole
- Temple de Baalat
- Marché (macellum)
- Thermes d'été et d'hiver""",

        "histoire": """HISTOIRE THUBURBO MAJUS

Origine : Camp militaire romain (Ier siècle av. J.-C.)
Développement : Colonie de vétérans
Apogée : IIe-IIIe siècles (production d'huile et de céréales)
Déclin : IVe siècle""",

        "architecture": """ARCHITECTURE THUBURBO MAJUS

Capitole :
- Temple bien conservé
- Escalier monumental
- Colonnade corinthienne

Thermes :
- Deux complexes (été/hiver)
- Système de chauffage visible""",

        "fouilles": """FOUILLES THUBURBO MAJUS

Fouilles débutées en 1912
Importantes découvertes épigraphiques
Site partiellement dégagé""",

        "unesco": """THUBURBO MAJUS - VILLE ROMAINE TYPIQUE

Exemple d'urbanisme romain en Afrique
Architecture bien préservée
Site classé Monument Historique"""
    },

    "makthar": {
        "general": """MAKTHAR (MACTARIS) - SITE NUMIDE-ROMAIN

Localisation : Gouvernorat de Siliana
Altitude : 900 m
Particularité : Transition numide-romaine bien documentée

Description :
Ancienne cité numide devenue romaine.
Site étendu avec monuments variés.

Monuments :
- Arc de triomphe de Trajan
- Capitole
- Théâtre
- Basiliques chrétiennes""",

        "histoire": """HISTOIRE MAKTHAR

Origine : Cité numide (IVe siècle av. J.-C.)
Intégration romaine : Ier siècle ap. J.-C.
Apogée : IIe-IIIe siècles
Période chrétienne : IVe-VIe siècles (siège épiscopal)""",

        "architecture": """ARCHITECTURE MAKTHAR

Arc de Trajan :
- Monument bien conservé
- Dédié à l'empereur Trajan
- Inscriptions importantes

Édifices chrétiens :
- Plusieurs basiliques
- Baptistère
- Églises à nefs multiples""",

        "fouilles": """FOUILLES MAKTHAR

Fouilles depuis 1900
Importantes inscriptions numides et latines
Site musée avec collections locales""",

        "unesco": """MAKTHAR - SITE MIXTE NUMIDE-ROMAIN

Valeur : Témoignage de la romanisation
Importance épigraphique
Site classé Monument Historique"""
    },

    "chemtou": {
        "general": """CHEMTOU (SIMITTHUS) - CARRIÈRES DE MARBRE

Localisation : Gouvernorat de Jendouba
Particularité : Carrières de marbre jaune antique
Période : IIe siècle av. J.-C. - IVe siècle ap. J.-C.

Description :
Site célèbre pour ses carrières de marbre numidique (giallo antico).
Marbre exporté dans tout l'Empire romain.

Monuments :
- Carrières antiques
- Ville des ouvriers
- Sanctuaire
- Musée du marbre""",

        "histoire": """HISTOIRE CHEMTOU

Exploitation début : IIe siècle av. J.-C. (période numide)
Apogée : Époque romaine (Ier-IIIe siècles)
Production : Marbre pour monuments impériaux
Abandon : IVe siècle ap. J.-C.""",

        "architecture": """ARCHITECTURE CHEMTOU

Carrières :
- Fronts de taille visibles
- Techniques d'extraction romaines
- Rampes et voies d'évacuation

Ville ouvrière :
- Habitat modeste
- Ateliers de transformation
- Sanctuaire des carrières""",

        "fouilles": """FOUILLES CHEMTOU

Fouilles tuniso-allemandes depuis 1965
Découverte des techniques d'extraction
Musée archéologique sur site""",

        "unesco": """CHEMTOU - PATRIMOINE INDUSTRIEL ANTIQUE

Importance : Carrières impériales romaines
Valeur : Témoignage technologique
Site classé Monument Historique"""
    }
}

def generate_documents():
    """Génère les 50 documents"""
    print("\n🔧 Début de la génération...")
    print("-" * 50)
    
    total_created = 0
    
    for site_name, documents in SITES_COMPLET.items():
        print(f"\n🏛️  Traitement du site : {site_name.upper()}")
        
        for doc_type, content in documents.items():
            # Nom du fichier
            filename = f"{site_name}_{doc_type}.txt"
            filepath = os.path.join("data", filename)
            
            # Vérifier si le fichier existe déjà
            if os.path.exists(filepath):
                print(f"   ⚠️  {filename} existe déjà - écrasement")
            
            # Écrire le fichier
            with open(filepath, 'w', encoding='utf-8') as f:
                # En-tête standardisé
                f.write("=" * 60 + "\n")
                f.write(f"SITE ARCHÉOLOGIQUE : {site_name.upper()}\n")
                f.write(f"TYPE DE DOCUMENT : {doc_type.upper()}\n")
                f.write(f"RÉFÉRENCE : TN-ARCH-{site_name[:3].upper()}-{doc_type[:3].upper()}\n")
                f.write("=" * 60 + "\n\n")
                
                # Contenu principal
                f.write(content + "\n\n")
                
                # Pied de page
                f.write("-" * 60 + "\n")
                f.write("SOURCE : Institut National du Patrimoine Tunisien\n")
                f.write("DERNIÈRE MISE À JOUR : Décembre 2024\n")
                f.write("STATUT : Document public - Usage pédagogique\n")
                f.write("=" * 60 + "\n")
            
            total_created += 1
            print(f"   ✅ {filename}")
    
    return total_created

def count_existing_files():
    """Compte les fichiers existants"""
    if not os.path.exists("data"):
        return 0
    
    files = [f for f in os.listdir("data") if f.endswith('.txt')]
    return len(files)

def main():
    """Fonction principale"""
    
    # Compter les fichiers existants
    existing = count_existing_files()
    print(f"📁 Fichiers existants dans data/ : {existing}")
    
    # Générer les documents
    created = generate_documents()
    
    # Compter le total final
    final_count = count_existing_files()
    
    # Afficher les résultats
    print("\n" + "=" * 70)
    print("📊 RÉSULTATS DE LA GÉNÉRATION")
    print("=" * 70)
    
    print(f"\n✅ DOCUMENTS GÉNÉRÉS : {created}")
    print(f"📁 TOTAL FINAL : {final_count} fichiers")
    
    # Liste des sites traités
    sites = list(SITES_COMPLET.keys())
    print(f"\n🏛️  SITES TRAITÉS ({len(sites)}) :")
    for i, site in enumerate(sites, 1):
        print(f"   {i:2}. {site.upper()}")
    
    # Vérifier l'objectif
    if final_count >= 50:
        print(f"\n🎉 OBJECTIF ATTEINT ! {final_count}/50 documents")
    else:
        print(f"\n⚠️  OBJECTIF PARTIEL : {final_count}/50 documents")
    
    # Afficher quelques exemples
    print("\n📋 EXEMPLES DE FICHIERS CRÉÉS :")
    sample_files = [f"{site}_general.txt" for site in list(SITES_COMPLET.keys())[:3]]
    for file in sample_files:
        print(f"   • {file}")
    
    print("\n💾 EMPLACEMENT : data/")
    print("🔧 PRÊT POUR L'INGESTION DANS CHROMADB")

if __name__ == "__main__":
    main()