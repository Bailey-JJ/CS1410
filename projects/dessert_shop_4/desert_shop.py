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
import receipt

class DesertShop():
  '''
  Defines the DesertShop class. Contains functions necessary to
  gather user input. 
  '''

  def user_prompt_candy(self):
    '''
    Validates user input for the Candy class.
    '''
    while True:
      try:
        name = input("Enter the type of candy: ")
        if name.replace(" ", "").isalpha():
          break
        else:
          print("Enter a valid Candy name.")
      except ValueError:
        print("Enter a valid Candy name.")

    while True:
      try:
        weight = float(input("Enter the candy weight (in pounds): "))
        if weight >= 0:
          break
        else:
          print("Weight must be a positive number.")
      except ValueError:
        print("Enter valid numbers for weight.")
    
    while True:
      try:
        price = float(input("Enter the candy price per pound: "))
        if price >= 0:
          break
        else:
          print("Price must be a positive number.")
      except ValueError:
        print("Enter valid numbers for price.")

    return Candy(name, weight, price)


  def user_prompt_cookie(self):
    '''
    Validates user input for the Cookie class.
    '''
    while True:
      try:
        name = input("Enter the type of Cookie: ")
        if name.replace(" ", "").isalpha():
          break
        else:
          print("Enter a valid Cookie name.")
      except ValueError:
        print("Enter a valid Cookie name.")

    while True:
      try:
        quantity = int(input("Enter the quantity purchased: "))
        if quantity >= 0:
          break
        else:
          print("Quantity must be a positive number.")
      except ValueError:
        print("Enter valid numbers for quantity.")
    
    while True:
      try:
        price = float(input("Enter the price per dozen: "))
        if price >= 0:
          break
        else:
          print("Price must be a positive number.")
      except ValueError:
        print("Enter valid numbers for price.")

    return Cookie(name, quantity, price)


  def user_prompt_icecream(self):
    '''
    Validates user input for the IceCream class.
    '''
    while True:
      try:
        name = input("Enter the type of Icecream: ")
        if name.replace(" ", "").isalpha():
          break
        else:
          print("Enter a valid Icecream name.")
      except ValueError:
        print("Enter a valid Icecream name.")

    while True:
      try:
        scoops = int(input("Enter the number of scoops: "))
        if scoops >= 0:
          break
        else:
          print("Number of scoops must be a positive number.")
      except ValueError:
        print("Enter valid number of scoops.")
    
    while True:
      try:
        price = float(input("Enter the price per scoop: "))
        if price >= 0:
          break
        else:
          print("Price must be a positive number.")
      except ValueError:
        print("Enter valid numbers for price.")

    return IceCream(name, scoops, price)
  

  def user_prompt_sundae(self):
    '''
    Validates user input for the Sundae class.
    '''
    while True:
      try:
        name = input("Enter the type of Icecream: ")
        if name.replace(" ", "").isalpha():
          break
        else:
          print("Enter a valid Icecream name.")
      except ValueError:
        print("Enter a valid Icecream name.")

    while True:
      try:
        scoops = int(input("Enter the number of scoops: "))
        if scoops >= 0:
          break
        else:
          print("Number of scoops must be a positive number.")
      except ValueError:
        print("Enter valid number of scoops.")
    
    while True:
      try:
        scoop_price = float(input("Enter the price per scoop: "))
        if scoop_price >= 0:
          break
        else:
          print("Price must be a positive number.")
      except ValueError:
        print("Enter valid numbers for price.")

    while True:
      try:
        topping = input("Enter the topping: ")
        if topping.replace(" ", "").isalpha():
          break
        else:
          print("Enter a valid topping name.")
      except ValueError:
        print("Enter a valid topping name.")

    while True:
      try:
        price_of_topping = float(input("Enter the price for the topping: "))
        if price_of_topping >= 0:
          break
        else:
          print("Price must be a positive number.")
      except ValueError:
        print("Enter valid numbers for price.")

    return Sundae(name, scoops, scoop_price, topping, price_of_topping)
  

def main():
  shop = DesertShop() 
  order = Order()
  data = [[ "Name" , "Item Cost", "Tax" ]]
  
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
  
  receipt_list = [[item._name, f"${item.calculate_cost():.2f}", f"${item.calculate_tax():.2f}"] for item in order._order]

  for row in receipt_list:
    data.append(row)

  data.append([ "Order Subtotal", f"${order.order_cost():.2f}", f"${order.order_tax():.2f}"])
  data.append([ "Order Total", "", f"${(order.order_cost() + order.order_tax()):.2f}"])
  data.append([ "Total Items in the Order", "", len(order)])

  receipt.make_receipt(data)


if __name__ == "__main__":
  main()