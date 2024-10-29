'''
Author Name: Bailey Jannuzzi
Module: order.py
Description: Describes the Order class.
'''
from candy import Candy
from cookie import Cookie
from ice_cream import IceCream
from sundae import Sundae 

class Order:
  '''
  Takes no parameters. Creates a list of order items, and contains
  functions add(), __len__(), get_item_names(), __str__(),
  order_cost(), and order_tax().
  '''
  def __init__(self):
    self._order = []

  def add(self, item):
    self._order.append(item)

  def __len__(self):
    return len(self._order)

  def get_item_names(self):
    return [item._name for item in self._order]

  def __str__(self):
    ord = ''
    for name in self.get_item_names():
      ord += f"{name}\n"
    ord += f"Total number of items in order: {len(self)}"
    return ord
      
  def order_cost(self):
    cost = 0
    for item in self._order:
      cost += float(item.calculate_cost())
    return round(cost, 2)

  def order_tax(self):
    tax = 0
    for item in self._order:
      tax += float(item.calculate_tax())
    return round(tax, 2)