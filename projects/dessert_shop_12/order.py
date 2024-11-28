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
from payment import PayType, Payable 
from typing import List, Iterator 
from combine import Combinable

class Order(Payable):
  '''
  Takes no parameters. Creates a list of order items, and contains
  functions add(), __len__(), get_item_names(), __str__(),
  order_cost(), and order_tax().
  '''
  def __init__(self):
    self._order: List[object] = []
    self._payment_method = None
    self._index = 0

  def add(self, item: object) -> None:
    if isinstance(item, Combinable):
      for existing in self._order:
        if isinstance(existing, Combinable) and item.can_combine(existing):
          existing.combine(item)
          return
    self._order.append(item)

  def __iter__(self) -> Iterator:
    self._index = 0
    return self

  def __next__(self):
    if self._index < len(self._order):
      output = self._order[self._index]
      self._index += 1
      return output
    else:
      raise StopIteration

  def sort(self):
    self._order.sort()

  def __len__(self):
    return len(self._order)

  def get_item_names(self):
    return [item._name for item in self._order]

  def get_pay_type(self) -> PayType:
    return self._payment_method

  def set_pay_type(self, new_payment_method: PayType) -> None:
    if isinstance(new_payment_method, PayType):
      self._payment_method = new_payment_method
    else:
      raise ValueError("Error. Invalid input. Payment method must be either CARD, CASH, or PHONE.")

  def __str__(self):
    '''
    Takes values from self._order and prints receipt to the terminal and a pdf.
    '''
    output = '----------------------------------------------Receipt-------------------------------\n'

    data = [[ "Name", "Quantity", "Unit Price", "Cost", "Tax" ]]

    for item in self._order:
      item_line = str(item).split('\n')
      for line in item_line:
        if len(line.split(", ")) > 5:
          receipt_list = line.split(", ")
          name, quantity, price, cost, tax, topping, topping_qty, topping_price = line.split(", ")
          output += f"{name}\n"
          size = f"      {quantity} @ {price}\n"
          number = f"      {topping} @ {topping_price}"
          output += f"{size}{number:45}           {cost:>4}           [Tax: {tax:>4}]\n"

          data.append(receipt_list[0:5])
          data.append(receipt_list[5:8])
        else:
          receipt_list = line.split(", ")
          name, quantity, price, cost, tax = line.split(", ")
          output += f"{name}\n"
          size = f"      {quantity} @ {price}:"
          output += f"{size:45}           {cost:>4}           [Tax: {tax:>4}]\n"

          data.append(receipt_list)

    data.append([ "Order Subtotal", "", "", f"${self.order_cost():.2f}", f"${self.order_tax():.2f}"])
    data.append([ "Order Total", "", "", "", f"${(self.order_cost() + self.order_tax()):.2f}"])
    data.append([ "Total Items in the Order", "", "", "", str(len(self._order))])
    data.append([ f"Paid with {self.get_pay_type().name}", "", "", "", ""])

    output += '-------------------------------------------------------------------------------------\n'
    output += f'Total number of items in order: {len(self._order)}\n'
    order_sub = 'Order Subtotals:'
    order_tot = 'Order Total:'
    tcost = f'{order_sub:56}${self.order_cost():>4.2f}'

    ttax = f'[Tax: ${self.order_tax():>4.2f}]'
    output += f'{tcost}           {ttax}\n'
    total = f'${(self.order_cost() + self.order_tax()):.2f}'
    output += f'{order_tot:77} {total:>4}\n'
    output += '-------------------------------------------------------------------------------------\n'
    if self._payment_method:
      output += f'Paid with {self.get_pay_type().name}'
    else:
      output += 'Payment Type: Unknown.'

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