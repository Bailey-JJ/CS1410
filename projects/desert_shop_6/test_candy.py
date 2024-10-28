'''
Author Name: Bailey Jannuzzi
Module: test_candy.py
Description: Tests the candy.py class attributes, setters, getters, and functions.
'''
from candy import Candy

def test_candy_init_default():
  candy = Candy()
    
  assert candy._candy_weight == 0.0
  assert candy._price_per_pound == 0.0    
  assert candy._packaging == 'Bag'
    

def test_candy_init_nominal():
  candy = Candy('Gushers', 2.0, 4.0)
    
  assert candy._candy_weight == 2.0
  assert candy._price_per_pound == 4.0 
  assert candy._packaging == 'Bag'


def test_candy_getters():
  candy = Candy('Gushers', 2.0, 4.0)
    
  assert candy.candy_weight == 2.0
  assert candy.price_per_pound == 4.0
    

def test_candy_setters():
  candy = Candy('Gushers')
    
  candy.candy_weight = 3.0
  candy.price_per_pound = 5.0
    
  assert candy._candy_weight == 3.0
  assert candy._price_per_pound == 5.0


def test_candy_calculate_cost():
  candy = Candy('Gushers', 2.0, 4.0)
    
  assert candy._candy_weight == 2.0
  assert candy._price_per_pound == 4.0 
  assert candy.calculate_cost() == 8.00


def test_candy_calculate_tax():
  candy = Candy('Gushers', 2.0, 4.0)
    
  assert candy._candy_weight == 2.0
  assert candy._price_per_pound == 4.0 
  assert candy.calculate_tax() == 0.58