from candy import Candy

def test_candy_init_default():
  candy = Candy()
    
  assert candy._name == ''
  assert candy._candy_weight == 0.0
  assert candy._price_per_pound == 0.0    
    

def test_candy_init_nominal():
  candy = Candy('Gushers', 2.0, 4.0)
    
  assert candy._name == 'Gushers'
  assert candy._candy_weight == 2.0
  assert candy._price_per_pound == 4.0 


def test_candy_getters():
  candy = Candy('Gushers', 2.0, 4.0)
    
  assert candy.name == 'Gushers'
  assert candy.candy_weight == 2.0
  assert candy.price_per_pound == 4.0
    

def test_candy_setters():
  candy = Candy('Gushers')
    
  candy.name = 'KitKat'
  candy.candy_weight = 3.0
  candy.price_per_pound = 5.0
    
  assert candy._name == 'KitKat'
  assert candy._candy_weight == 3.0
  assert candy._price_per_pound == 5.0


def test_candy_calculate_cost():
  candy = Candy('Gushers', 2.0, 4.0)
    
  assert candy._name == 'Gushers'
  assert candy._candy_weight == 2.0
  assert candy._price_per_pound == 4.0 
  assert candy.calculate_cost() == 8.00


def test_candy_calculate_tax():
  candy = Candy('Gushers', 2.0, 4.0)
    
  assert candy._name == 'Gushers'
  assert candy._candy_weight == 2.0
  assert candy._price_per_pound == 4.0 
  assert candy.calculate_cost() == 8.00
  assert candy.calculate_tax() == 0.58