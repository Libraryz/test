# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 22:15:06 2018

@author: Libraryz
"""

def g(x):
    return (2**x)+(2*(x**7))

def Derivative(x):
    h = 1.0e-1
    rise = g(x + h/2)-g(x - h/2)
    run = h
    slope = rise / run
    return slope

def Taylor_Expansion(a, sum, x, n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
        sum += (Derivative(g(a))/factorial)*((x-a)**i)
        print(i, factorial, sum)
    return sum

print('g(x)', g(3))
print('Derivative(x)', Derivative(3))
print('Taylor_Expansion(0, 0, 3, 7)', Taylor_Expansion(0, 0, 3, 7))

