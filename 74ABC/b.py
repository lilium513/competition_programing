import itertools
import math
H,W = list(map(int,input().split(" ")))
mines = []
dirs = [0,1,-1]

for _ in range(H):
    l =input()
    mines.append(l)


for h in range(H):
    for w in range(W):

        if mines[h][w] == "#":
            print("#",end="")

        else:
            c = 0
            for d1 in dirs:
                for d2 in dirs:
                    x = w - d1
                    y = h - d2
                    if x >=0 and x < W and y >= 0 and y < H:
                        if mines[y][x] == "#":
                            c += 1
            print(c,end="")
    print()

