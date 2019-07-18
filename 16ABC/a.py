from itertools import accumulate

N,M = list(map(int,input().split(" ")))
colors = [0] * 1000001
total = 0
for _ in range(N):
    l,r,s= list(map(int,input().split(" ")))
    colors[l] += s
    colors[r + 1] -= s
    total += s
# print(colors[:10])

colors = accumulate(colors[1:M+1])
print(total -min(colors))
