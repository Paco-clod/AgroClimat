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
    
st.title("Analyse des données agricoles")
st.write("Dans cette section, nous allons explorer les données agricoles pour comprendre les tendances générales des rendements agricoles, des superficies cultivées et de la production agricole.")

df_agroclimat.fillna(0, inplace=True)
df_agroclimat[['Sup(ha)', 'Prod(T)']] = df_agroclimat[['Sup(ha)', 'Prod(T)']].apply(pd.to_numeric, errors='coerce')


st.title("#Departement avec les meilleures production en moyenne")
# Calcul du rendement moyen par commune
df_rendement_moyen = df_agroclimat.groupby('Departement')['Prod(T)'].mean().sort_values(ascending=False)
# Création du graphique
cmap = cm.get_cmap('tab10')
colors = cmap(np.linspace(0, 1, len(df_rendement_moyen)))
df_rendement_moyen.plot(kind='bar', color=colors, figsize=(10, 5))
# Ajout des labels et du titre
plt.xlabel('Département')
plt.ylabel('Production moyenne (T)')
plt.title('Départements avec les meilleures productions en moyenne')
# Affichage du graphique
st.pyplot(plt)
# Description du graphique
st.write("Le graphique ci-dessus montre les départements avec les meilleures productions agricoles en moyenne. Les départements sont classés en fonction de leur production moyenne en tonnes (T).")


st.title("#Production totale en moyenne dans chaque commune par département")
# Sélection du département à analyser
departements = df_agroclimat['Departement'].unique()
departement_selectionne = st.selectbox('Choisissez un département', departements)
# Filtrer les données pour le département sélectionné
df_temp = df_agroclimat[df_agroclimat['Departement'] == departement_selectionne]
# Créer le graphique
plt.figure(figsize=(10, 6))
sns.barplot(x='Communes', y='Prod(T)', data=df_temp, palette='viridis')
plt.title(f'Production totale en moyenne dans chaque commune dans le département de {departement_selectionne}')
plt.xlabel('Communes')
plt.ylabel('Production totale (T)')
plt.xticks(rotation=90)  # Faire pivoter les étiquettes de l'axe des x pour une meilleure lisibilité
plt.tight_layout()  # Ajuster la disposition pour éviter le chevauchement
# Afficher le graphique dans l'application Streamlit
st.pyplot(plt)
# Description du graphique
st.write("Le graphique ci-dessus montre la production totale moyenne en tonnes pour chaque commune dans le département sélectionné.")


st.title("#Rendement moyen par département")
df_rendement_moyen = df_agroclimat.groupby('Departement')['Rend(kg/ha)'].mean().sort_values(ascending=False)
# Création du graphique
cmap = cm.get_cmap('tab10')
colors = cmap(np.linspace(0, 1, len(df_rendement_moyen)))
plt.figure(figsize=(10, 5))
df_rendement_moyen.plot(kind='bar', color=colors)
# Ajout des labels et du titre
plt.xlabel('Département')
plt.ylabel('Rendement moyen en (kg/ha)')
plt.title('Départements avec les meilleurs rendements agricoles en moyenne')
# Affichage du graphique
st.pyplot(plt)
plt.clf()  # Nettoyage de la figure
# Description du graphique
st.write("Le graphique ci-dessus montre les départements avec les meilleurs rendements agricoles en moyenne. Les départements sont classés en fonction de leur rendement moyen en kilogrammes par hectare (kg/ha).")



st.title("#Rendement moyen par commune dans un département")
# Récupérer la liste des départements
departements = df_agroclimat['Departement'].unique()

# Sélectionner un département interactif sur la page principale
departement_selectionne = st.selectbox("Choisissez un département", departements, key="departement_select")

# Filtrer les données pour le département sélectionné
df_prod_par_commune = df_agroclimat.groupby(['Departement', 'Communes'])['Rend(kg/ha)'].mean().reset_index()
df_prod_par_commune = df_prod_par_commune[df_prod_par_commune['Departement'] == departement_selectionne]

# Trier les données par rendement décroissant
df_prod_par_commune = df_prod_par_commune.sort_values('Rend(kg/ha)', ascending=False)

