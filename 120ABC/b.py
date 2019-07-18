import math
A,B,K = list(map(int,input().split(" ")))
LIM = max(A,B)+1
cands = []
for i in range(1,LIM):
    if A%i == 0 and B % i == 0:
        cands.append(i)
print(cands[-K])