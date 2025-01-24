import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
import plotly.express as px

df_agroclimat = pd.read_excel("agroclimat.xlsx")

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


st.subheader("Matrice de corrélation entre nos données agricoles et climatique")
# Corrélation entre données climatique
df_agroclimat_selected = df_agroclimat[['Sup(ha)', 'Prod(T)', 'PS(kPa)', 'T2M(°C)', 'T2M_MIN(°C)', 'T2M_MAX(°C)', 'QV2M(g/kg)', 'RH2M(%)', 'WD2M(°)', 'WS2M(m/s)', 'GWETROOT(1)', 'GWETTOP(1)', 'PRECTOTCORR(mm/an)']]

# Calculate the correlation matrix
matrix_agroclimat = df_agroclimat_selected.corr()
#Matrice de corrélation
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(matrix_agroclimat, annot=True, fmt=".2f", ax=ax, cmap="coolwarm")
# Set the title and show the plot
plt.title("Matrix de corrélation entre nos données agricole et climatique")
st.pyplot(fig)
st.write("La matrice de corrélation ci-dessus montre la relation entre les différentes variables climatiques et agricoles. Les valeurs de corrélation varient de -1 à 1. Une valeur de 1 signifie une corrélation positive parfaite, tandis qu'une valeur de -1 signifie une corrélation négative parfaite. Une valeur de 0 signifie qu'il n'y a pas de corrélation entre les variables.")

st.subheader("Matrice de corrélation entre nos données Climatiques uniquement")
# Calculate the correlation matrix
matrix_climat = df_agroclimat_selected.corr()
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(matrix_climat, annot=True, fmt=".2f", ax=ax, cmap="coolwarm")
# Set the title and show the plot
plt.title("Matrix de Correlation entre nos données Climatiques uniquement")
st.pyplot(fig)
st.write("La matrice de corrélation ci-dessus montre la relation entre les différentes variables climatiques. Les valeurs de corrélation varient de -1 à 1. Une valeur de 1 signifie une corrélation positive parfaite, tandis qu'une valeur de -1 signifie une corrélation négative parfaite. Une valeur de 0 signifie qu'il n'y a pas de corrélation entre les variables.")
st.write("L'objectif ici est de comprendre la realation entre les variables climatiques entre elles. Cela nous permettra de mieux comprendre les interactions entre les différentes variables climatiques.")

st.subheader("Matrice de corrélation entre toutes les données Agricoles par produit avec les données Climatiques")
# Vérifiez que les colonnes nécessaires existent
required_columns = ['Produit', 'Prod(T)', 'PS(kPa)', 'T2M(°C)', 'T2M_MIN(°C)', 'T2M_MAX(°C)', 'QV2M(g/kg)', 'RH2M(%)', 'WD2M(°)', 'WS2M(m/s)', 'GWETROOT(1)', 'GWETTOP(1)', 'PRECTOTCORR(mm/an)']
if not all(col in df_agroclimat.columns for col in required_columns):
    st.error("Le DataFrame ne contient pas toutes les colonnes nécessaires.")
else:
    # Liste unique des produits
    produits = df_agroclimat["Produit"].unique()
    # Sélecteur de produit
    produit_selectionne = st.selectbox("Sélectionnez un produit", produits)
    # Filtrer les données pour le produit sélectionné
    df_product = df_agroclimat[df_agroclimat["Produit"] == produit_selectionne]
    # Sélectionner les colonnes pour la matrice de corrélation
    df_corr = df_product[['Prod(T)', 'PS(kPa)', 'T2M(°C)', 'T2M_MIN(°C)', 'T2M_MAX(°C)', 
                          'QV2M(g/kg)', 'RH2M(%)', 'WD2M(°)', 'WS2M(m/s)', 'GWETROOT(1)', 
                          'GWETTOP(1)', 'PRECTOTCORR(mm/an)']]
    # Calcul de la matrice de corrélation
    corr_matrix = df_corr.corr()
    # Création de la heatmap
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    # Ajouter un titre
    ax.set_title(f"Matrice de corrélation pour le produit : {produit_selectionne}")
    # Afficher le graphique dans Streamlit
    st.pyplot(fig)
    st.write("La matrice de corrélation ci-dessus montre la relation entre les différentes variables climatiques et agricoles pour le produit sélectionné.")


