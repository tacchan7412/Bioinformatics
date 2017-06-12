f = open('bioinformatics_1/week1/data/Vibrio_cholerae.txt')
line = f.read()
pattern = 'CTTGATCAT'

def pattern_match(pattern, genome):
    ans = []
    for i in range(len(genome)-len(pattern)+1):
        if pattern == genome[i:i+len(pattern)]:
            ans.append(str(i))
    return ans

print(' '.join(pattern_match(pattern, line)))
