# Pattern A
for row in range(1, 11):
    for col in range(row):
        print('*', end='')
    print()

print()

# Pattern B
for row in range(10, 0, -1):
    for col in range(row):
        print('*', end='')
    print()

print()

# Pattern C
for row in range(10, 0, -1):
    for space in range(10 - row):
        print(' ', end='')
    for col in range(row):
        print('*', end='')
    print()

print()

# Pattern D
for row in range(1, 11):
    for space in range(10 - row):
        print(' ', end='')
    for col in range(row):
        print('*', end='')
    print()