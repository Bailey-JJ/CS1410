'''
Author Name: Bailey Jannuzzi
Module: test_ice_cream.py
Description: Tests the ice_cream.py class attributes, setters, getters, and functions.
'''
from ice_cream import IceCream

def test_icecream_init_default():
  icecream = IceCream()
    
  assert icecream._scoop_count == 0
  assert icecream._price_per_scoop == 0.0
  assert icecream._packaging == 'Bowl'
    
    
def test_icecream_init_nominal():
  icecream = IceCream('Chocolate', 2, 4.0)
    
  assert icecream._scoop_count == 2
  assert icecream._price_per_scoop == 4.0  
  assert icecream._packaging == 'Bowl'
  

def test_icecream_getters():
  icecream = IceCream('Chocolate', 2, 4.0)
    
  assert icecream._scoop_count == 2
  assert icecream._price_per_scoop == 4.0
    

def test_icecream_setters():
  icecream = IceCream('Chocolate')
    
  icecream.scoop_count = 3
  icecream.price_per_scoop = 5.0
    
  assert icecream._scoop_count == 3
  assert icecream._price_per_scoop == 5.0


def test_icecream_calculate_cost():
  icecream = IceCream('Chocolate', 2, 4.0)
    
  assert icecream._scoop_count == 2
  assert icecream._price_per_scoop == 4.0  
  assert icecream.calculate_cost() == 8.00


def test_icecream_calculate_tax():
  icecream = IceCream('Chocolate', 2, 4.0)
    
  assert icecream._scoop_count == 2
  assert icecream._price_per_scoop == 4.0 
  assert icecream.calculate_tax() == 0.58