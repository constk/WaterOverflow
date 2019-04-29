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
    def test_types_of_input_variables(self):
        ii = 11;
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

if __name__ == '__main__':
    unittest.main()
