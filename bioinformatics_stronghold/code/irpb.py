"""
Mendel's First Law
"""

f = open('../data/irpb.txt')
k, m, n = [int(x) for x in f.readline().rstrip().split()]
f.close()

prob = 2*k*m + 2*k*n + m*n + k*(k-1) + 0.75*m*(m-1)
total = (k + m + n) * (k + m + n - 1)
print(prob/total)
