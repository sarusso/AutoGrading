

def sum_list(the_list):
    if not the_list:
        return None
    else:
        total = 0
        for element in the_list:
            total+=element
        return total

def sum_csv(the_file):
    if not the_file:
        return None
    else:
        # Inizializzo una lista vuota per salvare i valori
        values = []
        header_processed = False
        
        # Apro e leggo il file, linea per linea
        my_file = open(the_file, 'r')
        for line in my_file:
        
            # Faccio lo split di ogni riga sulla virgola
            elements = line.split(',')
        
            # Se NON sto processando l'intestazione... 
            if not header_processed:
                header_processed = True
            else:
        
                # Setto la data e il valore
                date  = elements[0]
                value = elements[1]
                
                if value.strip().isnumeric():
                    values.append(float(value))

        my_file.close()
                
        return sum_list(values)