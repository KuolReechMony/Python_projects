# Key
# rt = read only, text file(file must exist); 
# r+ = read, write, text file(file must exist)
# wt = write only, text file(creates new file if non-existent)
# at = append only, text file(creates new file if non-existent)

import os, sys

current_directory = os.getcwd()


# Write content to new file/ overwrite current content
def write(text_file):
    try:
        with open(f"{current_directory}/{text_file}", 'wt') as file:
            file.write(input('Enter some text to the file: '))
    except:
        print("Some Error!!")


# Read content from a file
def read(text_file):
    os.system("cls")
    try:
        with open(text_file, 'rt') as file:
            output = file.readlines()
            for count in range(len(output)):
                print(output[count])
    except FileNotFoundError:
        print(f'"{text_file}" file not found!!')

def menu():
    while True:
        print("Enter 'exit()' to stop the program anytime!")
        try:
            choice = input("Menu: 1 - write, 2 - read: ")
            file = input("File path: ")
        except KeyboardInterrupt:
            print("Enter 'exit()' to stop the program")
        else:
            match choice.lower():
                case '1':
                    write(file)
                case '2':
                    read(file)
                case 'exit()':
                    sys.exit()
                case _:
                    try:
                        menu()
                    except RecursionError:
                        print('Too many errors')
                        sys.exit()
        finally:
            choice = ''
            file = ''
menu()