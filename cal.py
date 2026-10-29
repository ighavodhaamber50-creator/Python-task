def calculate_tax(earnings):

    if earnings <= 30000:
        tax = earnings * 0.15
    else:
        tax = earnings * 0.20

    return tax


for count in range(3):

    name = input("Enter citizen's name: ")

    earnings = float(input("Enter earnings: "))

    tax = calculate_tax(earnings)

    print("Citizen:", name)
    print("Total Tax: $", tax)
    print()