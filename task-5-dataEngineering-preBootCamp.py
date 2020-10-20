# -*- coding: utf-8 -*-
"""
Umuzi Data Engineering Pre-Bootcamp

@author: Simphiwe Shongwe
@Git: S1mp41w3
@E-mail: Sim01Shongwe@gmail.com

Task 5

Write a function that takes in three numbers. 
These numbers represent the lengths of the sides of a triangle. 
The function should return the area of a triangle.

"""

def find_area(x,y,z):
    per = (x + y + z) 
    semi = per / 2 
    a = (semi*(semi-x)*(semi-y)*(semi-z))**(0.5)
    return a
    
print(find_area(6, 8, 10))
print(find_area(2, 2, 2))
print(find_area(18, 30, 24))

