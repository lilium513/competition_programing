from collections import defaultdict
N = int(input())
Xs = []
Ys = []
za = []


for i in range(N):
    x,y = list(map(int, input().split(" ")))
    Xs.append(x)
    Ys.append(y)
    za.append((x,y))
ps = []
qs = []

for i in range(N):
    for j in range(i,N):
        ps.append(Xs[i]-Xs[j])

