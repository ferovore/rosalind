"""
Finding a Shared Motif
"""
f = open('../data/lcsm.txt')
dataset = []
c = -1
for lines in f:   
    if lines[0] == '>':
        c += 1
        dataset.append('')
    else:
        dataset[c] += lines.rstrip()
f.close()

for i in range(1, len(dataset)):
    if len(dataset[i]) < len(dataset[0]):
        dataset[i], dataset[0] = dataset[0], dataset[i]

longest_motif = ''
for i in range(len(dataset[0])):
    for j in range(i, len(dataset[0])):
        IfFound = False
        motif = dataset[0][i:j + 1]
        if len(motif) > len(longest_motif):
            for k in dataset[1:]:
                if motif in k:
                    IfFound = True
                else:
                    IfFound = False
                    break
            if IfFound:
                longest_motif = motif

print(longest_motif)
