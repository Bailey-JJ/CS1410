'''
Author Name: Bailey Jannuzzi
Module: test_desert_item.py
Description: Tests the desert_item.py class attributes, setters, and getters.
'''
from dessert_item import DesertItem
from candy import Candy

def test_desertitem_init_default():
  candy = Candy()
    
  assert candy._name == ''
  assert candy._tax_percent == 7.25
  assert candy._packaging == 'Bag'
    
    
def test_desertitem_init_nominal():
  candy = Candy('Gushers')
    
  assert candy._name == 'Gushers'
  assert candy._tax_percent == 7.25
  assert candy._packaging == 'Bag'
    
    
def test_desertitem_getters():
  candy = Candy('Gushers')
    
  assert candy.name == 'Gushers'
    
    
def test_desertitem_setters():
  candy = Candy('Gushers')
    
  candy.name = 'KitKat'
    
  assert candy._name == 'KitKat'


def test_eq():
  candy = Candy('Gushers', 2.0, 4.0)
  candy2 = Candy('KitKat', 2.0, 4.0)

  assert candy == candy2


def test_ne():
  candy = Candy('Gushers', 2.0, 4.0)
  candy2 = Candy('KitKat', 2.0, 3.0)

  assert candy != candy2


def test_lt():
  candy = Candy('Gushers', 2.0, 4.0)
  candy2 = Candy('KitKat', 2.0, 5.0)

  assert candy < candy2


def test_gt():
  candy = Candy('Gushers', 2.0, 4.0)
  candy2 = Candy('KitKat', 2.0, 3.0)

  assert candy > candy2


def test_le():
  candy = Candy('Gushers', 2.0, 4.0)
  candy2 = Candy('KitKat', 2.0, 4.0)
  candy3 = Candy('Skittles', 2.0, 3.0)

  assert candy <= candy2
  assert candy3 <= candy
  assert candy3 <= candy2


def test_ge():
  candy = Candy('Gushers', 2.0, 4.0)
  candy2 = Candy('KitKat', 2.0, 4.0)
  candy3 = Candy('Skittles', 2.0, 5.0)

  assert candy >= candy2
  assert candy3 >= candy
  assert candy3 >= candy2