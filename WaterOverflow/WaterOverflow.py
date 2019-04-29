import unittest

#remove after use
import inspect

# Calculates the volume of liquid in glass j of row i 
def calculate_liquid(i: int, j: float, K: float):
    return K

# The main to use the function
if __name__ == "__main__":
    i = 2;
    j = 2;
    K = 2.0;

    water = repr(calculate_liquid(i, j, K))
    print('Water volume in glass ' + str(j) + ', of row ' + str(i) + ': ' + water)

    l = 0