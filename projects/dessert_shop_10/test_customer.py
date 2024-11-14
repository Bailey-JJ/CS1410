'''
Author Name: Bailey Jannuzzi
Module: test_customer.py
Description: Tests the customer.py class.
'''
from customer import Customer
from order import Order
from candy import Candy
import pytest

def test_customer_init():
  customer = Customer('Bailey')
  
  assert customer._customer_name == 'Bailey'
  assert customer._order_history == []
  assert isinstance(customer._customer_id, int) == True


def test_add_history():
  customer = Customer('Bailey')
  order = Order()
  customer.add_history(order)

  assert len(customer._order_history) == 1
  assert str(type(customer._order_history[0])) == "<class 'order.Order'>"


def test_customer_id():
  customer1 = Customer('Bailey')
  customer2 = Customer('Hailey')

  assert customer1._customer_id != customer2._customer_id
  assert customer2._customer_id == (customer1._customer_id + 1)