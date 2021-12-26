"""
Counting DNA Nucleotides
"""

f = open('../data/dna.txt')
dna = f.readline().rstrip()
a = 0
c = 0
g = 0
t = 0
for i in dna:
    if i == 'A':
        a += 1
    if i == 'C':
        c += 1
    if i == 'G':
        g += 1
    if i == 'T':
        t += 1

print(a, c, g, t)
