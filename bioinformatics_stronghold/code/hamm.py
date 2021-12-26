"""
Counting Point Mutations
"""

f = open('../data/hamm.txt')
s = f.readline().rstrip()
t = f.readline().rstrip()
f.close()

ans = 0
for i, j in zip(s, t):
    if i != j:
        ans += 1
print(ans)
