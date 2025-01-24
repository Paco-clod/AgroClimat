import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder

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

def apply_pca(df, variance_threshold=0.95):
    """
    Applique l'ACP et retourne les données transformées et les paramètres clés.
    """
    data = preprocessing.StandardScaler().fit_transform(df_clim.iloc[:, 2:])
    
    # Initialisation et ajustement du PCA
    pca = PCA().fit(data)
    cumulative_explained_variance = np.cumsum(pca.explained_variance_ratio_)
    
    # Déterminer le nombre optimal de composantes
    n_components = np.argmax(cumulative_explained_variance >= variance_threshold) + 1
    pca = PCA(n_components=n_components).fit(data)
    pca_data = pca.transform(data)
    
    return pca, pca_data, n_components, cumulative_explained_variance

def plot_explained_variance(cumulative_explained_variance):
    """
    Affiche la variance expliquée cumulée sous forme de graphique.
    """
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(cumulative_explained_variance, marker='o')
    ax.axhline(y=0.95, color='r', linestyle='--', label="Seuil 95%")
    ax.set_xlabel("Nombre de composantes")
    ax.set_ylabel("Variance expliquée cumulée")
    ax.set_title("Variance expliquée par l'ACP")
    ax.set_xticks(range(len(cumulative_explained_variance)))
    ax.set_yticks(np.arange(0, 1.1, 0.1))
    ax.grid(True)
    ax.legend()
    return fig

def plot_correlation_circle(pca, df):
    """
    Affiche le cercle de corrélation des composantes principales.
    """
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    
    # Cercle
    cercle = plt.Circle((0, 0), 1, color='blue', fill=False)
    ax.add_artist(cercle)
    
    # Affichage des flèches et des labels
    for i, (x, y) in enumerate(zip(pca.components_[0, :], pca.components_[1, :])):
        ax.arrow(0, 0, x, y, alpha=0.5)
        ax.text(x, y, df.columns[i+2], fontsize=12)  # Décalage pour ignorer les 2 premières colonnes
    
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_title("Cercle de corrélation des composantes principales")
    
    return fig
def elbow_method(pca_data, max_clusters=40):
    """
    Calcule l'inertie pour différents nombres de clusters (méthode du coude).
    """
    elbow = []
    for i in range(2, max_clusters):
        km = KMeans(n_clusters=i, random_state=42)
        km.fit(pca_data)
        elbow.append(km.inertia_)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(range(2, max_clusters), elbow, "x-")
    ax.set_xlabel("Nombre de clusters")
    ax.set_ylabel("Inertie")
    ax.set_title("Méthode du Coude pour déterminer le nombre optimal de clusters")
    
    return fig

def apply_kmeans(pca_data, n_clusters):
    """
    Applique KMeans sur les données transformées par PCA.
    """
    km = KMeans(n_clusters=n_clusters, random_state=42)
    pred = km.fit_predict(pca_data)
    
    return km, pred

def plot_clusters(pca, km, df):
    """
    Affiche les clusters sous forme de barres pour voir les profils des groupes.
    """
    tab20 = plt.get_cmap('tab20')
    cols = (df_clim.columns.tolist())

    real_centers = pca.inverse_transform(km.cluster_centers_)
    fig, axs = plt.subplots(km.n_clusters // 2, 2, sharey=True, sharex=True, figsize=(10, 20))
    
    for i,k in enumerate(real_centers):
        # Use modulo operator to cycle through the colors
        axs.flatten()[i].bar(range(len(k)),k,color=tab20.colors[i%len(tab20.colors)])
        axs.flatten()[i].set_xticks(range(len(k)))
        axs.flatten()[i].set_xticklabels(cols[:len(k)],rotation="vertical")
        axs.flatten()[i].set_title(f'Cluster {i+1}')

    
    plt.tight_layout()
    return fig