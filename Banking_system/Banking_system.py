# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 00:03:46 2024

@author: prath
"""
from Modules import account

print("\nWelcome, noble citizen of Constantinople!\n")
print("Initializing the Constantinople Banking System...")

def display_main_menu():
    print("\nConstantinople Banking System")
    print("1. Create an Account")
    print("2. Log In")
    print("3. Close an Account")
    print("4. Exit\n")

def main_menu(): 
    while True: 
        display_main_menu()
        choice = input("Please enter your choice, citizen: ")

        if choice == "1": 
            account.create_account()
        elif choice == "2": 
            account.login()
        elif choice == "3":
            account.delete_account()
        elif choice == "4": 
            print("\nThe Constantinople Banking System is shutting down. Farewell, noble citizen!")
            break
        else:
            print("Invalid choice. Please try again, citizen.")

if __name__ == "__main__": 
    print("Launching Main Menu...")
    main_menu()
