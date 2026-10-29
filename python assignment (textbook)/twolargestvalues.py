first_number = int(input("Enter number 1: "))
largest = first_number
second_largest = first_number

counter = 2
while counter <= 10:
    number = int(input("Enter number " + str(counter) + ": "))
    if number > largest:
        second_largest = largest
        largest = number
    else:
        if number > second_largest:
            second_largest = number
    counter = counter + 1

print("Largest:", largest)
print("Second largest:", second_largest)