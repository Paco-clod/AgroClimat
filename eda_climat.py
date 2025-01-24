import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns

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

st.dataframe(df_agroclimat.head(25))



# Filter the data for selected communes
communes_to_plot = ['KANDI', 'NATITINGOU', 'PARAKOU', 'BOHICON', 'SAVE', 'COTONOU']
filtered_data = df_agroclimat[df_agroclimat['Communes'].isin(communes_to_plot)]
# Group the data by department and year
grouped_data = filtered_data.groupby(['Annees', 'Communes'])[['PRECTOTCORR(mm/an)', 'PS(kPa)', 'T2M(°C)', 'T2M_MIN(°C)', 'T2M_MAX(°C)', 'QV2M(g/kg)', 'RH2M(%)', 'WD2M(°)', 'WS2M(m/s)', 'GWETROOT(1)', 'GWETTOP(1)']].mean()
# Streamlit interface
st.title("Évolution des Variables Climatiques")
st.write("Sélectionnez une variable pour afficher son évolution par station synoptique et par année.")
# Selectbox to choose the variable
variables = ['PRECTOTCORR(mm/an)', 'PS(kPa)', 'T2M(°C)', 'T2M_MIN(°C)', 'T2M_MAX(°C)', 'QV2M(g/kg)', 'RH2M(%)', 'WD2M(°)', 'WS2M(m/s)', 'GWETROOT(1)', 'GWETTOP(1)']
selected_variable = st.selectbox("Choisissez une variable", variables, key='variable')
# Create the line chart for the selected variable
if selected_variable:
    st.write(f"Évolution de la variable {selected_variable} par station synoptique et par année")
    # Plot the line chart
    plt.figure(figsize=(20, 12))
    grouped_data[selected_variable].unstack().plot(kind='line', figsize=(16, 8), marker='o')
    # Add titles and labels
    plt.title(f'Évolution de la variable {selected_variable} par Station synoptique et par année')
    plt.xlabel('Années')
    plt.ylabel(f'{selected_variable} (1)')
    # Display the plot in Streamlit
    st.pyplot(plt)
# Description of the data
st.write("Les données climatiques sont collectées par station synoptique et par année. Les variables climatiques disponibles sont les suivantes :")
st.write("- PRECTOTCORR(mm/an) : Précipitations totales corrigées (mm/an)")
st.write("- PS(kPa) : Pression de surface (kPa)")
st.write("- T2M(°C) : Température de l'air à 2m (°C)")
st.write("- T2M_MIN(°C) : Température minimale de l'air à 2m (°C)")
st.write("- T2M_MAX(°C) : Température maximale de l'air à 2m (°C)")
st.write("- QV2M(g/kg) : Humidité spécifique à 2m (g/kg)")
st.write("- RH2M(%) : Humidité relative à 2m (%)")
st.write("- WD2M(°) : Direction du vent à 2m (°)")
st.write("- WS2M(m/s) : Vitesse du vent à 2m (m/s)")
st.write("- GWETROOT(1) : Humidité du sol à 1m (1)")
st.write("- GWETTOP(1) : Humidité du sol à la surface (1)")
st.write("On peut retenir que les précipitations totales corrigées sont plus élevées à Parakou, tandis que la pression de surface est plus élevée à Natitingou. La température de l'air à 2m est plus élevée à Bohicon, tandis que la température minimale de l'air à")



# Grouper les données par département et calculer la somme des facteurs climatiques
df_climat_par_departement = df_agroclimat.groupby('Departement')[[
    'PRECTOTCORR(mm/an)', 'PS(kPa)', 'T2M(°C)', 'T2M_MIN(°C)', 'T2M_MAX(°C)', 
    'QV2M(g/kg)', 'RH2M(%)', 'WD2M(°)', 'WS2M(m/s)', 'GWETROOT(1)', 'GWETTOP(1)'
]].sum().reset_index()

# Streamlit title and description
st.title("Évolution des facteurs climatiques par département")
st.write("Sélectionnez un facteur climatique pour voir son évolution par département.")

# Liste des facteurs climatiques disponibles
climatic_factors = [
    'PRECTOTCORR(mm/an)', 'PS(kPa)', 'T2M(°C)', 'T2M_MIN(°C)', 'T2M_MAX(°C)', 
    'QV2M(g/kg)', 'RH2M(%)', 'WD2M(°)', 'WS2M(m/s)', 'GWETROOT(1)', 'GWETTOP(1)'
]

# Sélectionner un facteur climatique
selected_factor = st.selectbox("Choisissez un facteur climatique", climatic_factors, key='climatic_factor')

