

import math


H,W = list(map(int,input().split(" ")))
x1 = 0
y1 = 0
x2 = 0
y2 = 0
cond = 0
mass = []
for _ in range(H):
    mass.append(list(map(int, input().split(" "))))

ans = []
for y,As in enumerate(mass):
    for x,a in enumerate(As):
        if a % 2 == 1:
            if cond %2 == 0:
                x1 = x + 1
                y1 = y + 1
                cond += 1
            else:
                x2 = x + 1
                y2 = y + 1
                if x2 > x1:
                    step = -1
                else:
                    step = 1
                cot  = abs(x2 -x1)
                for _ in range(cot): #横に動く
                    ans.append([y2,x2,y2,x2+step])
                    x2 = x2+step
                cot = abs(y2 -y1)
                for _ in range(cot):
                    ans.append([y2,x2,  y2 -1, x2])
                    y2 = y2 -1
                cond += 1
n = len(ans)
print(n)
for temp in ans:
    a,b,c,d = temp
    print(a,b,c,d)