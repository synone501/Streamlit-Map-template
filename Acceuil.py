from pathlib import Path

import folium
import pandas as pd
import streamlit as st
from folium.plugins import HeatMap
from streamlit_folium import st_folium
import leafmap.foliumap as leafmap
from pathlib import Path

ACCESSOIRE = Path(__file__).parent / "Accessoire"
photo = ACCESSOIRE / "linkdin.png"
st.set_page_config(
    page_title="Ibrahim Sinon | Portfolio",
    page_icon="🗺️",
    layout="wide",
)

BASE_DIR = Path(__file__).parent
ACCESSOIRE = BASE_DIR / "Accessoire"
DATA = BASE_DIR / "data"





# ---------- En-tête ----------
st.title("Ibrahim Sinon")
st.caption("Étudiant en Géomatique | SIG & Analyse spatiale | Python & Analyse de données")
st.divider()

col_photo, col_texte = st.columns([1, 2])

with col_photo:
    ACCESSOIRE = Path(__file__).parent / "Accessoire"
    photo = ACCESSOIRE / "linkdin.png"    
    if photo.exists():
        st.image(str(photo), width=200)

with col_texte:
    with st.container(border=True):
        st.write(
            "Étudiant en troisième année de Licence en Géomatique à l'Université "
            "Virtuelle du Burkina Faso. "
            "Je m'intéresse particulièrement aux systèmes d'information géographique, "
            "à l'analyse spatiale et au traitement des données géospatiales. "
            "En parallèle de ma formation, je développe mes compétences à travers "
            "l'apprentissage autodidacte et des projets personnels.\n\n"
            "À travers ce portfolio, je présente mon parcours, mes projets et les "
            "compétences que je développe en géomatique et en analyse de données."
        )

    btn1, btn2, btn3 = st.columns(3)

    with btn1:
        if st.button("🗺️ Voir mes projets", type="primary", width="stretch"):
            st.switch_page("pages/1_Projets.py")

    with btn2:
        cv_path = Path(r"C:\Users\HP\OneDrive\Documents\stream-app\Accessoire\CV_Ibrahim_Sinon.pdf")
        if cv_path.exists():
            st.download_button(
                label="📄 Télécharger mon CV",
                data=cv_path.read_bytes(),
                file_name="CV_Ibrahim_Sinon.pdf",
                mime="application/pdf",
                width="stretch",
            )

    with btn3:
        st.link_button(
            "LinkedIn",
            url="https://www.linkedin.com/in/ibrahim-didjob-sinon-1a6539333",
            width="stretch",
        )

st.divider()

with st.expander("À propos de moi"):
    st.write(
        "Après l'obtention de mon Baccalauréat série D, j'ai choisi de m'orienter "
        "vers la géomatique, un domaine qui combine SIG, cartographie, analyse "
        "spatiale et données géographiques.\n\n"
        "En parallèle de ma formation, je poursuis un apprentissage autodidacte en "
        "Python, en analyse de données et en bases de données.\n\n"
        "Je cherche aujourd'hui à mettre ces connaissances en pratique à travers "
        "des projets concrets et des expériences professionnelles."
    )
 
# ---------- Carte ----------
st.header("Aperçu de la topographie mondiale")

m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")

m.to_streamlit(height=500)


# ... (en-tête, boutons et expander inchangés, avec le CV corrigé)


