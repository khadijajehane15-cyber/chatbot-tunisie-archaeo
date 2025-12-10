import chromadb
from sentence_transformers import SentenceTransformer
import ollama
import time

print("=" * 60)
print("🤖 CHATBOT RAG - Gemma3:1b (Léger et rapide)")
print("=" * 60)

# Initialisation
print("\n🔧 Initialisation...")

# 1. Modèle d'embedding
print("📊 Chargement du modèle d'embedding...")
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# 2. Connexion à ChromaDB
print("💾 Connexion à la base de données...")
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection("sites_archeo_tunisie")

# 3. Vérification du modèle
print("🧠 Vérification du modèle Gemma3:1b...")
try:
    # Tester avec un petit prompt
    test_response = ollama.chat(
        model='gemma3:1b',
        messages=[{'role': 'user', 'content': 'Test'}],
        options={'num_gpu': 1, 'num_thread': 2}  # Utilise un peu de GPU
    )
    print("✅ Gemma3:1b fonctionne !")
    print(f"   Test: {test_response['message']['content'][:50]}...")
except Exception as e:
    print(f"⚠️  Erreur: {str(e)[:100]}")
    print("🔧 Passage en mode CPU...")

print("\n" + "✅ SYSTÈME PRÊT !".center(60))
print("-" * 60)

def recherche_documents(question, top_k=2):
    """Recherche les documents pertinents"""
    question_embedding = embedding_model.encode(question).tolist()
    
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=top_k
    )
    
    return results

def generer_reponse_gemma(question, documents, metadatas):
    """Génère une réponse avec Gemma3:1b"""
    # Contexte simple
    contexte = ""
    for i, (doc, meta) in enumerate(zip(documents, metadatas)):
        contexte += f"[Source {i+1}: {meta['site']}]\n{doc[:500]}\n\n"
    
    # Prompt court (important pour modèle léger)
    prompt = f"""Contexte:
{contexte}

Question: {question}

Réponds brièvement en français avec les informations ci-dessus. Cite [Source X]."""

    try:
        start_time = time.time()
        
        response = ollama.chat(
            model='gemma3:1b',
            messages=[{'role': 'user', 'content': prompt}],
            options={
                'num_gpu': 1,      # Essaie avec un peu de GPU
                'num_thread': 2,   # Peu de threads
                'temperature': 0.1 # Très factuel
            }
        )
        
        end_time = time.time()
        print(f"   ⏱️  Temps de réponse: {end_time - start_time:.1f}s")
        
        return response['message']['content']
        
    except Exception as e:
        # Fallback en mode CPU
        print(f"   ⚠️  Essai en mode CPU...")
        try:
            response = ollama.chat(
                model='gemma3:1b',
                messages=[{'role': 'user', 'content': prompt}],
                options={'num_gpu': 0, 'num_thread': 2}
            )
            return response['message']['content']
        except:
            # Réponse très simple
            if documents:
                return f"D'après {metadatas[0]['site']} : {documents[0][:150]}..."
            return "Information non disponible."

def chatbot_principal():
    """Boucle principale"""
    print("\n💬 Pose des questions sur Carthage, Dougga, El Jem, Kerkouane")
    print("   'quit'=quitter, 'sites'=liste")
    print("-" * 60)
    
    while True:
        question = input("\n👉 Question : ").strip()
        
        if question.lower() == 'quit':
            print("\n👋 Au revoir !")
            break
            
        elif question.lower() == 'sites':
            print("\n📚 SITES:")
            print("   • Carthage - Banlieue de Tunis")
            print("   • Dougga - Nord-ouest (Béja)")
            print("   • El Jem - Centre-est (Mahdia)")
            print("   • Kerkouane - Cap Bon")
            continue
        
        if not question:
            continue
        
        print("🔍 Recherche...", end='', flush=True)
        
        # Recherche
        results = recherche_documents(question)
        
        if not results['documents'][0]:
            print("\n❌ Aucun document trouvé.")
            continue
        
        print("✓")
        print("🧠 Génération...", end='', flush=True)
        
        # Génération
        documents = results['documents'][0]
        metadatas = results['metadatas'][0]
        
        reponse = generer_reponse_gemma(question, documents, metadatas)
        
        print("✓")
        
        # Affichage
        print("\n" + "📋 RÉPONSE " + "─" * 46)
        print(reponse)
        print("─" * 60)
        
        print("📚 SOURCES:")
        for i, meta in enumerate(metadatas):
            print(f"   {i+1}. {meta['site']}")

if __name__ == "__main__":
    chatbot_principal()