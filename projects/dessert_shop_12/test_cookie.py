'''
Author Name: Bailey Jannuzzi
Module: test_cookie.py
Description: Tests the cookie.py class attributes, setters, getters, and functions.
'''
from cookie import Cookie
from candy import Candy
import pytest

def test_cookie_init_default():
  cookie = Cookie()
    
  assert cookie._cookie_quantity == 0
  assert cookie._price_per_dozen == 0.0
  assert cookie._packaging == 'Box'

    
def test_cookie_init_nominal():
  cookie = Cookie('Chocolate', 2, 4.0)
    
  assert cookie._cookie_quantity == 2
  assert cookie._price_per_dozen == 4.0 
  assert cookie._packaging == 'Box' 

    
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

def test_cookie_can_combine():
  cookie1 = Cookie('Chocolate', 2, 4.0)
  cookie2 = Cookie('Chocolate', 2, 4.0)

  assert cookie1.can_combine(cookie2) == True


def test_cookie_cannot_combine_not_cookie():
  cookie1 = Cookie('Chocolate', 2, 4.0)
  cookie2 = Candy('Gushers', 2.0, 4.0)

  assert cookie1.can_combine(cookie2) == False


def test_cookie_combine_true():
  cookie1 = Cookie('Chocolate', 2, 4.0)
  cookie2 = Cookie('Chocolate', 2, 4.0)
  cookie1.combine(cookie2)

  assert cookie1._cookie_quantity == 4


def test_cookie_combine_false():
  cookie1 = Cookie('Chocolate', 2, 5.0)
  cookie2 = Candy('Gushers', 2.0, 4.0)
  
  with pytest.raises(ValueError):
    cookie1.combine(cookie2)