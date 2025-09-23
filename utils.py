import streamlit as st
import pandas as pd
import base64
1
# URL Dropbox (lien direct)
CSV_URL = "https://www.dropbox.com/scl/fi/95kkevx66y0teeyrqrfnp/creditcard.csv?rlkey=svlt3izx0v6qntwca7afrvop1&st=xsobeetj&dl=1"

@st.cache_data
def load_data():
    # Lecture du CSV directement depuis Dropbox
    data = pd.read_csv(CSV_URL)
    return data

def get_image_as_base64(path: str) -> str:
    """Lit un fichier image et le retourne en tant que chaîne base64."""
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()
