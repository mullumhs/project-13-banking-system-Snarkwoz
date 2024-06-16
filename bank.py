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
    
    def transfer(self,amount,id1,id2):
        if self.check_id(id1) == True:
            if self.check_id(id2) == True:
                