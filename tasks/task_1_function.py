# TASK 1
# Write a function, which accepts time delta specifier as a string argument and returns time interval in seconds as an integer.
# Supported time units: s – seconds, m – minute, h – hour, d – day, with seconds being default unit and 1 being default value.
# Please supply unit tests for the solution.
#
# Examples of input time delta specifier and output value:
# Time Delta Specifier = Output Value
# 30 = 30
# 30s = 30
# s = 1
# 60.5m = 3630
# 10seconds = Exception raised
# 1m30s = Exception raised
# 1y = Exception raised
# <empty string> = Exception raised

import re

class Specifier:
    def __init__(self,a):
        self.a = a

    def Delta(a: 's'== 1):
        values = list(a)
        s = 1
        m = 60
        h = 60*60
        d = 24*60*60

        count = re.findall('[a-z]',a)
        if len(count) > 1:
            return ("Only 1 unit time can be added")
        else:
            try:
                for i in values:
                    if i == 's' and values.count('m')==0 and values.count('h')==0 and values.count('d')==0:
                        s_position = values.index(i)
                        str_s = ''.join(str(e) for e in values[0:s_position])
                        if str_s != '':
                            return(int(str_s)*s)
                        else:
                            return(s)
                    elif i == 'm' and values.count('s')==0 and values.count('h')==0 and values.count('d')==0:
                        m_position = values.index(i)
                        str1 = ''.join(str(e) for e in values[0:m_position])
                        if str1 != '':
                            return(round(float(str1)*m))
                        else:
                            return(m)
                    elif i == 'h' and values.count('s')==0 and values.count('m')==0 and values.count('d')==0:
                        h_position = values.index(i)
                        str2 = ''.join(str(e) for e in values[0:h_position])
                        if str2 != '':
                            return(round(float(str2)*h))
                        else:
                            return(h)
                    elif i == 'd' and values.count('s')==0 and values.count('m')==0 and values.count('h')==0:
                        d_position = values.index(i)
                        str3 = ''.join(str(e) for e in values[0:d_position])
                        if str3 != '':
                            return(round(float(str3) * d))
                        else:
                            return(d)

                if values.count('m') == 0 and values.count('h') == 0 and values.count('d') == 0 and values.count('s') == 0:
                    str0 = ''.join(str(e) for e in values)
                    return(int(str0))


            except ValueError:
                        return("Unsupported time units have been added. Possible time units are 's', 'm', 'h', 'd' and possible format is number without '/'")



    def __eq__(self, other):
        return self.Delta() == other.Delta()

    # Delta('')

# spent time is about 8 h
