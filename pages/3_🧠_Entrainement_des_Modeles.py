import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
from imblearn.over_sampling import SMOTE
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
amount_scaler = prepared_data.get('amount_scaler', None)
time_scaler = prepared_data.get('time_scaler', None)

use_smote = st.checkbox("Utiliser SMOTE pour corriger le déséquilibre des classes ?")
if use_smote:
    st.info("SMOTE (Synthetic Minority Over-sampling Technique) va être appliqué sur les données d'entraînement pour générer des échantillons synthétiques de la classe minoritaire (fraude).")

# --- 2. Model Selection and Training ---
st.header("2. Sélection et Entraînement des Modèles")

model_options = ['Régression Logistique', 'Arbre de Décision', 'Forêt Aléatoire', 'Gradient Boosting']
selected_models = st.multiselect("Choisissez les modèles à entraîner", model_options, default=['Régression Logistique', 'Forêt Aléatoire'])

def get_model(model_name):
    models = {
        'Régression Logistique': LogisticRegression(random_state=42, max_iter=1000),
        'Arbre de Décision': DecisionTreeClassifier(random_state=42),
        'Forêt Aléatoire': RandomForestClassifier(random_state=42),
        'Gradient Boosting': GradientBoostingClassifier(random_state=42)
    }
    return models[model_name]

def plot_roc_curve(y_true, y_scores):
    try:
        fpr, tpr, _ = roc_curve(y_true, y_scores)
        roc_auc = auc(fpr, tpr)
    except Exception:
        return None
    fig = go.Figure(data=go.Scatter(x=fpr, y=tpr, mode='lines', name=f'Courbe ROC (AUC = {roc_auc:.2f})'))
    fig.add_shape(type='line', line=dict(dash='dash'), x0=0, x1=1, y0=0, y1=1)
    fig.update_layout(title_text="<b>Courbe ROC</b>", xaxis_title="Taux de Faux Positifs", yaxis_title="Taux de Vrais Positifs")
    return fig

def plot_feature_importance(model, feature_names):
    importances = None
    if hasattr(model, 'feature_importances_'):
        importances = np.array(model.feature_importances_)
    elif hasattr(model, 'coef_'):
        coef = np.array(model.coef_)
        # pour multi-classes, prendre la moyenne des valeurs absolues
        if coef.ndim > 1:
            importances = np.mean(np.abs(coef), axis=0)
        else:
            importances = np.abs(coef)
    else:
        return None

    if importances is None or len(importances) != len(feature_names):
        return None

    indices = np.argsort(importances)[-15:][::-1]
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
            X_res, y_res = smote.fit_resample(X_train, y_train)
            # Reconstruire DataFrame/Series si nécessaire pour conserver les noms de colonnes
            if isinstance(X_train, pd.DataFrame):
                X_train_processed = pd.DataFrame(X_res, columns=X_train.columns)
            else:
                X_train_processed = pd.DataFrame(X_res)
            if isinstance(y_train, pd.Series) or isinstance(y_train, pd.Index):
                y_train_processed = pd.Series(y_res, name=getattr(y_train, 'name', None))
            else:
                y_train_processed = pd.Series(y_res)
            st.success(f"SMOTE appliqué. Nouvelles dimensions de l'ensemble d'entraînement : {X_train_processed.shape}")

    for model_name in selected_models:
        st.subheader(f"Résultats pour : {model_name}")
        model = get_model(model_name)

        with st.spinner(f"Entraînement du modèle {model_name}..."):
            model.fit(X_train_processed, y_train_processed)
            st.session_state['trained_artifacts'][model_name] = {
                'model': model,
                'amount_scaler': amount_scaler,
                'time_scaler': time_scaler,
                'feature_names': list(X_train.columns) if isinstance(X_train, pd.DataFrame) else None
            }

            y_pred = model.predict(X_test)
            # Récupérer des scores pour la ROC si possible
            y_scores = None
            if hasattr(model, "predict_proba"):
                try:
                    y_scores = model.predict_proba(X_test)[:, 1]
                except Exception:
                    y_scores = None
            if y_scores is None and hasattr(model, "decision_function"):
                try:
                    y_scores = model.decision_function(X_test)
                except Exception:
                    y_scores = None

            # --- 3. Evaluation ---
            st.markdown("#### Évaluation du Modèle")
            col1, col2 = st.columns(2)

            with col1:
                report = classification_report(y_test, y_pred, target_names=['Non-Fraude', 'Fraude'], output_dict=True)
                st.write("<b>Rapport de Classification</b>", unsafe_allow_html=True)
                st.dataframe(pd.DataFrame(report).transpose())

            with col2:
                cm = confusion_matrix(y_test, y_pred)
                labels = ['Non-Fraude', 'Fraude']
                # Afficher matrice de confusion annotée
                try:
                    fig_cm = ff.create_annotated_heatmap(z=cm, x=labels, y=labels, colorscale='Blues', showscale=True)
                    fig_cm.update_layout(title_text="<b>Matrice de Confusion</b>", xaxis_title="Prédiction", yaxis_title="Vrai")
                    st.plotly_chart(fig_cm, use_container_width=True)
                except Exception:
                    st.write("Impossible d'afficher la matrice de confusion graphiquement.")

            col3, col4 = st.columns(2)
            with col3:
                if y_scores is not None:
                    roc_fig = plot_roc_curve(y_test, y_scores)
                    if roc_fig is not None:
                        st.plotly_chart(roc_fig, use_container_width=True)
                    else:
                        st.info("Impossible de tracer la ROC pour ce modèle.")
                else:
                    st.info("Pas de probabilités / scores disponibles pour tracer la courbe ROC pour ce modèle.")

            with col4:
                feat_fig = None
                feature_names = st.session_state['trained_artifacts'][model_name].get('feature_names', None)
                if feature_names is None and hasattr(X_test, 'columns'):
                    feature_names = list(X_test.columns)
                if feature_names is not None:
                    feat_fig = plot_feature_importance(model, feature_names)
                if feat_fig is not None:
                    st.plotly_chart(feat_fig, use_container_width=True)
                else:
                    st.info("Ce modèle ne fournit pas d'importance pour les caractéristiques ou impossibilité de l'afficher.")

        st.success(f"Le modèle **{model_name}** a été entraîné et est disponible sur la page '🔮 Prédiction' !")
        st.markdown("---")
