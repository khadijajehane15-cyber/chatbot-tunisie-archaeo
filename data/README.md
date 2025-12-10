\# Chatbot RAG - Sites Archéologiques de Tunisie



\## Description

Chatbot intelligent spécialisé sur les sites archéologiques tunisiens utilisant l'architecture RAG (Retrieval-Augmented Generation).



\## Installation

1\. Installer Python 3.10+

2\. `python -m venv venv`

3\. `venv\\Scripts\\activate` (Windows)

4\. `pip install -r requirements.txt`

5\. Installer Ollama : https://ollama.com

6\. `ollama pull gemma3:1b`



\## Utilisation

\- Créer la base : `python ingest.py`

\- Tester : `python rag.py`

\- Interface web : `streamlit run app.py`



\## Données

54 documents sur 10 sites : Carthage, Dougga, El Jem, Kerkouane, Bulla Regia, Sbeitla, Utique, Thuburbo Majus, Makthar, Chemtou



\## Auteur

\[TON NOM] - Projet IA Générative

