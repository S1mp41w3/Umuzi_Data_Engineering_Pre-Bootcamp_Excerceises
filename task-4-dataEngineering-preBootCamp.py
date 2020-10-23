# -*- coding: utf-8 -*-
"""
Umuzi Data Engineering Pre-Bootcamp

@author: Simphiwe Shongwe
@Git: S1mp41w3
@E-mail: Sim01Shongwe@gmail.com

Task 4

Write a function that takes 2 numbers as input. 
If either of the numbers is 3 AND the sum of the numbers contains a 3 
then return true.
Otherwise return false

"""

def find_3(x,y):
    
    if x == 3 or y == 3 and str(3) in str(x+y): 
        return True
    else:
        return False
    
print(find_3(10,3))
print(find_3(7, 3))
print(find_3(6,7))

