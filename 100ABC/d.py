import statistics
import math
N,M= list(map(int,input().split(" ")))

cakes = []
for i in range(N):
    cakes.append(list(map(int, input().split(" "))))

ans = -(10e9)
for i in range(3):
    for rev in [True,False]:
        cakes.sort(key=lambda x:x[i],reverse=rev)
        b = 0
        d = 0
        p = 0
        for j in range(M):
            b += cakes[j][0]
            d += cakes[j][1]
            p += cakes[j][2]
        temp = abs(b) +abs(d) +abs(p)
        if temp > ans:
            ans = temp

print(ans)