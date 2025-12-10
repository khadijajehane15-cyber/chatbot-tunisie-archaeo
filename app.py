import streamlit as st
import chromadb
from sentence_transformers import SentenceTransformer
import ollama
import time

# Configuration
st.set_page_config(
    page_title="Chatbot Archéologie Tunisie",
    page_icon="🏛️",
    layout="wide"
)

# Cache pour optimiser
@st.cache_resource
def load_models():
    """Charge les modèles une fois"""
    # Modèle d'embedding
    embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # Connexion ChromaDB
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_collection("sites_archeo_tunisie")
    
    return embedding_model, collection

def search_documents(question, top_k=3):
    """Recherche les documents pertinents"""
    embedding_model, collection = load_models()
    
    # Créer l'embedding
    question_embedding = embedding_model.encode(question).tolist()
    
    # Rechercher
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=top_k
    )
    
    return results

def generate_response(question, context_results):
    """Génère une réponse avec gemma3:1b"""
    if not context_results['documents'][0]:
        return "Je ne trouve pas d'information sur ce sujet dans ma base de données.", []
    
    docs = context_results['documents'][0]
    metas = context_results['metadatas'][0]
    
    # Construire le contexte
    contexte = ""
    for i, (doc, meta) in enumerate(zip(docs, metas)):
        contexte += f"\n[Source {i+1} - {meta['site']}]\n{doc[:400]}\n"
    
    # Prompt optimisé pour gemma3:1b
    prompt = f"""Tu es un expert en archéologie tunisienne.

CONTEXTE :{contexte}

QUESTION : {question}

Réponds en français en utilisant uniquement le contexte ci-dessus.
Sois précis et cite tes sources : [Source X - Site]"""

    try:
        # Générer avec gemma3:1b
        response = ollama.chat(
            model='gemma3:1b',
            messages=[{'role': 'user', 'content': prompt}],
            options={
                'num_gpu': 0,      # CPU seulement
                'temperature': 0.1, # Très factuel
                'num_predict': 200  # Réponse courte
            }
        )
        
        return response['message']['content'], metas
        
    except Exception as e:
        # Fallback simple
        st.error(f"Erreur avec le modèle : {str(e)[:100]}")
        if docs:
            return f"D'après {metas[0]['site']} : {docs[0][:200]}...", metas
        return "Erreur de génération.", []

def main():
    """Interface principale"""
    
    # Sidebar
    with st.sidebar:
        st.title("🏛️ Information")
        st.markdown("""
        **Chatbot RAG - Sites Archéologiques de Tunisie**
        
        **Technologie :**
        - Modèle : **gemma3:1b** (léger et rapide)
        - Base : **ChromaDB** avec 50+ documents
        - Recherche : **RAG** (Retrieval-Augmented Generation)
        
        **Sites disponibles (10) :**
        - Carthage, Dougga, El Jem, Kerkouane
        - Bulla Regia, Sbeitla, Utique
        - Thuburbo Majus, Makthar, Chemtou
        """)
        
        st.markdown("---")
        st.markdown("**Exemples de questions :**")
        st.markdown("- Où se trouve Carthage ?")
        st.markdown("- Quelle est la capacité du théâtre de Dougga ?")
        st.markdown("- Quelle est la particularité de Kerkouane ?")
        st.markdown("- Quels sites sont classés UNESCO ?")
        
        st.markdown("---")
        # Statistiques
        try:
            _, collection = load_models()
            count = collection.count()
            st.markdown(f"**📊 Statistiques :**")
            st.markdown(f"- Chunks dans la base : **{count}**")
            st.markdown(f"- Modèle : **gemma3:1b**")
        except:
            pass
    
    # Zone principale
    st.title("🏛️ Chatbot des Sites Archéologiques de Tunisie")
    st.markdown("Posez vos questions sur les 10 sites archéologiques tunisiens")
    
    # Initialiser l'historique
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Afficher l'historique
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
            if "sources" in message and message["sources"]:
                with st.expander("📚 Voir les sources"):
                    for source in message["sources"]:
                        st.markdown(f"• {source}")
    
    # Zone de saisie
    if prompt := st.chat_input("Posez votre question ici..."):
        # Ajouter la question à l'historique
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Afficher la question
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Afficher un indicateur de chargement
        with st.chat_message("assistant"):
            with st.spinner("Recherche dans 50 documents..."):
                # Rechercher les documents
                search_results = search_documents(prompt)
                
                # Générer la réponse
                start_time = time.time()
                response, sources_meta = generate_response(prompt, search_results)
                elapsed_time = time.time() - start_time
                
                # Afficher la réponse
                st.markdown(response)
                
                # Afficher les sources
                if sources_meta:
                    with st.expander(f"📚 Sources utilisées ({len(sources_meta)})"):
                        for i, meta in enumerate(sources_meta):
                            st.markdown(f"{i+1}. **{meta['site']}** - *{meta['document']}*")
                    
                    # Préparer pour l'historique
                    sources_list = [f"{meta['site']} ({meta['document']})" for meta in sources_meta]
                else:
                    sources_list = []
                
                # Afficher le temps
                st.caption(f"⏱️ Généré en {elapsed_time:.1f} secondes")
        
        # Ajouter la réponse à l'historique
        st.session_state.messages.append({
            "role": "assistant", 
            "content": response,
            "sources": sources_list
        })
    
    # Bouton pour effacer
    if st.sidebar.button("🧹 Effacer l'historique"):
        st.session_state.messages = []
        st.rerun()

if __name__ == "__main__":
    main()