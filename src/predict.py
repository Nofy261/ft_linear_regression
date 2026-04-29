utilise le modèle entraîné
fait des prédictions
calcul de prediction donné dans le sujet 
price_predict = theta0 + (thetha1 * km)

ecrire un efonction qui utilise la formule pour :
MAE = erreur (difference entre le vrai prix et le prix estimer)

erreur = prix_estimer - prix_reel

somme de toutes les erreurs divisé par le nombre des voitures = moyenne erreur 
----------------------------------
1) train = calculer theta0 et theta1
2) predict = utliser theta0 et theta1
-------------------------------

etapes:

lire theta0 et theta1 depuis le fichier

demander à l’utilisateur un mileage

calculer estimation :
    prix = theta0 + theta1 * mileage

afficher le prix estimé