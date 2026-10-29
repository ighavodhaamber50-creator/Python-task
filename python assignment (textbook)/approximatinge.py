e = 0
factorial = 1
counter = 0

while counter <= 10:
    if counter == 0:
        factorial = 1
    else:
        factorial = factorial * counter
    e = e + 1 / factorial
    print("Terms:", counter + 1, "  e approximation:", e)
    counter = counter + 1