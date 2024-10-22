from desert_item import DesertItem

class Candy(DesertItem):
  '''
  Takes parameters name, candy_weight, and price_per_pound
  '''
  def __init__(self, name = '', candy_weight = 0.0, price_per_pound = 0.0):
    super().__init__(name)
    self._candy_weight = candy_weight
    self._price_per_pound = price_per_pound
    
  @property
  def candy_weight(self):
      return self._candy_weight
  
  @candy_weight.setter
  def candy_weight(self, new_weight):
      self._candy_weight = new_weight

  @property
  def price_per_pound(self):
      return self._price_per_pound
  
  @price_per_pound.setter
  def price_per_pound(self, new_price):
      self._price_per_pound = new_price
      
  def calculate_cost(self):
    cost = self._candy_weight * self._price_per_pound
    return round(cost, 2)