
try:
    from esame import TrendModel
except ImportError:
    try:
        from esame import IncrementModel as TrendModel
        print('Deprecation warning: using old modle name "IncrementModel", please move to "TrendModel"')
    except ImportError:
        raise ImportError('Cannot find a class named TrendModel (nor IncrementModel)')

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

    def test_correctness(self):
   
            model = TrendModel()
            self.assertEqual(model.predict([50,52,60]), 65)
   
            global score; score += 7 # Increase score  

    def test_correctness_negative(self):
   
            model = TrendModel()
            self.assertEqual(model.predict([60,55,50]), 45)
   
            global score; score += 1 # Increase score  


    def test_input_value(self):
   
            model = TrendModel()
            
            with self.assertRaises(Exception):
                model.predict([60])
            
            try:
                model.predict([60])
            except ZeroDivisionError:
                self.fail("Predict raised ZeroDivisionError")
            except:
                pass
   
            global score; score += 1 # Increase score  

    def test_input_type(self):
        
            model = TrendModel()
   
            with self.assertRaises(TypeError):
                model.predict({'1':1})

            with self.assertRaises(TypeError):
                model.predict([None, 2, 3])
   
            global score; score += 1 # Increase score  


    #def test_base_and_inheritance(self):
    #    try:
    #        from esame import Model
    #    except ImportError:
    #        pass
    #    else:
    #        self.assertTrue(issubclass(TrendModel, Model))
    #        global score; score += 1 # Increase score  

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

