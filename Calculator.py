import math

symbols = ('/', '*', '+', '-') # BODMAS

question = []

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
    return num_1 ** (1/root)

def factorial(num_1):
    return math.factorial(num_1)

def bodmas(question):
    length = len(question)
    for i in range(len(question)):
        if i < 1:
            pass
        elif i+1 > length:
            pass
        else:
            if question[i] in symbols:
                match (question[i]):
                    case "/":
                        question[i] = division(int(question[i-1]), int(question[i+1]))
                        question.pop(i-1)
                        question.pop(i+1)
                    case "*":
                        if int(int(question[i-1])) or int(int(question[i+1])) == 0:
                            question[i] = 0
                            question.pop(i-1)
                            question.pop(i+1)
                        else:
                            question[i] = multiplication(int(question[i-1]), int(question[i+1]))
                            question.pop(i-1)
                            question.pop(i+1)
                    case "+":
                        question[i] = addition(int(question[i-1]), int(question[i+1]))
                        question.pop(i-1)
                        question.pop(i+1)
                    case "-":
                        question[i] = subtraction(int(question[i-1]), int(question[i+1]))
                        question.pop(i-1)
                        question.pop(i+1)

def Get_Question():
    global question
    x = input("Math problem:  ")
    index = 0
    for i in range(len(x)):
        if x[i] in symbols:
            question.append(x[index:i])
            question.append(x[i])
            index = i+1
    bodmas(question)

for i in range(4):
    Get_Question()
    print(question)