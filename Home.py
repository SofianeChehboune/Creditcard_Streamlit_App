import streamlit as st
from utils import load_data, get_image_as_base64 # Importer les fonctions utiles

# Configuration de la page, doit être la première commande Streamlit
st.set_page_config(
    page_title="Accueil - Détection de Fraude",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Barre Latérale ---
with st.sidebar:
    st.image("banniere/distributeur.png")
    st.markdown("Développé par :👇")
    
    # Encoder les images en base64
    id_photo_b64 = get_image_as_base64("banniere/ID.jpg")
    linkedin_icon_b64 = get_image_as_base64("banniere/linkedin.png")

    # HTML pour afficher la photo et le bouton LinkedIn côte à côte
    st.markdown(f'''
    <div style="display: flex; align-items: center; margin-bottom: 12px;">
        <img src="data:image/jpg;base64,{id_photo_b64}" alt="ID Photo" style="width: 70px; height: 70px; border-radius: 50%; margin-right: 15px; object-fit: cover;">
        <a href="https://www.linkedin.com/in/sofiane-chehboune-5b243766/" target="_blank" style="display: inline-block; text-decoration: none; background-color: #0077B5; color: white; padding: 8px 12px; border-radius: 4px; font-weight: bold;">
            <img src="data:image/png;base64,{linkedin_icon_b64}" alt="LinkedIn Logo" style="height: 20px; vertical-align: middle; margin-right: 8px;">
            Sofiane Chehboune
        </a>
    </div>
    ''', unsafe_allow_html=True)
    st.markdown("---")
    st.info("Naviguez entre les pages pour explorer les données, entraîner des modèles et faire des prédictions.")

# --- Page Principale ---
st.title("Bienvenue sur l'Application de Détection de Fraude")
st.markdown("Un outil interactif pour l'analyse et la modélisation des transactions par carte de crédit.")

st.markdown("---")

# --- Métriques Clés ---
st.subheader("Aperçu Rapide du Jeu de Données")

# Charger les données pour afficher les statistiques
data = load_data()
total_transactions = data.shape[0]
fraud = data['Class'].value_counts()[1]
fraud_percentage = (fraud / total_transactions) * 100

# Afficher les métriques dans des colonnes
m1, m2, m3 = st.columns(3)
m1.metric(label="Total des Transactions", value=f"{total_transactions:,}")
m2.metric(label="Transactions Frauduleuses", value=f"{fraud:,}")
m3.metric(label="Pourcentage de Fraude", value=f"{fraud_percentage:.3f}%")

st.markdown("---")

# --- Présentation de l'application ---
col1, col2 = st.columns([2, 1])
with col1:
    st.subheader("Comment utiliser cette application ?")
    st.markdown("""
    Cette application a été conçue pour illustrer un flux de travail complet en science des données.
    
    **Utilisez le menu sur la gauche pour naviguer entre les sections :**
    1.  **📊 Analyse Exploratoire :** Explorez les caractéristiques du jeu de données.
    2.  **🛠️ Preparation des Donnees :** Préparez les données pour l'entraînement.
    3.  **🧠 Entrainement des Modeles :** Entraînez et évaluez différents modèles de classification.
    4.  **🔮 Prediction :** Utilisez un modèle entraîné pour faire une prédiction sur une nouvelle transaction.
    """)

with col2:
    st.image("banniere/credit_card.png", use_container_width=True)
