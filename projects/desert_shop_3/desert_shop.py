from candy import Candy
from cookie import Cookie
from ice_cream import IceCream
from sundae import Sundae 
from order import Order
from desert_item import DesertItem
import receipt

def main():
  order = Order()
  data = [[ "Name" , "Item Cost", "Tax" ]]
  
  order.add(Candy("Candy Corn", 1.5, 0.25))
  order.add(Candy("Gummy Bears", 0.25, 0.35))
  order.add(Cookie("Chocolate Chip", 6, 3.99))
  order.add(IceCream("Pistachio", 2, 0.79))
  order.add(Sundae("Vanilla", 3, 0.69, "Hot Fudge", 1.29))
  order.add(Cookie("Oatmeal Raisin", 2, 3.45))

  receipt_list = [[item._name, f"${item.calculate_cost():.2f}", f"${item.calculate_tax():.2f}"] for item in order._order]

  for row in receipt_list:
    data.append(row)

  data.append([ "Order Subtotal", f"${order.order_cost():.2f}", f"${order.order_tax():.2f}"])
  data.append([ "Order Total", "", f"${order.order_cost() + order.order_tax()}"])
  data.append([ "Total Items in the Order", "", len(order)])

  receipt.make_receipt(data)


if __name__ == "__main__":
  main()