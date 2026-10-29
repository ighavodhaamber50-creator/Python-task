customers = int(input("Enter number of customers: "))

for count in range(customers):

    account_number = int(input("Enter account number: "))
    beginning_balance = int(input("Enter beginning balance: "))
    charges = int(input("Enter total charges: "))
    credits = int(input("Enter total credits: "))
    credit_limit = int(input("Enter credit limit: "))

    new_balance = beginning_balance + charges - credits

    print("Account Number:", account_number)
    print("New Balance:", new_balance)

    if new_balance > credit_limit:
        print("Credit limit exceeded")

    print()