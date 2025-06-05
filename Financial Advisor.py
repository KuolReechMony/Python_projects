# time = date and time

# amount

# physical account = savings(long-term, emergency), annual, debit card(checking account)

# expenses and incomes =
# [(housing and meals), IOM loan, phone bill, int phone bill, misc expenses]
# [salaries]

# Description

from datetime import datetime

ReccuringPayments = []

Subscriptions = {
    "Phone Bill": [37.66, [13, 15], True], # Amounts, when due{strat date, end date}, autopay
    "Internationa Phone Bill": [5, [1, 28], False],
    "IOM Loan": [42, [26, 1], False]
}

DebitCard = {
"Balance": 0,
"DateAndTime": 0,
"Goals": 0,
"Duration": 0
}

SavingsAccount = {
"Balance": 0,
"DateAndTime": 0,
"Goals": 0,
"Duration": 0
}



def DateAndTime():
    return str(datetime.now())[:-10]

def CreateReccuringPayment():
    try:
        Service = input("Subscription:  ")
        Cost = int(input("Reccurying cost:  "))
        StartDate = int(input("Earliest payment date:  "))
        EndDate = int(input("Latest payment date:  "))
        Automated = int(input("Automatic payment set up: 0 - NO, 1 - YES:  "))
    except (KeyboardInterrupt, TypeError):
        pass
    else:
        match (Automated):
            case 0:
                Subscriptions[Service] = [Cost, [StartDate, EndDate], False]
            case 1:
                Subscriptions[Service] = [Cost, [StartDate, EndDate], True]

def AccessRecurringPaymeny(service):
    return f"Subscription->{service}; cost->{Subscriptions[service][0]}; Due on->{Subscriptions[service][0][1]}; AutoPayment->{Subscriptions[service][2]}"


def RemoveReccuringPayment(service):
    confirm = input(f"Verifying the deletion of this subscription->{service}; that costs->{Subscriptions[service][0]}")
    if confirm.lower() == "yes":
        Subscriptions.pop(service)


print(CreateReccuringPayment())