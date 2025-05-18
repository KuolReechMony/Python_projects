# 2 bank actual bank account: savings, checking
# 4 way split money account: long-term savings, debit card, total financial year expenditure, emergency

# expenses = housing and meals, IOM, phone bill, int phone bill, shopping
# income = 
# Taxes estimate
# Salary tracking
# 

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

def Date_and_time():
    x = datetime.now()
    return x.strftime('%d-%b-%Y: %I:%M %p')

def Initialize(timestamp):
    pass

def Accounts(timestamp):
    task = input('Options: 1 - Physical Accounts balances, 2 - Planning accounts balances, 3 - Expenses history, 4 - Income history, 5 - Transaction history:   ')
    try:
        task = int(task)
        match task:
            case 1: # Physical accounts balances
                return (timestamp, 'First Financial Checking Account: ' + str(Physical_accounts['First financial checking']) + str('$'), 'First Financial Savings Account: ' + str(Physical_accounts['First financial savings']) + str('$'))
            case 2: # Planning accounts balances
                return (timestamp, 'Long term savings: ' + str(Planning_accounts['Long-term savings']) + str('$'), 'Annual Expenditure: ' + str(Planning_accounts['Annual expenditure']) + str('$'), 'Emergency funds: ' + str(Planning_accounts['Emergency funds']) + str('$'), 'Debit Card: ' + str(Planning_accounts['Debit card']) + str('$'))
            case 3: # Expenses history
                pass
            case 4: # Income history
                pass
            case 5: # Transaction history
                pass
    except ValueError or KeyboardInterrupt:
        main(1)
    
def Expenses_tracker(timestamp, choice):
    global Transaction_history
    transcation = []
    transcation.append(timestamp)
    if choice.upper() == 'YES':
        amount = input('Amount: ')
        expense_category = input('[Housing? IOM? Phone? International? Misc? ]')
        actual_account = input('[Checking? Savings? ]')
        planning_category = input('[Savings? Debit? Expenditure? Emergency? ]')
        description = input('Description: ')
        try:
            amount = int(amount)
            transcation.append(amount)
            match actual_account.lower():
                case 'savings':
                    Physical_accounts['First financial savings'] -= amount
                    transcation.append(actual_account.lower())
                case 'checking':
                    Physical_accounts['First financial checking'] -= amount
                    transcation.append(actual_account.lower())
            
            match planning_category.lower():
                case 'savings':
                    Planning_accounts['Long-term savings'].append[timestamp, amount, description]
                case 'debit':
                    Planning_accounts['Debut card'].append[timestamp, amount, description]
                case 'expenditure':
                    Planning_accounts['Annual expenditure'].append[timestamp, amount, description]
                case 'emergency':
                    Planning_accounts['Emergency funds'].append[timestamp, amount, description]

            transcation.append(description)
            transcation.append(expense_category.lower())
            transcation.append(actual_account.lower())
            transcation.append(planning_category.lower())

            match expense_category.lower():
                case 'housing':
                    Expenses['Housing and meals'].append(timestamp, amount, description)
                case 'iom':
                    Expenses['IOM Loan'].append(timestamp, amount, description)
                case 'phone':
                    Expenses['Phone bill'].append(timestamp, amount, description)
                case 'international':
                    Expenses['International phone bill'].append(timestamp, amount, description)
                case 'misc':
                    Miscellaneous_expenses[str(amount)] = [timestamp, amount, description]

            Transaction_history.append[transcation]
        
        except ValueError and KeyboardInterrupt:
            Expenses_tracker(timestamp, None)

def main(menu_option):
    try:
        menu_option = int(menu_option)
        match menu_option:
            case 0: # First time set up/ New financial year/ New academic year
                Initialize(Date_and_time())
            case 1: # Account information
                print(Accounts(Date_and_time()))
            case 2:
                Expenses_tracker(Date_and_time(), input("press yes: "))
                pass
            case 3:
                pass
    except ValueError or KeyboardInterrupt:
        print('Wrong input!')
        main(input("Menu options: 0 - Set up, 1 - Account, 2 - Income, 3 - Expenses:  "))
    
main(input("Menu options: 0 - Set up, 1 - Account, 2 - Income, 3 - Expenses:  "))

