import itertools
H,W = list(map(int,input().split(" ")))
mass = []
for _ in range(H):
    mass.append(input())


dirs = [[0,1],[1,0],[0,-1],[-1,0]]

flag = True
for h,row in enumerate(mass):
    for w,temp in enumerate(row):
        if temp == "#":
            cont = False
            for dir in dirs:
                x = dir[0]
                y = dir[1]
                hy =h+y
                wx = w + x
                if  hy < 0 or wx< 0 or wx==W or hy == H:
                    continue
                else:
                    if mass[hy][wx] == "#":
                        cont = True
            if not cont:
                flag = False
if flag:
    print("Yes")
else:
    print("No")

