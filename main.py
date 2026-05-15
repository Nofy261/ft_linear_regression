import sys
from predict import predict
from train import train_model
from parsing import read_data
from utils import save_thetas, save_minmax, load_minmax, load_thetas
from graph import graph_model
from mae import compute_mae

def run_train(data_file, theta_file, minmax_file):
    km_list, price_list = read_data(data_file)

    theta0, theta1 = train_model(km_list,
    price_list,
    learning_rate=0.1,
    iterations=3000
    )

    #learningRate 0.01 = petit pas et 0.1 = grand pas
    save_thetas(theta_file, theta0, theta1)
    save_minmax(minmax_file, km_list)

    


def run_predict(theta_file, minmax_file):
    theta0, theta1 = load_thetas(theta_file)
    min_km, max_km = load_minmax(minmax_file)

    try:
        km = float(input("Enter mileage: "))
    except ValueError:
        print("Error: bad input")
        return

    price = predict(km, min_km, max_km, theta0, theta1)

    print(f"Estimated price: {price}")



def run_evaluate(data_file, theta_file, minmax_file):
    km_list, price_list = read_data(data_file)
    theta0, theta1 = load_thetas(theta_file)
    min_km, max_km = load_minmax(minmax_file)

    mae = compute_mae(km_list, price_list, theta0, theta1, min_km, max_km)

    print("MAE =", mae)

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Error: invalid argv")
        sys.exit(1)
    
    mode = sys.argv[1]

    theta_file = "theta.txt"
    minmax_file = "minmax.txt"
    data_file = "data.csv"

    if mode == "train":
        run_train(data_file, theta_file, minmax_file)
    
    elif mode == "predict":
        run_predict(theta_file, minmax_file)

    elif mode == "graph":
        graph_model(data_file, theta_file, minmax_file)

    elif mode == "evaluate":
        run_evaluate(data_file, theta_file, minmax_file)


    else:
        print("Error: unknown mode")
        sys.exit(1)
