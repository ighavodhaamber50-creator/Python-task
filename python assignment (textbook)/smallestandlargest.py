total = 0
counter = 1

first_number = int(input("Enter number 1: "))
smallest = first_number
largest = first_number
total = first_number

counter = 2
while counter <= 4:
    number = int(input("Enter number " + str(counter) + ": "))
    total = total + number
    if number < smallest:
        smallest = number
    if number > largest:
        largest = number
    counter = counter + 1

average = total / 4

print("Sum:", total)
print("Average:", average)
print("Smallest:", smallest)
print("Largest:", largest)