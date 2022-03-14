from esame import CSVFile

import unittest
import tempfile
import datetime
from dateutil.relativedelta import relativedelta

score = 0

class TestAndGrade(unittest.TestCase):

    def test_correctness(self):

        with tempfile.NamedTemporaryFile('w+t') as file:
            file.write('Date,Sales\n')
            initial_timestamp = datetime.datetime.strptime("1949-1", '%Y-%m')
            timestamp = None
            values_sum = 0
            for y in range(1, 4): 
                for m in range(1, 13):  # 12 mesi
                    if timestamp is None:
                        timestamp = initial_timestamp
                    else:
                        timestamp + relativedelta(months=1)
                    value= y*m
                    values_sum += value
                    file_line = '{},{}'.format(timestamp.strftime("%Y-%m"), value)
                    file.write(file_line+'\n')
                    # valori del primo anno: 1, 2, 3 ... , 12
                    # valori del secondo anno: 2, 4, 6 ... , 24
                    # valori del terzo anno: 3, 6, 9 ... , 36
                    
                    # Increase timestamp
                    timestamp = timestamp + relativedelta(months=1)
            file.seek(0)

            # Check correct sum
            csv_file = CSVFile(file.name)
            data = csv_file.get_data()

            self.assertEqual(len(data), 36)
            
            self.assertEqual(data[0][0], '1949-01')
            self.assertEqual(str(data[0][1]), '1') # Conversion to numerical is the next lesson

            self.assertEqual(data[-1][0], '1951-12')
            self.assertEqual(str(data[-1][1]), '36') # Conversion to numerical is the next lesson
                             
            global score; score += 6 # Increase score  

    def test_empty_file(self):
        with tempfile.NamedTemporaryFile('w+t') as file:
            
            file.write('Date,Sales\n')
            file.seek(0)
            csv_file = CSVFile(file.name)
            data = csv_file.get_data()
            
            # Check correct sum
            self.assertEqual(data, [])
            global score; score += 2 # Increase score  


    def test_name(self):
        with tempfile.NamedTemporaryFile('w+t') as file:
            
            file.write('Date,Sales\n')
            file.write('1949-01,1\n')
            file.write('1949-03,1\n')
            file.seek(0)
    
            csv_file = CSVFile(name = file.name)
            data = csv_file.get_data()
            self.assertTrue(len(data),2)

            global score; score += 2# Increase score

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
