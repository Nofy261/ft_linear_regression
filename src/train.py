entraîne le modèle
trouve les bons paramètres

tester → mesurer erreur → ajuster → recommencer

1 ) train 
- calculer theta0 et theta1 

2) predict
- utiliser theta0 et theta1

---------------------------------

 Etape : gradient descent
lire le fichier data.csv
stocker toutes les valeurs mileage et price

initialiser theta0 = 0
initialiser theta1 = 0

choisir learningRate
choisir nombre d’itérations

répéter pour chaque itération :

    initialiser somme_erreur = 0
    initialiser somme_erreur_mileage = 0

    pour chaque donnée i :

        estimation = theta0 + theta1 * mileage[i]

        erreur = estimation - price[i]

        somme_erreur += erreur
        somme_erreur_mileage += erreur * mileage[i]

    tmp_theta0 = learningRate * (1/m) * somme_erreur
    tmp_theta1 = learningRate * (1/m) * somme_erreur_mileage

    theta0 = theta0 - tmp_theta0
    theta1 = theta1 - tmp_theta1

sauvegarder theta0 et theta1