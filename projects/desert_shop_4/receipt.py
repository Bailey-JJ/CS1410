'''
Author Name: Bailey Jannuzzi
Module: receipt.py
Description: Describes the Receipt class, defines the function
make_receipt() which takes an order list and prints a receipt to an
output file, which has the default 'receipt.pdf'.
Also contains a test data set named 'DATA', which can be run from this
module.
'''
from order import Order
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

def make_receipt(input, out_file_name = "receipt.pdf"):
  '''
  Takes the list made in the Order class, generates a pdf file receipt detailing
  the cost and tax for each item, and then lists the subtotals, total, and
  total number of items ordered.
  '''
  receipt = []

  for row in input:
    receipt.append(row)

  # creating a Base Document Template of page size A4
  pdf = SimpleDocTemplate( out_file_name , pagesize = A4)

  # standard stylesheet defined within reportlab itself
  styles = getSampleStyleSheet()

  # fetching the style of Top level heading (Heading1)
  title_style = styles[ "Heading1" ]

  # 0: left, 1: center, 2: right
  title_style.alignment = 1

  # creating the paragraph with
  # the heading text and passing the styles of it
  title = Paragraph( "GeeksforGeeks" , title_style )

  # creates a Table Style object and in it,
  # defines the styles row wise
  # the tuples which look like coordinates
  # are nothing but rows and columns
  style = TableStyle(
    [
      ( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.black ),
      ( "GRID" , ( 0, 0 ), ( 3, (len(receipt) - 4)), 1 , colors.black ),
      ( "BACKGROUND" , ( 0, 0 ), ( 3, 0 ), colors.gray ),
      ( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.whitesmoke ),
      ( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ),
      ( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.beige ),
    ]
  )

  # creates a table object and passes the style to it
  table = Table( receipt , style = style )

  # final step which builds the
  # actual pdf putting together all the elements
  pdf.build([ title , table ])

def main():
  DATA = [
    [ "Date" , "Name", "Subscription", "Price (Rs.)" ],
    [
      "16/11/2020",
      "Full Stack Development with React & Node JS - Live",
      "Lifetime",
      "10,999.00/-",
    ],
    [ "16/11/2020", "Geeks Classes: Live Session", "6 months", "9,999.00/-"],
    [ "Sub Total", "", "", "20,9998.00/-"],
    [ "Discount", "", "", "-3,000.00/-"],
    [ "Total", "", "", "17,998.00/-"],
  ]
  make_receipt(DATA, 'receipt.pdf')

if __name__ == "__main__":
  main()