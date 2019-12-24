### Day2: 1202 Program Alarm

import numpy as np

def run_opcode(opcode_array):
    counter=0
    indicatorInt=opcode_array[counter]
    while(indicatorInt != 99):
        if (indicatorInt == 1):
            int1=opcode_array[counter+1]
            int2=opcode_array[counter+2]
            int3=opcode_array[counter+3]
            opcode_array[int3] = opcode_array[int1] + opcode_array[int2]
        elif (indicatorInt == 2):
            int1=opcode_array[counter+1]
            int2=opcode_array[counter+2]
            int3=opcode_array[counter+3]
            opcode_array[int3] = opcode_array[int1] * opcode_array[int2]
        elif (indicatorInt == 99):
            break
        else:
            return(-1)
        counter=counter + 4
        indicatorInt=opcode_array[counter]

    return opcode_array
    


if __name__=="__main__":

    f_read = open("inputfile.txt", "r")
    for line in f_read:
        opcode_array_str = line.split(",")

    opcode_array = [int(i) for i in opcode_array_str]

    ### Performing manual modification as required in the problem statement:
    opcode_array[1] = 12
    opcode_array[2] = 2

#    opcode_array=[1,9,10,3,2,3,11,0,99,30,40,50]
    opcode_array2=run_opcode(opcode_array)
    print("The final opcode output array is:")
    print(opcode_array2)

    print("Value at position 0 in the final opcode output array is:")
    print(opcode_array2[0])

    ##### Part 2: Determining the pair of manual modification input values that will get the output to 19690720

    opcode_array=[]
    f_read = open("inputfile.txt", "r")
    for line in f_read:
        opcode_array_str = line.split(",")

    opcode_array = [int(i) for i in opcode_array_str]
    opcode_array_bak = opcode_array
    print(opcode_array_bak)

    output_value=0
    for i in range(1,99):
        for j in range(1,99):
            opcode_array = opcode_array_bak
            opcode_array[1]=i
            opcode_array[2]=j
            opcode_array2=run_opcode(opcode_array)
            print(opcode_array2)
            if (opcode_array2[0] == 19690720):
                output_value = 100*i + j

    print("The final output value to get the desired program output is:")
    print(output_value)


## This is a test for committing
