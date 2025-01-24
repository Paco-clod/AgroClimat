import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import branca.colormap as branca_cm
import seaborn as sns
import plotly.express as px
from sklearn.preprocessing import LabelEncoder
import streamlit as st
from joblib import load
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.ensemble import RandomForestRegressor

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


# Encodage des variables catégorielles
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

##################################    Modele Arima pour la prédiction      #####################################

# Sélection des données climatiques pertinentes
data_clim = df_agroclimat[['Departement', 'Communes', 'Produit', 'Annees', 'PS(kPa)', 'T2M(°C)', 'T2M_MIN(°C)', 'T2M_MAX(°C)', 'QV2M(g/kg)', 'RH2M(%)', 'WD2M(°)', 'WS2M(m/s)', 'GWETROOT(1)', 'GWETTOP(1)', 'PRECTOTCORR(mm/an)']]
# Groupement des données par commune
grouped_data = data_clim.groupby(['Departement','Communes', 'Produit'])
# DataFrames pour stocker les résultats
performance_df_arima = pd.DataFrame()
prediction_df_arima = pd.DataFrame()

model_arima = load('model_arima.joblib')

#############################    Modèle de prévision avec RandomForest   ##########################################
# Préparation des données
# Sélection des variables pertinentes
features = agrocleaned[['Departement', 'Communes', 'Produit', 'Sup(ha)', 'PS(kPa)', 'T2M(°C)', 'T2M_MIN(°C)',
                         'T2M_MAX(°C)', 'QV2M(g/kg)', 'RH2M(%)', 'WD2M(°)', 'WS2M(m/s)',
                         'GWETROOT(1)', 'GWETTOP(1)', 'PRECTOTCORR(mm/an)']]


target_clim = agrocleaned[['PS(kPa)', 'T2M(°C)', 'T2M_MIN(°C)', 'T2M_MAX(°C)', 'QV2M(g/kg)',
                           'RH2M(%)', 'WD2M(°)', 'WS2M(m/s)', 'GWETROOT(1)', 'GWETTOP(1)',
                           'PRECTOTCORR(mm/an)']]
target_prod = agrocleaned[['Prod(T)']]

# Vérification des valeurs manquantes dans les targets
target_prod.isnull().sum()
target_prod.fillna(0, inplace=True)
target_prod.isnull().sum()

X_train, X_test, y_train_clim, y_test_clim = train_test_split(features, target_clim, test_size=0.2, random_state=42)
_, _, y_train_prod, y_test_prod = train_test_split(features, target_prod, test_size=0.2, random_state=42)

# Chargement des modèles
model_clim = load('model_clim.joblib')
model_prod = load('model_prod.joblib')

# Prévision des facteurs climatiques et de la production
y_pred_clim = model_clim.predict(X_test)
y_pred_prod = model_prod.predict(X_test)

# Cross-validation
scores_clim = cross_val_score(model_clim, X_train, y_train_clim, cv=5)
scores_prod = cross_val_score(model_prod, X_train, y_train_prod, cv=5)

# Évaluation du modèle pour les facteurs climatiques et agricoles
# Calcul des métriques climatiques
mse_clim = mean_squared_error(y_test_clim, y_pred_clim)
r2_clim = r2_score(y_test_clim, y_pred_clim)
rmse_clim = np.sqrt(mse_clim)
mae_clim = mean_absolute_error(y_test_clim, y_pred_clim)
# Calcul des métriques de production
mse_prod = mean_squared_error(y_test_prod, y_pred_prod)
r2_prod = r2_score(y_test_prod, y_pred_prod)
mae_prod = mean_absolute_error(y_test_prod, y_pred_prod)
rmse_prod = np.sqrt(mse_prod)

# Prévision des facteurs climatiques et de la production pour les 5 prochaines années
# Création d'un DataFrame pour les 5 prochaines années
future_years_list = [] # Use a list to store the rows

for product in agrocleaned['Produit'].unique():
    for commune in agrocleaned['Communes'].unique():
        # Get the 'Departement' for this commune
        departement = agrocleaned[agrocleaned['Communes'] == commune]['Departement'].iloc[0]
        for year in range(2024, 2029):
            new_row = {'Produit': product, 'Departement': departement, 'Communes': commune, 'Annees': year} # Include 'Departement'
            future_years_list.append(new_row) # Append to list

