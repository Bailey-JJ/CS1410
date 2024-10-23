'''
Author Name: Bailey Jannuzzi
Module: cookie.py
Description: Describes the Cookie class.
'''
from desert_item import DesertItem

class Cookie(DesertItem):
  '''
  Takes parameters name, cookie_quantity, and price_per_dozen
  '''
  def __init__(self, name = '', cookie_quantity = 0, price_per_dozen = 0.0):
    super().__init__(name)
    self._cookie_quantity = cookie_quantity
    self._price_per_dozen = price_per_dozen
    
  @property
  def cookie_quantity(self):
      return self._cookie_quantity
  
  @cookie_quantity.setter
  def cookie_quantity(self, new_q):
      self._cookie_quantity = new_q

  @property
  def price_per_dozen(self):
      return self._price_per_dozen
  
  @price_per_dozen.setter
  def price_per_dozen(self, new_price):
      self._price_per_dozen = new_price

  def calculate_cost(self):
    cost = (self._cookie_quantity/12) * self._price_per_dozen
    return round(cost, 2)

  def __str__(self):
    return f'{self._name}, {self._cookie_quantity} cookie(s), ${self._price_per_dozen:.2f}/dozen, ${self.calculate_cost():.2f}, ${self.calculate_tax():.2f}'