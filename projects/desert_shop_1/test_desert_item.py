from desert_item import DesertItem

def test_desertitem_init_default():
  desert = DesertItem()
    
  assert desert._name == ''
    
    
def test_desertitem_init_nominal():
  desert = DesertItem('Gushers')
    
  assert desert._name == 'Gushers'
    
    
def test_desertitem_getters():
  desert = DesertItem('Gushers')
    
  assert desert.name == 'Gushers'
    
    
def test_desertitem_setters():
  desert = DesertItem('Gushers')
    
  desert.name = 'KitKat'
    
  assert desert._name == 'KitKat'