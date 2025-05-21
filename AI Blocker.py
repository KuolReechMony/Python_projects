# AI Blocker
from datetime import datetime
import os, sys

record = ''
current_location = str(os.getcwd())
List_of_rules = []
List_of_connections = []
Bans = []


def get_ip(name): # Returns the nslookup data of the ssuggested website and returns results as a list
    try:
        os.system(f"nslookup {name} 8.8.8.8 > temp_file.txt")
        with open("temp_file.txt", "r+t") as file:
            results = file.readlines()
    except FileExistsError:
        print('File already exists')        
    else:
        #os.remove("temp_file.txt")
        return results
 

def current_time(): # Records the date and time of the banned connection
    the_time = str(datetime.now())
    return the_time[:19]


def Sanitize(): # Writes active connections to the temp_file
    global current_location
    current_location += '/Test.py'
    try:
        os.system(f"netstat -afno | findstr /R :443 | findstr /R ESTABLISHED > temp.txt")
    except KeyboardInterrupt:
        Sanitize()
                

def Get_banned_connections_and_processes(): # Compares the recorded connections to the Rules, Returns PID of banned connections
    Sanitize()
    global List_of_connections, List_of_rules, Bans
    with open("temp.txt", "r+t") as file:
        with open("Rules.txt", "r+t") as template:
            material = file.readlines()
            guides = template.readlines()
            for i in range(len(material)):
                List_of_connections.append([(str(material[i])[32:55].replace(" ", "").replace(":443", "")), (str(material[i])[67:].replace(' ', ''))])
                #print((str(material[i])[67:].replace(' ', '')))
                pass
            
            for x in range(len(guides)):
                n = 0
                text = guides[x]
                for y in range(1,len(text)):
                    if text[y-1] == ';' and text[y] == ';':
                        test_subject = text[n:y-1]
                        for i in range(len(test_subject)):
                            if test_subject[i:i+10] == 'Addresses:':
                                m = (test_subject[i+10:])
                                k = 0
                                for i in range(len(m)):
                                    if m[i] == ';':
                                        List_of_rules.append(m[k:i])
                                        k = i+1
                                List_of_rules.append(m[k:])
                                            
                        n = y


    for x in range(len(List_of_connections)):
        connection = List_of_connections[x]
        current_connection = connection[0]
        for i in range(len(List_of_rules)):
            current_rule = List_of_rules[i]
            if current_connection.lower() == current_rule.lower():
                try:
                    print(current_connection, current_rule, connection[1])
                    os.system(f" TASKKILL /IM chrome.exe")
                    Bans.append([current_connection, current_time()])
                except:
                    pass
                        

def Parse_rules(): # Removes spaces and new lines from the rules and writes the formatted version to the Rules file
    get_ip(input('Which website do you want to block: '))
    with open("temp_file.txt", "r+t") as file:
        new_string = ''
        check = file.readlines()
        for i in range((len(check))):
                new_string += str(check[i].replace("\n", ";").replace(" ", "").replace("\t", ""))
        
        new_strings = new_string.replace(";;", ";")
        with open("Rules.txt", "at") as file:
            file.write(new_strings + ';;')

def Get_logs():
    with open("Logs.txt", "r+t") as file:
        logs = file.readlines
        print(type(logs))        

def main():
    global Bans
    while True:
        try:
            choice = input('Menu: 1 - Create new rule, 2 - Check logs, exit() - exit: ')
            match choice:
                case '1':
                    Parse_rules()
                    global record
                    record = ''
                case '2':
                    Get_logs()
                case 'exit()':
                    sys.exit()
            Get_banned_connections_and_processes()
            #os.system('cls')
        except (KeyboardInterrupt, ValueError):
            print('Error occured')
        else:
            with open("Logs.txt", "r+t") as file:
                file.write(str(Bans))

main()
