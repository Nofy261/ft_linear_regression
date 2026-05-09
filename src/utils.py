from parsing import read_data

def normalize_km(km_list: list):
    max_val = max(km_list)
    min_val = min(km_list)
    km_norm = []

    # if min != max
    for i in km_list:
        i_norm = (i - min_val) / (max_val - min_val)
        km_norm.append(i_norm)
    return km_norm


# // outils math reutilisable
# Étapes:
# Créer la fonction de normalisation (si utilisée) :
#     centrer / réduire ou min-max
# Créer la fonction de dénormalisation (si nécessaire)
# Créer la fonction de prédiction :
#     y = theta1 * x + theta0
# Créer la fonction de calcul d’erreur :
#     MSE (Mean Squared Error)
# Fonctions math simples (optionnel)  :
#     somme
#     moyenne...
# ------------------------------

# parsing - normalisation - gradient descent

# km brut → transformation mathématique → km normalisé
# normalisation : change les echelle des donnees pas leur valeurs
# Avec le calcul on transforme les valeurs reelles de base en position
# relative entre 0 et 1 
# 0 val min et 1 val max , et entre les deux position proportionnelle

# Faire la normalisation avant le training -> normalize(km, price) :
# rendre toutes les valeurs comparables sur une même échelle
# on travaille avec des petits nombre au lieu des grands nombres comme 24000
