import chromadb
from sentence_transformers import SentenceTransformer
import ollama
import sys

class RAGChatbot:
    def __init__(self):
        """
        Initialise le chatbot RAG avec gemma3:1b
        """
        print("🤖 Initialisation du chatbot RAG...")
        
        # 1. Charger le modèle d'embedding
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        print("✅ Modèle d'embedding chargé")
        
        # 2. Se connecter à ChromaDB
        self.chroma_client = chromadb.PersistentClient(path="./chroma_db")
        self.collection = self.chroma_client.get_collection("sites_archeo_tunisie")
        print("✅ Base de données ChromaDB connectée")
        
        # 3. Vérifier le modèle gemma3:1b
        print("🔍 Vérification du modèle gemma3:1b...")
        try:
            models = ollama.list()
            model_names = [m['name'] for m in models['models']]
            
            if 'gemma3:1b' in model_names:
                print("✅ gemma3:1b disponible")
            else:
                print("⚠️  gemma3:1b non trouvé")
                print("   Télécharge avec: ollama pull gemma3:1b")
                
        except Exception as e:
            print(f"⚠️  Erreur Ollama: {str(e)[:50]}")
        
        print("🚀 Chatbot RAG prêt !")
        print("-" * 40)
    
    def search_in_chromadb(self, question, top_k=3):
        """
        Recherche les documents pertinents dans ChromaDB
        """
        # Créer l'embedding de la question
        question_embedding = self.embedding_model.encode(question).tolist()
        
        # Rechercher dans ChromaDB
        results = self.collection.query(
            query_embeddings=[question_embedding],
            n_results=top_k
        )
        
        return results
    
    def build_prompt(self, question, search_results):
        """
        Construit le prompt pour le LLM
        """
        # Extraire les documents et métadonnées
        documents = search_results['documents'][0]
        metadatas = search_results['metadatas'][0]
        
        # Construire le contexte
        context_parts = []
        for i, (doc, meta) in enumerate(zip(documents, metadatas)):
            context_parts.append(f"[Source {i+1}: {meta['site']}]")
            context_parts.append(doc[:500])  # Limiter la longueur
            context_parts.append("")
        
        context = "\n".join(context_parts)
        
        # Prompt optimisé pour gemma3:1b
        prompt = f"""Tu es un expert en archéologie tunisienne.

INFORMATIONS DISPONIBLES:
{context}

QUESTION: {question}

INSTRUCTIONS:
1. Réponds en français
2. Utilise UNIQUEMENT les informations ci-dessus
3. Sois précis et factuel
4. Cite tes sources comme [Source X]
5. Si l'information n'est pas disponible, dis-le clairement

RÉPONSE:"""
        
        return prompt, metadatas
    
    def generate_answer(self, prompt):
        """
        Génère une réponse avec gemma3:1b via Ollama
        """
        try:
            # Appeler gemma3:1b avec options CPU
            response = ollama.chat(
                model='gemma3:1b',
                messages=[
                    {
                        'role': 'user',
                        'content': prompt
                    }
                ],
                options={
                    'num_gpu': 0,      # Force CPU
                    'temperature': 0.1, # Faible créativité
                    'num_predict': 200  # Réponse courte
                }
            )
            
            return response['message']['content']
            
        except Exception as e:
            return f"❌ Erreur avec le modèle : {str(e)[:100]}"
    
    def ask_question(self, question):
        """
        Pose une question au chatbot
        """
        print(f"\n❓ Question : {question}")
        print("🔍 Recherche dans la base de données...")
        
        # 1. Rechercher dans ChromaDB
        search_results = self.search_in_chromadb(question, top_k=3)
        
        # Vérifier si on a des résultats
        if not search_results['documents'][0]:
            return "Je ne trouve pas d'information sur ce sujet dans ma base de données.", []
        
        # 2. Construire le prompt
        prompt, metadatas = self.build_prompt(question, search_results)
        
        # 3. Générer la réponse
        print("🧠 Génération de la réponse avec gemma3:1b...")
        answer = self.generate_answer(prompt)
        
        # 4. Préparer les sources
        sources = []
        for i, meta in enumerate(metadatas):
            sources.append(f"{i+1}. {meta['site']} - {meta['document']}")
        
        return answer, sources
    
    def chat_loop(self):
        """
        Boucle de chat interactive
        """
        print("\n" + "="*50)
        print("💬 CHATBOT RAG - SITES ARCHÉOLOGIQUES TUNISIENS")
        print("="*50)
        print("Modèle : gemma3:1b (léger et rapide)")
        print("Commandes : 'quit'=quitter, 'sources'=liste")
        print("-"*50)
        
        while True:
            # Poser une question
            question = input("\n👉 Pose ta question : ").strip()
            
            # Commandes spéciales
            if question.lower() in ['quit', 'exit', 'q']:
                print("👋 Au revoir !")
                break
                
            elif question.lower() == 'sources':
                print("\n📚 Sources disponibles :")
                count = self.collection.count()
                print(f"   {count} chunks dans la base de données")
                
                # Compter les sites uniques
                all_docs = self.collection.get()
                if all_docs and 'metadatas' in all_docs:
                    sites = set()
                    for meta in all_docs['metadatas']:
                        if meta and 'site' in meta:
                            sites.add(meta['site'])
                    print(f"   Sites : {', '.join(sorted(sites))}")
                continue
            
            elif not question:
                continue
            
            # Générer une réponse
            try:
                answer, sources = self.ask_question(question)
                
                print("\n🤖 RÉPONSE :")
                print("-" * 40)
                print(answer)
                print("-" * 40)
                
                if sources:
                    print("\n📚 SOURCES :")
                    for source in sources:
                        print(f"   • {source}")
                    
            except Exception as e:
                print(f"❌ Erreur : {e}")

def main():
    """
    Fonction principale
    """
    # Créer le chatbot
    chatbot = RAGChatbot()
    
    # Démarrer la boucle de chat
    chatbot.chat_loop()

# Exécuter le script si appelé directement
if __name__ == "__main__":
    main()