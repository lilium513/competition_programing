
N,M= list(map(int,input().split(" ")))
a,b,c = [N*2,N*3,N*4]
if a <= M <= b:
    print(N - M + a ,M - a,0)
elif b<= M <= c:
    print(0, N- M + b, M-b)
else:
    print(-1,-1,-1)
