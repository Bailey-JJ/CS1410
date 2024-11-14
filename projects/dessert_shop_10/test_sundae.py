'''
Author Name: Bailey Jannuzzi
Module: test_sundae.py
Description: Tests the sundae.py class attributes, setters, getters, and functions.
'''
from sundae import Sundae

def test_sundae_init_default():
  sundae = Sundae()
    
  assert sundae._topping_name == ''
  assert sundae._topping_price == 0.0
  assert sundae._packaging == 'Boat'

    
def test_sundae_init_nominal():
  sundae = Sundae('Chocolate Sundae', 2, 3.0, 'Oreo Bits', 4.0)
    
  assert sundae._topping_name == 'Oreo Bits'
  assert sundae._topping_price == 4.0  
  assert sundae._packaging == 'Boat'
  
    
def test_sundae_getters():
  sundae = Sundae('Chocolate Sundae', 2, 3.0, 'Oreo Bits', 4.0)
    
  assert sundae._topping_name == 'Oreo Bits'
  assert sundae._topping_price == 4.0
    
def test_sundae_setters():
  sundae = Sundae('Chocolate Sundae', 2, 3.0, 'Oreo Bits', 4.0)
    
  sundae.topping_name = 'Sprinkles'
  sundae.topping_price = 5.0
    
  assert sundae._topping_name == 'Sprinkles'
  assert sundae._topping_price == 5.0


def test_sundae_calculate_cost():
  sundae = Sundae('Chocolate Sundae', 2, 3.0, 'Oreo Bits', 4.0)
    
  assert sundae._topping_name == 'Oreo Bits'
  assert sundae._topping_price == 4.0  
  assert sundae.calculate_cost() == 10.00


def test_sundae_calculate_tax():
  sundae = Sundae('Chocolate Sundae', 2, 3.0, 'Oreo Bits', 4.0)
    
  assert sundae._topping_name == 'Oreo Bits'
  assert sundae._topping_price == 4.0  
  assert sundae.calculate_tax() == 0.72