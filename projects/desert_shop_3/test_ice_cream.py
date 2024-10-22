from ice_cream import IceCream

def test_icecream_init_default():
  icecream = IceCream()
    
  assert icecream._name == ''
  assert icecream._scoop_count == 0
  assert icecream._price_per_scoop == 0.0
    
    
def test_icecream_init_nominal():
  icecream = IceCream('Chocolate', 2, 4.0)
    
  assert icecream._name == 'Chocolate'
  assert icecream._scoop_count == 2
  assert icecream._price_per_scoop == 4.0  
    

def test_icecream_getters():
  icecream = IceCream('Chocolate', 2, 4.0)
    
  assert icecream.name == 'Chocolate'
  assert icecream._scoop_count == 2
  assert icecream._price_per_scoop == 4.0
    

def test_icecream_setters():
  icecream = IceCream('Chocolate')
    
  icecream.name = 'Mint'
  icecream.scoop_count = 3
  icecream.price_per_scoop = 5.0
    
  assert icecream.name == 'Mint'
  assert icecream._scoop_count == 3
  assert icecream._price_per_scoop == 5.0


def test_icecream_calculate_cost():
  icecream = IceCream('Chocolate', 2, 4.0)
    
  assert icecream._name == 'Chocolate'
  assert icecream._scoop_count == 2
  assert icecream._price_per_scoop == 4.0  
  assert icecream.calculate_cost() == 8.00


def test_icecream_calculate_tax():
  icecream = IceCream('Chocolate', 2, 4.0)
    
  assert icecream._name == 'Chocolate'
  assert icecream._scoop_count == 2
  assert icecream._price_per_scoop == 4.0  
  assert icecream.calculate_cost() == 8.00
  assert icecream.calculate_tax() == 0.58