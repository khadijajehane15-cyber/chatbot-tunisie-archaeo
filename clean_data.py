import os
import re

# Chemin vers le dossier data
DATA_PATH = "data"

def clean_text(text):
    """
    Nettoie le texte : enlève les caractères spéciaux, espaces multiples, etc.
    """
    # Enlever les espaces multiples
    text = re.sub(r'\s+', ' ', text)
    
    # Enlever les retours à la ligne inutiles
    text = text.replace('\n', ' ').replace('\r', ' ')
    
    # Standardiser les guillemets
    text = text.replace('"', "'")
    
    # Supprimer les espaces au début et à la fin
    text = text.strip()
    
    return text

def read_and_clean_files():
    """
    Lit tous les fichiers texte du dossier data et les nettoie
    """
    cleaned_documents = []
    
    # Lister tous les fichiers .txt dans le dossier data
    for filename in os.listdir(DATA_PATH):
        if filename.endswith('.txt'):
            filepath = os.path.join(DATA_PATH, filename)
            
            print(f"📖 Lecture de : {filename}")
            
            # Lire le fichier
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Nettoyer le texte
            cleaned_content = clean_text(content)
            
            # Ajouter des métadonnées
            document = {
                'filename': filename,
                'content': cleaned_content,
                'site': filename.replace('.txt', '').capitalize(),
                'source': 'INP Tunisie / UNESCO'  # Tu peux adapter selon tes sources
            }
            
            cleaned_documents.append(document)
            
            print(f"   ✓ Nettoyé : {len(cleaned_content)} caractères")
    
    return cleaned_documents

def save_cleaned_data(documents, output_file="cleaned_documents.txt"):
    """
    Sauvegarde les documents nettoyés dans un fichier pour vérification
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        for doc in documents:
            f.write(f"=== {doc['site']} ===\n")
            f.write(f"Fichier : {doc['filename']}\n")
            f.write(f"Source : {doc['source']}\n")
            f.write("-" * 50 + "\n")
            f.write(doc['content'])
            f.write("\n\n" + "="*50 + "\n\n")
    
    print(f"\n💾 Données sauvegardées dans : {output_file}")

def main():
    """
    Fonction principale
    """
    print("🔧 Début du nettoyage des données...")
    print("-" * 40)
    
    # 1. Lire et nettoyer les fichiers
    documents = read_and_clean_files()
    
    # 2. Afficher un résumé
    print(f"\n✅ Nettoyage terminé !")
    print(f"📊 Résumé :")
    print(f"   - Documents traités : {len(documents)}")
    
    total_chars = sum(len(doc['content']) for doc in documents)
    print(f"   - Total de caractères : {total_chars}")
    
    for doc in documents:
        print(f"   • {doc['site']} : {len(doc['content'])} caractères")
    
    # 3. Sauvegarder pour vérification
    save_cleaned_data(documents)
    
    # 4. Retourner les documents pour l'étape suivante
    return documents

# Exécuter le script si appelé directement
if __name__ == "__main__":
    cleaned_docs = main()
    
    # Afficher un exemple
    if cleaned_docs:
        print(f"\n📄 Exemple du premier document nettoyé :")
        print("-" * 40)
        print(cleaned_docs[0]['content'][:500] + "...")  # Premiers 500 caractères