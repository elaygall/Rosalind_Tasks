import re

with open('rosalind_rna.txt') as file, open('RNA.txt', 'w') as result:
    dna = file.readline()
    rna = re.sub(r'T', r'U', dna)
    result.write(rna)