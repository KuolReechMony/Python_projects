from datetime import datetime
import os


def main(option):
    match option:
        case 1:
            os.system('shutdown /s /t 60 /c "A MINUTE TO SHUTDOWN!!"')
        case 2:
            os.system('shutdown /s /t 1200 /c "A MINUTE TO SHUTDOWN!!"')
        case 3:
            os.system('shutdown /s /t 2400 /c "A MINUTE TO SHUTDOWN!!"')

def sleep_checklist():
    current_time = datetime.now()
    return current_time

def menu(time_argument):
    match time_argument.hour:
        case 00:
            if time_argument.minute >= 30: # Past 12:30 am
                return 1
            else:
                return 2 # 12:00am-12:30 am
        case 23:
            if time_argument.minute >= 30: # 11:30pm-12:00am
                return 2
            else:
                return 3 # 11:00pm-11:30pm
            
main(menu(sleep_checklist()))