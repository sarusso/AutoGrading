
from esame import NumericalCSVFile

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
                    #If last year, add 0.1 to values
                    if y == 3:
                        value+=0.1
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
            csv_file = NumericalCSVFile(file.name)
            data = csv_file.get_data()

            self.assertEqual(len(data), 36)
            
            self.assertEqual(data[0][0], '1949-01')
            self.assertEqual(data[0][1], 1.0) # Conversion to numerical

            self.assertEqual(data[-1][0], '1951-12')
            self.assertEqual(data[-1][1], 36.1) # Conversion to numerical
                             
            global score; score += 6 # Increase score  

    def test_empty_file(self):
        with tempfile.NamedTemporaryFile('w+t') as file:
            
            file.write('Date,Sales\n')
            file.seek(0)
            csv_file = NumericalCSVFile(file.name)
            data = csv_file.get_data()
            
            # Check correct data
            self.assertEqual(data, [])
            global score; score += 0.5 # Increase score  


    def test_name(self):
        with tempfile.NamedTemporaryFile('w+t') as file:
            
            file.write('Date,Sales\n')
            file.write('1949-01,1\n')
            file.write('1949-03,1\n')
            file.seek(0)
    
            csv_file = NumericalCSVFile(name = file.name)
            data = csv_file.get_data()
            self.assertTrue(len(data),2)

            global score; score += 0.5 # Increase score


    def test_dirty_file(self):

        with tempfile.NamedTemporaryFile('w+t') as file:
            
            file.write('Date,Sales\n')
            file.write('1949-01,1\n')
            file.write('1949-02,1\n')
            file.write('1949-03,\n')
            file.write('1949-04,ciao\n')
            file.seek(0)
              
            out = os_shell('python3 -c "from esame import NumericalCSVFile; NumericalCSVFile(\'{}\').get_data()"'.format(file.name), capture=True)

            ## Check error message
            error_count=0
            for line in out.stdout.split('\n'):
                if 'Errore' in line:
                    error_count+=1 
            self.assertEqual(error_count,2)
            global score; score += 2 # Increase score  


    def test_three_columns(self):

        with tempfile.NamedTemporaryFile('w+t') as file:
            
            file.write('Date,Sales\n')
            file.write('1949-01,1,2\n')
            file.write('1949-02,1,4\n')
            file.seek(0)

            # Check correct data
            csv_file = NumericalCSVFile(file.name)
            data = csv_file.get_data()
                          
            self.assertEqual(data[0][0], '1949-01')
            self.assertEqual(data[0][1], 1.0) # Conversion to numerical
            self.assertEqual(data[0][2], 2.0) # Conversion to numerical

            self.assertEqual(data[-1][0], '1949-02')
            self.assertEqual(data[-1][1], 1.0) # Conversion to numerical
            self.assertEqual(data[-1][2], 4.0) # Conversion to numerical

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

#===================================
#  OS shell utility
#===================================

import subprocess
from collections import namedtuple

def sanitize_shell_encoding(text):
    return text.encode("utf-8", errors="ignore").decode("utf-8")


def format_shell_error(stdout, stderr, exit_code):
    
    string  = '\n#---------------------------------'
    string += '\n# Shell exited with exit code {}'.format(exit_code)
    string += '\n#---------------------------------\n'
    string += '\nStandard output: "'
    string += sanitize_shell_encoding(stdout)
    string += '"\n\nStandard error: "'
    string += sanitize_shell_encoding(stderr) +'"\n\n'
    string += '#---------------------------------\n'
    string += '# End Shell output\n'
    string += '#---------------------------------\n'

    return string


def os_shell(command, capture=False, verbose=False, interactive=False, silent=False):
    '''Execute a command in the OS shell. By default prints everything. If the capture switch is set,
    then it returns a namedtuple with stdout, stderr, and exit code.'''
    
    if capture and verbose:
        raise Exception('You cannot ask at the same time for capture and verbose, sorry')

    # Log command
    #logger.debug('Shell executing command: "%s"', command)

    # Execute command in interactive mode    
    if verbose or interactive:
        exit_code = subprocess.call(command, shell=True)
        if exit_code == 0:
            return True
        else:
            return False

    # Execute command getting stdout and stderr
    # http://www.saltycrane.com/blog/2008/09/how-get-stdout-and-stderr-using-python-subprocess-module/
    
    process          = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (stdout, stderr) = process.communicate()
    exit_code        = process.wait()

    # Convert to str (Python 3)
    stdout = stdout.decode(encoding='UTF-8')
    stderr = stderr.decode(encoding='UTF-8')

    # Formatting..
    stdout = stdout[:-1] if (stdout and stdout[-1] == '\n') else stdout
    stderr = stderr[:-1] if (stderr and stderr[-1] == '\n') else stderr

    # Output namedtuple
    Output = namedtuple('Output', 'stdout stderr exit_code')

    if exit_code != 0:
        if capture:
            return Output(stdout, stderr, exit_code)
        else:
            print(format_shell_error(stdout, stderr, exit_code))      
            return False    
    else:
        if capture:
            return Output(stdout, stderr, exit_code)
        elif not silent:
            # Just print stdout and stderr cleanly
            print(stdout)
            print(stderr)
            return True
        else:
            return True

