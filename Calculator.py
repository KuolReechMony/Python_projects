import math

symbols = ('/', '*', '+', '-') # BODMAS

question = []
questionOrder = []

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
    counter = 1
    while counter < len(question):
        questionOrder.append(question[counter-1:counter+2])
        counter += 2

    for i in range(len(questionOrder)):
        if i == 0:
            if question[i][0] == "/":
                match (questionOrder[i][1]):
                    case "/":
                        questionOrder.pop[i+1][0] = division(int(questionOrder[i][0]), int(questionOrder[i][2]))
                        questionOrder.pop(i)
                    case "*":
                        if int(int(questionOrder[i][0])) or int(int(questionOrder[i][2])) == 0:
                            questionOrder[i+1][0] = 0
                            questionOrder.pop(i)
                        else:
                            questionOrder[i+1][0] = multiplication(int(questionOrder[i][0]), int(questionOrder[i][2]))
                            questionOrder.pop(i)
                    case "+":
                        questionOrder[i+1][0] = addition(int(questionOrder[i][0]), int(questionOrder[i][2]))
                        questionOrder.pop(i)
                    case "-":
                        questionOrder[i+1][0] = subtraction(int(questionOrder[i][0]), int(questionOrder[i][2]))
                        questionOrder.pop(i)


            elif i+1 == len(questionOrder):
                match (questionOrder[i][1]):
                    case "/":
                        questionOrder[i-1][2] = division(int(questionOrder[i][0]), int(questionOrder[i][2]))
                        questionOrder.pop(i)
                    case "*":
                        if int(int(questionOrder[i][0])) or int(int(questionOrder[i][2])) == 0:
                            questionOrder[i-1][2] = 0
                            questionOrder.pop(i)
                        else:
                            questionOrder[i-1][2] = multiplication(int(questionOrder[i][0]), int(questionOrder[i][2]))
                            questionOrder.pop(i)
                    case "+":
                        questionOrder[i-1][2] = addition(int(questionOrder[i][0]), int(questionOrder[i][2]))
                        questionOrder.pop(i)
                    case "-":
                        questionOrder[i-1][2] = subtraction(int(questionOrder[i][0]), int(questionOrder[i][2]))
                        questionOrder.pop(i)

            else:
                match (questionOrder[i][1]):
                    case "/":
                        questionOrder[i-1][2] = division(int(questionOrder[i][0]), int(questionOrder[i][2]))
                        questionOrder.pop[i+1][0] = division(int(questionOrder[i][0]), int(questionOrder[i][2]))
                        questionOrder.pop(i)
                    case "*":
                        if int(int(questionOrder[i][0])) or int(int(questionOrder[i][2])) == 0:
                            questionOrder[i-1][2] = 0
                            questionOrder[i+1][0] = 0
                            questionOrder.pop(i)
                        else:
                            questionOrder[i-1][2] = multiplication(int(questionOrder[i][0]), int(questionOrder[i][2]))
                            questionOrder[i+1][0] = multiplication(int(questionOrder[i][0]), int(questionOrder[i][2]))
                            questionOrder.pop(i)
                    case "+":
                        questionOrder[i-1][2] = addition(int(questionOrder[i][0]), int(questionOrder[i][2]))
                        questionOrder[i+1][0] = addition(int(questionOrder[i][0]), int(questionOrder[i][2]))
                        questionOrder.pop(i)
                    case "-":
                        questionOrder[i-1][2] = subtraction(int(questionOrder[i][0]), int(questionOrder[i][2]))
                        questionOrder[i+1][0] = subtraction(int(questionOrder[i][0]), int(questionOrder[i][2]))
                        questionOrder.pop(i)

        print(questionOrder)


def Get_Question():
    global question
    x = input("Math problem:  ")
    index = 0
    last = 0
    for i in range(len(x)):
        if x[i] in symbols:
            question.append(x[index:i])
            question.append(x[i])
            index = i + 1
            last = i +1
    
    question.append(x[last:])
    bodmas(question)



