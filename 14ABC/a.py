from itertools import accumulate

N = int(input())
colors = [0] * 1000002
for _ in range(N):
    s,g= list(map(int,input().split(" ")))
    colors[s] += 1
    colors[g+1] -= 1
# print(colors[:10])

colors = accumulate(colors[:1000001])
print(max(colors))