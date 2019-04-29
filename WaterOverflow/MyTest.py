import unittest
import inspect
import WaterOverflow

class Test_MyTest(unittest.TestCase):

    # Requirement: to have a function named calculate_liquid
    def test_function_exists(self):
        self.assertTrue(inspect.isfunction(WaterOverflow.calculate_liquid))

    # Requirement: to have three variables as input to calculate_liquid (i, j, K)
    def test_number_of_input_variables(self):
        sig = inspect.signature(WaterOverflow.calculate_liquid)
        numberOfParameters = len(sig.parameters)
        self.assertTrue(numberOfParameters == 3)

    # Data type validation on parameters: we need to integers (i, j) and a float (K)
    # The order of parameters is conventional, assuming they appear as ints first and the float after
    # Therefore, the expected order of parameters is (int i, int j, float K)
    # There can be an additional test to check if the function returns a float
    def test_types_of_input_variables(self):
        sig = inspect.signature(WaterOverflow.calculate_liquid)
        params = sig.parameters
        if 'i' in params and 'j' in params and 'K' in params:
            doKeysExist = True
            iParam = params.get('i')
            jParam = params.get('j')
            KParam = params.get('K')
            if iParam.annotation is int and jParam.annotation is int and KParam.annotation == float:
                areParamsCorrectType = True
        self.assertTrue(doKeysExist and areParamsCorrectType)

    # Data validation for j: it has to be lesser or equal than i
    # If a user inputs a j larger than i, it should use j = i (expected functionality - can be amended if the requirement is different)
    # There is an error in the glass demonstration diagram in the exercise, for i = 3: j = 0, j = 1, j = 1, j = 2
    # Should read: i = 3: j = 0, j = 1, j = 2, j = 3
    def test_j_lesser_or_equal_than_i(self):
        i = 5;
        j = 6;
        K = 2.0;
        self.assertTrue(j > i)
        
        waterJGreaterThanI = WaterOverflow.calculate_liquid(i, j, K)
        waterJEqualToI = WaterOverflow.calculate_liquid(i, i, K)

        # Initially this test passes if the function returns K
        self.assertTrue(waterJGreaterThanI == waterJEqualToI)

    # The first test for the body: Each glass can hold 250ml
    # The output of the function must not exceed 0.25
    def test_glass_max_volume(self):
        i = 5;
        j = 6;
        K = 2.0;
        water = WaterOverflow.calculate_liquid(i, j, K)
        self.assertLessEqual(0.25, water)

if __name__ == '__main__':
    unittest.main()
