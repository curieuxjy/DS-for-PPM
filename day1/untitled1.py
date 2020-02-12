# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 13:24:00 2020

@author: LG
"""

# by reference
def my_function(input_arg):
  print('Value received: ', input_arg, 'id: ', id(input_arg))
  
  input_arg *= 10
  print('Value multipied: ', input_arg, 'id: ', id(input_arg))
  
x = 10
print('Value before being passed: ', x, 'id: ', id(x))
my_function(x)
print('Value after being passed: ', x, 'id: ', id(x))
###############################################################
# global variable
def say_hello():
#  global user_name
  
  user_name = 'Steve'
  print("Changed name: ", user_name)
  return
user_name = 'John'
print("user name before called = ", user_name)
say_hello()
print("user name after called = ", user_name)
###############################################################
