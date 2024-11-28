'''
Author Name: Bailey Jannuzzi
Module: payment.py
Description: 
'''
from enum import Enum
from typing import Protocol

class PayType(Enum):
  CASH = 'CASH'
  CARD = 'CARD'
  PHONE = 'PHONE'


class Payable(Protocol):

  def get_pay_type(self) -> PayType:
    pass

  def set_pay_type(self, new_payment_method = PayType) -> None:
    pass
