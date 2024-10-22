from sundae import Sundae

def test_sundae_init_default():
  sundae = Sundae()
    
  assert sundae._name == ''
  assert sundae._scoop_count == 0
  assert sundae._price_per_scoop == 0.0
  assert sundae._topping_name == ''
  assert sundae._topping_price == 0.0
    
    
def test_sundae_init_nominal():
  sundae = Sundae('Chocolate Sundae', 2, 3.0, 'Oreo Bits', 4.0)
    
  assert sundae._name == 'Chocolate Sundae'
  assert sundae._scoop_count == 2
  assert sundae._price_per_scoop == 3.0
  assert sundae._topping_name == 'Oreo Bits'
  assert sundae._topping_price == 4.0  
    
def test_sundae_getters():
  sundae = Sundae('Chocolate Sundae', 2, 3.0, 'Oreo Bits', 4.0)
    
  assert sundae.name == 'Chocolate Sundae'
  assert sundae._scoop_count == 2
  assert sundae._price_per_scoop == 3.0
  assert sundae._topping_name == 'Oreo Bits'
  assert sundae._topping_price == 4.0
    
def test_sundae_setters():
  sundae = Sundae('Chocolate Sundae', 2, 3.0, 'Oreo Bits', 4.0)
    
  sundae.name = 'Vanilla Sundae'
  sundae.scoop_count = 3
  sundae.price_per_scoop = 4.0
  sundae.topping_name = 'Sprinkles'
  sundae.topping_price = 5.0
    
  assert sundae.name == 'Vanilla Sundae'
  assert sundae._scoop_count == 3
  assert sundae._price_per_scoop == 4.0
  assert sundae._topping_name == 'Sprinkles'
  assert sundae._topping_price == 5.0


def test_sundae_calculate_cost():
  sundae = Sundae('Chocolate Sundae', 2, 3.0, 'Oreo Bits', 4.0)
    
  assert sundae._name == 'Chocolate Sundae'
  assert sundae._scoop_count == 2
  assert sundae._price_per_scoop == 3.0
  assert sundae._topping_name == 'Oreo Bits'
  assert sundae._topping_price == 4.0  
  assert sundae.calculate_cost() == 10.00


def test_sundae_calculate_tax():
  sundae = Sundae('Chocolate Sundae', 2, 3.0, 'Oreo Bits', 4.0)
    
  assert sundae._name == 'Chocolate Sundae'
  assert sundae._scoop_count == 2
  assert sundae._price_per_scoop == 3.0
  assert sundae._topping_name == 'Oreo Bits'
  assert sundae._topping_price == 4.0  
  assert sundae.calculate_cost() == 10.00
  assert sundae.calculate_tax() == 0.72