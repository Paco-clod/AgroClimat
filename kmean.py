import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as cm
import branca.colormap as branca_cm
import seaborn as sns
import plotly.express as px
from sklearn.preprocessing import LabelEncoder
import streamlit as st
import pandas as pd
from pca_analysis import apply_pca, plot_explained_variance, plot_correlation_circle, elbow_method, apply_kmeans, plot_clusters
import geopandas as gpd
import folium
from streamlit_folium import folium_static

df_agroclimat = pd.read_excel("agroclimat.xlsx")
geo = gpd.read_file("benin_geographie")

df_agroclimat = df_agroclimat.rename(columns={"Communes": "Departement"})
df_agroclimat = df_agroclimat.rename(columns={"Département": "Communes"})
#Contenus de Communes
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['ABOMEY0CALAVI', 'ABOMEY CALAVI'], 'ABOMEY-CALAVI')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['DASSA0ZOUME', 'Dassa-Zoumè'], 'DASSA-ZOUME')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['PORTO0NOVO'], 'PORTO-NOVO')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['SEME0PODJI'], 'SEME-PODJI')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['ADJA0OUERE', 'Adja-Ouèrè'], 'ADJA-OUERE')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['AKPRO0MISSERETE'], 'AKPRO-MISSERETE')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['TORI0BOSSITO'], 'TORI-BOSSITO')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['TORI'], 'TORI-BOSSITO')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['GRAND0POPO'], 'GRAND-POPO')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['ZA0KPOTA', 'Za-Kpota'], 'ZA-KPOTA')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Ouinhi'], 'OUINHI')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Zagnanado'], 'ZAGNANADO')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Zogbodomey'], 'ZOGBODOMEY')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Bantè'], 'BANTE')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Glazoué'], 'GLAZOUE')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Ouèsse'], 'OUESSE')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Savalou'], 'SAVALOU')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Savè'], 'SAVE')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Lokossa', 'LOKOSSA '], 'LOKOSSA')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Athiémé'], 'ATHIEME')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Aplahoué'], 'APLAHOUE')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Djakotomey'], 'DJAKOTOMEY')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Dogbo'], 'DOGBO')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Klouékanmè'], 'KLOUEKANME')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Lalo'], 'LALO')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Toviklin'], 'TOVIKLIN')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Kétou'], 'KETOU')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Pobé'], 'POBE')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Kalalé'], 'KALALE')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(["N'Dali"], "N'DALI")
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Nikki'], 'NIKKI')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Parakou'], 'PARAKOU')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Pèrèrè'], 'PERERE')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Sinendé'], 'SINENDE')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Tchaourou'], 'TCHAOUROU')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Banikoara'], 'BANIKOARA')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Gogounou'], 'GOGOUNOU')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Kandi'], 'KANDI')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Karimama'], 'KARIMAMA')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Malanville'], 'MALANVILLE')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Ségbana'], 'SEGBANA')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Abomey'], 'ABOMEY')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Agbangnizoun'], 'AGBANGNIZOUN')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Bohicon'], 'BOHICON')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Covè'], 'COVE')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Djidja'], 'DJIDJA')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Péhunco', 'PEHOUCO', 'PEHOUNCO'], 'PEHUNCO')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Tanguiéta', 'TANGUIETE'], 'TANGUIETA')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Toucountouna'], 'TOUCOUNTOUNA')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Bassila'], 'BASSILA')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Copargo'], 'COPARGO')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Djougou'], 'DJOUGOU')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Ouaké'], 'OUAKE')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Bembèrèkè'], 'BEMBEREKE')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Bonou'], 'BONOU')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Boukoumbé'], 'BOUKOUMBE')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Cobly'], 'COBLY')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Kérou'], 'KEROU')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Kouandé'], 'KOUANDE')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['SO0AVA'], 'SO-AVA')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Matéri'], 'MATERI')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['Natitingou'], 'NATITINGOU')
df_agroclimat['Communes'] = df_agroclimat['Communes'].replace(['AFANGNI'], 'IFANGNI')

df_agroclimat.fillna(0, inplace=True)
df_agroclimat[['Sup(ha)', 'Prod(T)']] = df_agroclimat[['Sup(ha)', 'Prod(T)']].apply(pd.to_numeric, errors='coerce')

agrocleaned = df_agroclimat.copy()

# Création d'un LabelEncoder distinct pour chaque variable
le_produit = LabelEncoder()
le_departement = LabelEncoder()
le_communes = LabelEncoder()

# Encodage des variables catégorielles
Produit_categories = le_produit.fit_transform(agrocleaned['Produit'])
Departement_categories = le_departement.fit_transform(agrocleaned['Departement'])
Communes_categories = le_communes.fit_transform(agrocleaned['Communes'])

# Fonction pour encoder les données
def labelisation(agrocleaned):
    agrocleaned['Produit'] = Produit_categories
    agrocleaned['Departement'] = Departement_categories
    agrocleaned['Communes'] = Communes_categories
    return agrocleaned

