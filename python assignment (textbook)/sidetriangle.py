for row in range(1, 11):
    # Pattern A
    for col in range(row):
        print('*', end='')
    for space in range(10 - row):
        print(' ', end='')

    print('   ', end='')

    # Pattern B
    for col in range(10 - row + 1):
        print('*', end='')
    for space in range(row - 1):
        print(' ', end='')

    print('   ', end='')

    # Pattern C
    for space in range(10 - row):
        print(' ', end='')
    for col in range(row):
        print('*', end='')

    print('   ', end='')

    # Pattern D
    for space in range(row - 1):
        print(' ', end='')
    for col in range(10 - row + 1):
        print('*', end='')

    print()