from collections import defaultdict
N,M = list(map(int,input().split(" ")))
di = defaultdict(lambda :0)
for i in range(N):
    temp= list(map(int,input().split(" ")))
    temp = temp[1:]
    for i in temp:
        di[i] += 1
ans = 0
for v in di.values():
    if v == N :
        ans+= 1
print(ans)