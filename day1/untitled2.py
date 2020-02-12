# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 13:25:14 2020

@author: LG
"""

class person:
  def __init__(self, name="Guest", age=25, enery_level=100):
    self.name = name
    self.age = age
    self.energy_level = energy_level
  def power_up(self):
    self.energy_level = self.energy_level+5
  def power_down(self):
    self.energy_level -= 5
  def display_all_attributes(self):
    print('Name: ', self.name)
    print('Age: ', self.age)
    print('Power level: ', self.energy_level)

person1 = person()
person1.name = 'James'

person1.display_all_attribure()
person1.power_down()

person2 = person()