# Générer une palette de couleurs pour les communes du département sélectionné
cmap = cm.get_cmap('tab10')
colors = cmap(np.linspace(0, 1, len(df_prod_par_commune)))  # Générer une palette dynamique
# Créer le graphique
plt.figure(figsize=(12, 6))
sns.barplot(x='Communes', y='Rend(kg/ha)', data=df_prod_par_commune, palette=colors)
# Ajouter les labels et le titre
plt.title(f'Rendement moyen par commune dans le département de {departement_selectionne}')
plt.xlabel('Commune')
plt.ylabel('Rendement moyen (kg/ha)')
# Pivoter les étiquettes de l'axe des X pour plus de lisibilité
plt.xticks(rotation=90, ha='right')
# Ajuster la mise en page pour éviter le chevauchement des éléments
plt.tight_layout()
# Afficher le graphique dans l'application Streamlit
st.pyplot(plt)
# Description du graphique
st.write("Le graphique ci-dessus montre le rendement moyen en kilogrammes par hectare (kg/ha) pour chaque commune dans le département sélectionné.")

st.title("#Superficie moyenne cultivée par commune dans un département")
df_superficie_moyenne = df_agroclimat.groupby('Departement')['Sup(ha)'].mean().sort_values(ascending=False)

# Création du graphique
cmap = cm.get_cmap('tab10')
colors = cmap(np.linspace(0, 1, len(df_superficie_moyenne)))
plt.figure(figsize=(10, 5))
df_superficie_moyenne.plot(kind='bar', color=colors)

# Ajout des labels et du titre
plt.xlabel('Département')
plt.ylabel('Superficie moyenne en hectares (ha)')
plt.title('Départements avec les plus grandes superficies moyennes cultivées')

# Affichage du graphique
st.pyplot(plt)
plt.clf()  # Nettoyage de la figure

# Description du graphique
st.write("Le graphique ci-dessus montre les départements avec les plus grandes superficies moyennes cultivées en hectares (ha). "
             "Les départements sont classés par ordre décroissant en fonction de la superficie moyenne.")



# Sélectionner un département interactif sur la page principale
departements = df_agroclimat['Departement'].unique()  
# Récupérer les départements du DataFrame
# Ajouter une clé unique pour le selectbox
departement_selectionne = st.selectbox("Choisissez un département", departements, key="departement_select1")
# Filtrer les données pour le département sélectionné
df_prod_par_commune = df_agroclimat.groupby(['Departement', 'Communes'])['Sup(ha)'].mean().reset_index()
df_prod_par_commune = df_prod_par_commune[df_prod_par_commune['Departement'] == departement_selectionne]
# Trier les données par superficie décroissante
df_prod_par_commune = df_prod_par_commune.sort_values('Sup(ha)', ascending=False)
# Générer une palette de couleurs pour les communes du département sélectionné
cmap = cm.get_cmap('tab10')
colors = cmap(np.linspace(0, 1, len(df_prod_par_commune)))  # Générer une palette dynamique
# Créer le graphique
plt.figure(figsize=(12, 6))
sns.barplot(x='Communes', y='Sup(ha)', data=df_prod_par_commune, palette=colors)
# Ajouter les labels et le titre
plt.title(f'Superficie moyenne par commune dans le département de {departement_selectionne}')
plt.xlabel('Commune')
plt.ylabel('Superficie moyenne (hectar)')
# Pivoter les étiquettes de l'axe des X pour plus de lisibilité
plt.xticks(rotation=90, ha='right')
# Ajuster la mise en page pour éviter le chevauchement des éléments
plt.tight_layout()
# Afficher le graphique dans l'application Streamlit
st.pyplot(plt)


st.title("# Moyenne de production par produit")
# Calcul de la moyenne de production par produit
production = df_agroclimat.groupby('Produit')['Prod(T)'].mean().sort_values(ascending=False)
# Création du graphique
cmap = cm.get_cmap('tab10')
colors = cmap(np.linspace(0, 1, len(production)))
plt.figure(figsize=(10, 5))
production.plot(kind='bar', color=colors)
# Ajout des labels et du titre
plt.title('Moyenne de production par produit')
plt.xlabel('Produit')
plt.ylabel('Production moyenne (tonnes)')
plt.xticks(rotation=90)
# Affichage du graphique
st.pyplot(plt)
plt.clf()  # Nettoyage de la figure
# Description du graphique
st.write("Le graphique ci-dessus montre la moyenne de production en tonnes pour chaque produit agricole. "
             "Les produits sont classés par ordre décroissant de production moyenne.")


st.title("#Produits avec les meilleurs rendements moyens")
rendements = df_agroclimat.groupby('Produit')['Rend(kg/ha)'].mean().sort_values(ascending=False)
# Création du graphique
cmap = cm.get_cmap('tab10')
colors = cmap(np.linspace(0, 1, len(rendements)))
plt.figure(figsize=(10, 5))
rendements.plot(kind='bar', color=colors)

