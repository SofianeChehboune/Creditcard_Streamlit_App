# 💳 Credit Card Fraud Detection – Streamlit App

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

---

## 📸 Aperçu

(Ajoutez ici une capture d’écran de votre application si nécessaire)

---

## 📜 Licence

Ce projet est sous licence **MIT**.  
Vous êtes libre de l’utiliser, le modifier et le distribuer en respectant les termes de la licence.
