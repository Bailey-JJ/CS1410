'''
Author Name: Bailey Jannuzzi
Module: combine.py
Description: Describes the Combinable Protocol
'''
from typing import Protocol, runtime_checkable

@runtime_checkable
class Combinable(Protocol):

  def can_combine(self, other: 'Combinable') -> bool:
    pass

  def combine(self, other: 'Combinable' ) -> 'Combinable':
    pass