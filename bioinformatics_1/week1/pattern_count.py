f = open('bioinformatics_1/week1/data/dataset_2_7.txt')
lines = f.readlines()

def pattern_count(line, pattern):
    count = 0
    for i in range(len(line)-len(pattern)+1):
        if line[i:i+len(pattern)] == pattern:
            count += 1
    return count

print(pattern_count(lines[0][:-1], lines[1][:-1]))
