💳 Credit Card Fraud Detection – Streamlit App
Cette application permet d'analyser et de prédire les fraudes de cartes bancaires à partir du dataset Kaggle - Credit Card Fraud Detection.

Elle a été développée avec Python, Pandas, Scikit-learn et Streamlit.

🚀 Fonctionnalités
📊 Analyse exploratoire des données - Visualisation des distributions et des corrélations

🛠️ Préparation des données - Nettoyage et traitement des données déséquilibrées

🧠 Machine Learning - Entraînement de modèles (Random Forest, Logistic Regression, etc.)

🔮 Prédiction en temps réel - Interface intuitive pour tester de nouvelles transactions

📈 Évaluation des modèles - Métriques de performance détaillées

📂 Structure du projet
Creditcard_Streamlit_App/
│
├── Home.py                       # Page principale de l'application
├── pages/                        # Pages Streamlit supplémentaires
│   ├── 1_📊_Analyse.py           # Analyse exploratoire
│   ├── 2_🤖_ML_Models.py         # Entraînement des modèles
│   └── 3_🔮_Prediction.py        # Prédiction en temps réel
│
├── utils.py                      # Fonctions utilitaires
├── requirements.txt              # Dépendances Python
├── README.md                     # Ce fichier
└── creditcard.csv                # Dataset (à ajouter manuellement)

⚙️ Installation
1. Cloner le dépôt
git clone [https://github.com/SofianeChehboune/Creditcard_Streamlit_App.git](https://github.com/SofianeChehboune/Creditcard_Streamlit_App.git)
cd Creditcard_Streamlit_App

2. Créer un environnement virtuel (recommandé)
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate

3. Installer les dépendances
pip install -r requirements.txt

📥 Dataset
⚠️ Le dataset n’est pas inclus dans ce dépôt (trop volumineux + confidentialité).

👉 Téléchargez-le depuis Kaggle :
Credit Card Fraud Detection Dataset

Ensuite, placez le fichier creditcard.csv à la racine du projet ou utilisez la méthode décrite ci-dessous.

Creditcard_Streamlit_App/
│── creditcard.csv  # <- à ajouter ici
│── Home.py
│── pages/
│── utils.py
│── requirements.txt
│── README.md
│── ...

Remarques / options :

Si le CSV est trop volumineux pour GitHub, placez-le localement et utilisez un lien externe (Dropbox / Google Drive / Kaggle API) dans le code.

Pour accélérer le chargement et réduire la taille, convertissez en parquet (recommandé) :

import pandas as pd

df = pd.read_csv("creditcard.csv")
df.to_parquet("creditcard.parquet", engine="pyarrow", compression="snappy")

# puis dans l'app :
# df = pd.read_parquet("creditcard.parquet")

▶️ Lancer l’application
streamlit run Home.py

Ensuite, ouvrez le lien généré dans votre navigateur :
👉 http://localhost:8501

📸 Aperçu
(Ajoutez ici une capture d’écran de votre application si nécessaire)

📜 Licence
Ce projet est sous licence MIT.
Vous êtes libre de l’utiliser, le modifier et le distribuer en respectant les termes de la licence.

📌 Contacts / Notes rapides
Repo : https://github.com/SofianeChehboune/Creditcard_Streamlit_App

Dataset original : Kaggle (voir lien ci-dessus)

Si vous déployez sur Streamlit Cloud, préférez un fichier parquet dans le dépôt ou un lien stable (Dropbox/GDrive/HuggingFace) pour éviter les problèmes de taille et de latence.

Fichier LICENSE
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
