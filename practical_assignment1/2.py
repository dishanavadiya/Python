# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 23:34:23 2022

@author: 91982
"""

num = list(range(10))
previousNum = 0
for i in num:
    sum = previousNum + i
    print('Current Number '+ str(i) + 'Previous Number ' + str(previousNum) + 'is ' + str(sum)) # <- This is the issue.
    previousNum=i


# iterate from 1 to 10 and print the sum of current number and previous number
for i in range(1, 11):
    print(i, "+", i-1, "=", i+i-1)