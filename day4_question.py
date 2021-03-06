# -*- coding: utf-8 -*-
"""Day3_HW.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Enfkxz3o5bm5ymttyC17TIja6-0oZGmJ
"""

# Define a function for finding prime numbers over a given range
def findingPrimes(lower, upper):
# lower : the starting number, lower value of the range
# upper : the terminating number, upper value of the range

  PrimeNumber=[]
  for num in range(lower, upper + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           PrimeNumber.append(num)
  return (PrimeNumber)

#Calculate the primes between 0 and 100
lower = 0
upper = 100
Primes= findingPrimes(lower, upper) 
print("The prime numbers between", lower, "and", upper, "are:", Primes)
# OR 
Primes= findingPrimes(lower=0, upper=100)
print(Primes)