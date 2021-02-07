# -*- coding: utf-8 -*-
"""HW2-Question.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tLvVqQCy6rU0ioTAuMYd7GTTg-Q2jRTZ
"""

# Simple user Login application

# Predefined user name and password for checking
user_name = "GlobalAI"
password = "toplearn5"

# To get the username and password values from the user 
user_name_given =input("Please enter your user name:")
password_given= input("Please enter your password:")

# Checking the given information is true or not with if-elif-else statement
if (user_name == user_name_given and password == password_given):
  print("Login is successful")
elif (user_name != user_name_given and password == password_given):
  print("The user name is not correct")
elif (user_name == user_name_given and password != password_given):
  print("The password is not correct")
else:
  print("The user name and password are both incorrect")

"""Alternative, dictionary based solution

"""

# Creating the same application with dictionary

# Predefined user name and password as dictionary 
# with two keys; username and password
user_information = {"user_name" : "GlobalAI", "password" : "toplearn5"}

# To get the username and password values from the user 
user_name_given =input("Please enter your user name:")
password_given= input("Please enter your password:")

# Checking the given information is true or not with if-elif-else statement
if (user_information["user_name"] == user_name_given and user_information["password"] == password_given):
  print("Login is successful")
elif (user_information["user_name"] != user_name_given and user_information["password"] == password_given):
  print("The user name is not correct")
elif (user_information["user_name"] == user_name_given and user_information["password"] != password_given):
  print("The password is not correct")
else:
  print("The user name and password are both incorrect")