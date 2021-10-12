#Ejercicio 1: Date Detection

'''
Write a regular expression that can detect dates in the DD/MM/YYYY format.
Assume that the days range from 01 to 31, the months range from 01 to 12,
and the years range from 1000 to 2999. Note that if the day or month is a
single digit, it’ll have a leading zero.

The regular expression doesn’t have to detect correct days for each month
or for leap years; it will accept nonexistent dates like 31/02/2020 or
31/04/2021.

Then store these strings into variables named month, day, and year,
and write additional code that can detect if it is a valid date.
April, June, September, and November have 30 days, February has 28 days,
and the rest of the months have 31 days.

February has 29 days in leap years. Leap years are every year evenly divisible
by 4, except for years evenly divisible by 100, unless the year is also evenly
divisible by 400.

Note how this calculation makes it impossible to make a reasonably sized regular
expression that can detect a valid date.

#devuelve false si alguna fecha está mal no importa cual, y true si estan todas
bien

'''

import re

string='Hoy me voy de fiesta el 31/08/2099 y mañana duermo (18/12/2010) bisiesto= 29/2/1200)'


def detectDates(string):
    regex = re.compile(r'''
    (
    \d\d       #dia
    /          #separador
    \d\d       #mes
    /          #separador
    \d\d\d\d   #año
    )
    ''',re.VERBOSE)

    fechas=regex.findall(string)
    
    respuesta=True

    for dates in fechas:
        day=int(dates[0:2])
        month=int(dates[3:5])
        year=int(dates[6:10])
        
        if 1000<=year<=2999:
            if (month==(4|6|9|11)) & (day==31):
                return False
            
            elif month==2:
                if day==29:
                    if (year%4 == 0) & ((year%100 !=0) | (year%400 ==0)):
                        continue
                    else:
                        return False
                elif day>29:
                    return False
                else:
                    continue
                
            else:
                continue
        else:
            return False
            
    return respuesta
            
            

print(detectDates(string))
    



