import itertools
import sys
sys.setrecursionlimit(10000000)
MAZE =[]
reached =[]
W,H = 0,0
SX,SY = 0,0
GX,GY = 0,0
def rec (x,y):

    if y >= H or x >= W or x< 0 or y < 0 or MAZE[y][x] == "#":
        return
    if reached[y][x]:
        return
    if x == GX and y == GY:
        print("Yes")
        exit()
    reached[y][x] = True

    rec(x+1,y)
    rec(x-1,y)
    rec(x , y+1)
    rec(x,y-1)


def do():
    global W,H,SX,SY,GX,GY
    H,W= list(map(int,list(input().split(" "))))

    for i in range(H):
        temp = input()
        if "s" in temp:
            SX,SY =temp.index("s"),i
        if "g" in temp:
            GX,GY =temp.index("g"),i
        MAZE.append(temp)
        reached.append(len(temp)*[False])
    rec(SX,SY)
    print("No")




if __name__ == "__main__":
    do()