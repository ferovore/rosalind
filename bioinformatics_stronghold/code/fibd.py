"""
Mortal Fibonacci Rabbits
"""

f = open('../data/fibd.txt')
n, m = [int(x) for x in f.readline().rstrip().split()]
f.close()

new = [1] 
ad = [0] 
for i in range(1, n):
    if i < m:
        ad.append(new[i-1] + ad[i-1])
    else:
        ad.append(new[i-1] + ad[i-1] - new[i-m])
    new.append(ad[i-1])
print(ad[n-1] + new[n-1])
