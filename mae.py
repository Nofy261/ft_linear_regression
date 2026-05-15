

def compute_mae(km_list, price_list, theta0, theta1, min_km, max_km):
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
    return mean_error

