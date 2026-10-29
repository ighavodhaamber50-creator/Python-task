binary = int(input("Enter a binary number: "))

decimal = 0
position = 1
remaining = binary

while remaining > 0:
    last_digit = remaining % 10
    decimal = decimal + last_digit * position
    position = position * 2
    remaining = remaining // 10

print("Decimal value:", decimal)