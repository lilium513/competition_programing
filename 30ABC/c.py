import itertools
N,M =list(map(int,input().split(" ")))
X,Y =list(map(int,input().split(" ")))
As =list(map(int,input().split(" ")))
Bs =list(map(int,input().split(" ")))

a = b = 0
t= 0
ans = 0
here = 0 # 0→ A 1 → B
while True:

    if here == 0:
        while True:
            if a == N :
                print(ans)
                exit()
            if As[a] >= t:
                t =  As[a] + X
                here = 1
                break
            else:
                a+=1
    if here == 1:
        while True:
            if b == M:
                print(ans)
                exit()
            if Bs[b] >= t:
                t =  Bs[b] + Y
                here = 0
                ans += 1
                break
            else:
                b+=1