principal = 1000
rate = 0.07

year = 1
while year <= 30:
    amount = principal * (1 + rate) ** year
    print("After year", year, ":", round(amount, 2))
    year = year + 1