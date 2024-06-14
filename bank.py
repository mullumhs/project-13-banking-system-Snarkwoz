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

    def add_account(self,):

    
    def transfer(self):
        transfer_id = input("Type the id of the account you want to transfer to: ")
        if isinstance(transfer_id,int):
            for account_id in 