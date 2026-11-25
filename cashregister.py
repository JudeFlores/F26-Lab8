# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Jude Flores
# Date:November 25th, 2026
# Purpose: models the cash register in super markets.

# TO DO 1: Complete the functions below according to given instructions. 

class CashRegister:
    def __init__(self):
        self._itemCount = 0
        self._totalPrice = 0.0
        self._undoPrice = []
              
    def addItem(self, price):
        self._itemCount = self._itemCount + 1
        self._totalPrice = self._totalPrice + price
        self._undoPrice.append(price)
        
    def getTotal(self):
        return f"Price: {self._totalPrice}"
    
    def getCount(self):
        return f"Count: {self._itemCount}"
    
    def clear(self):
        self._itemCount = 0
        self._totalPrice = 0.0
        self._undoPrice.clear()
        
    #complete the following undo() method
    def undo(self):
        self._itemCount -= 1
        self._totalPrice -= self._undoPrice[len(self._undoPrice)-1]
        self._undoPrice.pop(len(self._undoPrice)-1)
        

