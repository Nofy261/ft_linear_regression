import sys

def save_thetas(filename, theta0, theta1):
    try:
        with open(filename, "w") as file:
            file.write(f"{theta0},{theta1}\n")
    except IOError:
        print("Error: could not save thetas")
        sys.exit(1)


def save_minmax(filename, km_list):
    min_val = min(km_list)
    max_val = max(km_list)

    try:
        with open(filename, "w") as file:
            file.write(f"{min_val},{max_val}\n")
    except IOError:
        print("Error: could not save min/max")
        sys.exit(1)    


def load_thetas(filename):
    try:
        with open(filename, "r") as file:
            content = file.read().strip()
            values = content.split(",")

            if len(values) != 2:
                 raise ValueError("Invalid theta file format")

            theta0 = float(values[0])
            theta1 = float(values[1])

            return theta0, theta1

    except (FileNotFoundError, ValueError, PermissionError):
        print("Error loading thetas")
        sys.exit(1)


def load_minmax(filename):
    try:
        with open(filename, "r") as file:
            content = file.read().strip()
            if not content:
                raise ValueError("Empty minmax file")

            values = content.split(",")

            if len(values) != 2:
                raise ValueError("Invalid minmax file format")

            min_val = float(values[0])
            max_val = float(values[1])

            return min_val, max_val
            
    except (FileNotFoundError, PermissionError, ValueError):
        print("Error loading min/max values")
        sys.exit(1)


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
