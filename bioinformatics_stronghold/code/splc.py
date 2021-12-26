"""
RNA Splicing
"""

def prot(s):
    rna_codon = {
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

    for i in range(0, len(s), 3):
        temp = rna_codon[s[i:i+3]]
        if temp != 'Stop':
            answer += temp
    return answer

def subs(s, t): #finding substring t in string s
    for i in range(len(s) - len(t) + 1):
        if s[i:i + len(t)] == t:
            ans = [i, i + len(t)]
            break
    return ans

f = open('../data/splc.txt')
introns = []
cut = [[0,0]]

dna = f.readline().rstrip()
dna = ''
for lines in f:
    if lines[0] == '>':
        break
    else:
        dna += lines.rstrip()
for lines in f:
    if lines[0] != '>':
        introns.append(lines.rstrip())
        cut.append(subs(dna, lines.rstrip()))
f.close()

cut.append([len(dna)])   
cut.sort()

rna = ''
#delete the introns
for i in range(len(cut) - 1):
    rna += dna[cut[i][1]:cut[i + 1][0]]

print(prot(rna))
