price = float(input("Enter purchase price (max $1.00): "))

change = round(100 - price * 100)

quarters = change // 25
change = change % 25

dimes = change // 10
change = change % 10

nickels = change // 5
change = change % 5

pennies = change

print("Your change is:")
print(quarters, "quarters")
print(dimes, "dimes")
print(nickels, "nickels")
print(pennies, "pennies")