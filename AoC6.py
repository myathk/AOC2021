with open('AoC6input.txt') as f:
    contents = f.readline()


list_of_input = list(map(lambda x: int(x), contents.rsplit(",")))

zeros = list_of_input.count(0)
ones = list_of_input.count(1)
twos = list_of_input.count(2)
threes = list_of_input.count(3)
fours = list_of_input.count(4)
fives = list_of_input.count(5)
sixes = list_of_input.count(6)

dict = {
    '0s':zeros,
    '1s':ones,
    '2s':twos,
    '3s':threes,
    '4s':fours,
    '5s':fives,
    '6s':sixes,
    '7s':0,
    '8s':0
}


for i in range (0, 256):
    zeros = dict['0s']
    ones = dict['1s']
    twos = dict['2s']
    threes = dict['3s']
    fours = dict['4s']
    fives = dict['5s']
    sixes = dict['6s']
    sevens = dict['7s']
    eights = dict['8s']

    dict['0s'] = ones
    dict['1s'] = twos
    dict['2s'] = threes
    dict['3s'] = fours
    dict['4s'] = fives
    dict['5s'] = sixes
    dict['6s'] = sevens + zeros
    dict['7s'] = eights
    dict['8s'] = zeros

print(dict['0s'] + dict['1s'] + dict['2s'] + dict['3s'] + dict['4s'] + dict['5s'] + dict['6s'] + dict['7s'] + dict['8s'])