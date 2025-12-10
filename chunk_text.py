from sentence_transformers import SentenceTransformer
import re

# Charger le modèle pour les embeddings (on l'utilisera plus tard)
model = SentenceTransformer('all-MiniLM-L6-v2')

def chunk_text(text, chunk_size=300, overlap=50):
    """
    Découpe un texte en chunks avec chevauchement
    """
    # Séparer le texte en mots
    words = text.split()
    
    chunks = []
    
    # Découper avec chevauchement
    for i in range(0, len(words), chunk_size - overlap):
        # Créer un chunk
        chunk = " ".join(words[i:i + chunk_size])
        
        # Vérifier que le chunk n'est pas vide
        if chunk.strip():
            chunks.append(chunk)
            
            # Arrêter si on a dépassé la longueur du texte
            if i + chunk_size >= len(words):
                break
    
    return chunks

def create_chunks_from_documents(documents, chunk_size=300, overlap=50):
    """
    Crée des chunks à partir de tous les documents
    """
    all_chunks = []
    chunk_metadata = []
    
    for doc in documents:
        # Créer les chunks pour ce document
        chunks = chunk_text(doc['content'], chunk_size, overlap)
        
        print(f"📄 {doc['site']} : {len(chunks)} chunks créés")
        
        # Ajouter chaque chunk avec ses métadonnées
        for i, chunk in enumerate(chunks):
            all_chunks.append(chunk)
            
            # Métadonnées pour ce chunk
            metadata = {
                'chunk_id': f"{doc['filename']}_chunk_{i}",
                'document': doc['filename'],
                'site': doc['site'],
                'source': doc['source'],
                'chunk_number': i,
                'total_chunks_doc': len(chunks)
            }
            chunk_metadata.append(metadata)
    
    return all_chunks, chunk_metadata

def save_chunks_to_file(chunks, metadata, filename="chunks_output.txt"):
    """
    Sauvegarde les chunks dans un fichier pour vérification
    """
    with open(filename, 'w', encoding='utf-8') as f:
        for i, (chunk, meta) in enumerate(zip(chunks, metadata)):
            f.write(f"=== CHUNK {i+1} ===\n")
            f.write(f"Document : {meta['document']}\n")
            f.write(f"Site : {meta['site']}\n")
            f.write(f"Source : {meta['source']}\n")
            f.write(f"Chunk {meta['chunk_number']+1}/{meta['total_chunks_doc']}\n")
            f.write("-" * 50 + "\n")
            f.write(chunk)
            f.write("\n\n" + "="*50 + "\n\n")
    
    print(f"💾 Chunks sauvegardés dans : {filename}")

def main():
    """
    Fonction principale - lit les données nettoyées et crée les chunks
    """
    print("✂️  Début du découpage en chunks...")
    print("-" * 40)
    
    # Importer la fonction de nettoyage depuis le script précédent
    try:
        from clean_data import read_and_clean_files
        
        # Lire et nettoyer les fichiers
        documents = read_and_clean_files()
        
        # Créer les chunks
        chunks, metadata = create_chunks_from_documents(
            documents, 
            chunk_size=300,  # Taille des chunks (en mots)
            overlap=50       # Chevauchement entre chunks
        )
        
        # Afficher un résumé
        print(f"\n✅ Découpage terminé !")
        print(f"📊 Résumé :")
        print(f"   - Documents traités : {len(documents)}")
        print(f"   - Chunks créés : {len(chunks)}")
        
        # Calculer la taille moyenne des chunks
        avg_chunk_length = sum(len(chunk.split()) for chunk in chunks) / len(chunks)
        print(f"   - Taille moyenne des chunks : {avg_chunk_length:.1f} mots")
        
        # Sauvegarder les chunks
        save_chunks_to_file(chunks, metadata)
        
        # Afficher un exemple
        print(f"\n📄 Exemple de chunk :")
        print("-" * 40)
        if chunks:
            print(f"Chunk 1 (document: {metadata[0]['document']}) :")
            print(chunks[0][:200] + "...")  # Premiers 200 caractères
            
        # Retourner les chunks pour l'étape suivante
        return chunks, metadata
        
    except ImportError as e:
        print(f"❌ Erreur : {e}")
        print("Assure-toi que clean_data.py est dans le même dossier")
        return None, None

# Exécuter le script si appelé directement
if __name__ == "__main__":
    chunks, metadata = main()