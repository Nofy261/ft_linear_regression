
format cohérent ✔️
données numériques ✔️

# // creer une focntion qui return km et price(liste de nombre)


def read_data(csvfile):
    km = []
    price = []
    try:
        with open(csvfile, "r") as file:
            file.readline()
            for line in file:
                print(line)

            # mettre le parsing ici
            # lire et ignorer la 1ere ligne
            # parcourir toutes les autres lignes du fichier
            # pour chaque ligne : verifier qu elle n est pas vide et
            #                     enlever les espaces et le \n
            # split les deux valeurs km et price
            # convertir les valeurs en float
            # ajouter : les km dans la liste km et les prices dans liste price
            # gerer les lignes invalides:
            # si ligne mal former : ignorer ou message d erreur ??
            # 

    except FileNotFoundError:
        print("Can't open the file")

    return (km, price)

# for line in file:
#     line = line.strip()
    # if not line:
    #     continue