numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

print("List:", numbers)

# B. Highest occurring number
highest = max(set(numbers), key=numbers.count)
print("Highest occurring number:", highest)

# C. Numbers divisible by 2, 3 and 5

print("Numbers divisible by 2:")
for num in numbers:
    if num % 2 == 0:
        print(num)

print("Numbers divisible by 3:")
for num in numbers:
    if num % 3 == 0:
        print(num)

print("Numbers divisible by 5:")
for num in numbers:
    if num % 5 == 0:
        print(num)

# D. Prime numbers

print("Prime numbers:")

for num in numbers:

    if num > 1:

        prime = True

        for i in range(2, num):

            if num % i == 0:
                prime = False
                break

        if prime:
            print(num)