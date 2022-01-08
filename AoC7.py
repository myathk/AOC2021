with open('AoC7input.txt') as f:
    contents = f.readline()


contents = list(map(lambda x: int(x), contents.rsplit(",")))

minimum = min(contents)
maximum = max(contents)

def sum_from_1_to(x):
    return (x * (x + 1))/2

list_of_fuel = []
for i in range(minimum, maximum + 1):
    total_fuel = 0
    for each in contents:
        total_fuel = sum_from_1_to(abs(each - i)) + total_fuel
    list_of_fuel.append(total_fuel)

print(min(list_of_fuel))