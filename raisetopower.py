base = 10
exponent = 3 

result = 1

counter = 1
while counter <= exponent:
    temp = 0
    add_counter = 1

    while add_counter <= base:
        temp = temp + result
        add_counter = add_counter + 1

    result = temp
    counter = counter + 1

print(result)