# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
n = int(input("Enter number:"))
    
def collatz(number):
    r = number % 2
    if r == 0:
        return number // 2
            #print(n)
    else:
        return 3 * number + 1
        
while n != 1:   
    #print(collatz(n))
    n = collatz(n)
    print(n)

