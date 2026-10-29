pi = 0
sign = 1
denominator = 1
counter = 1

while counter <= 100:
    pi = pi + sign * (4 / denominator)
    print("Terms:", counter, "  Pi approximation:", pi)
    sign = sign * -1
    denominator = denominator + 2
    counter = counter + 1