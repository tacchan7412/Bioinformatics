f = open('bioinformatics_1/week1/data/dataset_2994_5.txt', 'r')
lines = f.readlines()

text = lines[0][:-1]
k = int(lines[1][:-1])

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
    return sum([letter2number(x)*(4**(len(pattern)-i-1)) for i, x in enumerate(pattern)])

def compute_frequencies(text, k):
    frequency_array = []
    for _ in range(4**k):
        frequency_array.append(0)
    for i in range(len(text)-k+1):
        index = pattern2number(text[i:i+k])
        frequency_array[index] += 1
    frequency_array = [str(x) for x in frequency_array]
    return frequency_array

print(' '.join(compute_frequencies(text, k)))
