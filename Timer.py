import time

def Timer(duration):
    for counter in range(duration):
        try:
            print(f"{duration-counter} seconds left")
            time.sleep(1)
        except KeyboardInterrupt:
            pass


def Parser(duration, units):
    match units.lower():
        case "seconds" | "second":
            Timer(duration)
        case "minutes" | "minute":
            Timer(duration*60)
        case "hours" | "hour":
            Timer(duration*3600)
        case "days" | "day":
            Timer(duration*86400)

def main():
    try:
        duration = 0
        units = ""
        timeArg = input("Duration: ")
        for x in range(len(timeArg)):
            if timeArg[x] == " ":
                try:
                    duration = int(timeArg[:x])
                except:
                    print("First try-except")
                else:
                    units += timeArg[x+1:]   
    except:
        print("Second try-except")
    else:
        Parser(duration, units)

main()