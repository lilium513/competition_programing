def warshall_floyd(N):
    INF = 10**20
    path = [[INF for _ in range(N+ 1)] for _ in range(N+1)]
    graph = get_graph()
    for i in range(N+1):
        path[i][i] = 0
    for g in graph:
        x = g[0]
        y = g[1]
        l = g[2]
        path[x][y] = path[y][x] = l
    for start in range(N+1):
        for goal in range(N+1):
            for way in range(N+1):
                path[start][goal] = path[goal][start] = min(path[start][goal], path[start][way] + path[way][goal])
    return path

def get_graph():
    graph = [input_as_int() for _ in range(M)]
    return graph
def input_as_int():
    return list(map(int,input().split()))

N,M = input_as_int()
path = warshall_floyd(M)
ans = 10**10
for i in range(2,N+1):
    for j in range(2,N+1):
        if i == j:
            continue
        ans = min(ans, path[1][i] + path[i][j] + path[j][i])

print(ans)