from parsing import read_data
from utils import normalize_km
import sys


# learnig_rate = determine la vitesse d'apprentissage
# trop grand -> instable
# trop petit -> lent
# iter = nombre de fois qu on repete l'apprentissage
# a chaque iter : calcul erreur + ajuste theta0 et theta1
# km_list → données
# price_list → vérité
# learning_rate → vitesse
# iter → nombre d’essais


def train_model(km_norm, price_list, learning_rate, iter):
    if len(km_norm) != len(price_list):
        print("Error in the list")
        sys.exit()

    normalize_km(km_norm)
    theta_0 = 0
    theta_1 = 0





















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


