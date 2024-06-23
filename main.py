""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: main.py
# Description: Contains the user interface for the banking system.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from account import Account
from bank import Bank
import random

def add_account(bank):
    owner = input("Name of owner: ")
    new_id = random.randint(100,999)
    print(new_id)
    bank.add_account(owner,new_id)

def del_account(bank):
    print("")

def deposit(bank):
    amount = input("How much $: ")
    id = input("Input id: ")

def withdraw(bank):
    amount = input("How much $: ")
    id = input("Input id: ")


def main():
    bank = Bank()
    while True:
        choice = input("1 to create account, 2 to delete account, 3 to desposit, 4 to withdraw, 5 to exit: ")
        if choice == "1":
            add_account(bank)
        if choice == "2":
            del_account(bank)
        if choice == "3":
            deposit(bank)
        if choice == "4":
            withdraw(bank)
        if choice == "5":
            break

if __name__ == "__main__":
    main()