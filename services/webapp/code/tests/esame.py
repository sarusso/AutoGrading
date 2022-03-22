
# Lezione 1
import os
if os.environ.get('L1', False):
    print('Hello world!')

# Lezione 2
def sum_list(the_list):
    if not the_list:
        return None
    else:
        total = 0
        for element in the_list:
            total+=element
        return total

# Lezione 3
def sum_csv(the_file):
    if not the_file:
        return None
    else:
        # Inizializzo una lista vuota per salvare i valori
        values = []
        
        # Apro e leggo il file, linea per linea
        my_file = open(the_file, 'r')
        for line in my_file:
        
            # Faccio lo split di ogni riga sulla virgola
            elements = line.split(',')
        
            # Se NON sto processando l'intestazione... 
            if elements[0] != 'Date':
        
                # Setto la data e il valore
                date  = elements[0]
                value = elements[1]
        
                # Aggiungo alla lista dei valori questo valore (se riesco a convertirlo a float)
                try: 
                    values.append(float(value))
                except:
                    pass
        my_file.close()
                
        return sum_list(values)


# Lezione 4
class CSVFile4:

    def __init__(self, name):
        
        # Setto il nome del file
        self.name = name
        

    def get_data(self):
        
        # Inizializzo una lista vuota per salvare tutti i dati
        data = []

        # Apro il file
        my_file = open(self.name, 'r')

        # Leggo il file linea per linea
        for line in my_file:
            
            # Faccio lo split di ogni linea sulla virgola
            elements = line.split(',')
            
            # Posso anche pulire il carattere di newline 
            # dall'ultimo elemento con la funzione strip():
            elements[-1] = elements[-1].strip()
            
            # p.s. in realta' strip() toglie anche gli spazi
            # bianchi all'inizio e alla fine di una stringa.

            # Se NON sto processando l'intestazione...
            if elements[0] != 'Date':
                    
                # Aggiungo alla lista gli elementi di questa linea
                data.append(elements)
        
        # Chiudo il file
        my_file.close()
        
        # Quando ho processato tutte le righe, ritorno i dati
        return data


# Lezione 5a
# Questo deve chiamarsi cosi' perche' viene importato via python -c
# e risulta quindi difficile fare try-execpe con CSVFile5

class CSVFile:

    def __init__(self, name):
        
        # Setto il nome del file
        self.name = name
        
        # Provo ad aprirlo e leggere una riga
        self.can_read = True
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except Exception as e:
            self.can_read = False
            print('Errore in apertura del file: "{}"'.format(e))


    def get_data(self):
        
        if not self.can_read:
            
            # Se nell'init ho settato can_read a False vuol dire che
            # il file non poteva essere aperto o era illeggibile
            print('Errore, file non aperto o illeggibile')
            
            # Esco dalla funzione tornando "niente".
            return None

        else:
            # Inizializzo una lista vuota per salvare tutti i dati
            data = []
    
            # Apro il file
            my_file = open(self.name, 'r')

            # Leggo il file linea per linea
            for line in my_file:
                
                # Faccio lo split di ogni linea sulla virgola
                elements = line.split(',')
                
                # Posso anche pulire il carattere di newline 
                # dall'ultimo elemento con la funzione strip():
                elements[-1] = elements[-1].strip()
                
                # p.s. in realta' strip() toglie anche gli spazi
                # bianchi all'inizio e alla fine di una stringa.
    
                # Se NON sto processando l'intestazione...
                if elements[0] != 'Date':
                        
                    # Aggiungo alla lista gli elementi di questa linea
                    data.append(elements)
            
            # Chiudo il file
            my_file.close()
            
            # Quando ho processato tutte le righe, ritorno i dati
            return data



# Lezione 5b
class NumericalCSVFile(CSVFile):
    
    def get_data(self):
        numerical_data = []
        string_data = super().get_data()
        
        for i, line in enumerate(string_data):
            line_as_numerical = []
            try:
                for j, item in enumerate(line):
                    if j == 0:
                        line_as_numerical.append(item)
                    else:
                        line_as_numerical.append(float(item))
                numerical_data.append(line_as_numerical)
            except:
                print('Errore, impossibile convertire il valore "{}" della linea {} a numerico (float)'.format(item,i))
        return numerical_data


