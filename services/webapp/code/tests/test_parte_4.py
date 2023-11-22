try:
    from esame import CSVFile4 as CSVFile
except ImportError:
    from esame import CSVFile

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

            # Check correct data
            csv_file = CSVFile(file.name)
            data = csv_file.get_data()

            self.assertEqual(len(data), 36)
            
            self.assertEqual(data[0][0], '1949-01')
            self.assertEqual(data[0][1].strip(), '1')

            self.assertEqual(data[-1][0], '1951-12')
            self.assertEqual(data[-1][1].strip(), '36')
                             
            global score; score += 6 # Increase score  

    def test_empty_file(self):
        with tempfile.NamedTemporaryFile('w+t') as file:
            
            file.write('Date,Sales\n')
            file.seek(0)
            csv_file = CSVFile(file.name)
            data = csv_file.get_data()
            
            # Check correct sum
            self.assertEqual(data, [])
            global score; score += 1 # Increase score  

    def test_name(self):
        with tempfile.NamedTemporaryFile('w+t') as file:
            
            file.write('Date,Sales\n')
            file.write('1949-01,1\n')
            file.write('1949-02,1\n')
            file.seek(0)
            csv_file = CSVFile(file.name)
            self.assertEqual(csv_file.name, file.name)

            global score; score += 2# Increase score

    def test_no_newline_chars(self):
        with tempfile.NamedTemporaryFile('w+t') as file:
            
            file.write('Date,Sales\n')
            file.write('1949-01,1\n')
            file.write('1949-02,2\n')
            file.seek(0)
    
            csv_file = CSVFile(file.name)
            data = csv_file.get_data()            
            self.assertEqual(data[0][1], '1', 'Expected value "1", got "{}": Maybe check cleaning the newline character?'.format(data[0][1].replace('\n', '\\n')))
            
            global score; score += 1# Increase score

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
