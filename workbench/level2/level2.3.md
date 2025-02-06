# Phase 3 - Création de l’interface utilisateur avec Streamlit

🎯 **Objectif** : Afficher le questionnaire et récupérer les réponses en temps réel.  

🔹 **Key Results** :  

- [ ] Développer une interface minimaliste avec Streamlit.  
- [ ] Se connecter à l’API Supabase pour récupérer/enregistrer les données.  
- [ ] Implémenter un premier scoring dynamique (affichage des jauges).  
- [ ] Déployer le tout avec Docker Compose.  

🛠 **Exercice pratique** :  

- Un formulaire interactif avec une barre de progression du scoring.  
- Stocker les réponses et afficher une jauge de maturité en fonction du score.  

---

## Key Components of a Streamlit App

Let's break down the "big picture" and how Streamlit fits in.

### Your Current Flask Setup

You've created a classic web application setup:

1. Frontend (index.html): Handles user input.
2. Backend (Flask in Python): Receives the input, interacts with Supabase (via API key), retrieves data, and renders the HTML with results.
3. Docker/Docker Compose: Packages the Flask app and its dependencies into a container for easy deployment.
This is a solid architecture, and Docker Compose helps manage the different parts efficiently.

### How Streamlit Simplifies Things

Streamlit fundamentally changes the way you build the frontend and backend.  It lets you write Python code that directly generates the user interface and handles the logic, effectively merging the frontend and backend into a single Python script.

### Here's how it compares to your Flask setup

1. No Separate HTML: You don't write HTML files. Streamlit uses Python commands to create UI elements like text boxes, buttons, and displays.
2. Simplified Backend: Streamlit handles the communication between the UI and your Python code. You don't need to manage routes or handle HTTP requests directly like in Flask. Your Python code interacts directly with the UI elements and Supabase.
3. Still Dockerizable: You can absolutely still Dockerize a Streamlit app. This gives you the same benefits of containerization (consistent environment, easy deployment) as with your Flask app.

### Why Streamlit is Often Preferred for Data Apps

Streamlit excels at building data-driven applications quickly.  If your primary goal is to visualize data, create interactive dashboards, or build simple web apps with data input and output (like your Supabase example), Streamlit often reduces the development time significantly.
