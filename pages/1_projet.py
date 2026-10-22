import streamlit as st
import geopandas as gpd
import folium
import matplotlib.pyplot as plt
from folium.plugins import FastMarkerCluster

import pandas as pd
from folium import Choropleth
import leafmap.foliumap as leafmap

plate = gpd.read_file(r"c:\Users\HP\OneDrive\Desktop\Training Datasets\Geospatial Learn Course Data\Plate_Boundaries\Plate_Boundaries\Plate_Boundaries.shp")
quakes = gpd.read_file(r"C:\Users\HP\OneDrive\Desktop\Training Datasets\earthquakes.csv",encoding = 'utf-8')

# Conversion des types
quakes['year'] = pd.to_numeric(quakes['year'], errors='coerce')
quakes['depth_km'] = pd.to_numeric(quakes['depth_km'], errors='coerce')
quakes = quakes.dropna(subset=['year', 'depth_km', 'lat', 'lon'])

m2 = leafmap.Map(location=[0, 0], zoom_start=2, minimap_control=True)

for idx, row in plate.iterrows():
    geom = row.geometry
    lines = geom.geoms if geom.geom_type == "MultiLineString" else [geom]
    for line in lines:
        folium.PolyLine(
            locations=[(y, x) for x, y in line.coords],
            weight=2.5,
            opacity=1
        ).add_to(m2)

def color_maker(val):
    if val < 50:
        return 'forestgreen'
    elif val < 100:
        return 'darkorange'
    else:
        return 'darkred'

for idx, row in quakes[quakes['year'] >= 2024].head(1000).iterrows():
    folium.CircleMarker(
        location=(row.lat, row.lon),
        radius=3,
        color=color_maker(row.depth_km),
        fill=True,
        fill_opacity=0.7
    ).add_to(m2)

m2.to_streamlit(height=500)

st.expander('A propos de la carte').write("La carte montre les limites des plaques tectoniques et les séismes récents (depuis 2020) avec une couleur indiquant la profondeur du séisme. Les séismes peu profonds sont en vert, les séismes de profondeur moyenne en orange et les séismes profonds en rouge. Cette visualisation permet de comprendre la relation entre les limites des plaques et l'activité sismique."
                                          "Ainsi nous constatons que les seisme les plus violents donc les plus profonds sont situés le long des limites des plaques tectoniques, ce qui est cohérent avec la théorie de la tectonique des plaques. Les séismes peu profonds sont souvent associés à des zones de subduction ou à des failles transformantes, tandis que les séismes profonds se produisent généralement dans les zones de convergence où une plaque est poussée sous une autre.")


# ---------- Carte ----------
stations = pd.read_csv(r"C:\Users\HP\OneDrive\Documents\stream-app\Accessoire\health_facilities.csv")
stations.dropna(subset=["Latitude", "Longitude"],inplace = True)



CARTO_KEY = "cb1_4g8i_1_9d366dd44740bce3da54e6bf"
  # Assurez-vous que la clé est correctement définie dans les secrets de Streamlit

m = leafmap.Map(location=[7.946527, -1.023194], zoom_start=6, minimap_control=True)


FastMarkerCluster(
    data= stations[["Latitude", "Longitude"]].dropna().values.tolist(),
    callback=None,
    name=None,
    overlay=True,
    control=True,
    show=True,
    icon_create_function=None
    
).add_to(m)
m.add_heatmap(
    data=stations[["Latitude", "Longitude"]].dropna().values.tolist(),
    radius=15,
    name="Heatmap"
)
m.to_streamlit(height=500)

st.expander("À propos de la carte").write("La carte montre une densité de centres de santé plus faible dans la partie centrale du pays, alors que les établissements sont plus nombreux dans le sud et le long de la côte."
                                           " Ce constat reste visuel : il peut refléter une faible densité de population dans ces zones, la présence de zones peu accessibles, ou des données incomplètes. Une analyse du nombre de centres par habitant et par région serait nécessaire pour l’interpréter."
                                           "La carte montre moins de centres de santé dans la partie centrale du pays. Cette différence pourrait s’expliquer par une densité de population plus faible dans ces zones : les besoins en centres de santé varient selon les régions et selon le nombre d’habitants. Cette hypothèse reste à vérifier en comparant le nombre de centres à la population de chaque région")