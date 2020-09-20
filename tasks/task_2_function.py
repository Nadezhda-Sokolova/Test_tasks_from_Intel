# TASK 2
# Write a function that accepts non-negative integer number and returns another integer
# that is a "mirrored" representation of the input.
#
# Examples of input and output values:
# Input = Output
# 123 = 321
# 0 = 0
# 7777 = 7777
# 30 = 3
#
# There is obvious solution like output = int(str(input)[::-1]) but here you are asked to work only with numeric representation.
#
# Additionally, be ready to discuss how to expand this solution to floating point numbers, like 123.45 = 54.321

class INT:
    def __init__(self,a):
        self.a=a

    def integer(a):

        try:
            if a >=0:
                string = str(a)
                l = list(string)
                num = len(l)
                new = []
                j=0
                i=-1
                while j<num:
                    new.append(l[i])
                    i-=1
                    j+=1
                    str_s = ''.join(str(e) for e in new)
                return(float(str_s))
            else:
                return('The value is negative')
        except TypeError:
            return('Added value is not integer')

    def __eq__(self, other):
        return self.integer() == other.integer()



# INT(123)


# spent time is about 4 h
