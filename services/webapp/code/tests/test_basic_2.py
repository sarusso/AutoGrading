from esame import sum_list

import unittest

score = 0

class TestAndGrade(unittest.TestCase):

    def test_correctness(self):
        self.assertEqual(sum_list([1,2,3]), 6)
        global score; score += 6 # Increase score  

    def test_negative_values(self):
        self.assertEqual(sum_list([-1,1]), 0)
        global score; score += 1 # Increase score  

    def test_empty_list(self):
        self.assertEqual(sum_list([]), None)
        global score; score += 1 # Increase score  

    def test_wrong_list_type(self):
        self.assertEqual(sum_list('hello'), None)
        global score; score += 1 # Increase score  

    def test_wrong_list_elements_type(self):
        self.assertEqual(sum_list([1,2,'hello']), None)
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