future_years = pd.DataFrame(future_years_list) # Create DataFrame from list

last_year = agrocleaned['Annees'].max()  # Trouver la dernière année
last_year_data = agrocleaned[agrocleaned['Annees'] == last_year]

for idx, row in future_years.iterrows():
    filtered_last_year_data = last_year_data[
        (last_year_data['Produit'] == row['Produit']) &
        (last_year_data['Communes'] == row['Communes'])
    ]
    if not filtered_last_year_data.empty:
        for col in ['Sup(ha)', 'PS(kPa)', 'T2M(°C)', 'T2M_MIN(°C)', 'T2M_MAX(°C)', 'QV2M(g/kg)', 'RH2M(%)',
                    'WD2M(°)', 'WS2M(m/s)', 'GWETROOT(1)', 'GWETTOP(1)', 'PRECTOTCORR(mm/an)']:
            future_years.at[idx, col] = filtered_last_year_data[col].values[0]

# Prédiction des facteurs climatiques pour les 5 prochaines années
# Use the same columns as those used during training
future_clim = model_clim.predict(future_years[['Departement', 'Communes', 'Produit', 'Sup(ha)', 'PS(kPa)', 'T2M(°C)', 'T2M_MIN(°C)',
                         'T2M_MAX(°C)', 'QV2M(g/kg)', 'RH2M(%)', 'WD2M(°)', 'WS2M(m/s)',
                         'GWETROOT(1)', 'GWETTOP(1)', 'PRECTOTCORR(mm/an)']])
future_years[['PS(kPa)', 'T2M(°C)', 'T2M_MIN(°C)', 'T2M_MAX(°C)', 'QV2M(g/kg)', 'RH2M(%)',
              'WD2M(°)', 'WS2M(m/s)', 'GWETROOT(1)', 'GWETTOP(1)', 'PRECTOTCORR(mm/an)']] = future_clim

# Prédiction de la production agricole
# Include 'Sup(ha)' in the prediction
future_years['Prod(T)_predite'] = model_prod.predict(future_years[['Departement', 'Communes', 'Produit', 'Sup(ha)', 'PS(kPa)', 'T2M(°C)', 'T2M_MIN(°C)',
                                                                   'T2M_MAX(°C)', 'QV2M(g/kg)', 'RH2M(%)',
                                                                   'WD2M(°)', 'WS2M(m/s)', 'GWETROOT(1)',
                                                                   'GWETTOP(1)', 'PRECTOTCORR(mm/an)']])

# Affichage des résultats

# Inverser l'encodage
inverse_labelisation(future_years)



# Fonction pour prédire les facteurs climatiques et la production agricole
modele_choisi = st.selectbox(label = "Choisissez un modèle ", options=["ARIMA", "Random Forest"])

def test_model(modele_choisi):
    if modele_choisi == "ARIMA":
        y_pred_arima = prediction_df_arima
        st.subheader("Prévision des facteurs climatiques et de la production pour les 5 prochaines années:")
        st.dataframe(prediction_df_arima)

    elif modele_choisi == "Random Forest" :
        y_pred_climat = y_pred_clim
        y_pred_production = y_pred_prod
        st.write("Cross-validation")
        st.write(f"Scores climatiques : {scores_clim.mean()}, Scores production : {scores_prod.mean()}")
        # Évaluation du modèle pour les facteurs climatiques et agricoles
        st.write("Évaluation de la Performance du modèle pour la prédiction des facteurs climatiques:")
        st.write("MSE (Erreur Quadratique Moyenne):", mse_clim)
        st.write("R² (Coefficient de détermination) :", r2_clim)
        st.write("RMSE (Racine Carrée de l'Erreur Quadratique Moyenne):", rmse_clim)
        st.write("MAE (Erreur Absolue Moyenne):", mae_clim)
        st.write("\nÉvaluation de la Performance du modèle pour la prédiction de la production:")
        st.write("MSE (Erreur Quadratique Moyenne):", mse_prod)
        st.write("R² (Coefficient de détermination) :", r2_prod)
        st.write("RMSE (Racine Carrée de l'Erreur Quadratique Moyenne):", rmse_prod)
        st.write("MAE (Erreur Absolue Moyenne):", mae_prod)

        st.subheader("Prévision des facteurs climatiques et de la production pour les 5 prochaines années:")
        st.dataframe(future_years)
    else:
        st.write("Données non disponibles")

