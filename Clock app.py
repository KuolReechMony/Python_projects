import time
h = 0
m = 0
current_time = [h, m]

def clock():
    global h, m
    while True:
        if m < 60:
            m += 1
        elif m == 60:
            h += 1
            m = 0
        
        time.sleep(1)
        print(f"{current_time[0]}:{current_time[1]}")

clock()