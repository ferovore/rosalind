"""
Complementing a Strand of DNA
"""

f = open('../data/revc.txt')
s = f.readline().rstrip()
f.close()

ans = ''
for i in s:
    if i == 'A':
        ans = 'T' + ans
    elif i == 'T':
        ans = 'A' + ans
    elif i == 'C':
        ans = 'G' + ans
    else:
        ans = 'C' + ans
print(ans) 
