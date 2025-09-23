import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Prédiction de Fraude", layout="wide", page_icon="🔮")

st.title("4. Prédiction sur de Nouvelles Données")

# Vérifier si des modèles ont été entraînés sur la page 2
if 'trained_artifacts' not in st.session_state or not st.session_state['trained_artifacts']:
    st.warning("Aucun modèle n'a été entraîné. Veuillez vous rendre sur la page '🧠 3. Entrainement des Modèles' pour en entraîner un.")
    st.stop() # Arrêter l'exécution de la page

st.markdown("Cette page vous permet d'utiliser un des modèles entraînés pour prédire si une transaction est frauduleuse.")

# Sélection du modèle par l'utilisateur
trained_models_dict = st.session_state['trained_artifacts']
available_models = list(trained_models_dict.keys())

selected_model_name = st.selectbox(
    "Choisissez un modèle entraîné pour la prédiction",
    options=available_models
)

# Récupérer les artefacts (modèle et scalers) du modèle sélectionné
artifacts = trained_models_dict[selected_model_name]
model = artifacts['model']
amount_scaler = artifacts['amount_scaler']
time_scaler = artifacts['time_scaler']

st.header("Entrez les détails de la transaction")
st.markdown("Utilisez les curseurs pour fournir les valeurs des caractéristiques. Pour simplifier, seules quelques caractéristiques sont modifiables.")

# Obtenir les noms de colonnes pour les entrées
data_cols = model.feature_names_in_

# Créer des champs de saisie pour un sous-ensemble de caractéristiques
input_features = {}
col1, col2, col3 = st.columns(3)

# Caractéristiques importantes (basé sur l'analyse de corrélation typique pour ce dataset)
important_features = ['V10', 'V12', 'V14', 'V17', 'V4', 'V11']

with col1:
    time_input = st.number_input("Temps (secondes depuis la première transaction)", value=40000.0, min_value=0.0)
    for feature in important_features[:2]:
        input_features[feature] = st.slider(f"Valeur pour {feature}", -25.0, 25.0, 0.0, 0.1)

with col2:
    amount_input = st.number_input("Montant de la transaction (€)", value=100.0, min_value=0.0, format="%.2f")
    for feature in important_features[2:4]:
        input_features[feature] = st.slider(f"Valeur pour {feature}", -25.0, 25.0, 0.0, 0.1)

with col3:
    st.write(" ") # Espace
    st.write(" ") # Espace
    for feature in important_features[4:]:
        input_features[feature] = st.slider(f"Valeur pour {feature}", -25.0, 25.0, 0.0, 0.1)

# Pour les autres caractéristiques, utiliser la moyenne (0 après standardisation PCA)
for feature in data_cols:
    if feature not in important_features and feature not in ['scaled_amount', 'scaled_time']:
        input_features[feature] = 0.0

# Mettre à l'échelle les entrées utilisateur pour Time et Amount
input_features['scaled_time'] = time_scaler.transform(np.array([[time_input]]))[0, 0]
input_features['scaled_amount'] = amount_scaler.transform(np.array([[amount_input]]))[0, 0]

# Préparer le DataFrame pour la prédiction
input_df = pd.DataFrame([input_features])
# S'assurer que l'ordre des colonnes est le même que celui de l'entraînement
input_df = input_df[model.feature_names_in_]

st.subheader("Données d'entrée pour la prédiction")
st.dataframe(input_df)

if st.button("Lancer la Prédiction"):
    prediction = model.predict(input_df)
    prediction_proba = model.predict_proba(input_df)

    st.subheader("Résultat de la Prédiction")
    if prediction[0] == 1:
        st.error("**Transaction détectée comme FRAUDULEUSE**")
    else:
        st.success("**Transaction considérée comme NON-FRAUDULEUSE**")

    st.write("**Probabilités :**")
    st.write(f"Probabilité de non-fraude (Classe 0) : **{prediction_proba[0][0]:.4f}**")
    st.write(f"Probabilité de fraude (Classe 1) : **{prediction_proba[0][1]:.4f}**")