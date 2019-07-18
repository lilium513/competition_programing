import itertools
N = input()
N = int(N)
querys = []
graph = {}
for i in range(N-1):
    l = list(map(int,input().split(" ")))
    querys.append(l)
    a = l[0]
    b = l[1]
    if a not in graph:
        graph[a] = []
    graph[a].append(b)
    if b not in graph:
        graph[b] = []
    graph[b].append(a)

# print(graph)
graph = sorted(graph.items(), key=lambda x:len(x[1]))
nums = list(map(int,input().split(" ")))
nums.sort()
ans_graph = {}

for num,temp in zip(nums,graph):
    ans_graph[temp[0]] = num
ans = 0
for temp in querys:
    a,b = temp
    ans += min(ans_graph[a],ans_graph[b])

print(ans)
ans_graph= sorted(ans_graph.items(), key=lambda x:x[0])
ans = list(map(lambda x:str(x[1]),ans_graph))
print(" ".join(ans))