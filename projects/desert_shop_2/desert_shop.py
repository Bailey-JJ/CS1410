from candy import Candy
from cookie import Cookie
from ice_cream import IceCream
from sundae import Sundae 
from order import Order

def main():
   o = Order()

   o.add(Candy("Candy Corn", 1.5, 0.25))
   o.add(Candy("Gummy Bears", 0.25, 0.35))
   o.add(Cookie("Chocolate Chip", 6, 3.99))
   o.add(IceCream("Pistachio", 2, 0.79))
   o.add(Sundae("Vanilla", 3, 0.69, "Hot Fudge", 1.29))
   o.add(Cookie("Oatmeal Raisin", 2, 3.45))

   print(o)

if __name__ == "__main__":
   main()