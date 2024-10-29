'''
Author Name: Bailey Jannuzzi
Module: test_cookie.py
Description: Tests the cookie.py class attributes, setters, getters, and functions.
'''
from cookie import Cookie

def test_cookie_init_default():
  cookie = Cookie()
    
  assert cookie._cookie_quantity == 0
  assert cookie._price_per_dozen == 0.0
    
    
def test_cookie_init_nominal():
  cookie = Cookie('Chocolate', 2, 4.0)
    
  assert cookie._cookie_quantity == 2
  assert cookie._price_per_dozen == 4.0  

    
def test_cookie_getters():
  cookie = Cookie('Chocolate', 2, 4.0)
    
  assert cookie.cookie_quantity == 2
  assert cookie.price_per_dozen == 4.0

    
def test_cookie_setters():
  cookie = Cookie('Chocolate')
    
  cookie.cookie_quantity = 3
  cookie.price_per_dozen = 5.0
    
  assert cookie._cookie_quantity == 3
  assert cookie._price_per_dozen == 5.0


def test_cookie_calculate_cost():
  cookie = Cookie('Chocolate', 2, 4.0)
    
  assert cookie._cookie_quantity == 2
  assert cookie._price_per_dozen == 4.0  
  assert cookie.calculate_cost() == 0.67


def test_cookie_calculate_tax():
  cookie = Cookie('Chocolate', 2, 4.0)
    
  assert cookie._cookie_quantity == 2
  assert cookie._price_per_dozen == 4.0  
  assert cookie.calculate_tax() == 0.05