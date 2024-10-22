'''
Author Name: Bailey Jannuzzi
Module: desert_item.py
Description: Describes the abstract DesertItem class.
'''
from abc import ABC, abstractmethod

class DesertItem(ABC):
  '''
  Takes one parameter called 'name'.
  '''

  def __init__(self, name = ''):
    self._name = name
    self._tax_percent = 7.25

  @property
  def name(self):
      return self._name
  
  @name.setter
  def name(self, new_name):
      self._name = new_name

  @abstractmethod
  def calculate_cost(self):
    pass

  def calculate_tax(self):
    cost = self.calculate_cost()
    tax =  round((cost * (self._tax_percent/100)), 2)
    return round(tax, 2)