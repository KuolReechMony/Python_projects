# time = date and time

# amount

# physical account = savings(long-term, emergency), annual, debit card(checking account)

# expenses and incomes =
# [(housing and meals), IOM loan, phone bill, int phone bill, misc expenses]
# [salaries]

# Description

import os
from datetime import datetime

Physical_accounts = {
    'First financial savings': 0,
    'First financial checking': 0
}

Planning_accounts = {
    'Long-term savings': 0,
    'Debit card': 0,
    'Annual expenditure': 0,
    'Emergency funds': 0
}

Expenses = {
    'Housing and meals': [],
    'IOM Loan': [],
    'Phone bill': [],
    'International phone bill': []
}

Transaction_history = []

Miscellaneous_expenses = {}

Income_sources = {}


def Initialize(timestamp):
    pass


def ID_gen(Physical_accounts, Category):
    current_time = str(datetime.now()) 
    id = f"Time: {current_time[11:16]}, Date: {current_time[5:10]}; "
    match Physical_accounts.lower():
        case 'short':
            id = id + "SH"
        case 'medium':
            id = id + "MD"
        case 'long':
            id = id + "LO"

    match Category.lower():
        case 'expense':
            id = id + 'XP'
        case 'income':
            id = id + 'IN'
    
    return id

class Transactions:
    def __init__(self, amount, account, category):
        self.amount = amount
        self.account = account
        self.category = category
        self.id = self.get_id(account, category)

    def get_id(self, accounts, category):
        current_time = str(datetime.now()) 
        id = f"Time: {current_time[11:16]}, Date: {current_time[5:10]}; "
        match accounts.lower():
            case 'short':
                id += "SH"
            case 'medium':
                id += "MD"
            case 'long':
                id += "LO"

        match category.lower():
            case 'expense':
                id += 'XP'
            case 'income':
                id += 'IN'
    
        return id
    

try:
    amount = float(input('Which amount: '))
    account = input('Which account: ')
    category = input('What category: ')
except (ValueError, KeyboardInterrupt):
    pass
else:
    First = Transactions(amount, account, category)

try:
    print(First.amount, First.account, First.category)
except NameError:
    print('Error')

