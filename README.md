<p align="center">
  <img src="https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit" alt="Streamlit">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Scikit--learn-ML-yellow?style=for-the-badge&logo=scikitlearn" alt="Scikit-learn">
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-green?style=for-the-badge&logo=pandas" alt="Pandas">
</p>

<h1 align="center">💳 Credit Card Fraud Detection – Streamlit App</h1>

<p align="center">
  <i>Application interactive pour analyser et prédire les fraudes de cartes bancaires avec Python et Machine Learning</i>
</p>

---

Cette application permet d’analyser et de prédire les fraudes de cartes bancaires à partir du dataset [Kaggle - Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud).  
Elle a été développée avec **Python**, **Pandas**, **Scikit-learn** et **Streamlit**.

---

## 🚀 Fonctionnalités
- 📊 Analyse exploratoire des données  
- 🛠️ Préparation et nettoyage des données  
- 🧠 Entraînement de modèles de Machine Learning (Random Forest, etc.)  
- 🔮 Prédiction en temps réel via une interface Streamlit  

---

## 📂 Installation

### 1. Cloner le dépôt
```bash
git clone https://github.com/SofianeChehboune/Creditcard_Streamlit_App.git
cd Creditcard_Streamlit_App
```

### 2. Créer un environnement virtuel (recommandé)
```bash
python -m venv venv
# Linux / Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

---

## 📥 Dataset

⚠️ Le dataset n’est pas inclus dans ce dépôt (trop volumineux + confidentialité).

👉 Téléchargez-le depuis Kaggle :  
[Credit Card Fraud Detection Dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud)  

Ensuite, placez le fichier **`creditcard.csv`** à la racine du projet :

```
Creditcard_Streamlit_App/
│── creditcard.csv   <- à ajouter ici
│── Home.py
│── pages/
│── utils.py
│── requirements.txt
│── ...
```

---

## ▶️ Lancer l’application
```bash
streamlit run Home.py
```

Ensuite, ouvrez le lien généré dans votre navigateur :  
👉 [http://localhost:8501](http://localhost:8501)
👉 [🌐 Accéder à l'application en ligne](https://creditcardappapp-rsqekjdydujnc5jaktjg8q.streamlit.app/)

<p align="center">
  <a href="https://creditcardappapp-cqfyezbn8yrqdua3pbyemh.streamlit.app/">
    <img src="https://img.shields.io/badge/Demo-Live%20App-brightgreen?style=for-the-badge&logo=streamlit" alt="Live Demo App"/>
  </a>
</p>
---

## 📸 Aperçu


<img width="1588" height="758" alt="banniere" src="https://github.com/user-attachments/assets/5793f88a-d13d-4720-8870-94e290f5b5d8" />

---

## 📜 Licence

Ce projet est sous licence **MIT**.  
Vous êtes libre de l’utiliser, le modifier et le distribuer en respectant les termes de la licence.
