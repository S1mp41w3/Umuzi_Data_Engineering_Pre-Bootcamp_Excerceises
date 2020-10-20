# -*- coding: utf-8 -*-
"""
Umuzi Data Engineering Pre-Bootcamp

@author: Simphiwe Shongwe
@Git: S1mp41w3
@E-mail: Sim01Shongwe@gmail.com


Task 11

Make a function that takes two strings as input,
and outputs the common characters/letters that they share. 
(For example, Input: ‘house’, ‘computers’ . Output: ‘Common letters: o, u, e, s’)

""" 

def common_char(x,y):
    z = x.intersection(y)
    return z

print(common_char('coding','crazy'))

           


#Not yet working