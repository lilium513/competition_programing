import itertools

N,M = list(map(int,input().split(" ")))

graph = [list(map(int,input().split(" "))) for _  in range(M)]
used = [False] * M
INF = 10**20
cost = [[INF for _ in range(N+1)] for _ in range(N+1)]


for a,b,c in graph:
    cost[a][b] =min(c,cost[a][b])
    cost[b][a] = min(c,cost[b][a])

for i  in range(1,N+1):
    cost[i][i] = 0

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            cost[i][j] = min(cost[i][j],cost[i][k] + cost[k][j])


ans = 0
for k,temp  in enumerate(graph):
    a,b,c = temp
    if cost[a][b]  <  c:
        ans +=1
print(ans)
for temp in cost:
    print(temp)