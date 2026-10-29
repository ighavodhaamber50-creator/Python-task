number = int(input("Enter a 5 digit number: "))

remaining = number
counter = 10000

while counter >= 1:
    digit = remaining // counter
    remaining = remaining % counter
    counter = counter // 10
    print(digit)