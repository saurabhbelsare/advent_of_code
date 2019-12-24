import numpy as np

## Function to calculate the total fuel requirement based on the list of module masses. Each module requires floor(mass/3)+2 fuel. This assumes no extra fuel required for the mass of the fuel itself.
def calculate_fuel_requirements1(module_masses_list, int1, int2):
    fuel_list = [np.floor(x/int1)-int2 for x in module_masses_list]
    total_fuel = sum(fuel_list)
    return(total_fuel)


## Function to calculate the total fuel requirement based on the list of module masses. Each module requires floor(mass/3)+2 fuel. This takes into account the extra fuel requirement for the mass of the fuel itself. 
def calculate_fuel_requirements2(module_masses_list, int1, int2):
    cumulative_fuel_list = []
    fuel_list = [np.floor(x/int1)-int2 for x in module_masses_list]
    while(sum(fuel_list) > 0):
        cumulative_fuel_list = cumulative_fuel_list + fuel_list
        fuel_list = [max(np.floor(x/int1)-int2,0) for x in fuel_list]
    total_fuel = sum(cumulative_fuel_list)
    return(total_fuel)


if __name__=="__main__":
    
    module_masses_list = [] # List to hold all the masses of the modules.
    
    ## Read in all the inputs from a file and load them into a list:
    f_read = open("inputfile.txt", "r")
    for line in f_read:
        module_masses_list.append(int(line))

    print(module_masses_list)
#    module_masses_list = [14,1969,100756]
    ## Parameters for calculating the fuel from the mass of the module, given in the problem.
    int1 = 3
    int2 = 2
    
    ## Function call to calculate the total fuel requirement
    total_fuel = calculate_fuel_requirements2(module_masses_list, int1, int2)

    ## Print the total fuel requirement to screen
    print("The total fuel requirement for the spacecraft given by the module_masses_list is:")
    print(total_fuel)

