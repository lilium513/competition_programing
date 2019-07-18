import itertools
N,M = list(map(int,input().split(" ")))
humans = []
points = []

for _ in range(N):
    humans.append(list(map(int,input().split(" "))))
for _ in range(M):
    points.append(list(map(int, input().split(" "))))
for human in humans:
    mindis = 10e10
    minind = -1
    a = human[0]
    b = human[1]
    for ind,point in enumerate(points):
        c = point[0]
        d = point[1]
        dist = abs(a-c) + abs(d-b)
        if mindis > dist:
            minind = ind + 1
            mindis = dist
    print(minind)
