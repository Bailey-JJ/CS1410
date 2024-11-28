'''
Author Name: Bailey Jannuzzi
Module: customer.py
Description: Describes the customer class.
'''

from typing import List
from order import Order

class Customer():
  next_id: int = 1000

  def __init__(self, customer_name: str):
    self._customer_name: str = customer_name
    self._order_history: List[Order] = []
    self._customer_id: int = Customer.next_id
    Customer.next_id += 1

  
  def add_history(self, order: Order) -> 'Customer':
    self._order_history.append(order)

  def get_history(self) -> List[Order]:
    for order in self._order_history:
      print(order)
    return ''

  def __str__(self) -> str:
    return f'Customer Name: {self._customer_name}\nCustomer ID: {self._customer_id}\nTotal Orders: {len(self._order_history)}'

    