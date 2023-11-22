
from esame import IncrementModel, FitIncrementModel

import sys
import unittest
import tempfile
import datetime
from dateutil.relativedelta import relativedelta

score = 0

class TestAndGrade(unittest.TestCase):

    def setUp(self):
        if not sys.warnoptions:
            import warnings
            warnings.simplefilter("ignore")

    def test_correctness_increment_model(self):

            increment_model = IncrementModel(3)
            self.assertEqual(increment_model.evaluate([51,52,53,54,57]), 1)
                
            global score; score += 5 # Increase score  
 

    def test_correctness_fit_increment_model(self):

            fit_increment_model = FitIncrementModel(3)
            fit_increment_model.fit([8,19,31,41])
            
            self.assertEqual(fit_increment_model.evaluate([51,52,53,54,55]), 5)
                
            global score; score += 5 # Increase score  
 


    # Print the score
    @classmethod
    def tearDownClass(cls):
        global score
        print('\n\n--------------')
        print('| Score: {}  |'.format(score))
        print('--------------\n')


# Run the tests
if __name__ == "__main__":
    unittest.main()

