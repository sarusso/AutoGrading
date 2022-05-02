
month_names = { 1: 'January',
                2: 'February',
                3: 'March',
                4: 'April',
                5: 'May',
                6: 'June',
                7: 'July',
                8: 'August',
                9: 'September',
                10: 'October',
                11: 'November',                    
                12: 'December' }


month_days = { 1: 31,
               2: 28,
               3: 31,
               4: 31,
               5: 30,
               6: 31,
               7: 30,
               8: 31,
               9: 30,
               10: 31,
               11: 30,                    
               12: 31 }

for i in range(12):
    print('{}: {}, {}'.format(i+1, month_names[i+1], month_days[i+1]))






















