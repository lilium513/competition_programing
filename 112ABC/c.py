import math
N = int( input())
di = [[-1] * 101 for i in range(101)]



ps = []
basep=0
for k in range(N):
    temp = list(map(int,input().split(" ")))
    ps.append(temp)
    if temp[2] != 0:
        basep = temp
# print(ps)
basex = basep[0]
basey = basep[1]
baseh = basep[2]
# print(basep)
flag = True
for i in range(101):
    for j in range(101):
        flag = True
        X = i
        Y = j
        H = abs(basex - X) + abs(basey - Y) + baseh
        for l,p in enumerate(ps):
            x = p[0]
            y = p[1]
            h = p[2]
        #     print(l,":",p)       
            if max(H -abs(X-x)-abs(Y-y),0) != h: 
                flag = False
                # print("x,y,h:",x,y,h)
                # print("X,Y,H:",X,Y,H)

                # print("break")
                break
        if flag:
                print(X,Y,H)
                break
    if flag:
        break

#         di[i][j].append(h + abs(x-i)  + abs(y-j))
#         print
# for i in range(0,101):
# for j in range(0,101):
#         if len(list(set(di[i][j]))) == 1:
#         print(i,j,di[i][j][0])
