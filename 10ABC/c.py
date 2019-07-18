import math


sx,sy,gx,gy,t,v = list(map(int,input().split(" ")))
l = t * v
N = input()
N =int(N)

for _ in range(N):
    x,y= list(map(int,input().split(" ")))
    dist = math.sqrt((sx-x)** 2 + (sy-y)** 2) + math.sqrt((gx-x)** 2 + (gy-y)** 2)
    if dist <= l:
        print("YES")
        exit()

print("NO")