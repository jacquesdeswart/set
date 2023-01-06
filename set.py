import random
import matplotlib.pyplot as plt

colors = ['g', 'p', 'r']
forms = ['r', 'o', 't']
numbers = ['1', '2', '3']
fillings = ['d', 'o', 's']

cards = []
for color in colors:
    for form in forms:
        for number in numbers:
            for filling in fillings:
                cards.append(color + form + number + filling)


def assess(x, y, z, a):
    if (x[a] == y[a] and x[a] == z[a]) or (x[a] != y[a] and x[a] != z[a] and y[a] != z[a]):
        return 'same or different'
    else:
        return 'in between'


def is_set(x, y, z):
    if assess(x, y, z, 0) == 'same or different':
        if assess(x, y, z, 1) == 'same or different':
            if assess(x, y, z, 2) == 'same or different':
                if assess(x, y, z, 3) == 'same or different':
                    return 1
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    else:
        return 0


number_of_plays = 4
number_of_sets_per_play = []
for play in range(0, number_of_plays):
    cards_on_table = random.sample(cards, 12)
    print('the 12 cards on the table are ', cards_on_table)

    triples = []
    for x in cards_on_table:
        for y in cards_on_table:
            if cards_on_table.index(y) > cards_on_table.index(x):
                for z in cards_on_table:
                    if cards_on_table.index(z) > cards_on_table.index(y):
                        triples.append([x, y, z])

    number_of_sets: int = 0
    for triple in triples:
        if is_set(triple[0], triple[1], triple[2]) == 1:
            print('the following triple is a set: ', triple[0], triple[1], triple[2])
            number_of_sets += 1

    number_of_sets_per_play.append(number_of_sets)

possible_number_of_sets = list(set(number_of_sets_per_play))
possible_number_of_sets.sort()
frequency = []
for i in possible_number_of_sets:
    frequency.append(number_of_sets_per_play.count(i))
relative_frequency = []
for j in frequency:
    relative_frequency.append(j/number_of_plays)
print('occurrency of number of sets ', possible_number_of_sets, ':', relative_frequency)
plt.bar(possible_number_of_sets,relative_frequency)
plt.show()
