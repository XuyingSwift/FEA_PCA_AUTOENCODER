import numpy as np
import matplotlib.pyplot as plt
import csv

import os

def write_results(csv_file_name, combined_data):
    # Open the CSV file for writing
    with open(csv_file_name, 'w', newline='') as csv_file:
        # Create a CSV writer object
        csv_writer = csv.writer(csv_file)
        
        # Write the header row (optional)
        csv_writer.writerow(["Column1", "Column2", "Column3"])
        
        # Write the data from the combined_data list
        csv_writer.writerows(combined_data)

    print(f"Data has been written to {csv_file_name}")

def process_files_in_directory(directory):
    results = []

    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            file_path = os.path.join(directory, filename)
            performance_list = get_performance_list(file_path)
            best_performance = get_best_performance(performance_list)
            results.append(best_performance)

    return results

def get_performance_list(file_name):

    global_best_fitnesses = []

    # Open the CSV file for reading
    with open(file_name, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header

        for row in csv_reader:
            global_best_fitnesses.append(float(row[1]))
    return global_best_fitnesses

def get_best_performance(best_list):
    smallest_item = min(best_list)
    return smallest_item

def draw(data_points):
    plt.plot(data_points, marker='o', linestyle='-', color='blue')

    # Adding title and labels
    plt.title('Line Plot Example')
    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')

    # Displaying the plot
    plt.show()

def main():
    best_pca = "/Users/xuyingwangswift/Desktop/FEA_PCA_AUTOENCODER/src/Results/Bests/pca"
    pca_10 = process_files_in_directory("/Users/xuyingwangswift/Desktop/FEA_PCA_AUTOENCODER/src/Results/PCA_dim10")
    pca_30 = process_files_in_directory("/Users/xuyingwangswift/Desktop/FEA_PCA_AUTOENCODER/src/Results/PCA_dim30")
    pca_50 = process_files_in_directory("/Users/xuyingwangswift/Desktop/FEA_PCA_AUTOENCODER/src/Results/PCA_dim50")
    pca_combined = list(zip(pca_10, pca_30, pca_50))
    write_results(best_pca, pca_combined)

    best_ran = "/Users/xuyingwangswift/Desktop/FEA_PCA_AUTOENCODER/src/Results/Bests/ran"
    ran_10 = process_files_in_directory("/Users/xuyingwangswift/Desktop/FEA_PCA_AUTOENCODER/src/Results/Random_dim10")
    ran_30 = process_files_in_directory("/Users/xuyingwangswift/Desktop/FEA_PCA_AUTOENCODER/src/Results/Random_dim30")
    ran_50 = process_files_in_directory("/Users/xuyingwangswift/Desktop/FEA_PCA_AUTOENCODER/src/Results/Random_dim50")
    ran_combined = list(zip(ran_10, ran_30, ran_50))
    write_results (best_ran, ran_combined)

main()

