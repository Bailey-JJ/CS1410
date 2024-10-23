'''
Author Name: Bailey Jannuzzi
Module: order.py
Description: Describes the Order class.
'''
from candy import Candy
from cookie import Cookie
from ice_cream import IceCream
from sundae import Sundae 
from receipt import make_receipt

class Order:
  '''
  Takes no parameters. Creates a list of order items, and contains
  functions add(), __len__(), get_item_names(), __str__(),
  order_cost(), and order_tax().
  '''
  def __init__(self):
    self._order = []

  def __str__(self):
    '''
    Overrides the __str__ method and prints a receipt from an order input.
    '''
    items = [[print(item)] for item in self._order]
    return f'{items}\nOrder Subtotal: ${self.order_cost():.2f}\nOrder Tax: ${self.order_tax():.2f}\nOrder Total: ${self.order_cost() + self.order_tax():.2f}'

  def add(self, item):
    self._order.append(item)

  def __len__(self):
    return len(self._order)

  def get_item_names(self):
    return [item._name for item in self._order]

  def __str__(self):
    output = ''
    data = [[ "Name" , "Quantity", "Unit Price", "Cost", "Tax" ]]
    #receipt_list = [[str(item).strip(',')] for item in order._order]

    for item in self._order:
      item_line = str(item).split('\n')
      for line in item_line:
        receipt_list = line.split(", ")
        data.append(receipt_list)


    data.append([ "Order Subtotal", "", "", f"${self.order_cost():.2f}", f"${self.order_tax():.2f}"])
    data.append([ "Order Total", "", "", "", f"${(self.order_cost() + self.order_tax()):.2f}"])
    data.append([ "Total Items in the Order", "", "", "", str(len(self._order))])

    make_receipt(data)

    for item in data:
      output += ', '.join(item) + '\n'
    return output

      
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