# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 23:58:30 2022

@author: 91982
"""

num1, num2 = 1,22
sum = int((num2*(num2+1)/2) - (num1*(num1+1)/2) + num1)
print(sum)




n = int(input("Enter a number: "))
sum = 0
for i in range(1,n+1):
    sum += i

print("The sum of all numbers between 1 and {} is {}".format(n,sum))        