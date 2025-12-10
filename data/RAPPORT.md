\# Rapport - Chatbot RAG Sites Archéologiques Tunisie



\## 1. Introduction

Projet de chatbot intelligent spécialisé sur l'archéologie tunisienne utilisant RAG (Retrieval-Augmented Generation).



\## 2. Architecture

\- \*\*LLM\*\* : Gemma3:1b via Ollama

\- \*\*Base vectorielle\*\* : ChromaDB

\- \*\*Embeddings\*\* : all-MiniLM-L6-v2

\- \*\*Interface\*\* : Streamlit

\- \*\*Données\*\* : 54 documents sur 10 sites



\## 3. Difficultés

1\. \*\*Mémoire GPU limitée\*\* → Passage à Gemma3:1b

2\. \*\*Configuration Ollama\*\* → Mode CPU forcé

3\. \*\*Gestion 50+ documents\*\* → Optimisation chunking



\## 4. Résultats

\- Chatbot fonctionnel avec réponses sourcées

\- Interface web intuitive

\- Absence d'hallucinations vérifiée

\- 54 documents traités, 10 sites couverts



\## 5. Conclusion

Projet réussi démontrant le pipeline RAG complet.

