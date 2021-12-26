"""
Consensus and Profile
"""

f = open('../data/cons.txt')
dataset = []
i = -1
for lines in f:   
    if lines[0] == '>':
        dataset.append('')
        i += 1
    else:
        dataset[i] += lines.rstrip()
f.close()

n = len(dataset[0])
profile = {'A': [0] * n, 'C': [0] * n, 'G': [0] * n, 'T': [0] * n}

for i in dataset:
    for j in range(len(i)):     
        profile[i[j]][j] += 1

ans = [''] * n
t = [-1] * n

print(profile)

for i in range(len(dataset[0])):
    for j in profile:
        if profile[j][i] > t[i]:
            t[i] = profile[j][i]
            ans[i] = j

ansstr = ''
for i in ans:
    ansstr += i
print(ansstr)

for i in profile:
    temp = i + ': '
    for j in profile[i]:
        temp += str(j) + ' '
    print(temp)
