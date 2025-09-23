import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_data

st.set_page_config(page_title="Analyse Exploratoire", layout="wide", page_icon="📊")

st.title("1. Analyse Exploratoire des Données")

st.markdown("Cette page présente une analyse exploratoire du jeu de données sur la fraude par carte de crédit.")

# Charger les données
data = load_data()

st.header("Aperçu du jeu de données")
st.write(f"Le jeu de données contient **{data.shape[0]}** lignes et **{data.shape[1]}** colonnes.")
st.dataframe(data.head())

st.header("Statistiques descriptives")
st.write("Voici quelques statistiques descriptives pour les caractéristiques numériques du jeu de données.")
st.write(data.describe())

st.header("Distribution des Classes (Fraude vs Non-Fraude)")
class_counts = data['Class'].value_counts()
class_counts.index = ['Non-Fraude (0)', 'Fraude (1)']
st.write(f"Transactions non frauduleuses (Classe 0) : **{class_counts.get('Non-Fraude (0)', 0)}**")
st.write(f"Transactions frauduleuses (Classe 1) : **{class_counts.get('Fraude (1)', 0)}**")

# Remplacer Matplotlib/Seaborn par Plotly
fig = px.bar(
    class_counts,
    x=class_counts.index,
    y=class_counts.values,
    title="Distribution des Classes",
    labels={'x': 'Classe', 'y': 'Nombre de Transactions'},
    color=class_counts.index,
    color_discrete_map={'Non-Fraude (0)': 'royalblue', 'Fraude (1)': 'crimson'}
)
fig.update_layout(showlegend=False)
st.plotly_chart(fig, use_container_width=True)

st.markdown("Comme on peut le voir, le jeu de données est très déséquilibré.")

st.header("Matrice de Corrélation Interactive")
st.markdown("Pour visualiser les relations entre les caractéristiques, nous pouvons tracer une matrice de corrélation. Passez la souris sur les cellules pour voir les valeurs.")
st.warning("Le calcul de la matrice de corrélation sur l'ensemble des données peut être long. Nous utilisons un échantillon pour l'affichage.")

# Utiliser un échantillon pour la performance
sample_data = data.sample(n=50000, random_state=42)

corr = sample_data.corr()

fig_corr = px.imshow(
    corr,
    color_continuous_scale="RdBu_r",
    title="Matrice de Corrélation (sur un échantillon de 50k lignes)"
)
fig_corr.update_layout(height=700)
st.plotly_chart(fig_corr, use_container_width=True)