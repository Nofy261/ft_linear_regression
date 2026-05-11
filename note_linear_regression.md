
    OBJECTIF:
 
 1) comprendre comment une machine apprend une formule toute seule
 2)   Le but du projet est de créer un programme qui estime le prix d’une voiture en fonction de son kilométrage, en utilisant des données fournies dans un fichier, et en ajustant progressivement une formule pour obtenir l’estimation la plus précise possible.(Le programme regarde des exemples de voitures, fait des erreurs au début, puis ajuste sa formule petit à petit pour faire des prédictions de plus en plus proches des vrais prix).
    (utiliser les données (km, prix) pour apprendre une relation générale
afin de pouvoir prédire le prix pour n’importe quel km)

On doit coder la suite d’étapes qui permettent à mon programme de “découvrir” la meilleure droite.

implémenter une régression linéaire simple = écrire un programme qui trouve automatiquement les meilleurs paramètres d’une droite
Donc concrètement
Le programme doit apprendre : y = θ₀ + (θ₁ × x) et ajuster : θ₀ et θ₁ jusqu’à obtenir la meilleure approximation possible des données.

------------------------------------------------------
La régression linéaire = le modele mathematique de la formule ci dessous
y = (theta1 * x) + theta0 = une droite 
La formule finale = le résultat de cette méthode

Le gradient descent = la methode d'apprentissage (algo d'optimisation)
Role: trouver les meilleurs theta0 et theta1
------------------------------------------------------

Régression linéaire : 👉 “QUOI utiliser ?” -> Une droite.
Gradient descent :👉 “COMMENT trouver la bonne droite ?” ->
En corrigeant progressivement les erreurs.

Le gradient descent est un algorithme qui ajuste θ₀ et θ₁ progressivement afin de réduire l’erreur entre les prédictions et les vraies valeurs.
Gradient descent = méthode pour améliorer progressivement θ₀ et θ₁ jusqu’à obtenir le meilleur modèle possible.

À chaque itération :
calculer les prédictions -calculer l’erreur -ajuster θ₀ et θ₁ - recommencer


 Données → modèle → erreur → correction → répétition → modèle entraîné 
    
    Ordre complet du projet
📥 lire data.csv
📊 définir la droite (θ₀, θ₁)
🎯 initialiser θ₀, θ₁
🔁 gradient descent (phase centrale)
💾 sauvegarder θ₀, θ₁
🔮 prédire avec la droite finale
    
    OU 
    
