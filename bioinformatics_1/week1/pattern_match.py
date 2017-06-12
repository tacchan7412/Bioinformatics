f = open('bioinformatics_1/week1/data/dataset_3_5.txt')
lines = f.readlines()

def pattern_match(pattern, genome):
    ans = []
    for i in range(len(genome)-len(pattern)+1):
        if pattern == genome[i:i+len(pattern)]:
            ans.append(str(i))
    return ans

print(' '.join(pattern_match(lines[0][:-1], lines[1][:-1])))
