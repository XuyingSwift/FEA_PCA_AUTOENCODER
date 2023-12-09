from classic_random_grouping import run_random_fea_process
from pca_grouping import run_pca_fea_process
    
# ANSI escape codes for color (e.g., green)
GREEN = "\033[92m"
RESET = "\033[0m"
RED = "\033[91m"

def check_function(function_name, fcn_num, lb, ub, benchmark_functions):
    for func, bounds in benchmark_functions:
        if func == function_name:
            if bounds[0] == lb and bounds[1] == ub:
                return True
    return False

def pca():
    print(RED + f"PCA 50 is processing... ")
    # List of benchmark functions and their domain ranges
    benchmark_functions = [
        ('ackley', (-32, 32)),
        ('dixon_price', (-10, 10)),
        ('griewank', (-100, 100)),
        ('powell_singular', (-4, 5)),
        ('powell_sum',     (-1, 1)),
        ('rana', (-500, 500)),
        ('rastrigin', (-5.12, 5.12)),
        ('rosenbrock', (-2.048, 2.048)),
        ('schwefel', (-512, 512)),
        ('sphere', (-5.12, 5.12))
    ]

    # Base paths
    base_data_path = "/Users/xuyingwangswift/Desktop/FEA_PCA_AUTOENCODER/src/Data/Generated_data_dim50_row50000/"
    base_performance_result_dir = "/Users/xuyingwangswift/Desktop/FEA_PCA_AUTOENCODER/src/Results/PCA_dim50"
    threshold_dir = '/Users/xuyingwangswift/Desktop/FEA_PCA_AUTOENCODER/src/Results/Threshold/'

    # Common parameters
    num_factors = 50
    fea_runs = 50
    generations = 100
    pop_size = 100
    function_name = 'powell_singular'
    fcn_num = 4
    lb = -4
    ub = 5
    # Define file paths
    data_file_path = base_data_path + function_name + ".csv"
    performance_result_file = function_name + '_pca_data_dim_50_gen_50000_result.csv'
    max_threshold_factors_file = function_name + '_dim50_threshold.csv'
    
    # Your print statement with color
    print(f"{GREEN}Running FEA process for {function_name} (Function #{fcn_num}){RESET}")

    match = check_function(function_name, fcn_num, lb, ub, benchmark_functions)

    if (match):
        # Call the FEA process function
        run_pca_fea_process(data_file_path, num_factors, 
                            fea_runs, generations, 
                            pop_size,
                            fcn_num, lb, ub,
                            base_performance_result_dir,
                            performance_result_file,
                            threshold_dir,
                            max_threshold_factors_file)


def random_fea():
    print(RED + f"Random 50 is processing... ")
    benchmark_functions = [
        ('ackley', (-32, 32)),
        ('dixon_price', (-10, 10)),
        ('griewank', (-100, 100)),
        ('powell_singular', (-4, 5)),
        ('powell_sum',     (-1, 1)),
        ('rana', (-500, 500)),
        ('rastrigin', (-5.12, 5.12)),
        ('rosenbrock', (-2.048, 2.048)),
        ('schwefel', (-512, 512)),
        ('sphere', (-5.12, 5.12))
    ]
    # Base paths
    base_performance_result_dir = "/Users/xuyingwangswift/Desktop/FEA_PCA_AUTOENCODER/src/Results/Random_dim50"

    # Common parameters
    dim = 50
    fea_runs = 50
    generations = 100
    pop_size = 100
    
    function_name ='powell_singular'
    fcn_num = 4
    lb = -4
    ub = 5
    # Define file paths
    performance_result_file = function_name + '_random_data_dim_50_gen_50000_result.csv'

    # Your print statement with color
    print(f"{GREEN}Running FEA process for {function_name} (Function #{fcn_num}){RESET}")
        # Call the FEA process function

    match = check_function(function_name, fcn_num, lb, ub, benchmark_functions)
    if (match):
        run_random_fea_process(dim, 
                            fea_runs, generations, 
                            pop_size,
                            fcn_num, lb, ub,
                            base_performance_result_dir,
                            performance_result_file)

def main():
    pca()
    #random_fea()

main()