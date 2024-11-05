'''
Author Name: Bailey Jannuzzi
Module: desert_shop.py
Description: Describes the DesertShop class and runs main(), which takes an user
input and prints an order receipt.
'''
from candy import Candy
from cookie import Cookie
from ice_cream import IceCream
from sundae import Sundae 
from order import Order
from desert_item import DesertItem
from receipt import make_receipt

def validate(question, warning, type):
  while (True): 
    try:
      if type == 'int':
        answer = int(input(question))
      elif type == 'float':
        answer = float(input(question))
      else:
        print('Error. Invalid type.')
        return None
      return answer
    except:
      print(warning + '\n')

class DesertShop():
  '''
  Defines the DesertShop class. Contains functions necessary to
  gather user input. 
  '''

  def user_prompt_candy(self):
    '''
    Validates user input for the Candy class.
    '''
    name = input("Enter the type of candy: ")
    weight = validate('Enter the candy weight (in lbs)', 'Weight must be positive number.', 'float')
    price = validate('Enter the candy price per pound: ', 'Price must be a positive number.', 'float')

    return Candy(name, weight, price)


  def user_prompt_cookie(self):
    '''
    Validates user input for the Cookie class.
    '''
    name = input("Enter the type of Cookie: ")
    quantity = validate('Enter the quantity purchased: ', 'Quantity must be a positive number.', 'int')
    price = validate('Enter the price per dozen: ', 'Price must be a positive number.', 'float')

    return Cookie(name, quantity, price)


  def user_prompt_icecream(self):
    '''
    Validates user input for the IceCream class.
    '''
    name = input("Enter the type of Icecream: ")
    scoops = validate('Enter the number of scoops: ', 'Number of scoops must be a positive number.', 'int')
    price = validate('Enter the price per scoop: ', 'Price must be a positive number.', 'float')

    return IceCream(name, scoops, price)
  

  def user_prompt_sundae(self):
    '''
    Validates user input for the Sundae class.
    '''
    name = input("Enter the type of Icecream: ")
    scoops = validate('Enter the number of scoops: ', 'Number of scoops must be a positive number.', 'int')
    scoop_price = validate('Enter the price per scoop: ', 'Price must be a positive number.', 'float')
    topping = input("Enter the topping: ")
    price_of_topping = validate('Enter the price for the topping: ', 'Price must be a positive number.', 'float')

    return Sundae(name, scoops, scoop_price, topping, price_of_topping)
  

def main():
  shop = DesertShop() 
  order = Order()
  
  order.add(Candy('Candy Corn', 1.5, 0.25))
  order.add(Candy('Gummy Bears', 0.25, 0.35))
  order.add(Cookie('Chocolate Chip', 6, 3.99))
  order.add(IceCream('Pistachio', 2, 0.79))
  order.add(Sundae('Vanilla', 3, 0.69, 'Hot Fudge', 1.29))
  order.add(Cookie('Oatmeal Raisin', 2, 3.45))
  
  # boolean done = false
  done: bool = False
  # build the prompt string once
  prompt = '\n'.join([ '\n',
          '1: Candy',
          '2: Cookie',            
          '3: Ice Cream',
          '4: Sundae',
          '\nWhat would you like to add to the order? (1-4, Enter for done): '
    ])

  while not done:
    choice = input(prompt)
    match choice:
      case '':
        done = True
      case '1':            
        item = shop.user_prompt_candy()
        order.add(item)
        print(f'{item.name} has been added to your order.')
      case '2':            
        item = shop.user_prompt_cookie()
        order.add(item)
        print(f'{item.name} has been added to your order.')
      case '3':            
        item = shop.user_prompt_icecream()
        order.add(item)
        print(f'{item.name} has been added to your order.')
      case '4':            
        item = shop.user_prompt_sundae()
        order.add(item)
        print(f'{item.name} has been added to your order.')
      case _:            
        print('Invalid response:  Please enter a choice from the menu (1-4) or Enter')
  print()
  #
  #add your code below here to print the PDF receipt as the last thing in main()
  
  print(order)


if __name__ == "__main__":
  main()