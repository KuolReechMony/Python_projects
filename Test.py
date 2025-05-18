with open('Test.txt', 'w') as file:
    file.write(input('Enter some text to the new file: '))

with open('Test.txt', 'r') as file:
    print(file.readlines())

