passes = 0
counter = 1

while counter <= 10:
    result = int(input("Enter result for student " + str(counter) + " (1=pass, 2=fail): "))
    
    while result != 1 and result != 2:
        print("Invalid input! Please enter 1 or 2")
        result = int(input("Enter result for student " + str(counter) + " (1=pass, 2=fail): "))
    
    if result == 1:
        passes = passes + 1
    
    counter = counter + 1

failures = 10 - passes

print("Passes:", passes)
print("Failures:", failures)