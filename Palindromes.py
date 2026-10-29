number = int(input("Enter a 5 digit number: "))
digit1 = number // 10000
digit2 = (number // 1000) % 10
digit3 = (number // 100) % 10
digit4 = (number // 10) % 10
digit5 = number % 10

print("The digits are:", digit1, digit2, digit3, digit4, digit5)

if digit1 == digit5 and digit2 == digit4:
    print(str(number) + " is a palindrome")
else:
    print(str(number) + " is not a palindrome") 