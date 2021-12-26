"""
Calculating Expected Offspring 
"""

f = open('../data/iev.txt')
a = [int(x) for x in f.readline().rstrip().split()]
f.close()

ans = (a[0] + a[1] + a[2]) * 2 + a[3] * 1.5 + a[4] 
print(ans)
