
# // creer une focntion qui return km et price(liste de nombre)

import sys

def read_data(csvfile):
    km = []
    price = []
    try:
        with open(csvfile, "r") as file:
            # lire et ignore la 1ere ligne
            file.readline()
            for line in file:
                cleanedLine = line.strip()
                # si ligne vide apres strip() on ignore sinon on traite
                if not cleanedLine: 
                    continue
                splitLine = cleanedLine.split(",")
                if len(splitLine) != 2:
                    continue
                try:
                    kmToFloat = float(splitLine[0])
                    priceToFloat = float(splitLine[1])
                except ValueError:
                    continue
                # ajoute km le kmList et price dans priceList
                km.append(kmToFloat)
                price.append(priceToFloat)
    except FileNotFoundError:
        sys.exit()

    return (km, price)