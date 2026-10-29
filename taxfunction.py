def calculate_tax(earnings):

    if earnings <= 30000:
        tax = earnings * 15 / 100
    else:
        tax = earnings * 20 / 100

    return tax


for count in range(3):

    name = input("Enter citizen name: ")
    earnings = float(input("Enter earnings: "))

    tax = calculate_tax(earnings)

    print("Name:", name)
    print("Tax:", tax)
    print()