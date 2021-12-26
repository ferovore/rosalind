"""
Open Reading Frames
"""

import math

def prot(s):
    dna_codon = {
    'TTT': 'F',     'CTT': 'L',     'ATT': 'I',     'GTT': 'V',
    'TTC': 'F',     'CTC': 'L',     'ATC': 'I',     'GTC': 'V',
    'TTA': 'L',     'CTA': 'L',     'ATA': 'I',     'GTA': 'V',
    'TTG': 'L',     'CTG': 'L',     'ATG': 'M',     'GTG': 'V',
    'TCT': 'S',     'CCT': 'P',     'ACT': 'T',     'GCT': 'A',
    'TCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'TCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'TCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'TAT': 'Y',     'CAT': 'H',     'AAT': 'N',     'GAT': 'D',
    'TAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'TAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'TAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'TGT': 'C',     'CGT': 'R',     'AGT': 'S',     'GGT': 'G',
    'TGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'TGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'TGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
    }

    answer = ''
    ifstop = False

    for i in range(math.floor(len(s)/3)):
        if dna_codon[s[i*3:i*3+3]] != 'Stop':
            answer += dna_codon[s[i*3:i*3+3]]
        else:
            ifstop = True
            break

    if ifstop:
        return answer
    else:
        return ''

f = open('../data/orf.txt')
dna = ''
for lines in f:
    if lines[0] != '>':
        dna += lines.rstrip()
f.close()

frames = []
for i in range(len(dna)-3):
    if dna[i:i+3] == 'ATG':
        frames.append(prot(dna[i:]))

ans = ''
for i in dna:
    if i == 'A':
        ans = 'T' + ans
    elif i == 'T':
        ans = 'A' + ans
    elif i == 'C':
        ans = 'G' + ans
    else:
        ans = 'C' + ans

dna = ans

for i in range(len(dna)-3):
    if dna[i:i+3] == 'ATG':
        temp = prot(dna[i:])
        if not temp in frames:
            frames.append(temp)

for i in frames:
    if i != '':
        print(i)
