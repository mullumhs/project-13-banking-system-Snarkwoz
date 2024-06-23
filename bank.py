""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: bank.py
# Description: Contains the facade class for the banking system.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from account import Account

class Bank():
    def __init__(self):
        self._accounts = []

    def check_id(self,id):
        for account in self._accounts:
            if account.get_account_id() == id:
                return True
        return False

    def add_account(self,owner,id):
        if self.check_id(id) == True:
                print("That id already exists")
                return
        self._accounts.append(owner,id,0.00)

    def del_account(self,id):
        for i in self._accounts:
            if self.check_id(id) == True:
                del self._accounts[i]
                return

    def deposit(self,id,amount):
        if self.check_id(id) == True:
            Account.deposit(amount)

    def withdraw(self,id,amount):
        if self.check_id(id) == True:
            Account.withdraw(amount)
    
