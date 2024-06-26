""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: account.py
# Description: Contains the base Account class and derived classes.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class Account():
    
    def __init__(self,account_id,account_owner,balance):
        self._account_id = account_id
        self._account_owner = account_owner
        self._balance = float(balance)
    
    def get_account_id(self):
        return f"Account id is {self._account_id}"
    def get_account_owner(self):
        return f"Account owner is {self._account_owner}"
    def get_balance(self):
        return f"Balance - ${float(self._balance):.2f}"
    
    def set_account_id(self,new_id):
        if isinstance(new_id,int):
            self._account_id = new_id
        else:
            raise ValueError("Invalid id")
    def set_account_name(self,new_name):
        if isinstance(new_name,str):
            self._account_owner = new_name
        else:
            raise ValueError("Invalid name")
    def set_balance(self):
        if isinstance(self._balance,float):
            return
        else:
            raise ValueError("Balance is not a number")
    
    def deposit(self,amount):
        if isinstance(amount,float):
            amount = float(amount)
            if amount > 0:
                self._balance += amount
                return
        raise ValueError("Deposit must be a number greater than zero")
    def withdraw(self,amount):
        if isinstance(amount,float):
            amount = float(amount)
            if amount > 0:
                self._balance = self._balance-amount
                return
        raise ValueError("Withdrawal must be a number greater than zero")
