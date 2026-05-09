
# // creer une focntion qui return km et price(liste de nombre)

import sys

def read_data(csvfile):
    km_list = []
    price_list = []
    try:
        with open(csvfile, "r") as file:
            # lire et ignore la 1ere ligne
            file.readline()
            for line in file:
                cleaned_line = line.strip()
            # si ligne vide apres strip() on ignore sinon on traite
                if not cleaned_line: 
                    continue
                split_line = cleaned_line.split(",")
                if len(split_line) != 2:
                    continue
                try:
                    km_to_float = float(split_line[0])
                    price_to_float = float(split_line[1])
                except ValueError:
                    continue
            # ajoute km le kmList et price dans priceList
                km_list.append(km_to_float)
                price_list.append(price_to_float)
            # ou if not km:
            if len(km_list) == 0 or len(price_list) == 0:
                print("Empty file")
                sys.exit()

    except FileNotFoundError:
        print("File error")
        sys.exit()
    return (km_list, price_list)


# def test():
#     tab = read_data("data.csv")
#     print(tab)
#     # ([listKm], [listPrice])
    
# test()