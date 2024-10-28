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
    output = '----------------------------------------------Receipt-------------------------------\n'

    data = [[ "Name", "Packaging", "Quantity", "Unit Price", "Cost", "Tax" ]]

    for item in self._order:
      item_line = str(item).split('\n')
      for line in item_line:
        if len(line.split(", ")) > 6:
          receipt_list = line.split(", ")
          name, package, quantity, price, cost, tax, topping, topping_qty, topping_price, _, _, _ = line.split(", ")
          output += f"{name} ({package})\n"
          size = f"      {quantity} @ {price}\n"
          number = f"      {topping} @ {topping_price}"
          output += f"{size}{number:45}           {cost:>4}           [Tax: {tax:>4}]\n"

          #del receipt_list[1]
          data.append(receipt_list[0:6])
          topping_details = [receipt_list[6], _, receipt_list[7], receipt_list[8]]
          data.append(topping_details)
        else:
          receipt_list = line.split(", ")
          name, package, quantity, price, cost, tax = line.split(", ")
          output += f"{name} ({package})\n"
          size = f"      {quantity} @ {price}:"
          output += f"{size:45}           {cost:>4}           [Tax: {tax:>4}]\n"

          #del receipt_list[1]
          data.append(receipt_list)

    data.append([ "Order Subtotal", "", "", "", f"${self.order_cost():.2f}", f"${self.order_tax():.2f}"])
    data.append([ "Order Total", "", "", "", "", f"${(self.order_cost() + self.order_tax()):.2f}"])
    data.append([ "Total Items in the Order", "", "", "", "", str(len(self._order))])

    output += '-------------------------------------------------------------------------------------\n'
    output += f'Total number of items in order: {len(self._order)}\n'
    order_sub = 'Order Subtotals:'
    order_tot = 'Order Total:'
    tcost = f'{order_sub:56}${self.order_cost():>4.2f}'

    ttax = f'[Tax: ${self.order_tax():>4.2f}]'
    output += f'{tcost}           {ttax}\n'
    total = f'${(self.order_cost() + self.order_tax())}'
    output += f'{order_tot:77} {total:>4}\n'
    output += '-------------------------------------------------------------------------------------'

    make_receipt(data)
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