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


def Common_char(x,y):
    out_ = set(x).intersection(y)
    return out_

print(Common_char('Coding','Crazy'))
print(Common_char('Good Moring','How are you?'))
print(Common_char('Mercedes','Maserati'))
