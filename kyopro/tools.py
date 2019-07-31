import heapq
def input_as_int():
    return list(map(int,input().split()))

def factorize(n):
    fct = []  # prime factor
    b, e = 2, 0  # base, exponent
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append((b, e))
        b, e = b + 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct


def get_comb(n):  # n C n まで

    fac = get_fact(n)
    com  = [["error" for _ in range(n+1)] for _ in range (n + 1)]
    for i in range(n + 1):
        for j in range(i + 1):
            if  i >= j:
                com[i][j] = fac[i] // (fac[i-j] * fac[j])

    return com

def gcd(a,b):
    r = a % b
    if r == 0:
        return b
    return gcd(b,r)

def lcm(a,b):
    return (a * b)//gcd(a,b)


def get_fact(n):
    temp = 1
    fac = [1]
    for i in range(1, n + 1):
        temp *= i
        fac.append(temp)
    return fac

def prime_method(graph):
    start = graph[0]
    n = len(graph)
    went = [False] * n #n個の点に行ったかという話
    edges = []
    for temp in start:
        heapq.heappush(edges,temp)
    went[0] = True
    cost = 0
    while len(edges) != 0:
        minedge = heapq.heappop(edges)
        if went[minedge[1]]:
            continue
        v = minedge[1]
        for temp in graph[v]:
            if not went[temp[1]]: #その頂点に行ってなければ
                heapq.heappush(edges,temp)
        went[v] = True
        cost += minedge[0]
    return cost
    # a[1] = [[2,3],[5,11]] → 点1からコスト2で頂点3に行ける辺、点1からコスト5で頂点11に行ける辺がある

def get_graph():
    n = input()
    graph = [input_as_int() for _ in range(n)]

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