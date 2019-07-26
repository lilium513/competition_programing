from itertools import accumulate
import sys
def rec (y,x,Ynokori,Xnokori,kuro,siro):
    global ans

    if mass[y][x] == "." or mass[y][x] ==  "G":
        siro+= 1
    elif mass[y][x] == "#":
        kuro+= 1

    if Ynokori > 0:
        rec(y + yDis, x, Ynokori -1 , Xnokori, kuro  ,siro )
    if Xnokori > 0:
        rec(y , x + xDis, Ynokori , Xnokori -1 , kuro , siro)

    if Ynokori == 0 and Xnokori == 0:
        ans = max(ans,(T-siro)//kuro  )

sys.setrecursionlimit(77310577)

H, W, T = list(map(int, input().split(" ")))
mass = []
start = 0
goal = 0
ans = 1
for h in range(H):
    temp  = input()
    mass.append(temp)
    if "S" in temp:
        start = (h,temp.index("S"))
    if "G" in temp:
        goal= (h,temp.index("G"))
xDis = 1 if start[1] <  goal[1] else -1
yDis = 1 if start[0] <  goal[0] else -1


rec(start[0], start[1], abs(goal[0] - start[0]),abs(goal[1] - start[1] ),0,0)
print(ans)

