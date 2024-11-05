'''
Author Name: Bailey Jannuzzi
Module: test_order.py
Description: Tests the desert_item.py class attributes, setters, and getters.
'''
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
