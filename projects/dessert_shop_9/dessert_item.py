'''
Author Name: Bailey Jannuzzi
Module: desert_item.py
Description: Describes the abstract DesertItem class.
'''
from abc import ABC, abstractmethod
from packaging import Packaging

class DesertItem(ABC, Packaging):
  '''
  Takes one parameter called 'name'.
  '''

  def __init__(self, name: str):
    super().__init__(self)
    self._name = name
    self._tax_percent = 7.25
    self._packaging = None

  @property
  def name(self):
      return self._name
  
  @name.setter
  def name(self, new_name):
      self._name = new_name

  @abstractmethod
  def calculate_cost(self):
    pass

  @abstractmethod
  def __str__(self):
    pass

  def calculate_tax(self):
    cost = self.calculate_cost()
    tax =  round((cost * (self._tax_percent/100)), 2)
    return round(tax, 2)

  def __eq__(self, other):
    return self.calculate_cost() == other.calculate_cost()

  def __ne__(self, other):
    return self.calculate_cost() != other.calculate_cost()

  def __lt__(self, other):
    return self.calculate_cost() < other.calculate_cost()

  def __gt__(self, other):
    return self.calculate_cost() > other.calculate_cost()

  def __le__(self, other):
    return self.calculate_cost() <= other.calculate_cost()

  def __ge__(self, other):
    return self.calculate_cost() >= other.calculate_cost()