# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 21:04:02 2016

@author: Pi Tian
"""

print("This program was made by Pi Tian in the United States of America \
on October 21, 2016. All Rights Reserved.\n")

digit = int(input("Please enter how many digit(s) of π do you need \
(it must be a integer and it should be bigger than zero): \n"))

import time
t= time.time()

import sys

if digit <= 0:
    print("Please check it again!")
    sys.exit()
else:
    if digit == 1:
        print("The first digit of π is 3.")
    else:
        def calculate_pi():
            a = 1
            b = 0
            c = 1
            d = 1
            e = 3
            f = 3
            while True:
                if 4 * a + b - c < e * c:
                    yield e
                    a, b, e = (10 * a, 10 * (b - e * c), (10 * (3 * a + b)) \
                    // c - 10 * e)
                else:
                    a, b, c, d, e, f = (a * d, (2 * a + b) * f, c * f, d + 1, \
                    (a * (7 * d + 2) + b * f) // (c * f), f + 2)
        
        pi = ''
        digits = 0
        
        for f in calculate_pi():
            pi += str(f)
            digits += 1
            
            if digits == digit:
               break
           
        print("\nHere are {:} digits" .format(digits) + " of π: \n")
        print(pi[:1] + "." + pi[1:])
        
    T = time.time()
    print("\nUsing {:} seconds to finish this program. \
    \nThanks for using this program!" .format(T - t))