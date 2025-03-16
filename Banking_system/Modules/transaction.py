# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 00:20:48 2024
@author: prath
"""
from Modules import account
from Modules.utility import validate_amount

# Deposit Fucntion

def deposit(account_number):
    print("\nEnter the amount you want to deposit, noble citizen of Constantinople.")
    
    deposit_amount = input("Amount: ").strip()
    while not validate_amount(deposit_amount):
        print("Please Enter a Valid Amount")
        deposit_amount = input("Amount: ").strip()
    
    deposit_amount = int(deposit_amount)  # Convert to Integer
    
    # Read Existing Account
    existing_accounts = account.read_existing_account()
    
    # Update Balance
    account_found = False
    updated_accounts = []
    
    for accounts in existing_accounts:
        if accounts[0] == account_number:  # Matching Account Number
            account_found = True
            current_balance = int(accounts[3].strip())
            new_balance = current_balance + deposit_amount
            accounts[3] = str(new_balance)
            
            print("Gold deposit successful.")
            print(f"Your new balance is {new_balance} gold coins.")
        
        updated_accounts.append(accounts)  # Update Account Info
    
    # Rewrite account.txt with updated balance
    if account_found:
        try: 
            with open("accounts.txt", "w") as file:  # Use "w" to overwrite
                for accounts in updated_accounts:
                    file.write(",".join(accounts) + "\n")
                    
            from datetime import datetime
            with open("transactions.txt", "a") as file:
                file.write(f"{account_number}, DEPOSIT, {deposit_amount}, {datetime.now().strftime('%Y-%m-%d | %H:%M:%S')}\n")
        except Exception as e:
            print(f"Error in updating account details: {e}")
    else:
        print("Account not found. Please check the account number, citizen.")



# Withdraw Function

def withdraw(account_number):
    print("\nEnter the amount you want to withdraw, noble citizen of Constantinople.")
    
    withdraw_amount = input("Amount: ").strip()
    while not validate_amount(withdraw_amount):
        print("\nPlease Enter a Valid Amount")
        withdraw_amount = input("Amount: ").strip()
    
    withdraw_amount = int(withdraw_amount)  # Convert to Integer
    
    # Read Existing Account
    existing_accounts = account.read_existing_account()
    
    # Update Balance
    account_found = False
    updated_accounts = []
    
    for accounts in existing_accounts:
        if accounts[0] == account_number:  # Matching Account Number
            account_found = True
            current_balance = int(accounts[3].strip())
            if current_balance >= withdraw_amount:
                new_balance = current_balance - withdraw_amount
                accounts[3] = str(new_balance)
            
                print("\nGold withdrawal successful.")
                print(f"Your new balance is {new_balance} gold coins.\n")
            
            else:
                print("Insufficient balance in your treasury.")
                return
        
        updated_accounts.append(accounts)  # Update Account Info
    
    # Rewrite account.txt with updated balance
    if account_found:
        try: 
            with open("accounts.txt", "w") as file:  # Use "w" to overwrite
                for accounts in updated_accounts:
                    file.write(",".join(accounts) + "\n")
                    
            from datetime import datetime
            with open("transactions.txt", "a") as file:
                file.write(f"{account_number}, WITHDRAW, {withdraw_amount}, {datetime.now().strftime('%Y-%m-%d | %H:%M:%S')}\n")
        except Exception as e:
            print(f"Error in updating account details: {e}")
    else:
        print("Account not found. Please check the account number, citizen.")



# Transaction History

def transaction_history(account_number):
    print("\n ---Transaction History--- \n")
    
    try: 
        with open("transactions.txt", "r") as file:
            transactions = file.readlines()
            found = False
            
            print(f"\nTransaction records for Account: {account_number}\n")
            print("{:<15} {:<10} {:<10} {:<20}".format("Account No.", "Type", "Amount", "Date & Time"))
            print("-" * 60)
            
            for transaction in transactions:
                if transaction.startswith(account_number):
                    record = transaction.strip().split(",")
                    print("{:<15} {:<10} {:<10} {:<20}\n".format(record[0], record[1], record[2], record[3]))
                    found = True
            
            if not found:
                print("No transaction found for this account, citizen.")
                
    except FileNotFoundError:
        print("No transaction records found.")


