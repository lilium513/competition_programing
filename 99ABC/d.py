import collections
import itertools
def warshall_floyd(graph):
    INF = 10 ** 10
    n = len(graph)
    cost = [[INF for i in range(n )]for j in range(n)]
    for i in range(0,n):
        for j in range(0,n):
            for k in range(0,n):
                cost[i][j] = min(graph[i][j],graph[i][k] +graph[k][j] )

    return cost


N,C = list(map(int,input().split(" ")))
graph = [list(map(int,input().split(" ")) )for _ in range(C)]

cost = warshall_floyd(graph)
masses = [list(map(int,input().split(" ")) )for _ in range(N)]

c1 = collections.defaultdict(lambda :0)
c2 = collections.defaultdict(lambda :0)
c3 = collections.defaultdict(lambda :0)
cs = [c1,c2,c3]

for i in range(N):
    for j in range(N):
        cs[(i + j) % 3][masses[j][i]] += 1
print(cs)
ans = 10 ** 10

com = list(itertools.permutations(list(range(0,C)),3))
for colors in com: #a,b,cが色を変えた先

    scores = [0,0,0]
    temp_num = 0
    for i in range(3):
        color = colors[i]
        temp = cs[i]
        for k,v in temp.items():
            temp_num += cost[k-1][color] * v
    if ans> temp_num:
        ans = temp_num

print(ans)