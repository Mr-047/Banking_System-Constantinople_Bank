# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 00:19:53 2024

@author: prath
"""
import random 
import hashlib
from Modules import transaction
import string
from Modules.utility import validate_amount, hash_password, generate_backup_code

def create_account():
    
    #Step - 1: Collect user account
    
    print("\n ---Create a new account, noble citizen of Constantinople---\n")
    user_name = input("Enter Your Name: ").strip()
    initial_deposit = input("Enter the initial deposit amount: ").strip()
    while not validate_amount(initial_deposit):
        print("Invalid amount. Please Enter the valid amount.\n")
        initial_deposit = input("Enter the initial deposit amount: ").strip()
    password = input("Enter your password: ").strip()
        
    #Step - 2: Read Existing Account
    
    existing_accounts = read_existing_account()
    
    #Step - 3: Check for duplicate name
    
    for accounts in existing_accounts:
        if accounts[1] == user_name:
            print("An account with this name already exists. Please try a different name.")
            return
    
    #Step - 4: Generate unique account number
    
    while True: 
        account_number = str(random.randint(10000000000,99999999999))
        if not any(account[0] == account_number for account in existing_accounts):
            break
    
    #Step - 5: Secure Password (hash it)
    
    hashed_password = hash_password(password)
    
    #Step - Generate a Backup Code
    
    backup_code = generate_backup_code()
    
    #Step - 6: Save details to accounts.txt
    
    try:
        with open("accounts.txt", "a") as file: 
            file.write(f"{account_number},{user_name},{hashed_password},{initial_deposit},{backup_code}\n")
            print(f"\nAccount created successfully! Your account number is: {account_number}\n")
            print(f"Your backup code is: {backup_code}. Save this code to reset your password if you forget it, citizen.")
    except Exception as e:
            print(f"Error saving account details: {e}")

def read_existing_account():
    accounts = []
    try:
        with open("accounts.txt", "r") as file:
            for line in file:
                accounts_details = line.strip().split(",")
                accounts.append(accounts_details)
    except FileNotFoundError:
        #If the file doesn't exist yet, return an empty list
        pass
    return accounts

def login():
    print("\n ---Enter your details to log in, noble citizen of Constantinople--- \n")
    
    #Step - 1: Input of Exisitng Account Credentials
    
    account_number = input("Enter your Account Number: ").strip()
    password = input("Enter your password: ").strip()
    
    #Step - 2: Read Existing Account
    
    existing_accounts = read_existing_account()
    
    #Step - 3: Matching Credentials
    
    account_found = False
    password_matched = False 
    
    for accounts in existing_accounts:
        if accounts[0] == account_number: #Matching Account Number
            account_found = True
            
            #Hash password for validation
            
            hashed_password = hash_password(password)
            
            if accounts[2].strip() == hashed_password.strip(): #Verify Passowrd
                print("\n ---Login Successful---")
                print(f"\nWelcome, {accounts[1]}") #Display Name
                print(f"Your current balance is {accounts[3]} gold coins.\n")
                password_matched = True
                
                #Transactions Options
                print("Would you like to continue into the transaction section, citizen?")
                option = input("Y/N - ").strip()
                
                
                if option == "Y" or "y":
                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Transaction History\n")
                    
                    choice = input("Choose the option: ")
                    
                    if choice == "1":
                        transaction.deposit(account_number)
                    elif choice == "2":
                        transaction.withdraw(account_number)
                    elif choice == "3":
                         transaction.transaction_history(account_number)
                    else:
                        print("Enter a valid option, citizen.")
                break
            else:
                print("\nIncorrect password. Please try again, citizen.\n")
                
    if not account_found:
        print("\nAccount not found, citizen.\n")
    
    
def delete_account():
    print("\n ---It's sad to see you leaving us, noble citizen of Constantinople--- \n")
    print("Confirm to close your account, citizen.")
    option = input("Y/N - ").strip()
    
    if option == "Y" or "y":
        
        #Step - 1: Logging-In for Account Closure
        
        account_number = input("\nEnter Your Account Number: ").strip()
        password = input("Enter your Password: ").strip()
        
        #Step - 2: Read Existing Account
        
        existing_accounts = read_existing_account()
        
        #Step - 4: Matching Credentials
        
        account_found = False
        updated_accounts = []
        
        for accounts in existing_accounts:
            if accounts[0] == account_number: #Matching Account Number
            
                hashed_password = hash_password(password)
                
                if accounts[2].strip() == hashed_password.strip(): #Verify Passowrd
                    print(f"\nAccount {account_number} deleted successfully.\n")  
                    account_found = True
                else:
                    print("Incorrect password. Please try again, citizen.")
                    updated_accounts.append(accounts)
                
            else:
                updated_accounts.append(accounts)
                
        if account_found:
            with open("accounts.txt", "w") as file:
                for accounts in updated_accounts:
                    file.write(",".join(accounts) + "\n")
        else:
            print("Account not found, citizen.")
            
    elif option == "N" or "n":
        print("Thanks for reconsidering, citizen.")
        
    else:
        print("Invalid option. Please enter Y or N, citizen.")






