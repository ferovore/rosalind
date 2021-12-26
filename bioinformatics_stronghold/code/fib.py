"""
Rabbits and Recurrence Relations
"""

f = open('../data/fib.txt')
n, k = [int(x) for x in f.readline().rstrip().split()]
f.close()

rab = [1, 1]
for i in range(2, n):
    rab.append(rab[i-1] + k * rab[i-2])

print(rab[n-1])
