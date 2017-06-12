f = open('bioinformatics_1/week1/data/dataset_3010_5.txt', 'r')
lines = f.readlines()

index = int(lines[0][:-1])
k = int(lines[1][:-1])

def number2letter(number):
    if number == 0:
        return 'A'
    elif number == 1:
        return 'C'
    elif number == 2:
        return 'G'
    elif number == 3:
        return 'T'

def number2pattern(index, k):
    if k == 1:
        return number2letter(index)
    prefix_index = index // 4
    remainder = index % 4
    pattern = number2pattern(prefix_index, k-1) + number2letter(remainder)
    return pattern

print(number2pattern(index, k))
