import unittest

#remove after use
import inspect

# Calculates the volume of liquid in glass j of row i 
def calculate_liquid(i: int, j: int, K: float):
    #code for test_j_lesser_or_equal_than_i
    if (j > i):
        j = i
    #code for test_glass_max_volume
    if(K < 0.25):
        return K
    else:
        return 0.25

# The main to use the function
if __name__ == "__main__":
    i = 2;
    j = 2;
    K = 2.0;

    water = repr(calculate_liquid(i, j, K))
    print('Water volume in glass ' + str(j) + ', of row ' + str(i) + ': ' + water)

    l = 0