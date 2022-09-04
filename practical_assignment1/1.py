# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 23:20:48 2022

@author: 91982
"""



#Assignment Question 1
def multiplication_or_sum(num1, num2):
    product = num1 * num2
    if num1*num2 <= 1000:
        return num1*num2
    else:
        return num1+num2 

result = multiplication_or_sum(20,30)
print("The result is = ", result)

result = multiplication_or_sum(50,10)
print("The result is = ", result)



