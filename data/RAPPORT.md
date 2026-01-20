# 📘 Rapport de Projet  
## Chatbot RAG sur les Sites Archéologiques de Tunisie

---

## 📝 Résumé

Ce projet consiste à développer un **chatbot intelligent basé sur l’architecture Retrieval-Augmented Generation (RAG)**, capable de répondre aux questions des utilisateurs sur les **sites archéologiques de Tunisie**.  

Le système combine une **recherche sémantique** sur des documents réels avec un **modèle de langage (LLM)** afin de fournir des réponses pertinentes, fiables et compréhensibles.

---

## 🔑 Mots-clés

Chatbot, RAG, Intelligence Artificielle, LLM, Recherche sémantique, Patrimoine, Tunisie

---

## 1️⃣ Introduction

L’intelligence artificielle, et plus particulièrement les **modèles de langage**, permet aujourd’hui de créer des systèmes capables de comprendre et de générer du texte en langage naturel.  

Dans ce contexte, ce projet vise à appliquer l’architecture **RAG** à un domaine culturel : **le patrimoine archéologique tunisien**, afin de faciliter l’accès à l’information.

---

## 2️⃣ Objectifs du Projet

| Objectif                  | Description                                               |
| ------------------------- | --------------------------------------------------------- |
| Compréhension du langage  | Interpréter des questions formulées naturellement         |
| Exploitation documentaire | Utiliser des documents réels sur les sites archéologiques |
| Qualité des réponses      | Générer des réponses claires et fiables                   |
| Accessibilité             | Proposer une interface simple pour l’utilisateur          |

---

## 3️⃣ Architecture Générale du Système

### 🔹 Principe de l’architecture RAG

Documents (PDF / TXT / HTML)
            ↓
     Prétraitement
 (Nettoyage + Chunking)
            ↓
      Embeddings
   (Vectorisation)
            ↓
 Base de données vectorielle
            ↓
      Question utilisateur
            ↓
   Recherche sémantique
            ↓
      Modèle LLM
 (Réponse augmentée)
            ↓
     Interface utilisateur

---

## 4️⃣ Méthodologie Adoptée

| Étape                | Description                                            |
| -------------------- | ------------------------------------------------------ |
| Collecte des données | Récupération de documents sur les sites archéologiques |
| Prétraitement        | Nettoyage et découpage des textes                      |
| Indexation           | Création et stockage des embeddings                    |
| Recherche            | Sélection des informations pertinentes                 |
| Génération           | Production de la réponse par le LLM                    |

---

## 5️⃣ Technologies Utilisées

| Composant | Technologie                 | Rôle                    |
| --------- | --------------------------- | ----------------------- |
| Langage   | Python                      | Développement du projet |
| Modèle IA | LLM open-source (Ollama)    | Génération des réponses |
| Recherche | Base de données vectorielle | Recherche sémantique    |
| Interface | Streamlit                   | Interaction utilisateur |

---

## 6️⃣ Interface Utilisateur

L’interface développée permet :

. La saisie de questions en langage naturel

. L’affichage des réponses générées

. La consultation des sources utilisées

. Une navigation simple et intuitive

🎯 Objectif : masquer la complexité technique tout en offrant une bonne expérience utilisateur.

---

## 7️⃣ Difficultés Rencontrées et Solutions

| Problème                 | Solution                                 |
| ------------------------ | ---------------------------------------- |
| Mémoire GPU insuffisante | Utilisation de modèles plus légers       |
| Instabilité du modèle    | Amélioration de la gestion des appels    |
| Réponses génériques      | Ajustement du chunking et des paramètres |

---

## 8️⃣ Résultats et Évaluation

| Critère                 | Résultat      |
| ----------------------- | ------------- |
| Pertinence des réponses | Bonne         |
| Exactitude factuelle    | Satisfaisante |
| Cohérence linguistique  | Élevée        |
| Temps de réponse        | Acceptable    |

### 🔹 Analyse qualitative

## Points forts :

- Réponses claires et compréhensibles

- Bonne récupération de l’information

- Architecture modulaire et évolutive

## Limites :

- Dépendance à la qualité des données

- Difficultés avec des questions très spécifiques

---

### 9️⃣ Conclusion et Perspectives

Ce projet a permis de mettre en œuvre avec succès un chatbot RAG appliqué au patrimoine archéologique tunisien.
Les résultats obtenus sont encourageants et démontrent la pertinence de cette approche.

🔮 Perspectives d’amélioration

- Enrichissement de la base documentaire

- Optimisation des performances

- Support multilingue

- Intégration d’images et de feedback utilisateur


🏁 Conclusion Générale

Ce travail constitue une preuve de concept réussie, combinant intelligence artificielle, valorisation culturelle et développement applicatif, dans un cadre pédagogique clair et structuré.



