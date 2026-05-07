entraîne le modèle
trouve les bons paramètres
une fois bons parametres trouvé -> ecris theta0 et 1 dans le fihcier theta.txt

tester → mesurer erreur → ajuster → recommencer

1 ) train 
- calculer theta0 et theta1 

2) predict
- utiliser theta0 et theta1
------------------------------------

Étapes à faire 
Initialiser les paramètres :
    theta0
    theta1
Normaliser les données 
Définir la fonction de prédiction :
    y = theta1 * x + theta0
Définir la fonction de coût :
    calculer l’erreur (MSE)
Boucle d’entraînement (gradient descent) :
    calculer les prédictions
    calculer l’erreur
    calculer les gradients
    mettre à jour theta0 et theta1
Répéter jusqu’à convergence ou nombre d’itérations fixé
Sauvegarder les résultats :
    écrire theta0 et theta1 dans theta.txt

---------------------------------

initialiser theta0 = 0
initialiser theta1 = 0

choisir learningRate
choisir nombre d’itérations

répéter pour chaque itération :

    initialiser somme_erreur = 0
    initialiser somme_erreur_mileage = 0

    m = nombre de (donnees) ligne dans le fichier
    m = len(km)
    pour chaque donnée i :

        estimation = theta0 + theta1 * mileage[i]

        erreur = estimation - price[i]

        somme_erreur += erreur
        somme_erreur_mileage += erreur * mileage[i]

    tmp_theta0 = learningRate * (1/m) * somme_erreur
    tmp_theta1 = learningRate * (1/m) * somme_erreur_mileage

    # ou 
    # theta0 -= learningRate * (1/m) * somme_erreur
    # theta1 -= learningRate * (1/m) * somme_erreur_mileage

    theta0 = theta0 - tmp_theta0
    theta1 = theta1 - tmp_theta1

sauvegarder theta0 et theta1

----------------------------
Faire la normalisation avant le training -> normalize(km, price) :
rendre toutes les valeurs comparables sur une même échelle
on travaille avec des petits nombre au lieu des grands nombres comme 24000
x_norm = (x - min) / (max - min)


def normalize(km, price):
    max = le plus grand  km du fichier
    min = le plus petit  km 
    km = [ listKm ] = [24000, 13545, 547758, ...]

    for i in km:
        x_norm = (x - min) / (max - min)





        ----------------------------

from parsing import read_data

def train_model(km, price, learnig_rate, iter):


