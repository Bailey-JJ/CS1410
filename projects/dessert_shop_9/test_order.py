'''
Author Name: Bailey Jannuzzi
Module: test_order.py
Description: Tests the order.py class.
'''
from candy import Candy
from cookie import Cookie
from order import Order
from payment import PayType, Payable
import pytest

def test_order_cash():
  order = Order()
  order.set_pay_type(PayType.CASH)

  assert order.get_pay_type().name == 'CASH'
    
    
def test_order_card():
  order = Order()
  order.set_pay_type(PayType.CARD)

  assert order.get_pay_type().name == 'CARD'
    
    
def test_order_phone():
  order = Order()
  order.set_pay_type(PayType.PHONE)

  assert order.get_pay_type().name == 'PHONE'
    
 
def test_order_invalid():
  order = Order()
  with pytest.raises(ValueError, match = 'Error. Invalid input. Payment method must be either CARD, CASH, or PHONE.'):
    order.set_pay_type('Invalid')


def test_order_return_invalid():
  order = Order()

  assert order.get_pay_type() == None


def test_order_sort():
  order = Order()

  n1 = Candy('Candy Corn', 1.5, 0.25)
  n2 = Candy('Gummy Bears', 0.25, 0.35)
  n3 = Cookie('Chocolate Chip', 6, 3.99)

  order.add(n1)
  order.add(n2)
  order.add(n3)

  order.sort()

  assert order._order == [n2, n1, n3]