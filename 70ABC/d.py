import itertools
import math

def dfs(N,E,start):
    d = [-1] * (N + 1)
    d[start] = 0
    q = [start]
    while q:
        now = q.pop()
        vertexes = E[now]
        for to in vertexes:
            if d[to] == -1:
                d[to] = d[now] + E[now][to]
                q.append(to)
    return d
N = int(input())
E = [{} for _ in range(N + 1)]
for _ in range(N-1):
    a,b,c = map(int, input().split(" "))
    E[a][b] = c
    E[b][a] = c

Q, K = map(int, input().split(" "))
d = dfs(N,E,K)
AB = [list(map(int, input().split(" "))) for _ in range(Q)]
for a,b in AB:
    print(d[a] + d[b])