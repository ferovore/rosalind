"""
Transcribing DNA into RNA 
"""

f = open('../data/rna.txt')
t = f.readline().rstrip()
f.close()

ans = ''
for i in t:
    if i == 'T':
        ans += 'U'
    else:
        ans += i
print(ans)
