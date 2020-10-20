# -*- coding: utf-8 -*-
"""
Umuzi Data Engineering Pre-Bootcamp

@author: Simphiwe Shongwe
@Git: S1mp41w3
@E-mail: Sim01Shongwe@gmail.com


Task 6

White a function that takes in three numbers and returns the maximum number. Do this without using any builtin methods. Write your own logic from scratch.

Bonus: How can you change the code so it can take in any number of numbers?


"""

def find_max(x,y,z):
    if (x >= y) and (x >= z):
        return x
    else:
        if (y >= z) and (y >= x):
            return y
        else:
            if (z >= x) and (z >= y):
                return z
        
    
print(find_max(4, 5, 6))
print(find_max(0.5, 0, 0.05))
print(find_max(1, -1, 1.1))


#Bonus

