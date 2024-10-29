'''
Author Name: Bailey Jannuzzi
Module: ice_cream.py
Description: Describes the IceCream class.
'''
from desert_item import DesertItem

class IceCream(DesertItem):
  '''
  Takes parameters name, scoop_count, and price_per_scoop
  '''
  def __init__(self, name = '', scoop_count = 0, price_per_scoop = 0.0):
    super().__init__(name)
    self._scoop_count = scoop_count
    self._price_per_scoop = price_per_scoop
    
  @property
  def scoop_count(self):
      return self._scoop_count
  
  @scoop_count.setter
  def scoop_count(self, new_count):
      self._scoop_count = new_count

  @property
  def price_per_scoop(self):
      return self._price_per_scoop
  
  @price_per_scoop.setter
  def price_per_scoop(self, new_price):
      self._price_per_scoop = new_price

  def calculate_cost(self):
    cost = self._scoop_count * self._price_per_scoop
    return round(cost, 2)