# Lezione 6
class CSVFile6:

    def __init__(self, name):
        
        if not isinstance(name,str):
            raise TypeError('Nome del file non stringa')
        
        # Setto il nome del file
        self.name = name
        
        # Provo ad aprirlo e leggere una riga
        self.can_read = True
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except Exception as e:
            self.can_read = False
            print('Errore in apertura del file: "{}"'.format(e))


    def get_data(self, start=None, end=None):

        # Check start/end        
        if start is not None:
            try:
                start = int(start)
            except:
                raise TypeError('Start non interpretabile come intero ("{}")'.format(start))
            if start <= 0:
                raise ValueError('Start minore o uguale a zero ("{}")'.format(start))
        if end is not None:
            try:
                end = int(end)
            except:
                raise TypeError('Start non interpretabile come intero ("{}")'.format(end))
            if end <= 0:
                raise ValueError('End minore o uguale a zero ("{}")'.format(end))

        if start is not None and end is not None and start > end:
            raise ValueError('Start maggiore di end! start="{}", end="{}"'.format(start,end))         
        
        if not self.can_read:
            
            # Se nell'init ho settato can_read a False vuol dire che
            # il file non poteva essere aperto o era illeggibile
            print('Errore, file non aperto o illeggibile')
            
            # Esco dalla funzione tornando "niente".
            return None

        else:
            # Inizializzo una lista vuota per salvare tutti i dati
            data = []
    
            # Apro il file
            my_file = open(self.name, 'r')

            # Leggo il file linea per linea
            for i, line in enumerate(my_file):
                
                # Faccio lo split di ogni linea sulla virgola
                elements = line.split(',')
                
                # Posso anche pulire il carattere di newline 
                # dall'ultimo elemento con la funzione strip():
                elements[-1] = elements[-1].strip()
                
                # p.s. in realta' strip() toglie anche gli spazi
                # bianchi all'inizio e alla fine di una stringa.
    
                # Se NON sto processando l'intestazione...
                if elements[0] != 'Date':
                    
                    # Aggiungo alla lista gli elementi di questa linea se devo
                    if start is not None and end is None:
                        if i+1 >= start:
                            data.append(elements)
                    elif end is not None and start is None:
                        if i+1 <= end:
                            data.append(elements)
                    elif start is not None and end is not None:
                        if i+1 >= start and i+1 <= end:
                            data.append(elements)  
                    else:
                        data.append(elements)

            if start is not None and start > i:
                raise ValueError('Start maggiore del totale delle righe del file (end="{}", righe="{}"'.format(start, i))
            
            if end is not None and end > i:
                raise ValueError('End maggiore del totale delle righe del file (end="{}", righe="{}"'.format(end, i))

            # Chiudo il file
            my_file.close()
            
            # Quando ho processato tutte le righe, ritorno i dati
            return data



#==============================
#  Classe per file CSV
#==============================

import csv
from unittest import result
try:
    import numpy as np
except:
    pass

class ExamException(Exception):
    pass

class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name = name
        # Provo ad aprirlo e leggere una riga
        self.can_read = True
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except Exception as e:
            self.can_read = False


    def get_data(self):
        if not self.can_read:
            # Se nell'init ho settato can_read a False vuol dire che
            # il file non poteva essere aperto o era illeggibile
            raise(ExamException(Exception))
        else:
            data, dates = list(), list()
            my_file = open(self.name, 'r')
            ordered, duplicate, last = True, False, False
            
            for line in my_file:
                elements = line.split(',')
                elements[-1] = elements[-1].strip()
                if elements[0] != 'date':
                    try:
                        # check if the number of passengers is valid or skip the line
                        elements[1] = int(elements[1])
                        # chech if the input number of passengers is negative
                        if int(elements[1]) < 0:
                            continue
                    except:
                        continue

                    # check if the date has valid inputs
                    try:
                        # if there are not two elements in date, dash-separated, skip the line
                        if len(elements[0].split("-")) != 2:
                            continue
                        int(elements[0].split("-")[0])
                        int(elements[0].split("-")[1])
                    except:
                        continue
                    
                    ordered = self.check_date_order(elements[0], last)
                    duplicate = self.check_date_dup(elements[0], dates)
                    if not ordered:
                        raise ExamException("Date not ordered")
                    if duplicate:
                        raise ExamException("Date duplicated")
                    last = elements[0]
                    dates.append(elements[0])
                    data.append(elements[:2])

            my_file.close()
            return data

    def check_date_order(self, date, last):
        # check if the dates are ordered
        if not last:
            return True
        year, month = int(date.split("-")[0]), int(date.split("-")[1])
        last_year, last_month = int(last.split("-")[0]), int(last.split("-")[1])

        if year < last_year:  # if current year smaller than previous
            return False
        if month < last_month:  # if current month and year smaller than previous
            if year == last_year:
                return False
            return True
        
        if month == last_month:
            if year == last_year:
                return False
            return True
        return True

    def check_date_dup(self, date, dates):
        if date not in dates:
            return False
        return True


def to_list_of_years(subset, first_year=None, last_year=None):
    if first_year is None:
        first_year = subset[0][0].split("-")[0]
    if last_year is None:
        last_year = subset[-1][0].split("-")[0]
    years = []
    for y in range(int(first_year), int(last_year)+1):  # for each year in the interval
        pas = [0 for _ in range(12)]  # will store the num of passenger per month
        for i in subset:  # for each row in the file
            year = int(i[0].split("-")[0])
            month = int(i[0].split("-")[1])
            if year == y:
                pas[month-1] = i[1]
        years.append(pas)
    return years


