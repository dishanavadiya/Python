# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 00:02:49 2022

@author: 91982
"""

lower = 1
upper = 20

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)