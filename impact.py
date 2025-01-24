import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
from scipy.stats import gaussian_kde

df_agroclimat = pd.read_excel("agroclimat.xlsx")

df_agroclimat = df_agroclimat.rename(columns={"Communes": "Departement"})
df_agroclimat = df_agroclimat.rename(columns={"Département": "Communes"})
#Contenus de Communes
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

st.subheader("Impact, Relation, Evolution ou/et Influence de la production agricole en fonction des facteurs climatiques")
st.dataframe(df_agroclimat.head(25))
st.write("Dans cette section, nous allons chercher à comprendre l'impact, la relation, l'évolution ou l'influence de la production agricole en fonction des facteurs climatiques.")
st.write("Nous allons donc chercher à répondre à des questions telles que:")
st.write("1. Quelle est la relation entre la production agricole et les facteurs climatiques ?")
st.write("2. Quelle est l'impact de la pluviométrie sur la production agricole pour chaque produit étudiés ?")
st.write("3. Quelle est l'impact de la température sur la production agricole pour chaque produit étudiés ?")
st.write("4. Quelle est l'impact de l'humidité sur la production agricole chaque produit étudiés ?")
st.write("5. Quelle est l'impact de la pression atmosphérique sur la production agricole chaque produit étudiés ?")
st.write("6. Quelle est l'impact du vent sur la production agricole chaque produit étudiés ?")
# Sélectionner un produit
produits = df_agroclimat['Produit'].unique()
selected_produit = st.selectbox("Sélectionnez un produit", produits, key='produit')

# Filtrer les données en fonction du produit sélectionné
df_filtered = df_agroclimat[df_agroclimat['Produit'] == selected_produit]
facteurs_climatiques = df_agroclimat.columns[-11:]
# Afficher un graphique pour chaque facteur climatique
st.subheader(f"Analyse et visualisation pour le : {selected_produit}")
for facteur in facteurs_climatiques:
    st.write(f"### {facteur} vs {selected_produit}")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df_filtered[facteur], df_filtered['Prod(T)'], alpha=0.5, color='blue')
    ax.set_title(f'Relation entre {facteur} et la production de ({selected_produit})')
    ax.set_xlabel(facteur)
    ax.set_ylabel('Production (T)')
    ax.grid(True)
    st.pyplot(fig)

# Titre de l'application
st.title("Evolution de la production de chaque produit agricole en fonction des facteurs climatiques")
# Sélectionner un facteur climatique
selected_facteur = st.selectbox("Sélectionnez un facteur climatique", facteurs_climatiques, key='facteur')
# Filtrer les produits disponibles pour ce facteur climatique
produits_disponibles = df_agroclimat['Produit'].unique()
selected_produit = st.selectbox("Sélectionnez un produit", produits_disponibles, key='produit1')
# Filtrer les données pour le produit sélectionné
df_filtered = df_agroclimat[df_agroclimat['Produit'] == selected_produit]
# Vérifier si les données sont disponibles
if not df_filtered.empty:
    st.write(f"### Histogramme et distribution pour le facteur {selected_facteur} et le produit {selected_produit}")
    # Créer l'histogramme avec une ligne de densité
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(
        df_filtered[selected_facteur], 
        kde=True, 
        color='blue', 
        bins=15, 
        edgecolor='black', 
        ax=ax
    )
    # Ajouter une ligne de densité avec `gaussian_kde`
    density = gaussian_kde(df_filtered[selected_facteur].dropna())
    x_vals = sns.utils.despine(fig=None, left=True)
    x_vals = plt.xlim()
    x = pd.Series([x / 100.0 * (x_vals[1] - x_vals[0]) + x_vals[0] for x in range(100)])
    y = density(x)
    ax.plot(x, y, color='red', lw=2, label="Densité")
    # Configurer les labels et le titre
    ax.set_title(f"Distribution de {selected_facteur} pour {selected_produit}")
    ax.set_xlabel(selected_facteur)
    ax.set_ylabel("Fréquence")
    ax.legend()
    # Afficher le graphique dans Streamlit
    st.pyplot(fig)