# Ajout des labels et du titre
plt.title('Moyenne des rendements par produit')
plt.xlabel('Produit')
plt.ylabel('Rendement moyen (kg/ha)')
plt.xticks(rotation=90)

# Affichage du graphique
st.pyplot(plt)
plt.clf()  # Nettoyage de la figure
# Description du graphique
st.write("Le graphique ci-dessus montre les produits agricoles avec les meilleurs rendements moyens en kilogrammes par hectare (kg/ha). "
             "Les produits sont classés par ordre décroissant de rendement moyen.")

st.title("#Produits avec les plus grandes superficies cultivées")
# Group the data by product and department
grouped_data = df_agroclimat.groupby(['Produit', 'Departement'])['Sup(ha)'].mean().unstack()
# Plot the data as a heatmap
plt.figure(figsize=(14, 7))
sns.heatmap(grouped_data, cmap='Blues', annot=True, fmt=".0f")
plt.xlabel('Departement')
plt.ylabel('Produit')
plt.title('Superficie cultivée par chaque produit par departement')
st.pyplot(plt)
# Description du graphique
st.write("Le graphique ci-dessus montre la superficie moyenne cultivée pour chaque produit agricole dans chaque département.")


st.header("#Rendement de chaque produit par departement")
# Group the data by product and department
grouped_data = df_agroclimat.groupby(['Produit', 'Departement'])['Rend(kg/ha)'].mean().unstack()

# Plot the data as a heatmap
plt.figure(figsize=(14, 7))
sns.heatmap(grouped_data, cmap='Blues', annot=True, fmt=".0f")
plt.xlabel('Departement')
plt.ylabel('Produit')
plt.title('Rendement de chaque produit par departement')
st.pyplot(plt)
# Description du graphique
st.write("Le graphique ci-dessus montre le rendement moyen en kilogrammes par hectare (kg/ha) pour chaque produit agricole dans chaque département.")


st.title("#Production par produit et par commune dans un département")
# Groupement des données
df_prod_par_commune_produit = df_agroclimat.groupby(['Departement', 'Communes', 'Produit'])['Prod(T)'].sum().reset_index()
# Sélectionner un département
departements = df_prod_par_commune_produit['Departement'].unique()
departement_selectionne = st.selectbox("Choisissez un département", departements, key="departement_select2")
# Filtrer les données pour le département sélectionné
df_temp = df_prod_par_commune_produit[df_prod_par_commune_produit['Departement'] == departement_selectionne]
# Liste des produits dans le département sélectionné
produits = df_temp['Produit'].unique()
# Créer des sous-graphiques pour chaque produit
st.write(f"### Production par produit et par commune dans le département de {departement_selectionne}")
for produit in produits:
    df_produit = df_temp[df_temp['Produit'] == produit].sort_values('Prod(T)', ascending=False)

    # Créer un graphique pour le produit courant
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Communes', y='Prod(T)', data=df_produit, palette='magma')
    plt.title(f'Production de {produit})')
    plt.xlabel('Communes')
    plt.ylabel('Production totale (T)')
    plt.xticks(rotation=90)
    # Afficher le graphique dans l'application Streamlit
    st.pyplot(plt)
# Description des résultats
st.write("Les graphiques ci-dessus montrent la répartition de la production totale (en tonnes) par commune pour chaque produit dans le département sélectionné.")



# Titre de l'application
st.title("Analyse des superficies moyennes par commune et produit dans chaque département")
# Groupement des données
df_prod_par_commune_produit = df_agroclimat.groupby(['Departement', 'Communes', 'Produit'])['Sup(ha)'].mean().reset_index()
# Sélectionner un département
departements = df_prod_par_commune_produit['Departement'].unique()
departement_selectionne = st.selectbox("Choisissez un département", departements, key="departement_select3")
# Filtrer les données pour le département sélectionné
df_temp = df_prod_par_commune_produit[df_prod_par_commune_produit['Departement'] == departement_selectionne]
# Liste des produits dans le département sélectionné
produits = df_temp['Produit'].unique()
# Afficher des graphiques pour chaque produit
st.write(f"### Superficie moyenne occupée par produit et commune dans le département de {departement_selectionne}")
for produit in produits:
    df_produit = df_temp[df_temp['Produit'] == produit].sort_values('Sup(ha)', ascending=False)

    # Créer un graphique pour le produit courant
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Communes', y='Sup(ha)', data=df_produit, palette='magma')
    plt.title(f'Superficie moyenne occupée par {produit} dans chaque commune ({departement_selectionne})')
    plt.xlabel('Communes')
    plt.ylabel('Superficie moyenne (ha)')
    plt.xticks(rotation=90)
    # Afficher le graphique dans Streamlit
    st.pyplot(plt)
