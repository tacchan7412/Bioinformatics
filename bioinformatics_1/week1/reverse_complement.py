f = open('bioinformatics_1/week1/data/dataset_3_2.txt')
line = f.read()

def complement(nucleotide):
    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'G':
        return 'C'

def reverse_complement(pattern):
    reversed_pattern = []
    for nucleotide in pattern[::-1]:
        reversed_pattern.append(complement(nucleotide))
    return reversed_pattern

print(''.join(reverse_complement(line[:-1])))
