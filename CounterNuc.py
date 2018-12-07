dict = {'A': 0, 'T': 0, 'G': 0, 'C': 0}

data = open('rosalind_dna.txt')
s = data.readline()

for i in s:
    if i in dict:
        dict[i] = dict[i] + 1

for k in sorted(dict.keys()):
    print(dict[k], end=' ')
    
