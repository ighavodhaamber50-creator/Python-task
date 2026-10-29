number = int(input("Enter a number: "))

factorial = 1
counter = 1

while counter <= number:
    factorial = factorial * counter
    counter = counter + 1

print("Factorial of", number, "is:", factorial)