# Créer un graphique à barres pour le facteur climatique sélectionné
if selected_factor:
    # Filtrer les données en fonction du facteur climatique sélectionné
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Définir une palette de couleurs
    palette = sns.color_palette("Set2", n_colors=1)
    
    # Créer le graphique à barres
    sns.barplot(x='Departement', y=selected_factor, data=df_climat_par_departement, palette=palette)
    
    # Ajouter des titres et des labels
    ax.set_title(f'Valeur de {selected_factor} par département')
    ax.set_xlabel('Département')
    ax.set_ylabel(selected_factor)
    
    # Afficher le graphique dans Streamlit
    st.pyplot(fig)
    
    # Description des données
    st.write(f"L'évolution du facteur climatique {selected_factor} est affichée pour chaque département.")
st.write("La courbe ci-dessus montre l'évolution des facteurs climatiques par département. De ce graphe on retient que les précipitations totales corrigées sont plus élevées dans le département de la Donga, tandis que la température minimale de l'air à 2m est plus basse dans le département de l'Alibori. La température maximale de l'air à 2m est plus élevée dans le département de l'Atlantique, tandis que l'humidité spécifique à 2m est plus élevée dans le département de l'Atacora. L'humidité relative à 2m est plus élevée dans le département de l'Atlantique, tandis que la vitesse du vent à 2m est plus élevée dans le département de l'Alibori. L'humidité du sol à 1m est plus élevée dans le département de l'Alibori, tandis que l'humidité du sol à la surface est plus élevée dans le département de l'Atlantique.")


# Grouper les données par département et commune, puis calculer la moyenne des facteurs climatiques
df_climat_par_commune = df_agroclimat.groupby(['Departement', 'Communes'])[['PRECTOTCORR(mm/an)', 'PS(kPa)', 'T2M(°C)', 'T2M_MIN(°C)', 'T2M_MAX(°C)', 'QV2M(g/kg)', 'RH2M(%)', 'WD2M(°)', 'WS2M(m/s)', 'GWETROOT(1)', 'GWETTOP(1)']].mean().reset_index()
# Streamlit title and description
st.title("Visualisation des Facteurs Climatiques par Commune")
st.write("Sélectionnez un facteur climatique pour afficher la répartition par commune.")
# Liste des facteurs climatiques disponibles
facteurs_climatiques = [
    'PRECTOTCORR(mm/an)', 'PS(kPa)', 'T2M(°C)', 'T2M_MIN(°C)', 'T2M_MAX(°C)', 
    'QV2M(g/kg)', 'RH2M(%)', 'WD2M(°)', 'WS2M(m/s)', 'GWETROOT(1)', 'GWETTOP(1)'
]

# Sélecteur pour choisir un facteur climatique
selected_factor = st.selectbox("Choisissez un facteur climatique", facteurs_climatiques, key='facteur_climatique')
# Définir les couleurs (par exemple, une palette de couleurs distinctes pour chaque département)
colors = sns.color_palette("Set2", n_colors=len(df_agroclimat['Departement'].unique()))
# Filtrer les données en fonction du facteur sélectionné
df_factor = df_climat_par_commune[['Departement', 'Communes', selected_factor]]
# Créer un graphique à barres pour le facteur climatique sélectionné, groupé par commune
fig, ax = plt.subplots(figsize=(16, 8))  # Ajuster la taille du graphique si nécessaire
sns.barplot(x='Communes', y=selected_factor, hue='Departement', data=df_factor, palette=colors)
# Ajouter un titre et des labels
ax.set_title(f'Valeur moyenne de {selected_factor} par commune')
ax.set_xlabel('Commune')
ax.set_ylabel(selected_factor)
# Rotation des labels de l'axe des X pour une meilleure lisibilité
plt.xticks(rotation=90)
# Légende
plt.legend(title='Département', loc='upper right')
# Ajuster la mise en page pour éviter les chevauchements
plt.tight_layout()
# Afficher le graphique dans Streamlit
st.pyplot(fig)
st.write("La répartition des facteurs climatiques par commune est affichée dans le graphique ci-dessus. On peut voir que les précipitations totales corrigées sont plus élevées à Kandi, tandis que la pression de surface est plus élevée à Natitingou. La température de l'air à 2m est plus élevée à Bohicon, tandis que la température minimale de l'air à 2m est plus basse à Kandi. La température maximale de l'air à 2m est plus élevée à Bohicon, tandis que l'humidité spécifique à 2m est plus élevée à Kandi. L'humidité relative à 2m est plus élevée à Bohicon, tandis que la direction du vent à 2m est plus élevée à Kandi. La vitesse du vent à 2m est plus élevée à Kandi, tandis que l'humidité du sol à 1m est plus élevée à Kandi. L'humidité du sol à la surface est plus élevée à Bohicon.")