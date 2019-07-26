
N,M = list(map(int,input().split(" ")))
INF = -(10 ** 20)
graph = [ INF for _ in range(N + 1)]
edges = []
for _ in range(M):
    a,b,c = list(map(int,input().split(" ")))
    edges.append((a,b,c))

graph[1] = 0
for i in range(2 * N): #ループがなければ更新は N - 1回 以降行われない
    for edge in edges:
        fr,to,point = edge
        if graph[fr] + point >  graph[to] and  graph[fr] != INF:
            graph[to] = graph[fr] + point
            if to == N and i > N:
                print("inf")
                exit()

print(graph[-1])




