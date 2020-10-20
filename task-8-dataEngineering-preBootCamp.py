# -*- coding: utf-8 -*-
"""
Umuzi Data Engineering Pre-Bootcamp

@author: Simphiwe Shongwe
@Git: S1mp41w3
@E-mail: Sim01Shongwe@gmail.com


Task 8

Make a function to convert any number into hours and minutes. 
(For example, 71 will become “1 hour, 11 minutes”; 133 will become “2 hours,
 13 minutes”.)

"""

def time_conv(x):
    hour = str(x // 60) + ' hour, '
    hours = str(x // 60) + ' hours, '
    minute = str(x % 60) + ' minutes'
    if x >= 120:
        return hours + minute 
    else:
        if x <= 120:
            return hour + minute
        else: 
            if x <= 60:
                return minute
        
        
print(time_conv(50))
print(time_conv(100))
print(time_conv(200))

