row = 1

    while row <= baseSS:

        column = 1

        while column <= row:

            print("*", end="")

            column = column + 1

        print()

        row = row + 1

else:

    print("Invalid input")