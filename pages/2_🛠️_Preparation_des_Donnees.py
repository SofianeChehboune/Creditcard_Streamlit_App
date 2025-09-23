import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from utils import load_data

st.set_page_config(page_title="Préparation des Données", layout="wide", page_icon="🛠️")

st.title("2. Préparation des Données")
st.markdown("Cette étape consiste à préparer les données pour l'entraînement : mise à l'échelle des caractéristiques et division en ensembles d'entraînement et de test.")

# Utiliser un spinner pour un retour visuel pendant le traitement
with st.spinner("Chargement et préparation des données en cours..."):
    # Charger les données
    data = load_data()

    # Initialiser les scalers
    amount_scaler = StandardScaler()
    time_scaler = StandardScaler()

    # Créer une copie pour éviter de modifier les données en cache
    data_processed = data.copy()

    # Mettre à l'échelle les caractéristiques 'Amount' et 'Time'
    data_processed['scaled_amount'] = amount_scaler.fit_transform(data_processed['Amount'].values.reshape(-1, 1))
    data_processed['scaled_time'] = time_scaler.fit_transform(data_processed['Time'].values.reshape(-1, 1))

    # Supprimer les colonnes originales
    data_processed.drop(['Time', 'Amount'], axis=1, inplace=True)

    # Définir les caractéristiques (X) et la cible (y)
    X = data_processed.drop('Class', axis=1)
    y = data_processed['Class']

    # Diviser les données (stratify=y est crucial pour les données déséquilibrées)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Stocker les données préparées et les scalers dans la session
    st.session_state['data_prepared'] = {
        'X_train': X_train,
        'X_test': X_test,
        'y_train': y_train,
        'y_test': y_test,
        'amount_scaler': amount_scaler,
        'time_scaler': time_scaler
    }

st.success("Les données ont été préparées avec succès !")
st.info("Les ensembles d'entraînement/test et les `scalers` sont maintenant disponibles pour la page d'entraînement.")

st.subheader("Aperçu des données d'entraînement (X_train)")
st.dataframe(X_train.head())

col1, col2 = st.columns(2)
with col1:
    st.metric("Taille de l'ensemble d'entraînement", f"{X_train.shape[0]} lignes")
with col2:
    st.metric("Taille de l'ensemble de test", f"{X_test.shape[0]} lignes")