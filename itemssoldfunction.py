total_sales = 0

number_of_items = int(input("How many items were sold? "))

for count in range(number_of_items):

    item = int(input("Enter item number (1-4): "))

    if item == 1:
        total_sales = total_sales + 239.99

    elif item == 2:
        total_sales = total_sales + 129.75

    elif item == 3:
        total_sales = total_sales + 99.95

    elif item == 4:
        total_sales = total_sales + 350.89

commission = total_sales * 9 / 100

earnings = 200 + commission

print("Total Sales:", total_sales)
print("Earnings:", earnings)