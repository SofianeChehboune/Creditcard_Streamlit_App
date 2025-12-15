
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc
import numpy as np

st.set_page_config(page_title="Entraînement des Modèles", layout="wide", page_icon="🧠")

st.title("3. Entraînement et Évaluation des Modèles")
st.markdown("Cette page vous permet d'entraîner plusieurs modèles de classification et de comparer leurs performances.")

# --- 1. Chargement des Données Préparées ---
st.header("1. Chargement des Données Préparées")

# Vérifier si les données ont été préparées
if 'data_prepared' not in st.session_state:
    st.warning("Les données n'ont pas été préparées. Veuillez d'abord vous rendre sur la page '🛠️ Préparation des Données'.")
    st.stop()

st.success("Données préparées chargées avec succès depuis la page précédente.")

# Charger les données depuis st.session_state
prepared_data = st.session_state['data_prepared']
X_train = prepared_data['X_train']
X_test = prepared_data['X_test']
y_train = prepared_data['y_train']
y_test = prepared_data['y_test']
amount_scaler = prepared_data['amount_scaler']
time_scaler = prepared_data['time_scaler']

use_smote = st.checkbox("Utiliser SMOTE pour corriger le déséquilibre des classes ?")
if use_smote:
    st.info("SMOTE (Synthetic Minority Over-sampling Technique) va être appliqué sur les données d'entraînement pour générer des échantillons synthétiques de la classe minoritaire (fraude).")

# --- 2. Model Selection and Training ---
st.header("2. Sélection et Entraînement des Modèles")

model_options = ['Régression Logistique', 'Arbre de Décision', 'Forêt Aléatoire', 'Gradient Boosting']
selected_models = st.multiselect("Choisissez les modèles à entraîner", model_options, default=['Régression Logistique', 'Forêt Aléatoire'])

@st.cache_resource
def get_model(model_name):
    models = {
        'Régression Logistique': LogisticRegression(random_state=42, max_iter=1000),
        'Arbre de Décision': DecisionTreeClassifier(random_state=42),
        'Forêt Aléatoire': RandomForestClassifier(random_state=42),
        'Gradient Boosting': GradientBoostingClassifier(random_state=42)
    }
    return models[model_name]

def plot_roc_curve(y_true, y_proba):
    fpr, tpr, _ = roc_curve(y_true, y_proba)
    roc_auc = auc(fpr, tpr)
    fig = go.Figure(data=go.Scatter(x=fpr, y=tpr, mode='lines', name=f'Courbe ROC (AUC = {roc_auc:.2f})'))
    fig.add_shape(type='line', line=dict(dash='dash'), x0=0, x1=1, y0=0, y1=1)
    fig.update_layout(title_text="<b>Courbe ROC</b>", xaxis_title="Taux de Faux Positifs", yaxis_title="Taux de Vrais Positifs")
    return fig

def plot_feature_importance(model, feature_names):
    importances = model.feature_importances_
    indices = np.argsort(importances)[-15:]
    fig = px.bar(x=importances[indices], y=[feature_names[i] for i in indices], orientation='h',
                 title="<b>Top 15 des Caractéristiques les plus Importantes</b>", labels={'x': 'Importance', 'y': 'Caractéristique'})
    return fig

if st.button("Lancer l'entraînement et l'évaluation"):
    if 'trained_artifacts' not in st.session_state:
        st.session_state['trained_artifacts'] = {}

    X_train_processed = X_train.copy()
    y_train_processed = y_train.copy()

    if use_smote:
        with st.spinner("Application de SMOTE..."):
            smote = SMOTE(random_state=42)
            X_train_processed, y_train_processed = smote.fit_resample(X_train, y_train)
            st.success(f"SMOTE appliqué. Nouvelles dimensions de l'ensemble d'entraînement : {X_train_processed.shape}")

    for model_name in selected_models:
        st.subheader(f"Résultats pour : {model_name}")
        model = get_model(model_name)

        with st.spinner(f"Entraînement du modèle {model_name}..."):
            model.fit(X_train_processed, y_train_processed)
            st.session_state['trained_artifacts'][model_name] = {'model': model, 'amount_scaler': amount_scaler, 'time_scaler': time_scaler}
            y_pred = model.predict(X_test)
            y_proba = model.predict_proba(X_test)[:, 1]

            # --- 3. Evaluation ---
            st.markdown("#### Évaluation du Modèle")
            col1, col2 = st.columns(2)

            with col1:
                report = classification_report(y_test, y_pred, target_names=['Non-Fraude', 'Fraude'], output_dict=True)
                st.write("<b>Rapport de Classification</b>", unsafe_allow_html=True)
                st.dataframe(pd.DataFrame(report).transpose())

            with col2:
                cm = confusion_matrix(y_test, y_pred)
                fig_cm = ff.create_annotated_heatmap(cm[::-1], x=['Non-Fraude', 'Fraude'], y=['Fraude', 'Non-Fraude'][::-1], colorscale='Blues')
                fig_cm.update_layout(title_text="<b>Matrice de Confusion</b>", xaxis_title="Prédiction", yaxis_title="Vrai")
                st.plotly_chart(fig_cm, width='stretch')

            col3, col4 = st.columns(2)
            with col3:
                st.plotly_chart(plot_roc_curve(y_test, y_proba), width='stretch')

            with col4:
                if hasattr(model, 'feature_importances_'):
                    st.plotly_chart(plot_feature_importance(model, X_test.columns), width='stretch')
                else:
                    st.info("Ce modèle ne fournit pas d'importance pour les caractéristiques.")

        st.success(f"Le modèle **{model_name}** a été entraîné et est disponible sur la page '🔮 Prédiction' !")
        st.markdown("---")