# Description des résultats
st.write("Les graphiques ci-dessus montrent la superficie moyenne (en hectares) occupée par chaque produit dans les communes du département sélectionné.")

# Titre de l'application
st.title("Analyse des rendements moyens par produit et commune dans chaque département")
# Groupement des données
df_prod_par_commune_produit = df_agroclimat.groupby(['Departement', 'Communes', 'Produit'])['Rend(kg/ha)'].mean().reset_index()
# Sélectionner un département
departements = df_prod_par_commune_produit['Departement'].unique()
departement_selectionne = st.selectbox("Choisissez un département", departements, key="departement_select4")
# Filtrer les données pour le département sélectionné
df_temp = df_prod_par_commune_produit[df_prod_par_commune_produit['Departement'] == departement_selectionne]
# Liste des produits dans le département sélectionné
produits = df_temp['Produit'].unique()
# Afficher des graphiques pour chaque produit
st.write(f"### Rendements moyens par produit et commune dans le département de {departement_selectionne}")
for produit in produits:
    df_produit = df_temp[df_temp['Produit'] == produit].sort_values('Rend(kg/ha)', ascending=False)
    # Créer un graphique pour le produit courant
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Communes', y='Rend(kg/ha)', data=df_produit, palette='magma')
    plt.title(f'Rendement moyen de {produit} dans chaque commune ({departement_selectionne})')
    plt.xlabel('Communes')
    plt.ylabel('Rendement moyen (kg/ha)')
    plt.xticks(rotation=90)
    # Afficher le graphique dans Streamlit
    st.pyplot(plt)
# Description des résultats
st.write("Les graphiques ci-dessus montrent les rendements moyens (en kg/ha) pour chaque produit dans les communes du département sélectionné.")


# Titre de l'application
st.title("Meilleure production par produit et département")
# Liste des départements pour la sélection
departements = df_agroclimat['Departement'].unique()
departement_selectionne = st.selectbox("Choisissez un département", departements, key="departement_select5")
# Filtrer les données pour le département sélectionné
df_temp = df_agroclimat[df_agroclimat['Departement'] == departement_selectionne]
# Trouver les communes avec la meilleure production pour chaque produit
if not df_temp.empty:
    best_communes = (
        df_temp.loc[df_temp.groupby('Produit')['Prod(T)'].idxmax()][['Produit', 'Communes', 'Prod(T)']]
    )

    # Afficher les résultats dans un tableau interactif
    st.write(f"Dans le département de **{departement_selectionne}**, les communes avec la meilleure production par produit sont :")
    st.dataframe(best_communes)

else:
    st.write("Aucune donnée disponible pour le département sélectionné.")


# Titre de l'application
st.title("Analyse des meilleures productions par produit et département")
# Liste des départements pour la sélection
departements = df_agroclimat['Departement'].unique()
departement_selectionne = st.selectbox("Choisissez un département", departements, key="departement_select6")
# Filtrer les données pour le département sélectionné
df_temp = df_agroclimat[df_agroclimat['Departement'] == departement_selectionne]
# Trouver les communes avec la meilleure production pour chaque produit
if not df_temp.empty:
    best_communes = (
        df_temp.loc[df_temp.groupby('Produit')['Prod(T)'].idxmax()][['Produit', 'Communes', 'Prod(T)']]
    )

    # Afficher les résultats dans un tableau interactif
    st.write(f"Dans le département de **{departement_selectionne}**, les communes avec la meilleure production par produit sont :")
    st.dataframe(best_communes)

    # Afficher un graphique pour visualiser les meilleures productions par produit
    st.subheader("Visualisation des meilleures productions par produit")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(
        x='Produit', y='Prod(T)', hue='Communes', data=best_communes, palette='viridis', dodge=False
    )
    ax.set_title(f"Meilleure production par produit dans le département de {departement_selectionne}")
    ax.set_xlabel("Produit")
    ax.set_ylabel("Production totale (T)")
    plt.legend(title="Communes", bbox_to_anchor=(1.05, 1), loc='upper left')
    # Afficher le graphique dans Streamlit
    st.pyplot(fig)

    # Afficher un graphique détaillé pour toutes les communes et produits
    st.subheader("Détail de la production pour toutes les communes et produits")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(
        x='Communes', y='Prod(T)', hue='Produit', data=df_temp, palette='magma'
    )
    ax.set_title(f"Production par commune et produit dans le département de {departement_selectionne}")
    ax.set_xlabel("Communes")
    ax.set_ylabel("Production totale (T)")
    plt.xticks(rotation=90)
    plt.legend(title="Produit", bbox_to_anchor=(1.05, 1), loc='upper left')
    st.pyplot(fig)

