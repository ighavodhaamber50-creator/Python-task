population = 8100000000
growth_rate = 0.0075

print("Year   Population         Increase")

year = 1
while year <= 100:
    new_population = population * (1 + growth_rate) ** year
    increase = new_population - population * (1 + growth_rate) ** (year - 1)
    print(year, "   ", round(new_population), "   ", round(increase))
    year = year + 1