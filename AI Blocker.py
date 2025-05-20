# AI Blocker
from datetime import datetime
import os, sys

record = ''

current_location = str(os.getcwd())

def get_ip(name):
    try:
        os.system(f"nslookup {name} 8.8.8.8 > temp_file.txt")
        with open("temp_file.txt", "r+t") as file:
            results = file.readlines()
    except FileExistsError:
        print('File already exists')        
    else:
        #os.remove("temp_file.txt")
        return results
           
def initialize():
    global record
    try:
        name = input('Which sites do you want to block: ')
        record += (str(name) + ', ')
        IP = get_ip(name)
        IP = IP[4:-1]
    except KeyboardInterrupt:
        pass
    else:
        for i in range(len(IP)):
            x = IP[i]
            x = x.replace("\n", ",")
            for i in range(len(x)):
                if x[i] == ' ' and x[i+1] != ' ':
                    record += str(x[i+1:])
    finally:
        with open("Rules.txt", "at") as rules:
            rules.write(f"{record}")
            rules.write(";")
 

def current_time():
    the_time = str(datetime.now())
    return the_time[:19]


def Sanitize():
    global current_location
    current_location += '/Test.py'
    while True:
        try:
            os.system(f"netstat -afno | findstr /R :443 | findstr /R ESTABLISHED > temp_file.txt")
            sys.exit()
        except KeyboardInterrupt:
            Sanitize()
                

def Parser():
    with open("temp_file.txt", "r+t") as file:
        with open("Rules.txt", "r+t") as template:
            try:
                material = str(file.readline())
                guides = file.readline()
                for i in range(len(guides)):
                    guide = guides[i]
                    if material[31:40] in guide:
                        print((f"User visited blocked website "), material[31:40]) 
                    else:
                        print(material[31:40])
            except:
                pass

def Get_rules():
    with open("Rules.txt", "rt") as the_rules:
        all_rules = str(the_rules.readline())
        n = 0
        for i in range(len(all_rules)):
            if all_rules[i] == ';':
                print(all_rules[n:i])
                n = i+1
def main():
    while True:
        try:
            choice = input('Menu: 1 - Create new rule, 2 - Check rules, 3 - Check logs: ')
            match int(choice):
                case 1:
                    initialize()
                    global record
                    record = ''
                case 2:
                    Get_rules()
                case 3:
                    Parser()
        except (KeyboardInterrupt, ValueError):
            print('Error occured')

main()
