from parsing import read_data
from utils import normalize_km
from utils import save_thetas
from utils import save_min_max
import sys


def train_model(km_list, price_list, learning_rate, iter):
    if len(km_list) != len(price_list):
        print("Error: km and price must have same length")
        sys.exit()

    km_norm = normalize_km(km_list)

    theta0 = 0
    theta1 = 0
    m = len(km_norm)

    # boucle d'apprentissage
    for i in range(iter):
        tmp_theta0 = 0
        tmp_theta1 = 0

        # parcours des donnees
        for j in range(m): 
            estimate_price = theta0 + theta1 * km_norm[j]

            error = estimate_price - price_list[j]

            # permet de comprendre si ma droite predit trop haut ou trop bas les prix

            tmp_theta0 += error
            tmp_theta1 += error * km_norm[j]

        # on clacule la moyenne des corrections 
        # on fait une petite correction répétée plusieurs fois
        # la moyenne sert à ajuster la droite doucement dans la bonne direction
        # de combien je dois changer theta0 et theta1 pour ameliorer la droite de facon stable et progressive
        tmp_theta0 = tmp_theta0 / m
        tmp_theta1 = tmp_theta1 / m

        # on modifie theta0 et theta1
        # nouveau_theta = ancien_theta - correction
        # correction = learning_rate * tmp_theta0
        # ON met à jour la droite en la déplaçant
        # légèrement dans la direction qui réduit l’erreur
        # learning_rate: taille du pas pour corriger la droite

        # on ajuste la hauteur de la droite
        theta0 = theta0 - learning_rate * tmp_theta0

        # on ajuste l inclinaison de la droite
        theta1 = theta1 - learning_rate * tmp_theta1

    save_min_max("minmax.txt", km_list)
    save_thetas("thetas.txt", theta0, theta1)
    return theta0, theta1  






# Python’s numpy.polyfit Interdit

# learnig_rate = determine la vitesse d'apprentissage
# trop grand -> instable
# trop petit -> lent
# iter = nombre de fois qu on repete l'apprentissage (nombre d amelioration)
# a chaque iter : calcul erreur + ajuste theta0 et theta1
# km_list → données
# price_list → vérité

# Modèle :
#     régression linéaire

# Méthode d’apprentissage :
#     gradient descent

# Étapes à faire 
# Initialiser les paramètres :
#     theta0
#     theta1
# Normaliser les données 
# Définir la fonction de prédiction :
#     y = theta1 * x + theta0
# Définir la fonction de coût :
#     calculer l’erreur (MSE)
# Boucle d’entraînement (gradient descent) :
#     calculer les prédictions
#     calculer l’erreur
#     calculer les gradients
#     mettre à jour theta0 et theta1
# Répéter jusqu’à convergence ou nombre d’itérations fixé
# Sauvegarder les résultats :
#     écrire theta0 et theta1 dans theta.txt

# ---------------------------------


# somme des erreurs = prediction - prix reel
# somme pondere par km = (prediction - prix reel) * km

# calcluer erreur pour chaque voiture
# erreur ligne 1 = prediction - prix reel 
# erreur ligne 1 km = 

# pour chaque donnee : on prend km[i] et price[i]
# puis faire une predicion y ​= θ0 ​+ θ1​x
# calclul erreur = prediction - prix reel

# function train_model(km_list, price_list, learning_rate, iterations):

#     # 1. sécurité des données
#     if taille(km_list) != taille(price_list):
#         erreur et stop

#     # 2. normalisation des km
#     km_norm = normalize_km(km_list)

#     # 3. initialisation des paramètres
#     theta0 = 0
#     theta1 = 0

#     # 4. nombre d'exemples
#     m = taille(km_norm)

#     # 5. boucle d'apprentissage
#     pour i de 0 à iterations - 1:

            # le gradient indique la direction,
            # le learning rate ajuste la vitesse d’apprentissage
#         # reset gradients
#         tmp_theta0 = 0 corrige le decalage
#         tmp_theta1 = 0 corrige la pente

#         # 6. parcourir toutes les données
#         pour chaque index j de 0 à m - 1:

#             # prédiction du modèle
#             prediction = theta0 + theta1 * km_norm[j]

#             # erreur
#             erreur = prediction - price_list[j]

#             # accumulation des gradients
#             tmp_theta0 += erreur
#             tmp_theta1 += erreur * km_norm[j]

#         # 7. moyenne des gradients
#         tmp_theta0 = tmp_theta0 / m
#         tmp_theta1 = tmp_theta1 / m

#         # 8. mise à jour des paramètres
#         theta0 = theta0 - learning_rate * tmp_theta0
#         theta1 = theta1 - learning_rate * tmp_theta1

#     # 9. fin du training
#     retourner theta0, theta1

# gradient descent: une méthode pour ajuster theta0 et theta1 progressivement
# But: trouver les meilleures valeurs de theta0 et theta1 qui minimisent l’erreur
 


# 1. utiliser theta actuel
# 2. calculer erreurs
# 3. calculer corrections
# 4. mettre à jour theta


# 1. prédire avec les nouvelles valeurs des thetas a chaque iteration
# 2. mesurer erreur
# 3. accumuler erreurs
# 4. calculer gradient
# 5. corriger theta
# 6. répéter

# | variable | effet sur la droite       |
# | -------- | ------------------------- |
# | theta0   | monte / descend la droite |
# | theta1   | incline la droite         |


    

        



























# ----------------------
# itération 1 :
#     modèle aveugle
#     grosse erreur
#     premier ajustement

# itérations suivantes :
#     correction progressive
#     amélioration continue
# le gradient descent, c’est une droite qui apprend à se déplacer
#  pour coller aux points
# -----------------------
# training ajuste theta0 et theta1 progressivement jusqau a ce que
# erreur entre prediction et vrai prix = minimale
# ----------------------
# price ≈ theta0 + theta1 * km
# theta0 = prix de base
# theta1 = impact du km sur le prix 

# ----------------------
# Input (km_list, price_list)
# ce qu on utilise (km normalisé)
# Output (theta0, theta1)

# ---------------------------

# entraîne le modèle
# trouve les bons paramètres
# une fois bons parametres trouvé -> ecris theta0 et 1 dans le fihcier theta.txt

# tester → mesurer erreur → ajuster → recommencer

# 1 ) train 
# - calculer theta0 et theta1 

# 2) predict
# - utiliser theta0 et theta1
# ------------------------------------



# initialiser theta0 = 0
# initialiser theta1 = 0

# choisir learningRate
# choisir nombre d’itérations

# répéter pour chaque itération :

#     initialiser somme_erreur = 0
#     initialiser somme_erreur_mileage = 0

#     m = nombre de (donnees) ligne dans le fichier
#     m = len(km)
#     pour chaque donnée i :

#         estimation = theta0 + theta1 * mileage[i]

#         erreur = estimation - price[i]

#         somme_erreur += erreur
#         somme_erreur_mileage += erreur * mileage[i]

#     tmp_theta0 = learningRate * (1/m) * somme_erreur
#     tmp_theta1 = learningRate * (1/m) * somme_erreur_mileage

#     # ou 
#     # theta0 -= learningRate * (1/m) * somme_erreur
#     # theta1 -= learningRate * (1/m) * somme_erreur_mileage

#     theta0 = theta0 - tmp_theta0
#     theta1 = theta1 - tmp_theta1

# sauvegarder theta0 et theta1

# ----------------------------


