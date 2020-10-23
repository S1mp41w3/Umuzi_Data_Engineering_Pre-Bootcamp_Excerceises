# -*- coding: utf-8 -*-
"""
Umuzi Data Engineering Pre-Bootcamp

@author: Simphiwe Shongwe
@Git: S1mp41w3
@E-mail: Sim01Shongwe@gmail.com


Task 10

Write a function that takes in a string and then prints out all the vowels
in the string.
Make sure it can deal with capital letters and small letters.

"""


def find_vowels(x):
    
    
    vowels =['a','A','e','E','i','I','o','O','u','U']
    out_ = set(x).intersection(vowels)
    return out_

  
    
print(find_vowels('amazing'))
print(find_vowels('Umuzi'))
print(find_vowels('Flood'))
