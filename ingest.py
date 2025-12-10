import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
import os
# ============ AJOUTE CETTE FONCTION ============
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
# ============ FIN DE L'AJOUT ============
# Charger le modèle pour les embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')

def setup_chromadb():
    """
    Configure et initialise ChromaDB
    """
    print("🔧 Configuration de ChromaDB...")
    
    # Chemin pour stocker la base de données
    chroma_path = "./chroma_db"
    
    # Créer le client ChromaDB
    client = chromadb.PersistentClient(path=chroma_path)
    
    # Créer ou récupérer la collection
    collection_name = "sites_archeo_tunisie"
    
    try:
        # Essayer de récupérer la collection existante
        collection = client.get_collection(collection_name)
        print(f"📂 Collection existante chargée : {collection_name}")
    except:
        # Créer une nouvelle collection
        collection = client.create_collection(
            name=collection_name,
            metadata={"description": "Sites archéologiques de Tunisie"}
        )
        print(f"🆕 Nouvelle collection créée : {collection_name}")
    
    return client, collection
def prepare_chunks_for_ingestion():
    """
    Prépare les chunks à partir de tous les fichiers .txt dans data/
    """
    import os
    print("📄 Préparation des chunks depuis tous les documents...")
    
    all_chunks = []
    chunk_metadata = []
    
    # Lister tous les fichiers .txt
    txt_files = [f for f in os.listdir("data") if f.endswith('.txt')]
    print(f"   📁 {len(txt_files)} fichiers .txt trouvés")
    
    for filename in txt_files:
        filepath = os.path.join("data", filename)
        
        try:
            # Lire le fichier
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Nettoyer un peu
            import re
            content = re.sub(r'\s+', ' ', content).strip()
            
            # Découper en chunks (appelle la fonction chunk_text qui existe déjà)
            chunks = chunk_text(content, chunk_size=350, overlap=50)
            
            # Extraire le nom du site (premier mot avant _)
            site_name = filename.split('_')[0].capitalize()
            
            print(f"   ✅ {filename}: {len(chunks)} chunks")
            
            # Ajouter chaque chunk
            for i, chunk in enumerate(chunks):
                all_chunks.append(chunk)
                
                metadata = {
                    'chunk_id': f"{filename}_chunk_{i}",
                    'document': filename,
                    'site': site_name,
                    'source': 'INP Tunisie / UNESCO',
                    'chunk_number': i,
                    'total_chunks_doc': len(chunks)
                }
                chunk_metadata.append(metadata)
                
        except Exception as e:
            print(f"   ❌ Erreur avec {filename}: {e}")
    
    print(f"\n📊 Total chunks créés : {len(all_chunks)}")
    return all_chunks, chunk_metadata

def create_embeddings(chunks):
    """
    Crée les embeddings pour tous les chunks
    """
    print("🧠 Création des embeddings...")
    
    # Créer les embeddings avec le modèle
    embeddings = model.encode(chunks).tolist()
    
    print(f"✅ {len(embeddings)} embeddings créés")
    return embeddings

def ingest_to_chromadb(collection, chunks, metadata, embeddings):
    """
    Ingère les données dans ChromaDB
    """
    print("📥 Ingestion dans ChromaDB...")
    
    # Préparer les IDs
    ids = [meta['chunk_id'] for meta in metadata]
    
    # Ajouter les documents à la collection
    collection.add(
        embeddings=embeddings,
        documents=chunks,
        metadatas=metadata,
        ids=ids
    )
    
    print(f"✅ {len(chunks)} documents ingérés")
    
    # Vérifier le compte
    count = collection.count()
    print(f"📊 Total dans la collection : {count} documents")

def test_search(collection):
    """
    Teste la recherche dans ChromaDB
    """
    print("\n🔍 Test de recherche...")
    
    # Question test
    test_query = "théâtre romain"
    print(f"Question test : '{test_query}'")
    
    # Créer l'embedding pour la question
    query_embedding = model.encode(test_query).tolist()
    
    # Rechercher
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )
    
    print(f"📄 {len(results['documents'][0])} résultats trouvés :")
    
    for i, (doc, metadata) in enumerate(zip(results['documents'][0], results['metadatas'][0])):
        print(f"\n--- Résultat {i+1} ---")
        print(f"Site : {metadata['site']}")
        print(f"Source : {metadata['document']}")
        print(f"Texte : {doc[:150]}...")  # Premiers 150 caractères
        print(f"Distance : {results['distances'][0][i]:.4f}")

def main():
    """
    Fonction principale
    """
    print("🚀 DÉBUT DE L'INGESTION DANS CHROMADB")
    print("=" * 40)
    
    # 1. Configurer ChromaDB
    client, collection = setup_chromadb()
    
    # 2. Préparer les chunks
    chunks, metadata = prepare_chunks_for_ingestion()
    if not chunks:
        print("❌ Échec de la préparation des chunks")
        return
    
    # 3. Créer les embeddings
    embeddings = create_embeddings(chunks)
    
    # 4. Ingérer dans ChromaDB
    ingest_to_chromadb(collection, chunks, metadata, embeddings)
    
    # 5. Tester la recherche
    test_search(collection)
    
    print("\n✅ INGESTION TERMINÉE !")
    print(f"📁 Base de données stockée dans : ./chroma_db")

# Exécuter le script si appelé directement
if __name__ == "__main__":
    main()