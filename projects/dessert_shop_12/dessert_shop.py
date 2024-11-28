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
from dessert_item import DesertItem
from receipt import make_receipt
from payment import PayType, Payable
from customer import Customer
from typing import Dict

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
  Defines the DesertShop class. Contains functions necessary to gather user input. 
  '''
  def __init__(self):
    self._customer_dict: Dict[str, Customer] = {}

  def add_order(self, name: str, order: Order):
    '''
    Takes a string input, checks if customer exists in the customer dictionary. If customer exists, order is added to the Customer's
    order history. If customer does not exist, a new customer key and value is created and added to dictionary, then order
    is added to the new customer's order history.
    '''
    if name in self._customer_dict.keys():
      customer = self._customer_dict[name]
      self._customer_dict[name].add_history(order)
    else:
      customer = Customer(name)
      self._customer_dict[name] = customer
      customer.add_history(order)
    return customer


  def list_customer_orders(self):
    '''
    Takes all customers from self._customer_dict, and prints out each customer's order history.
    '''
    for customer in self._customer_dict.values():
      print(customer)
      print(customer.get_history())


  def user_prompt_candy(self):
    '''
    Validates user input for the Candy class.
    '''
    name = input("Enter the type of candy: ")
    weight = validate('Enter the candy weight (in lbs): ', 'Weight must be positive number.', 'float')
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
  

def prompt_user_pay_type():
  valid = False
  while not valid:
    answer = input("Enter payment type: \nCASH \nCARD \nPHONE \n ")

    for type in PayType:
      if answer.upper() == type.name:
        return type
        valid = True

    if not valid:
      print("Error. Invalid datatype used.")


def prompt_user_name():
  valid = False
  while not valid:
    customer_name = input('Enter customer name: ').capitalize()
    
    if customer_name.isalpha():
      return customer_name
      valid = True
    
    if not valid:
      print('Error. Invalid name.')


def main():
  shop = DesertShop()
  new_order = True

  while new_order:
    print('\nNew order:\n') 
    order = Order()
    
    order.add(Candy('Candy Corn', 1.5, 0.25))
    order.add(Candy('Gummy Bears', 0.25, 0.35))
    order.add(Cookie('Chocolate Chip', 6, 3.99))
    order.add(Cookie('Chocolate Chip', 3, 3.99))
    order.add(IceCream('Pistachio', 2, 0.79))
    order.add(Sundae('Vanilla', 3, 0.69, 'Hot Fudge', 1.29))
    order.add(Cookie('Oatmeal Raisin', 2, 3.45))
    
    # boolean done = false
    done: bool = False
    skip = False
    # build the prompt string once
    prompt = '\n'.join([ '\n',
            '1: Candy',
            '2: Cookie',            
            '3: Ice Cream',
            '4: Sundae',
            '5: Admin Module',
            '\nWhat would you like to add to the order? (1-5, Enter for done): '
      ])

    while not done:
      choice = input(prompt)
      match choice:
        case '':
          done = True
          break
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
        case '5':
          finished = False
          prompt2 = '\n'.join([ '\n',
            '1: Shop Customer List',
            '2: Customer Order History',            
            '3: Best Customer',
            '4: Exit Admin Module',
            '\n(Choose options 1-3, enter 4 to exit.): '
            ])
          while not finished:
            admin_choice = input(prompt2)
            match admin_choice:
              case '4':
                complete_order = input("Do you want to continue current order? (Y to exit and continue current order, or type any other key to exit and end existing order.) ")
                if complete_order.upper() == 'Y':
                  new_order = True
                  done = False
                  print('\nExiting Admin Module.\n')
                else:
                  new_order = False
                  skip = True
                  done = True
                  print('\nExiting Admin Module and ending order.\n')
                finished = True
              case '1':
                for customer in shop._customer_dict.values():
                  print(f'Customer Name: {customer._customer_name}\nCustomer ID: {customer._customer_id}\n')
              case '2':
                choice = input("\n1: Complete Customer Order History\n2: Specific Customer Order History\nSelect a history option: ")
                if choice == '2':
                  customer_search = prompt_user_name()
                  if customer_search in shop._customer_dict.keys():
                    customer = shop._customer_dict[customer_search]
                    print(f"\n----- {customer._customer_name}'s Order History -----\n")
                    print(customer)
                    customer.get_history()
                  else:
                    print(f"{customer_search} cannot be found.")
                elif choice == '1':
                  print('\n\nAll Customer Orders:\n-------------------------------------------------------')
                  shop.list_customer_orders()
                else:
                  print('Invalid Input. Enter 1 or 2.')

              case '3':
                best_customer = None
                max_orders = 0
                amount_spent = 0

                for name, customer in shop._customer_dict.items():
                  total_spent = 0
                  number_orders = len(customer._order_history)
                  for order in customer._order_history:
                    total_spent += round((order.order_cost() + order.order_tax()), 2)
                  if number_orders > max_orders:
                    max_orders = number_orders
                    best_customer = name
                    amount_spent = total_spent

                if best_customer:
                  print(f"The best customer is: {best_customer}. Their total number of orders is {max_orders} and they have spent a total of ${amount_spent}.")
                else:
                  print('No best customer yet.')
              case _:
                print('Invalid response:  Please enter a choice from the menu (1-4).')

        case _:            
          print('Invalid response:  Please enter a choice from the menu (1-5) or Enter.')

    if not skip:
      customer_name = prompt_user_name()

      pay = prompt_user_pay_type()
      order.set_pay_type(pay)

      order.sort()
      print(order)

      shop.add_order(customer_name, order)

      end_order = input('\nWould you like to begin a new order? (Y to continue, type any other key to quit.) ')
      if end_order.upper() == 'Y':
        new_order = True
      else:
        new_order = False
        print(f'\nThanks for coming in {customer_name}! Enjoy your desserts!\n')


if __name__ == "__main__":
  main()