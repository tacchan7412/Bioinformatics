f = open('bioinformatics_1/week1/data/dataset_3010_2.txt', 'r')
line = f.read()

text = line[:-1]

def letter2number(letter):
    if letter == 'A':
        return 0
    elif letter == 'C':
        return 1
    elif letter == 'G':
        return 2
    elif letter == 'T':
        return 3

def pattern2number(pattern):
    if pattern == '':
        return 0
    return 4 * pattern2number(pattern[:len(pattern)-1])+letter2number(pattern[len(pattern)-1])

print(pattern2number(text))