# Fonction pour décoder les données (inverser l'encodage)
def inverse_labelisation(agrocleaned):
    agrocleaned['Produit'] = le_produit.inverse_transform(agrocleaned['Produit'])
    agrocleaned['Departement'] = le_departement.inverse_transform(agrocleaned['Departement'])
    agrocleaned['Communes'] = le_communes.inverse_transform(agrocleaned['Communes'])
    return agrocleaned
# Encodage des variables catégorielles
agrocleaned = labelisation(agrocleaned)

# Sélection des données agricoles
df_agro = agrocleaned[['Departement', 'Communes', 'Sup(ha)', 'Rend(kg/ha)', 'Annees', 'Prod(T)', 'Produit']]

# Sélection des données climatiques
df_clim = agrocleaned[['Departement', 'Communes', 'Annees', 'PS(kPa)', 'T2M(°C)', 'T2M_MIN(°C)', 'T2M_MAX(°C)', 'QV2M(g/kg)', 'RH2M(%)', 'WD2M(°)', 'WS2M(m/s)', 'GWETROOT(1)', 'GWETTOP(1)', 'PRECTOTCORR(mm/an)']]
cols = (df_clim.columns.tolist())


# Titre de l'application
st.subheader("Visualisation des Variables Agroclimatiques")
# Sélection du type de données
data_type = st.radio("Sélectionnez le type de données :", ["Agro", "Clim"])
# Déterminer le DataFrame en fonction du choix
if data_type == "Agro":
    df = df_agro
else:
    df = df_clim

# Sélection des variables à afficher
selected_vars = st.multiselect("Sélectionnez les variables :", df.columns, default=df.columns[:2])

# Affichage des distributions
st.subheader("Histogrammes des variables sélectionnées")
fig, axes = plt.subplots(nrows=len(selected_vars), ncols=1, figsize=(10, 4 * len(selected_vars)))

if len(selected_vars) == 1:
    axes = [axes]  # Convertir en liste pour éviter une erreur avec plt.subplots

for i, col in enumerate(selected_vars):
    sns.histplot(data=df, x=col, kde=True, ax=axes[i])
    axes[i].set_title(f"Distribution de {col}")

st.pyplot(fig)

# Affichage des boxplots
st.subheader("Boxplots des variables sélectionnées")
fig, axes = plt.subplots(nrows=len(selected_vars), ncols=1, figsize=(10, 4 * len(selected_vars)))

if len(selected_vars) == 1:
    axes = [axes]

for i, col in enumerate(selected_vars):
    sns.boxplot(x=df[col], ax=axes[i])
    axes[i].set_title(f"Boxplot de {col}")
st.pyplot(fig)


# Titre de l'application
st.title("Analyse en Composantes Principales (PCA)")
# Bouton pour exécuter l'ACP
if st.button("Lancer l'Analyse ACP"):
    pca, pca_data, n_components, explained_variance = apply_pca(df_clim)

    st.write(f"Nombre de composantes principales retenues : **{n_components}**")

    # Afficher la variance expliquée
    st.subheader("Variance expliquée cumulée")
    fig_var = plot_explained_variance(explained_variance)
    st.pyplot(fig_var)

    # Afficher le cercle de corrélation
    st.subheader("Cercle de corrélation")
    fig_corr = plot_correlation_circle(pca, df_clim)
    st.pyplot(fig_corr)


# Titre de l'application
st.subheader("Clustering des données climatiques avec KMeans")

if st.button("Lancer l'agorithme de Kmeans"):
    pca, pca_data, n_components, explained_variance = apply_pca(df_clim)

    st.write(f"Nombre optimal de composantes principales retenues : **{n_components}**")

    # Affichage de la méthode du coude
    st.subheader("Méthode du Coude pour choisir le nombre de clusters")
    fig_elbow = elbow_method(pca_data)
    st.pyplot(fig_elbow)

    # Sélection du nombre de clusters
    k = st.slider("Choisir le nombre de clusters", min_value=5, max_value=20, value=16)

    # Appliquer KMeans
    km, pred = apply_kmeans(pca_data, k)
    df_agroclimat['color'] = pred # Ajouter les clusters dans le dataframe
    set(pred)

    # Affichage des clusters
    st.subheader(f"Visualisation des {k} clusters")
    fig_clusters = plot_clusters(pca, km, df_clim)
    st.pyplot(fig_clusters)

tab20 = plt.get_cmap('tab20')
st.subheader("Cartographie des clusters sur la carte du Bénin")
# Fusionner les données géographiques et agroclimatiques
fig, ax = plt.subplots(figsize=(10, 6))
geo.merge(df_agroclimat, left_on='NOM_COM', right_on='Communes').plot(column='color', cmap=tab20, legend=True, ax=ax)
st.pyplot(fig)