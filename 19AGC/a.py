Q,H,S,D = list(map(int,input().split(" ")))
N = int(input())
min05 = min(Q*2,H)
min1 = min(min05*2 ,S)
min2 = min(min1 * 2 , D)

if N %2 == 0:
    print(N//2 * min2)

else:
    print((N-1)//2 * min2 + min1 )