def compute_avg_monthly_difference(time_series, first_year, last_year):
    try:
        int(last_year)
        int(first_year)
        if int(last_year) < int(first_year):
            raise ExamException("Last year smaller than first year")
    except:
        raise ExamException("Input non valido")

    first_idx = False
    last_idx = False
    for idx, data in enumerate(time_series):
        if data[0].split("-")[0] == first_year and first_idx is False:
            first_idx = idx  # index of the ts for the first year in the interval
        if data[0].split("-")[0] == last_year:
            last_idx = idx  # index of the ts for the last year in the interval

    # consider only the years in the interval
    subset = time_series[first_idx:last_idx+1]
    years = to_list_of_years(subset, first_year, last_year)

    diff = [0 for _ in range(12)]
    for m in range(12):
        d, n = 0, 0
        prev = years[0][m]
        for y in range(1, len(years)):
            if years[y][m] != 0 and prev != 0:
                d += years[y][m] - prev
                n += 1
            prev = years[y][m]
        if n != 0:
            diff[m] = int(d / n)

    return diff


def detect_similar_monthly_variations(time_series, years):
    
    try:
        first_year = str(int(years[0]) + 1)
    except:
        raise ExamException("Year not valid")

    try:
        last_year = str(int(years[1]) + 1)
    except:
        raise ExamException("Year not valid")

    list_years = []
    for i in time_series:
        list_years.append(i[0].split("-")[0])


    if first_year not in list_years:
        raise ExamException("Year not in the data")

    if last_year not in list_years:
        raise ExamException("Year not in the data")


    years = to_list_of_years(time_series, first_year, last_year)

    year_diff = [[0 for _ in range(11)] for _ in range(2)]
    for y in range(2):
        for m in range(0, 11):
            if years[y][m] != 0 and years[y][m+1] != 0:
                year_diff[y][m] = years[y][m+1] - years[y][m]
            else:
                year_diff[y][m] = False
    
    results = [False for _ in range(11)]
    for d in range(11):
        if year_diff[0][d] != False:
            if abs(year_diff[0][d] - year_diff[1][d]) <= 2:
                results[d] = True

    return results


def detect_increment(time_series, first_year, last_year):
    try:
        int(last_year)
        int(first_year)
        if int(last_year) < int(first_year):
            raise ExamException("Last year smaller than first year")
    except:
        raise ExamException("Input non valido")

    first_idx = False
    last_idx = False
    for idx, data in enumerate(time_series):
        if data[0].split("-")[0] == first_year and first_idx is False:
            first_idx = idx
        if data[0].split("-")[0] == last_year:
            last_idx = idx
    
    list_years = []
    for i in time_series:
        if int(i[0].split("-")[0]) >= int(first_year) and int(i[0].split("-")[0]) <= int(last_year) \
            and i[0].split("-")[0] not in list_years:
            list_years.append(i[0].split("-")[0])

    subset = time_series[first_idx:last_idx+1]
    years = to_list_of_years(subset, first_year, last_year)
    m = [0 for _ in range(len(years))]
    for idx, y in enumerate(years):
        y_nozero = [i for i in y if i > 0]
        if len(y_nozero) != 0:
            m[idx] = np.mean(y_nozero)
    
    results = []
    for i, year in enumerate(list_years):
        if i == 0:
            continue
        if m[i] > m[i-1]:
            results.append([year, m[i]-m[i-1]])
    return results


def detect_same_min_max(time_series):
    months = ["Gennaio", "Febbraio", "Marzo", "Aprile", \
        "Maggio", "Giugno", "Luglio", "Agosto", "Settembre", \
        "Ottobre", "Novembre", "Dicembre"]
    years = to_list_of_years(time_series)

    first_year = time_series[0][0].split("-")[0]
    last_year = time_series[-1][0].split("-")[0]
    list_years = [str(i) for i in range(int(first_year), int(last_year)+1)]
    
    mesi = []
    for idx, y in enumerate(years):
        if min_no_zero(y) > 0 and max(y) > 0 and min_no_zero(y) != max(y):
            min_idx = [i for i, v in enumerate(y) if v == min_no_zero(y)]
            max_idx = [i for i, v in enumerate(y) if v == max(y)]
            mesi.append([list_years[idx], [months[i] for i in min_idx],  [months[i] for i in max_idx]])

    results = []
    for idx in range(1, len(mesi)):
        minim = mesi[idx][1]
        maxim = mesi[idx][2]

        minim_last = mesi[idx-1][1]
        maxim_last = mesi[idx-1][2]

        if len(list(set(minim) & set(minim_last)))>0 and len(list(set(maxim) & set(maxim_last)))>0:
            mi = list(set(minim) & set(minim_last))
            ma = list(set(maxim) & set(maxim_last))
            results.append([mesi[idx][0], ','.join(sorted(mi)), ','.join(sorted(ma))])
    
    return results


def min_no_zero(l):
    m = max(l)
    for i in l:
        if i > 0 and i < m:
            m = i
    return m

