import math, decimal, fractions

symbols = ('(', ')', '/', '*', '+', '-') # BODMAS
complex_sysmbols = ('!', '|')
Answer = 0
pos = []

formatted_question = []

def formatter():
    pass

def addition(num_1, num_2):
    return num_1 + num_2

def subtraction(num_1, num_2):
    return num_1 - num_2

def multiplication(num_1, num_2):
    return num_1 * num_2

def division(num_1, num_2):
    match num_2:
        case 0:
            return ZeroDivisionError
        case _:
            return num_1/num_2

def nth_power(num_1, power):
    return math.pow(num_1, power)

def nth_root(num_1, root):
    pass

def factorial(num_1):
    return 

def Get_question():
    global Answer, symbols
    try:
        question = input("Question: ")
        placeholder = 0
        num_1 = 0
        num_2 = 0
        for x in range(len(question)):
            try:
                int(question[x])
                placeholder += 1
            except ValueError:
                if question[x] in symbols:
                    num_1 = question[x-placeholder:x], question[x]
                    placeholder = 0
    except KeyboardInterrupt:
        print("Enter 'exit()' to exit!")


# Get_question()


ques = input("Question: ")
p = 0
for x in range(len(ques)):
    try:
        int(ques[x])
        p += 1
    except ValueError:
        if ques[x] in symbols:
            pos.append([x, ques[x]])
            p = 0

for i in range(len(pos)):
    if i < 1:
        data = pos[i]
        upper = pos[i+1][0]
        print(upper)
    else:
        data = pos[i]
        upper = pos[i+1][0]-pos[i-1][0]
        print(upper)
    



'''match data[1]:
        case '+':
            print(ques[:])
        case '-':
            pass'''