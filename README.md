# 💳 Credit Card Fraud Detection – Streamlit App

Cette application permet d'analyser et de prédire les fraudes de cartes bancaires à partir du dataset [Kaggle - Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud).  
Elle a été développée avec **Python**, **Pandas**, **Scikit-learn** et **Streamlit**.

---

## 🚀 Fonctionnalités

- 📊 **Analyse exploratoire des données** - Visualisation des distributions et des corrélations
- 🛠️ **Préparation des données** - Nettoyage et traitement des données déséquilibrées
- 🧠 **Machine Learning** - Entraînement de modèles (Random Forest, Logistic Regression, etc.)
- 🔮 **Prédiction en temps réel** - Interface intuitive pour tester de nouvelles transactions
- 📈 **Évaluation des modèles** - Métriques de performance détaillées

---

## 📂 Structure du projet
Creditcard_Streamlit_App/
│
├── Home.py # Page principale de l'application
├── pages/ # Pages Streamlit supplémentaires
│ ├── 1_📊_Analyse.py # Analyse exploratoire
│ ├── 2_🤖_ML_Models.py # Entraînement des modèles
│ └── 3_🔮_Prediction.py # Prédiction en temps réel
│
├── utils.py # Fonctions utilitaires
├── requirements.txt # Dépendances Python
├── README.md # Ce fichier
└── creditcard.csv # Dataset (à ajouter manuellement)

text

---

## ⚙️ Installation

### 1. Cloner le dépôt
```bash
git clone https://github.com/SofianeChehboune/Creditcard_Streamlit_App.git
cd Creditcard_Streamlit_App
2. Créer un environnement virtuel (recommandé)
bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
3. Installer les dépendances
bash
pip install -r requirements.txt
📥 Dataset
⚠️ Le dataset n'est pas inclus dans ce dépôt pour des raisons de taille et de confidentialité.

Téléchargement du dataset :
Allez sur Kaggle - Credit Card Fraud Detection

Téléchargez le fichier creditcard.csv

Placez-le à la racine du projet :

text
Creditcard_Streamlit_App/
│── creditcard.csv          # ← Ajouter ici
│── Home.py
│── pages/
│── utils.py
│── requirements.txt
│── ...
📊 Caractéristiques du dataset :
284,807 transactions dont 492 fraudes (0.172%)

30 features numériques (anonymisées) + montant + temps

Déséquilibre important entre classes

▶️ Lancement de l'application
bash
streamlit run Home.py
L'application sera accessible à l'adresse :
👉 http://localhost:8501

🖥️ Utilisation
📊 Page d'analyse exploratoire
Distribution des transactions normales vs frauduleuses

Analyse des montants par type de transaction

Matrice de corrélation des features

🤖 Page modèles ML
Comparaison de plusieurs algorithmes

Métriques de performance (précision, rappel, F1-score, AUC)

Courbes ROC et matrice de confusion

🔮 Page de prédiction
Saisie manuelle des caractéristiques d'une transaction

Prédiction immédiate du risque de fraude

Score de confiance de la prédiction

🛠️ Technologies utilisées
Python 3.8+

Streamlit - Interface utilisateur

Pandas - Manipulation des données

Scikit-learn - Machine Learning

Matplotlib/Seaborn - Visualisations

Imbalanced-learn - Traitement des données déséquilibrées

📋 Dépendances
Les principales dépendances sont listées dans requirements.txt :

text
streamlit==1.28.0
pandas==2.0.3
numpy==1.24.3
scikit-learn==1.3.0
matplotlib==3.7.2
seaborn==0.12.2
imbalanced-learn==0.10.1
plotly==5.15.0
🤝 Contribution
Les contributions sont les bienvenues ! Pour contribuer :

Forkez le projet

Créez une branche feature (git checkout -b feature/AmazingFeature)

Committez vos changements (git commit -m 'Add AmazingFeature')

Pushez la branche (git push origin feature/AmazingFeature)

Ouvrez une Pull Request

📜 Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

👨‍💻 Auteur
Sofiane Chehboune

GitHub: @SofianeChehboune

LinkedIn: Sofiane Chehboune

⚠️ Disclaimer
Ce projet est à but éducatif et de démonstration. Les prédictions ne doivent pas être utilisées pour prendre des décisions financières réelles sans validation par des experts du domaine.

text

Et voici le fichier **LICENSE** MIT à créer à la racine de ton projet :

```plaintext
MIT License

Copyright (c) 2024 Sofiane Chehboune

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
