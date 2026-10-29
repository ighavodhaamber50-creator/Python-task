base = int(input("Enter the base length (1-10): "))

if base >= 1 and base <= 10:

    for row in range(1, base + 1):

        for column in range(1, row + 1):
            print("*", end="")

        print()

else:
    print("Invalid input")