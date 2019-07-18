from itertools import accumulate
import sys
def rec (y,x,Ynokori,Xnokori,kuro,siro):
    global ans
    ktemp = 0
    stemp = 0

    if mass[y][x] == "#":
        ktemp += 1
    if mass[y][x] == "." or  mass[y][x] == "G":
        stemp += 1

    if Xnokori  == 0 and Ynokori ==0:
        temp = T -siro-1
        if kuro != 0:
            temp =  (temp)//kuro
        ans = max(ans,temp)
        return 0

    if Ynokori != 0 :
        rec(y + yDis, x, Ynokori - 1, Xnokori, kuro + ktemp, siro+stemp)
    if Xnokori != 0 :
        rec(y, x + xDis, Ynokori , Xnokori - 1, kuro + ktemp, siro + stemp)


    return 0

sys.setrecursionlimit(773105)

H, W, T = list(map(int, input().split(" ")))
mass = []
start = 0
goal = 0
ans = 0
for h in range(H):
    temp  = input()
    mass.append(temp)
    if "S" in temp:
        start = (h,temp.index("S"))
    if "G" in temp:
        goal= (h,temp.index("G"))
xDis = 1 if start[1] <  goal[1] else -1
yDis = 1 if start[0] <  goal[0] else -1


rec(start[1],start[0],  goal[0] - start[0],goal[1] - start[1] ,0,0)
print(ans)