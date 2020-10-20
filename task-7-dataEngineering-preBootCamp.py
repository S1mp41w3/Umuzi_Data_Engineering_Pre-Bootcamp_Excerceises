# -*- coding: utf-8 -*-
"""
Umuzi Data Engineering Pre-Bootcamp

@author: Simphiwe Shongwe
@Git: S1mp41w3
@E-mail: Sim01Shongwe@gmail.com


Task 7


Write a function that takes in a number representing the temperature in 
Celsius and returns the temperature in Fahrenheit. 
Write another function that does the opposite (Fereignheit to Celsius)


"""


# Farenheit to Celcius

def far_cel(y):
    cel_ = (y - 32) * 5/9
    return cel_

print(far_cel(50))
print(far_cel(100))
print(far_cel(39))



# Celcius to Farenheit


def cel_far(x):
   far_ = (x * 1.8) + 32
   return far_
    
print(cel_far(0))
print(cel_far(100))
print(cel_far(30))
    
   



  
    
    
