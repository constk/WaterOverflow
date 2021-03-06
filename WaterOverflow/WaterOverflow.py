import unittest

# Calculates the volume of liquid in glass j of row i 
# for a liquid volume K in litres
def calculate_liquid(i: int, j: int, K: float):
    #Code for test_i_is_negative and test_j_is_negative
    if(i < 0):
        i = 0;
    if(j < 0):
        j = 0;
    number = 0;
    # Code for test_j_lesser_or_equal_than_i
    if (j > i):
        j = i

    #Code for test_K_is_negative
    if(K < 0.0):
        K = 0.0;

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

            # Adding conditional for test_glass_glass_doesnt_have_liquid
            # Reducing the volume by the volume consumed by the first glass
            if(K >= 0.25):
                K = K - 0.25
            else:
                K = 0.0

            # Code for test_glass_has_half_of_exceeded_above Part 1
            glassVolume[index + row] = (K/2) 
            # Making sure the line above is compliant with test_first_glass_max_volume
            if(glassVolume[index + row] > 0.25):
                glassVolume[index + row] = 0.25

            # Code for test_glass_has_equal_of_glass_next_to_it
            glassVolume[index + row + 1] = (K/2)

            if(glassVolume[index + row + 1] != glassVolume[index + row]):
                glassVolume[index + row + 1] = glassVolume[index + row]

            # Making sure the line above is compliant with test_first_glass_max_volume
            if(glassVolume[index + row + 1] > 0.25):
                glassVolume[index + row + 1] = 0.25
            number = index + row +1
    return float(glassVolume[number])

# The main to use the function
if __name__ == "__main__":

    i = 2;
    j = 1;
    K = 3*0.25 + 0.10;
    water = repr(calculate_liquid(i, j, K))
    
    print('For given volume of liquid K = ' + str(K) + ':\n ')
    print('Counting from 1: \nWater volume in glass ' + str(j + 1) + ', of row ' + str(i + 1) + ': ' + water + '\n')
    print('Counting from 0: \nWater volume in glass ' + str(j) + ', of row ' + str(i) + ': ' + water + '\n')