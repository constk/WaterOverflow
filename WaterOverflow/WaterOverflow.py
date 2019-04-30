import unittest

#remove after use
import inspect

# Calculates the volume of liquid in glass j of row i 
# for a liquid volume K in litres
def calculate_liquid(i: int, j: int, K: float):
    #code for test_j_lesser_or_equal_than_i
    if (j > i):
        j = i

    # i and j are zero based, so the total number of glasses will be:
    glassesTotal = (i+1)*(i+2)/2
    # Initialising a list for all glasses:
    glassVolume = [0]*int(glassesTotal);

    # I need to fill the first glass for test_first_glass_max_volume
    index = 0;
    if(K > 0.25):
        glassVolume[index] = 0.25
    # The else is added for test_first_glass_volume_smaller_than_capacity
    else:
        glassVolume[index] = K
    
    # Adding the loop to return the correct index for glasses other than the first one:
    # I will start filling the rest of the glasses in a double for
    # i and j are zero based, so is the glassVolume list.
    # The first glass is already filled.
    # I scan for each row (i) and the j will be from 0, up to i
    for row in range(0, i):
        for column in range(0, row + 1):
            # Going to the second glass since the first one is filled
            index += 1

            # Code for test_any_glass_has_some_liquid
            if(glassVolume[index] < K):
                glassVolume[index] = K
            # Making sure the code above is compliant with test_first_glass_max_volume
            if(glassVolume[index] > 0.25):
                glassVolume[index] = 0.25

    return float(glassVolume[index])

# The main to use the function
if __name__ == "__main__":
    #i = 2;
    #j = 2;
    #K = 2.0;


    i = 3;
    j = 3;
    K = 1000;
    water = repr(calculate_liquid(i, j, K))
    print('Counting from 1: \nWater volume in glass ' + str(j + 1) + ', of row ' + str(i + 1) + ': ' + water + '\n')
    print('Counting from 0: \nWater volume in glass ' + str(j) + ', of row ' + str(i) + ': ' + water + '\n')

    l = 0