# write a program to solve quadratic equation.

'''
The standard form of a quadratic equation is: ax^2 + bx + c = 0
where a,b and c are real numbers and 
a is not 0
the solutons of this quadratic equation is given by: (-b +- (b^2 - 4ac)^1/2)/(2a)
'''

import math
# input coefficients
a = float(input("Enter coefficients of a: "))
b = float(input("Enter coefficients of b: "))
c = float(input("Enter coefficients of c: "))

# calculate the discriminant
discriminant = 