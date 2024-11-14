'''
Author Name: Bailey Jannuzzi
Module: sundae.py
Description: Describes the Sundae class.
'''
from ice_cream import IceCream

class Sundae(IceCream):
  '''
  Takes parameters name, scoop_count, and price_per_scoop, topping_name, and topping_price
  '''
  def __init__(self, name = '', scoop_count = 0, price_per_scoop = 0, topping_name = '', topping_price = 0.0):
    super().__init__(name, scoop_count, price_per_scoop)
    self._topping_name = topping_name
    self._topping_price = topping_price
    self._packaging = 'Boat'
    
  @property
  def topping_name(self):
      return self._topping_name
  
  @topping_name.setter
  def topping_name(self, new_name):
      self._topping_name = new_name

  @property
  def topping_price(self):
      return self._topping_price
  
  @topping_price.setter
  def topping_price(self, new_price):
      self._topping_price = new_price

  def calculate_cost(self):
    icecream_cost = super().calculate_cost()
    cost = float(icecream_cost) + self._topping_price
    return round(cost, 2)

  def __str__(self):
    return (f'{self._name} Sundae ({self._packaging}), {self._scoop_count} scoop(s), ${self._price_per_scoop:.2f}/scoop, ${self.calculate_cost():.2f}, ${self.calculate_tax():.2f}, {self._topping_name} Topping, 1, ${self._topping_price}')