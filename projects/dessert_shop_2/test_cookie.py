from cookie import Cookie

def test_cookie_init_default():
  cookie = Cookie()
    
  assert cookie._name == ''
  assert cookie._cookie_quantity == 0
  assert cookie._price_per_dozen == 0.0
    
    
def test_cookie_init_nominal():
  cookie = Cookie('Chocolate', 2, 4.0)
    
  assert cookie._name == 'Chocolate'
  assert cookie._cookie_quantity == 2
  assert cookie._price_per_dozen == 4.0  
    
def test_cookie_getters():
  cookie = Cookie('Chocolate', 2, 4.0)
    
  assert cookie.name == 'Chocolate'
  assert cookie._cookie_quantity == 2
  assert cookie._price_per_dozen == 4.0
    
def test_cookie_setters():
  cookie = Cookie('Chocolate')
    
  cookie.name = 'Pumpkin'
  cookie.cookie_quantity = 3
  cookie.price_per_dozen = 5.0
    
  assert cookie.name == 'Pumpkin'
  assert cookie._cookie_quantity == 3
  assert cookie._price_per_dozen == 5.0