test_model(modele_choisi)

st.title("Tableau de Bord Climatique et Agricole")

# Widgets de sélection
produits = future_years['Produit'].unique()
annees = sorted(future_years['Annees'].unique())  # Trier par ordre croissant
communes = future_years['Communes'].unique()

selected_product = st.selectbox("Sélectionnez un produit", produits)
selected_year = st.selectbox("Sélectionnez une année", annees)
selected_commune = st.selectbox("Sélectionnez une commune", communes)

# Filtrage des données
filtered_data = future_years[
    (future_years['Produit'] == selected_product) &
    (future_years['Annees'] == selected_year) &
    (future_years['Communes'] == selected_commune)
]

if not filtered_data.empty:
    # Extraire les valeurs des indicateurs
    temp_moyenne = filtered_data["T2M(°C)"].values[0]
    temp_min = filtered_data["T2M_MIN(°C)"].values[0]
    temp_max = filtered_data["T2M_MAX(°C)"].values[0]
    precipitation = filtered_data["PRECTOTCORR(mm/an)"].values[0]
    production_predite = filtered_data["Prod(T)_predite"].values[0]

    # Seuils d'alerte
    temp_alerte = 30  # Seuil de température élevée (°C)
    precip_alerte = 500  # Seuil de faible précipitation (mm/an)
    prod_alerte = 50  # Seuil de production faible (tonnes)

    # Affichage des indicateurs sous forme de colonnes
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="🌡️ Température Moyenne (°C)", value=f"{temp_moyenne:.2f}", delta="⚠️ Alerte" if temp_moyenne > temp_alerte else "")

    with col2:
        st.metric(label="🌡️ Température Min / Max (°C)", value=f"{temp_min:.2f} / {temp_max:.2f}")

    with col3:
        st.metric(label="🌧️ Précipitations (mm/an)", value=f"{precipitation:.2f}", delta="⚠️ Alerte" if precipitation < precip_alerte else "")

    # Deuxième ligne d'indicateurs
    col4, col5 = st.columns(2)

    with col4:
        st.metric(label="🌾 Production Agricole Prédite (Tonnes)", value=f"{production_predite:.2f}", delta="⚠️ Alerte" if production_predite < prod_alerte else "")

    # Comparaison avec l'année précédente (si disponible)
    previous_year = selected_year - 1
    previous_data = future_years[
        (future_years['Produit'] == selected_product) &
        (future_years['Annees'] == previous_year) &
        (future_years['Communes'] == selected_commune)
    ]

    if not previous_data.empty:
        prev_production = previous_data["Prod(T)_predite"].values[0]
        variation = production_predite - prev_production
        variation_percent = (variation / prev_production) * 100

        with col5:
            st.metric(
                label="📉 Variation de Production (%)",
                value=f"{variation_percent:.2f}%",
                delta=f"{variation:.2f} Tonnes",
                delta_color="inverse" if variation < 0 else "normal"
            )
    else:
        with col5:
            st.write("📉 Pas de données pour l'année précédente.")

    # Carte Interactive : Visualisation des communes
    st.subheader("🌍 Carte des Communes avec Précipitations et Température")
    
    # Créer une carte avec Plotly
    map_data = future_years.groupby(['Departement', 'Communes', 'Annees']).agg({
        'T2M(°C)': 'mean',
        'PRECTOTCORR(mm/an)': 'mean'
    }).reset_index()

    fig = px.scatter_geo(map_data,
                         locations='Communes',
                         hover_name='Communes',
                         size='PRECTOTCORR(mm/an)',  # Taille basée sur les précipitations
                         color='T2M(°C)',  # Couleur basée sur la température
                         color_continuous_scale='Viridis',
                         size_max=50,
                         template="plotly_dark",
                         title="Carte Interactive : Température et Précipitations par Commune")

    st.plotly_chart(fig)

else:
    st.warning("⚠️ Aucune donnée trouvée pour cette combinaison.")