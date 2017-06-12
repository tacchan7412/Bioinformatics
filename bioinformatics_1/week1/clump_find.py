f = open('bioinformatics_1/week1/data/dataset_4_5.txt')
lines = f.readlines()

genome = lines[0][:-1]
k = int(lines[1].split(' ')[0])
L = int(lines[1].split(' ')[1])
t = int(lines[1].split(' ')[2][:-1])

def find_clump(genome, k, L, t):
    ans = []
    cnt_dict = {}
    for j in range(L-k+1):
        cnt_dict[genome[j:j+k]] = (cnt_dict.get(genome[j:j+k]) or 0) + 1
    for key, val in cnt_dict.items():
        if val >= t:
            ans.append(key)
    for i in range(len(genome)-L):
        cnt_dict[genome[i:i+k]] -= 1
        cnt_dict[genome[L-k+1+i:L+i+1]] = (cnt_dict.get(genome[L-k+1+i:L+i+1]) or 0) + 1
        if cnt_dict[genome[L-k+1+i:L+i+1]] >= t:
            ans.append(genome[L-k+1+i:L+i+1])
    return set(ans)

print(' '.join(find_clump(genome, k, L, t)))
