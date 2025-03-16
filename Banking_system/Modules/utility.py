# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 00:21:21 2024

@author: prath
"""

import hashlib
import random
import string

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def write_file(filename, data):
    with open(filename, 'a') as file:
        file.write(data + "\n")

def validate_amount(amount):
    return amount.isdigit() and int(amount) > 0

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def generate_backup_code(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    return ''.join(random.choice(characters) for _ in range(length))
