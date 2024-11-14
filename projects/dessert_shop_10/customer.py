'''
Author Name: Bailey Jannuzzi
Module: customer.py
Description: Describes the customer class.
'''

from typing import List
from order import Order

class Customer():
  next_id: int = 1

  def __init__(self, customer_name: str):
    self._customer_name: str = customer_name
    self._order_history: List[Order] = []
    self._customer_id: int = Customer.next_id
    Customer.next_id += 1

  
  def add_history(self, order: Order) -> 'Customer':
    self._order_history.append(order)
    return self



    