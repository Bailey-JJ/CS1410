'''
Author Name: Bailey Jannuzzi
Module: test_desert_item.py
Description: Tests the desert_item.py class attributes, setters, and getters.
'''
from desert_item import DesertItem
from candy import Candy

def test_desertitem_init_default():
  candy = Candy()
    
  assert candy._name == ''
  assert candy._tax_percent == 7.25
    
    
def test_desertitem_init_nominal():
  candy = Candy('Gushers')
    
  assert candy._name == 'Gushers'
  assert candy._tax_percent == 7.25
    
    
def test_desertitem_getters():
  candy = Candy('Gushers')
    
  assert candy.name == 'Gushers'
    
    
def test_desertitem_setters():
  candy = Candy('Gushers')
    
  candy.name = 'KitKat'
    
  assert candy._name == 'KitKat'
