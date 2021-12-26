"""
Independent Allels
"""

f = open('../data/lia.txt')
k, n = [int(x) for x in f.readline().rstrip().split()]
f.close()

ans = 0

C = []

for i in range(2**k + 2):
    C.append([])
    for j in range(i + 1):
        if i == j or j == 0:
            C[i].append(1)
        else:
            C[i].append(0)
            C[i][j] = C[i-1][j] + C[i-1][j-1]

for i in range(n, 2**k + 1):
    ans += (0.25)**i * C[2**k][i] * (0.75)**(2**k - i)

print(ans)
