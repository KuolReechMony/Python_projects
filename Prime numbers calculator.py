# Prime numbers calculator v1.0

def main(limit):
    for number in range(1,limit+1):
        factors_count = 0
        for i in range(1,number+1):
            if number % i != 0:
                pass
            else:
                factors_count += 1
        
        if factors_count == 2:
            print(str(number) + " is a prime number.")

main(limit = int(input("To which number do you want to check for prime numbers: ")))