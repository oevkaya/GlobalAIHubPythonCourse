# -*- coding: utf-8 -*-
"""Day2-Question2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JUUX1-0Zo5aXOIJuKVcfTeXPBObNkczc
"""

# Asking inout variable n
n = int(input("Please give a single digit integer"))
# Create the all numbers
mylist = list(range(n))
#choose the even ones in the list until n
even_numbers = [x for x in mylist if x % 2 == 0]
# Add the input value n to the even numbers
final_list = even_numbers.append(n)
# print the even numbers
print(even_numbers)
print(type(even_numbers))