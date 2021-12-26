"""
Computing GC Content
"""

f = open('../data/gc.txt')
dataset = {}
for lines in f:   
    if lines[0] == '>':
        temp = lines[1:-1]
        dataset[temp] = ''
    else:
        dataset[temp] += lines.rstrip()
 f.close()

max = 0
maxname = ''
for i in dataset:
    ans = (dataset[i].count('C') + dataset[i].count('G'))/len(dataset[i]) * 100
    if ans > max:
        max = ans
        maxname = i
print(maxname)
print(max)
