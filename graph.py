import matplotlib.pyplot as plt
from utils import load_thetas, load_minmax
from parsing import read_data


#pour le graphe on prend les km reel max et min
#et le y_min et y_max pour le prix predit par le modele creer 

def graph_model(data_file, theta_file, minmax_file):
    km_list, price_list = read_data(data_file)
    theta0, theta1 = load_thetas(theta_file)
    min_km, max_km = load_minmax(minmax_file)

    # afficher les points (bonus)
    plt.scatter(km_list, price_list, color="blue")

    # droite prédite
    km_line = [min_km, max_km]

    km_line_norm = []
    for x in km_line:
        normalized = (x - min_km) / (max_km - min_km)
        km_line_norm.append(normalized)
    
    price_line = [
        theta0 + theta1 * km_line_norm[0],
        theta0 + theta1 * km_line_norm[1]
    ]

    #affiche la droite(bonus)
    plt.plot(km_line, price_line, color="red")

    plt.xlabel("km", color="red")
    plt.ylabel("price", color="red")
    plt.title("Linear Regression Model")
    plt.show()
   