else:
    st.write("Aucune donnée disponible pour le département sélectionné.")


# Group the data by department, commune, and product, then calculate the total production for each combination
df_prod_par_commune_produit = df_agroclimat.groupby(['Departement', 'Communes', 'Produit'])['Prod(T)'].sum().reset_index()
# Application Streamlit
st.title("Analyse des pourcentages de production par produit dans chaque commune")
# Sélectionner un département
departements = df_prod_par_commune_produit['Departement'].unique()
departement_selectionne = st.selectbox("Choisissez un département", departements)
# Filtrer les données pour le département sélectionné
df_temp_dept = df_prod_par_commune_produit[df_prod_par_commune_produit['Departement'] == departement_selectionne]
# Créer des graphiques en camembert pour chaque commune
for commune in df_temp_dept['Communes'].unique():
    df_temp_commune = df_temp_dept[df_temp_dept['Communes'] == commune].copy()
    # Calculer le pourcentage de production pour chaque produit dans la commune
    total_production_commune = df_temp_commune['Prod(T)'].sum()
    df_temp_commune['Percentage'] = (df_temp_commune['Prod(T)'] / total_production_commune) * 100
    # Créer le graphique en camembert
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.pie(
        df_temp_commune['Percentage'],
        labels=df_temp_commune['Produit'],
        autopct='%1.1f%%',
        startangle=180
    )
    ax.set_title(f"Pourcentage de production dans la commune {commune} ({departement_selectionne})")
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)
    # Afficher les détails sous forme de tableau
    st.write(f"Répartition des produits dans la commune {commune} :")
    st.dataframe(df_temp_commune[['Produit', 'Prod(T)', 'Percentage']])
# Description des résultats
st.write("Les graphiques ci-dessus montrent la répartition de la production par produit dans chaque commune du département sélectionné.")


# Interface utilisateur Streamlit
st.title("Évolution de la Superficie Occupée par Produit")
st.write("Sélectionnez un produit pour voir l'évolution de la superficie occupée par ce produit.")

# Grouper les données par produit
grouped_data = df_agroclimat.groupby(['Produit', 'Communes'])

# Sélectionner un produit
products = df_agroclimat['Produit'].unique()
selected_product = st.selectbox("Choisissez un produit", products, key="product_select")

# Sélectionner une commune
communes = df_agroclimat['Communes'].unique()
selected_commune = st.selectbox("Choisissez une commune", communes, key="commune_select")

# Affichage des graphiques pour le produit et la commune sélectionnés
if selected_product and selected_commune:
    # Obtenir les données du groupe sélectionné (Produit et Commune)
    commune_data = grouped_data.get_group((selected_product, selected_commune))
    
    st.write(f"Affichage de la superficie occupée par la culture de {selected_product} dans la commune {selected_commune}")
    
    # Calcul de la superficie moyenne par année
    df_production_par_annee = commune_data.groupby(['Annees'])['Sup(ha)'].mean()

    # Créer un graphique linéaire
    fig, ax = plt.subplots(figsize=(15, 9))
    df_production_par_annee.plot(kind='line', marker='o', ax=ax)
    
    # Ajouter les labels et le titre
    ax.set_xlabel('Années')
    ax.set_ylabel('Superficie en Ha')
    ax.set_title(f'Évolution de la superficie occupée par la culture de {selected_product} dans la commune {selected_commune}')

    # Afficher le graphique dans Streamlit
    st.pyplot(fig)

    # Description des résultats
    st.write(f"L'évolution de la superficie occupée par la culture de {selected_product} dans la commune {selected_commune} est affichée ci-dessus.")
    st.write("Les données sont regroupées par année et la superficie moyenne est calculée pour chaque année.")
    st.write("Le graphique montre comment la superficie cultivée a évolué au fil des ans.")
    st.write("Vous pouvez sélectionner un autre produit ou une autre commune pour afficher les données correspondantes.")