from ice_cream import IceCream

class Sundae(IceCream):
  '''
  Takes parameters name, scoop_count, and price_per_scoop, topping_name, and topping_price
  '''
  def __init__(self, name = '', scoop_count = 0, price_per_scoop = 0, topping_name = '', topping_price = 0.0):
    super().__init__(name, scoop_count, price_per_scoop)
    self._topping_name = topping_name
    self._topping_price = topping_price
    
  @property
  def topping_name(self):
      return self._topping_name
  
  @topping_name.setter
  def topping_name(self, new_name):
      self._topping_name = new_name

  @property
  def topping_price(self):
      return self._topping_price
  
  @topping_price.setter
  def topping_price(self, new_price):
      self._topping_price = new_price