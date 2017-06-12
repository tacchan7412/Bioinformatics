f = open('bioinformatics_1/week1/data/dataset_2_10.txt')
lines = f.readlines()

def frequent_words(text, k):
    counts = {}
    for i in range(len(text)-k+1):
        kmer = text[i:i+k]
        counts[kmer] = (counts.get(kmer) or 0) + 1
    max_val = sorted(counts.values(), reverse=True)[0]
    print(max_val)
    ans_set = set()
    for k, v in counts.items():
        if max_val == v:
            ans_set.add(k)
    return ans_set

print(frequent_words(lines[0][:-1], int(lines[1][:-1])))
