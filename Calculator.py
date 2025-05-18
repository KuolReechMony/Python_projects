import math

symbols = ('+', '-', '*', '/', '%', '**')

memory = []

def formatter(question):
    x = 0
    for i in range(len(question)):
        if question[i] in symbols and i != len(question):
            memory.append(question[x:i])
            memory.append(question[i])
            x = i+1
        elif question[i] in symbols and i == len(question):
            memory.append(question[x:])
        
    memory.append(question[x:])


def power_functions(memory):
    for i in range(len(memory)):
        if memory[i] == symbols[-1]:
            x = memory[i-1]
            y = memory[i+1]
        pass

def sqrt_function(x):
    try:
        x = int(x)
    except ValueError:
        print('None interger input')
        return None
    else:
        try:
            if x < 0:
                raise Exception('Positive number only')
        except:
            print('Negative number')
        else:
            return(math.sqrt(x))


def main(query):
    formatter(query)

main(input('Any math problem: '))

print(memory)