st.subheader("Matrice de corrélation entre les données Agricoles par communes avec les données Climatiques spécifiques à chaque communes")
# Vérifiez que les colonnes nécessaires existent
required_columns = ['Departement', 'Communes', 'Produit', 'Prod(T)', 'PS(kPa)', 'T2M(°C)', 'T2M_MIN(°C)',
                    'T2M_MAX(°C)', 'QV2M(g/kg)', 'RH2M(%)', 'WD2M(°)', 'WS2M(m/s)',
                    'GWETROOT(1)', 'GWETTOP(1)', 'PRECTOTCORR(mm/an)']
if not all(col in df_agroclimat.columns for col in required_columns):
    st.error("Le DataFrame ne contient pas toutes les colonnes nécessaires.")
else:
    # Liste unique des départements et produits
    communes = df_agroclimat["Communes"].unique()
    produits = df_agroclimat["Produit"].unique()

    # Sélecteurs interactifs
    selected_communes = st.selectbox("Sélectionnez une commune ", communes, key='communes')
    selected_product = st.selectbox("Sélectionnez un produit", produits, key='produit3')

    # Filtrer les données par département et produit
    filtered_data = df_agroclimat[
        (df_agroclimat["Communes"] == selected_communes) &
        (df_agroclimat["Produit"] == selected_product)
    ]
    # Vérifier si des données correspondent au filtre
    if filtered_data.empty:
        st.warning("Aucune donnée disponible pour cette sélection.")
    else:
        # Sélectionner les colonnes pour la matrice de corrélation
        df_corr = filtered_data[['Prod(T)', 'PS(kPa)', 'T2M(°C)', 'T2M_MIN(°C)', 'T2M_MAX(°C)',
                                 'QV2M(g/kg)', 'RH2M(%)', 'WD2M(°)', 'WS2M(m/s)',
                                 'GWETROOT(1)', 'GWETTOP(1)', 'PRECTOTCORR(mm/an)']]
        # Calculer la matrice de corrélation
        corr_matrix = df_corr.corr()
        # Créer une heatmap
        fig, ax = plt.subplots(figsize=(12, 10))
        sns.heatmap(corr_matrix, annot=True, fmt=".2f", ax=ax, cmap="coolwarm")
        # Ajouter un titre
        ax.set_title(f"Matrice de corrélation pour {selected_product} dans la communes de {selected_communes}")
        # Afficher la heatmap dans Streamlit
        st.pyplot(fig)
        st.write("La matrice de corrélation ci-dessus montre la relation entre les différentes variables climatiques et agricoles pour le produit et la commune sélectionnés.")


st.subheader("Facteurs climatiques favorables à la production agricole")
if not all(col in df_agroclimat.columns for col in required_columns):
    st.error("Le DataFrame ne contient pas toutes les colonnes nécessaires.")
