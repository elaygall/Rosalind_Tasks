data = open('rosalind_dna.txt')
s = data.readline()

NucBase = {'A': 0, 'T': 0, 'G': 0, 'C': 0}

for i in s:
    if i in NucBase:
        NucBase[i] = NucBase[i] + 1

for k in sorted(NucBase.keys()):
    print(NucBase[k], end=' ')
