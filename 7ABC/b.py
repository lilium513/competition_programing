import math
import queue
R,C = list(map(int,input().split(" ")))
sy,sx = list(map(int,input().split(" ")))
sx -= 1
sy -= 1

gy,gx = list(map(int,input().split(" ")))
gx-=1
gy-=1
mass = [input() for _ in range(R)]
tejun =[ [-1 for i in range(C)] for j in range(R)]
xy = [(1,0),(0,1),(-1,0),(0,-1)]
q = queue.Queue()
q.put((sx,sy))
tejun[sy][sx] = 0
while True:
    if q.empty():
        break
    x,y = q.get()
    if x == gx and y == gy:
        break
    for go in xy:
        xmove,ymove = go
        if 0<=x + xmove < C and 0<=y + ymove < R and mass[y + ymove][x+xmove] != "#":
           if tejun[y + ymove ][x + xmove ] == -1:
               tejun[y + ymove][x + xmove]  = tejun[y][x] + 1
               q.put((x + xmove,y + ymove))
print(tejun[gy][gx])