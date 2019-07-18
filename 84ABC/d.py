import itertools
import math
from collections import defaultdict



def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

N = int(input())
ps = primes(10**5)

sim2017 = [0] * (10**5 + 1)
di =defaultdict(lambda :False)
for p in ps:
    di[p] = True
for p in ps:
    if di[(p+1)/2]:
        sim2017[p] +=1
l = len(sim2017)
for i in range(1,l):
    sim2017[i] = sim2017[i-1] + sim2017[i]
ins = []
for i in range(N):
    a,b = list(map(int,input().split(" ")))
    ins.append((a,b))
for a,b in ins:
    print(sim2017[b] - sim2017[a-1])

