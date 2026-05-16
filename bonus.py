
#MAE : Mean Absolute Error (Erreur Absolue Moyenne): sur toutes les voitures
# de combien l'erreur se trompe en moyenne
# calcule l’erreur moyenne entre les prix réels et prédits

#def compute_mae(km_list, price_list, theta0, theta1, min_km, max_km):
#   total_error = 0
#    m = len(km_list)

#    for i in range(m):
        #normalisation du km
#        km_norm = (km_list[i] - min_km) / (max_km - min_km)

        #prediction
#        y_pred = theta0 + theta1 * km_norm

        #erreur
#       error = abs(y_pred - price_list[i])

#        total_error += error

#   mean_error = total_error / m
#    return mean_error

from utils import load_minmax, load_thetas
from parsing import read_data
import matplotlib.pyplot as plt

def compute_mae(data_file, theta_file, minmax_file):
    km_list, price_list = read_data(data_file)
    theta0, theta1 = load_thetas(theta_file)
    min_km, max_km = load_minmax(minmax_file)

    total_error = 0
    m = len(km_list)

    for i in range(m):
        #normalisation du km
        km_norm = (km_list[i] - min_km) / (max_km - min_km)

        #prediction
        y_pred = theta0 + theta1 * km_norm

        #erreur
        error = abs(y_pred - price_list[i])
        total_error += error

    mean_error = total_error / m

    mean_price = sum(price_list) / m
    mae_percent = (mean_error / mean_price) * 100

    return mean_error, mae_percent



def compare_prediction(data_file, theta_file, minmax_file):
    km_list, price_list = read_data(data_file)
    theta0, theta1 = load_thetas(theta_file)
    min_km, max_km = load_minmax(minmax_file)

    i = int(input("Choose index of car: "))

    if i < 0 or i >= len(km_list):
        print("Invalid index")
        return
    
    km = km_list[i]
    real_price = price_list[i]

    km_norm = (km - min_km) / (max_km- min_km)
    price_pred = theta0 + theta1 * km_norm
    error = abs(price_pred - real_price)
    error_percent = (error / real_price) * 100

    print(f"Km = {km}")
    print(f"Real price = {real_price}")
    print(f"Predicted price = {price_pred:.1f}")
    print(f"Error = {error:.1f}")
    print(f"Error percent = {error_percent:.2f}%")




#pour le graphe on prend les km reel max et min
#et le y_min et y_max pour le prix predit par le modele creer 

def graph_model(data_file, theta_file, minmax_file):
    km_list, price_list = read_data(data_file)
    theta0, theta1 = load_thetas(theta_file)
    min_km, max_km = load_minmax(minmax_file)

    # afficher les donnees(points) bonus
    plt.scatter(km_list, price_list, color="blue", label="Real data")

    # droite prédite
    km_line = [min_km, max_km]

    price_line = [
        theta0 + theta1 * ((km_line[0] - min_km) / (max_km - min_km)),
        theta0 + theta1 * ((km_line[1] - min_km) / (max_km - min_km))
    ]

    #affiche la droite de regression (bonus)
    plt.plot(km_line, price_line, color="red", label="Regression line")

    plt.xlabel("Mileage (km)", color="red")
    plt.ylabel("Price (€)", color="red")
    plt.title("Linear Regression Model")

    plt.legend()
    plt.grid(True)
    plt.show()