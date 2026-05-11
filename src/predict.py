# utilise le modèle entraîné
# fait des prédictions
# calcul de prediction donné dans le sujet 
# price_predict = theta0 + (thetha1 * km)

# ecrire un efonction qui utilise la formule pour :
# MAE = erreur (difference entre le vrai prix et le prix estimer)

# 1) train = calculer theta0 et theta1
# 2) predict = utliser theta0 et theta1 ()
# -------------------------------

# input utilisateur → calcul → affichage résultat

# Vérifier le fichier theta.txt / lire theta0 et theta1 depuis fichier
#     existe - lisible -pas vide
# Lire le fichier theta.txt
# Recuperer les deux valeurs
# Vérifier l’entrée utilisateur (x)
#     est un nombre valide (km saisi par l'user')
# Appliquer la formule de prédiction :
#     y = theta1 * x + theta0
# Afficher le résultat(les utliser pour calculer la prediction) 


# OU 
# etapes:

# lire theta0 et theta1 depuis le fichier

# demander à l’utilisateur un km
# normaliser ce km (si nécessaire)
# calculer estimation :  calculer price estimé
#     prix = theta0 + theta1 * km
# afficher le prix estimé

# 1. lire theta0 et theta1 depuis fichier
# 2. récupérer km utilisateur
# 3. normaliser km (avec min/max sauvegardés)
# 4. calculer prix
# 5. afficher résultat


#  load_theta et load_min_max = load_model 
# A FAIRE creer load_model : sert a recuperer les valeurs stockés
# ici min et max , et theta0 et theta1
# 1. ouvrir fichier
# 2. lire ligne
# 3. découper valeurs
# 4. convertir en float
# 5. retourner les valeurs

def predict(km):
    theta0, theta1, min_km, max_km = load_model()

    km_norm = (km - min_km) / (max_km - min_km)

    price = theta0 + theta1 * km_norm

    print(f"Estimated price: {price}")