from entities import *
from account import *
from bank import *
from errors import *

user_names = []
accounts = []
currency = ["BGN", "EUR", "USD", "JPN"]
acc_type = ["CURRENT", "SAVINGS", "CREDIT"]

class Menu:
    def print_menu(self):
        print("1. Create new user")
        print("2. Create account for existing user")
        print("3. List users")
        print("4. List accounts for users")
        print("5. Deposit for users")
        print("6. Withdraw")
        print("7. Exit")

def command_new_user(self, account, name, EGN):
    return account, name, EGN

def command_new_account(self, balance, currency, acc_type, IBAN):
    return balance, currency, acc_type, IBAN

def command_print_users(self):
    pass

def command_print_accounts(self):
    pass

def command_withdraw(self):
    pass

def run(self):
    while True:
        Menu.print_menu(self)

        choise = input("Choose an option from the menu: ")
        try:
            if choise == "1":
                name = input("Enter name: ")
                if len(name) < 4:
                    raise InvalidName("Invalid name")
                if name.isdigit():
                    raise InvalidDataFormat("Moje samo bukvi")
                EGN = input("Enter EGN")
                if len(EGN) < 10:
                    raise InvalidEGN
                





