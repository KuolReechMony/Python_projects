import os, sys

def clear_terminal():
    os.system('clear')

def list_files_and_directories(file):
    try:
        for i in range(len(os.listdir(file))):
            print(os.listdir(file)[i])
    except FileNotFoundError:
        print('File not found!!')

def change_directory(file):
    os.chdir(file)

def create_directory(file):
    os.mkdir(file)

def create_file(file):
    os.system(f'echo  "" > {file}')

def remove_directory_or_file(file):
    try:
        os.remove(file)
    except PermissionError:
        print('Permission denied!!')
    except FileNotFoundError:
        print('File not found!!')
def main():
    while True:
        try:
            x = input(f"{os.getcwd()}: ")
            if x.lower() == 'clear':
                clear_terminal()
            elif x.lower == 'exit()':
                sys.exit()                              # Does not work for now
        except KeyboardInterrupt:
            sys.exit()
        else:
            for i in range(len(x)):
                if x[i] == ' ':
                    command  = x[0:i]
                    argument = x[i+1:]
                
                    match command.lower():
                        case 'cd':
                            change_directory(argument)
                        case 'ls':
                            list_files_and_directories(argument)
                        case 'mkdir':
                            create_directory(argument)
                        case 'rmdir':
                            remove_directory_or_file(argument)
                        case 'del':
                            remove_directory_or_file(argument)
                        case 'touch':
                            create_file(argument)

main()
