
from esame import FitIncrementModel

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
   
            model = FitIncrementModel()
            model.fit([8,19,31,41])
            self.assertEqual(model.predict([50,52,60]), 68)
   
            global score; score += 6 # Increase score  

    def test_correctness_negative_int(self):
    
            model = FitIncrementModel()
            model.fit([3,6,9,12])
            # 3+(-5) = 2, /2 = 1, 50-1 =49
            self.assertEqual(model.predict([60,55,50]), 49)
    
            global score; score += 1 # Increase score  


    def test_correctness_negative_float(self):
     
            model = FitIncrementModel()
            model.fit([2,4,6,8])

            self.assertEqual(model.predict([60,55,50]), 48.5)
     
            global score; score += 1 # Increase score  
  
    def test_input_value(self):
     
            model = FitIncrementModel()
              
            with self.assertRaises(Exception):
                model.predict([60])
              
            try:
                model.predict([60])
            except ZeroDivisionError:
                self.fail("Predict raised ZeroDivisionError")
            except:
                pass
     
            global score; score += 0.5 # Increase score  
  
    def test_input_type(self):
          
            model = FitIncrementModel()
     
            with self.assertRaises(TypeError):
                model.predict({'1':1})
  
            with self.assertRaises(TypeError):
                model.predict([None, 2, 3])
     
            global score; score += 0.5 # Increase score  
  
  
    def test_base_and_inheritance(self):
        try:
            from esame import IncrementModel
        except ImportError:
            pass
        else:
            self.assertTrue(issubclass(FitIncrementModel, IncrementModel))
            global score; score += 1 # Increase score  


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

