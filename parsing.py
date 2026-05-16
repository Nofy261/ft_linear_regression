
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
                    km = float(split_line[0])
                    price = float(split_line[1])
                except ValueError:
                    continue
            
                km_list.append(km)
                price_list.append(price)
            # ou if not km:
            if len(km_list) == 0:
                print("Empty file")
                sys.exit(1)

    except FileNotFoundError:
        print("Error: file not found")
        sys.exit(1)
    except PermissionError:
        print("Error: permission denied")
        sys.exit(1)
    except IsADirectoryError:
        print("Error: expected file, not directory")
        sys.exit(1)
    return km_list, price_list