problème : droite mauvaise au début
solution : ajuster petit à petit
outil : gradient descent (pour reduire l'erreur)
résultat : meilleure droite possible
    
    
    
 🧭 Les étapes du projet

👉 1. Le programme lit les données
Il récupère le fichier avec des exemples (kilométrage + prix). comprendre tes points

👉 2. Il commence avec une formule au hasard
Au début, il ne sait rien, donc il prend une droite “au pif”. 
tu choisis une droite : y = θ₀ + θ₁ × x

👉 3. Il fait des prédictions / Initialisation
Avec cette formule, il calcule un prix pour chaque voiture.
θ₀ et θ₁ au début sont mauvais (souvent 0)

👉 4. Il mesure ses erreurs
Il compare ses prédictions avec les vrais prix pour voir à quel point il se trompe.

👉 5. Il ajuste sa formule / Améliorer la droite
ajuster θ₀ et θ₁
Il modifie légèrement la droite pour réduire les erreurs.

👉 6. Il répète plusieurs fois
refaire erreur → correction → erreur → correction
jusqu’à stabilisation
Il recommence : prédire → mesurer → ajuster, encore et encore.

👉 7. Il garde la meilleure formule
Quand les erreurs deviennent les plus petites possibles, il s’arrête.
θ₀ et θ₁ sont optimisés
ta droite est la meilleure possible pour tes données

👉 8. Il utilise cette formule pour prédire
Maintenant, il peut estimer le prix d’une nouvelle voiture.
tu peux maintenant prédire un prix pour n’importe quel km


Le projet se fait en deux phases:

Phase I - Training : On apprend le modele 
“j’apprends à partir des données”
input : dataset (km, prix)
output : θ₀, θ₁


Phase II - Prediction: On utlise le modele
“j’utilise ce que j’ai appris”
input : km utilisateur
output : prix estimé


-------------------
data.csv = km | prix 

km -> variable d'entree(x)
prix -> variable de sortie(y)

chaque ligne = un point (km, prix)
l'esnsemble = mon dataset

Exemple concret
vrai prix = 10 000 €
prix estimé = 10 005 €

👉 erreur = +5

“Le programme utilise les erreurs de toutes les lignes pour calculer une erreur globale qui représente la performance moyenne de sa prédiction.”


À la fin de cette étape, le programme obtient une erreur globale, qu’on peut voir comme une erreur moyenne du modèle sur toutes les données.



Pour chaque ligne :

👉 il calcule une erreur :
erreur = prix estimé − vrai prix

Si on faisait juste une moyenne simple :

+10 et -10 donneraient 0 😬
alors que le modèle se trompe beaucoup en réalité

👉 Donc on transforme chaque erreur :

✔️ On les met au carré

👉 erreur²


📊 Puis on combine tout

Il fait :

👉 somme de toutes les erreurs²
👉 puis il divise par le nombre de lignes


“Le programme calcule l’erreur sur chaque ligne, les met au carré pour éviter les annulations, puis fait une moyenne pour obtenir une erreur globale.

🧭 Les étapes pour obtenir l’erreur globale
1. 🔮 Prédiction (par ligne)

Pour chaque voiture :
👉 il calcule un prix estimé avec la formule
θ0 + θ1 × kilométrage

2. 📉 Erreur (par ligne)

👉 il compare avec le vrai prix
👉 il obtient une erreur :
erreur = estimé − réel

3. 🔒 Transformation

👉 il met l’erreur au carré (pour éviter les signes négatifs)

4. 📊 Agrégation

👉 il additionne toutes les erreurs²

5. ➗ Moyenne

👉 il divise par le nombre de lignes

🎯 Résultat final

👉 un seul nombre : l’erreur globale du modèle



1. Phase d’apprentissage (training)
Tu regardes toutes les données
Tu ajustes θ₀ et θ₁
Tu trouves la “meilleure droite”

👉 C’est là que se passe le gros du projet

2. Phase d’utilisation (prédiction)
Tu prends un nouveau km
Tu appliques :
→ prix = θ₀ + θ₁ × km

-----------------------------------------------
 3 idées du projet :

1. Une droite
2. Une erreur
3. Une boucle qui corrige la droite


 je charge mes données
 je les comprends
 je définis une droite
 je calcule une erreur
 j’ajuste θ₀ et θ₁
 je répète
 je sauvegarde
 je prédis



ordre :

lecture data
prédiction simple (sans training)
gradient descent
boucle complète


1- training program

Le training fait ça en boucle :
je prédis
je me trompe
je mesure l’erreur
j’ajuste θ₀ et θ₁
je recommence

Pseudo code
charger data.csv

extraire:
    km[]
    price[]

normaliser km

initialiser:
    theta0 = 0
    theta1 = 0

répéter (ex: 1000 fois):

    predictions = []

    pour chaque i dans dataset:
        prediction = theta0 + theta1 * km[i]
        ajouter prediction à predictions

    erreur_theta0 = 0
    erreur_theta1 = 0

    pour chaque i dans dataset:
        erreur = prediction[i] - price[i]
        erreur_theta0 += erreur
        erreur_theta1 += erreur * km[i]

    theta0 = theta0 - learningRate * (erreur_theta0 / m)
    theta1 = theta1 - learningRate * (erreur_theta1 / m)

fin boucle

sauvegarder theta0 et theta1 dans un fichier


2 - prediction program

charger theta0 et theta1 depuis fichier

demander input:
    mileage utilisateur

normaliser mileage (si nécessaire)

prediction = theta0 + theta1 * mileage

afficher prediction

-----------------------

points (km, price)
        ↓
   droite au hasard
        ↓
   erreurs énormes
        ↓
   correction (gradient descent)
        ↓
   meilleure droite
        ↓
   modèle entraîné
        ↓
   prédiction

---------------------



model.py (le plus important):
la fonction de prédiction (y = ax + b)
le gradient descent
les calculs math

 train.py :
charger les données
appeler model.py pour entraîner
sauvegarder les paramètres (theta)

predict.py :
charger les paramètres
prendre une input utilisateur
afficher la prédiction





Étape 1 (la vraie priorité)

Coder l’apprentissage :

lire le dataset
initialiser θ₀ et θ₁
appliquer la descente de gradient
obtenir des valeurs finales de θ₀ et θ₁

👉 À la fin, ton programme doit être capable de dire :

“voici la meilleure droite que j’ai trouvée”

✅ Étape 2

Utiliser ces paramètres pour faire des prédictions :

tu donnes un kilométrage
le programme calcule un prix
---------------------------------

prix_predit = theta0 + (theta1 * km )
Erreur = prix_predit - prix_reel

si -100 = modele sous estime
si +100 = modele sur-estime

θ₀ → “ma droite est trop haute ou trop basse ?”
θ₁ → “ma droite est trop plate ou trop inclinée ?”

-------------------
1. tu calcules toutes les erreurs

✔️ -100, -200, -300

2. tu fais des sommes

✔️ somme des erreurs
✔️ somme des erreurs × km

3. tu appliques les formules du sujet

✔️ tmpθ₀
✔️ tmpθ₁

4. tu updates θ₀ et θ₁
5. tu recommences
---------------------------

✔️ θ₀ → somme des erreurs
✔️ θ₁ → somme des (erreurs × km)
------------------------
pipeline correct est :
calcul des erreurs
somme
division par m
multiplication par learningRate
update θ₀ et θ₁
--------------------

calcul des erreurs pour chaque ligne
erreur = (θ0 ​+ θ1 ​× km) − prix_reel
---------------

prediction = calcul du prix_predit  "estimatePrice = θ0​ + (θ1 ​× mileage)
Erreur = on a la moyenne de thetha0_tmp et thetha1_tmp on garde ces deux valeurs tmp


la descente de gradient, c’est juste :
“je regarde mes erreurs → je résume → je corrige θ₀ et θ₁”

Ce que représente cette étape
θ
0
	​

=θ
0
	​

−learningRate×gradient
0
	​

θ
1
	​

=θ
1
	​

−learningRate×gradient
1
	​


👉 Ça veut dire :

“je corrige mes paramètres en fonction de l’erreur globale”

la descente de gradient, c’est déplacer la droite dans la direction qui réduit l’erreur”


-----------------------

somme_erreur
somme_erreur km 
-------------------------

SYNTAXE:

with ; permet d'ouvrir le fichier et le fermer automatiquement
strip() permet de nettoyer le debut et la fin. Ex : "  a b c ! " devient "a b c !" et "\n" -> ""

--------------

normalisation :
-pour rendre le calcul de gradient descent stable et efficace

Ex: theta1 * km <--- Or les Km sont tres grands 240000 donc
    les erreurs deviennent trop grand, le resultat sera trop grand
    le gradient descnet peut apprendre tres lentement , osciller et diverger

Avec la normalisation , les valeurs deviennent petites et comparable

La normalisation sert a ameliorer le calcul des thetas pendant le gradient descent .
On normalise pour aider l'algorithme a apprendre correctemnt.

---------------------

read_data → données brutes
normalize_km → préparation
train → apprend theta0 / theta1
predict → utilise ces valeurs












































