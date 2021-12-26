"""
Finding a Motif in DNA
"""

f = open('../data/subs.txt')
s = f.readline().rstrip()
t = f.readline().rstrip()
f.close()

ans = ''
for i in range(len(s) - len(t)):
    if s[i:i + len(t)] == t:
        ans += str(i + 1) + ' '
print(ans)
