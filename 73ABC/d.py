
import itertools
from scipy.sparse.csgraph import floyd_warshall as wf

def do():
    N,M,R = list(map(int,input().split(" ")))
    rs = list(map(int,input().split(" ")))
    INF = float('inf')

    graph = [ [INF for _ in range(N + 1)]for _ in range(N + 1)]
    for _ in range(M):
        a,b,c = (map(int, input().split(" ")))
        graph[a][b] = c
        graph[b][a] = c

    graph = wf(graph)

    perms = itertools.permutations(rs)
    ans = INF
    for temp in perms:
        cand = 0
        for i in range(0,R-1):
            fr = temp[i]
            to = temp[i + 1]
            cand+= graph[fr][to]
        ans = min(cand,ans)
    print(int(ans))

if __name__ == "__main__":
    do()