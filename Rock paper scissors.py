import random

options = ["rock", "paper", "scissors"]
code = 0
win_rate = 0

def inputs():
    computer_choice = options[(random.randrange(1,4))-1]
    user_choice = input("Rock, paper, scissors: ")

    if user_choice.lower() in options:
        user_choice = user_choice.lower()
    else:
        user_choice = None

    choices = (user_choice, computer_choice)
    return choices

def main(choices):
    global code
    match choices:
        case ("rock", "paper"):
            code = 2
        case ("rock", "scissors"):
            code = 1
        case ("paper", "rock"):
            code = 1
        case ("paper", "scissors"):
            code = 2
        case ("scissors", "rock"):
            code = 2
        case ("scissors", "paper"):
            code = 1
        case (None, "rock"):
            code = 2
        case (None, "paper"):
            code = 2
        case (None, "scissors"):
            code = 2

    global win_rate

    if code == 1:
        win_rate += 1
        return "User wins"
    elif code == 2:
        return "Computer wins"
    elif code == 3:
        win_rate += 0.5
        return "Draw"
    
    return win_rate

while True:
    rounds = input("How many rounds do you want to play: ")
    try:
        rounds = int(rounds)
    except (ValueError, KeyboardInterrupt):
        rounds = input("How many rounds do you want to play: ")
    else:
        for i in range(rounds):
            print(main(inputs()))
    finally:
        print(f"{(win_rate / rounds) * 100} %")

