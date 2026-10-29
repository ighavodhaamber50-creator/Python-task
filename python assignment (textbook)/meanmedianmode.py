numbers = [9, 11, 22, 34, 17, 22, 34, 22, 40]

# Mean
total = 0
for number in numbers:
    total = total + number
mean = total / len(numbers)
print("Mean:", mean)

# Median
numbers.sort()
middle = len(numbers) // 2
median = numbers[middle]
print("Median:", median)

# Mode
most_common = 0
highest_count = 0
for number in numbers:
    count = 0
    for other in numbers:
        if number == other:
            count = count + 1
    if count > highest_count:
        highest_count = count
        most_common = number
print("Mode:", most_common)