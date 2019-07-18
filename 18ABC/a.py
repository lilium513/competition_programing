from itertools import accumulate

R,C,K = list(map(int,input().split(" ")))
mass = []

for i in range(R):
    mass.append(list(map(int, input().split(" "))))


xOK = [[False for i in range(C)] for j in range(R)]
yOK = [[False for i in range(C)] for j in range(R)]

for w in range(C):
    for h in range(R):
        if mass[h][w] == "x"
            pass
for h in range(R):
    for w in range(C):
