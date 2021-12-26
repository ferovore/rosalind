"""
Overlap Graphs
"""

f = open('../data/grph.txt')
dataset = {}
for lines in f:   
    if lines[0] == '>':
        temp = lines[1:-1]
        dataset[temp] = ''
    else:
        dataset[temp] += lines.rstrip()
f.close()

answer = []
for i in dataset:
    for j in dataset:
        if i != j:
            if dataset[i][-3:] == dataset[j][:3]:
                answer.append(i + ' ' + j)

for i in answer:
    print(i)
