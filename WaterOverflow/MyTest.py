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
        i = 2;
        j = 3;
        K = 2.0;
        self.assertTrue(j > i)
        
        waterJGreaterThanI = WaterOverflow.calculate_liquid(i, j, K)
        waterJEqualToI = WaterOverflow.calculate_liquid(i, i, K)

        # Initially this test passes if the function returns K
        self.assertTrue(waterJGreaterThanI == waterJEqualToI)

    # The first test for the body: Each glass can hold 250ml
    # Assuming that K is given in litres (mentioned in function documentation)
    # The first glass must have 0.25l for K>= 0.25l
    def test_first_glass_max_volume(self):
        i = 0;
        j = 0;
        K = 100.0;

        water = WaterOverflow.calculate_liquid(i, j, K)
        self.assertEqual(water, 0.25)

    # Expanding on the previous test: Each glass can hold 250ml
    # Assuming that K is given in litres (mentioned in function documentation)
    # The output of the function must not exceed 0.25
    def test_any_glass_max_volume(self):
        i = 3;
        j = 3;
        K = 100.0;

        # The test passes for the first glass, so, I add the while loops to scan all values
        # This will enable me to add the loop for all glasses in the body
        for row in range(0, i):
            for column in range(0, j):
                water = WaterOverflow.calculate_liquid(i, j, K)
                self.assertLessEqual(water, 0.25)


    # Making sure I can access all glasses will verify I have the correct iterators 
    # in the for loops in the body. 
    # This test checks if all glasses give results
    def test_any_glass_has_some_liquid(self):
        i = 3;
        j = 3;
        K = 100.0;
        index = 1;

        # The test passes for the first glass, so, I add the while loops to scan all values
        # This will enable me to add the loop for all glasses in the body
        for row in range(0, i):
            for column in range(0, row + 1):
                water = WaterOverflow.calculate_liquid(i, j, K)
                self.assertIsNotNone(water)
                self.assertNotEqual(water, 0.0)
                index +=1
        self.assertTrue(index + row + 1 == 10)

    # Making sure I can access all glasses will verify I have the correct iterators 
    # in the for loops in the body. 
    # This test checks if all glasses give results
    # The output of the function must not exceed 0.25
    # This test demonstrates a limitation in the memory usage where i = j = 100000 cannot instantiate the glassVolume = [0]*int(glassesTotal);
    # Similarly, i = j = 10000 or i = j = 1000 takes a significant time to run
    def test_any_glass_has_some_liquid_100(self):
        i = 100;
        j = 100;
        K = 250.0*i;
        index = 1;

        # The test passes for the first glass, so, I add the while loops to scan all values
        # This will enable me to add the loop for all glasses in the body
        for row in range(0, i):
            for column in range(0, row + 1):
                water = WaterOverflow.calculate_liquid(i, j, K)
                self.assertIsNotNone(water)
                index +=1
        self.assertTrue(index + row + 1 == (i+1)*(i+2)/2)

    # Each glass can hold up to 250ml
    # Assuming that K is given in litres (mentioned in function documentation)
    # The first glass must have K for K < 0.25l
    def test_first_glass_volume_smaller_than_capacity(self):
        i = 0;
        j = 0;
        K = 0.15;

        water = WaterOverflow.calculate_liquid(i, j, K)
        self.assertEqual(water, 0.15)

    # Each glass above must be full before we have liquid in the glasses below
    # i = 2 has j = 0 to 2, and this is total 6 glasses 
    # 6 glasses amount to 1.5l
    def test_glass_above_is_full(self):
        i = 2;
        #j is defined as zero and it will take values up to i in the while loop
        j = 2;
        K = 1.5;
        #while j <= i:
        water = WaterOverflow.calculate_liquid(i, j, K)
        waterAbove = WaterOverflow.calculate_liquid(i-1, j, K)
        self.assertTrue(waterAbove >= water)
        #    j += 1

    # Each glass starting from the first, must have some liquid if K > (numberOfGlasses)*250.0
    # i = 2 has j = 0 ... 2 and this is total 6 glasses 
    # 6 glasses amount to 1.5l
    # The test will check if given an adequate amount of liquid, the glasses are all full
    # This test passes, but I am keeping it as it may fail further in development
    def test_glass_has_liquid(self):
        i = 2;
        #j is defined as zero and it will take values up to i in the while loop
        j = 2;
        K = 1.5;
        water = WaterOverflow.calculate_liquid(i, j, K)
        self.assertTrue(water > 0.0)

    # Each glass starting from the first, must have some liquid if K > (numberOfGlasses)*250.0
    # i = 2 has j = 0 ... 2 and this is total 6 glasses 
    # 6 glasses amount to 1.5l
    # The test will check for empty glasses if there is not enought liquid for all
    def test_glass_doesnt_have_liquid(self):
        i = 2;
        #j is defined as zero and it will take values up to i in the while loop
        j = 2;
        K = 0.25;
        water = WaterOverflow.calculate_liquid(i, j, K)
        self.assertTrue(water == 0.0)

    # Each glass below a full glass must have 1/2 of the liquid that exceeded 250ml in the full glass above
    # i = 0 and K = 0.35l, I expect glasses i = 1, j = 0 and i = 1, j = 1 to have
    # 50ml each = 0.05l
    def test_glass_has_half_of_exceeded_above(self):

        K = 0.35;
        water00 = WaterOverflow.calculate_liquid(0, 0, K)
        water10 = WaterOverflow.calculate_liquid(1, 0, K)
        water11 = WaterOverflow.calculate_liquid(1, 1, K)

        self.assertTrue(water10 == water11)
        self.assertAlmostEqual(water10, (K - 0.25) / 2 )



if __name__ == '__main__':
    unittest.main()  