else:
    # Sélecteurs interactifs pour le département, la commune et le produit
    selected_departement = st.selectbox("Sélectionnez un département", df_agroclimat['Departement'].unique())
    selected_communed = st.selectbox(
        "Sélectionnez une commune", 
        df_agroclimat[df_agroclimat['Departement'] == selected_departement]['Communes'].unique()
    )
    selected_producted = st.selectbox(
        "Sélectionnez un produit", 
        df_agroclimat[
            (df_agroclimat['Departement'] == selected_departement) & 
            (df_agroclimat['Communes'] == selected_communed)
        ]['Produit'].unique()
    )

    # Filtrer les données pour le département, la commune et le produit sélectionnés
    filtered_data = df_agroclimat[
        (df_agroclimat['Departement'] == selected_departement) &
        (df_agroclimat['Communes'] == selected_communed) &
        (df_agroclimat['Produit'] == selected_producted)
    ]

    # Vérifier si les données filtrées existent
    if filtered_data.empty:
        st.warning("Aucune donnée disponible pour cette sélection.")
    else:
        # Calculer la matrice de corrélation
        df_corr = filtered_data[['Prod(T)', 'PS(kPa)', 'T2M(°C)', 'T2M_MIN(°C)', 'T2M_MAX(°C)',
                                 'QV2M(g/kg)', 'RH2M(%)', 'WD2M(°)', 'WS2M(m/s)', 
                                 'GWETROOT(1)', 'GWETTOP(1)', 'PRECTOTCORR(mm/an)']]
        corr_matrix = df_corr.corr()

        # Identifier les facteurs favorables
        favorable_factors = corr_matrix['Prod(T)'][corr_matrix['Prod(T)'] > 0.15].index.tolist()

        if 'Prod(T)' in favorable_factors:
            favorable_factors.remove('Prod(T)')  # Exclure la corrélation avec elle-même

        # Afficher les résultats
        if favorable_factors:
            st.success(f"Dans la commune de {selected_communed} ({selected_departement}), les facteurs climatiques suivants favorisent la production de {selected_producted} :")
            for factor in favorable_factors:
                st.write(f"- **{factor}**")
        else:
            st.info(f"Dans la commune de {selected_communed} ({selected_departement}), aucun facteur climatique n'a une forte corrélation positive avec la production de {selected_producted}.")
        
        st.write("La matrice de corrélation ci-dessus montre la relation entre les différentes variables climatiques et agricoles pour le produit, la commune et le département sélectionnés.")

st.write("L'objectif de cette analyse est de comprendre les relations entre les variables climatiques et agricoles, et d'identifier les facteurs climatiques qui favorisent la production agricole dans une région donnée. Ces informations peuvent être utiles pour les agriculteurs et les décideurs pour prendre des décisions éclairées sur la gestion des cultures et l'adaptation aux conditions climatiques.")

# Calculer la production moyenne par département et produit
commune_product_production = df_agroclimat.groupby(['Departement', 'Produit'])['Prod(T)'].mean().reset_index()

# Trouver les 6 produits avec la production moyenne la plus élevée pour chaque département
top_products_by_commune = commune_product_production.groupby('Departement').apply(
    lambda x: x.nlargest(6, 'Prod(T)')
).reset_index(drop=True)

# Interface Streamlit
st.title("Top 6 Produits par Département")
selected_department = st.selectbox("Sélectionnez un département :", df_agroclimat['Departement'].unique())

# Filtrer les données pour le département sélectionné
filtered_data = top_products_by_commune[top_products_by_commune['Departement'] == selected_department]
# Afficher les résultats sous forme de tableau
if not filtered_data.empty:
    st.write(f"Les 6 produits les plus performants pour le département **{selected_department}** :")
    st.table(filtered_data)
else:
    st.warning(f"Aucun produit trouvé pour le département {selected_department}.")
# Afficher un graphique des produits par production
if not filtered_data.empty:
    fig = px.bar(
        filtered_data,
        x='Produit',
        y='Prod(T)',
        title=f"Top 6 Produits par Production Moyenne dans le Département {selected_department}",
        labels={'Prod(T)': 'Production Moyenne (T)', 'Produit': 'Produit'},
        text='Prod(T)'
    )
    st.plotly_chart(fig)
st.write("L'objectif de cette analyse est d'identifier les 6 produits les plus performants pour chaque département en termes de production moyenne. Cela peut aider les agriculteurs et les décideurs à comprendre quels produits sont les plus rentables ou les plus productifs dans chaque région.")  