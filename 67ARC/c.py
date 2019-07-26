

N,A,B = list(map(int, input().split(" ")))
Xs = list(map(int, input().split(" ")))
Xs.sort()
ans = 0
for i in range(1,N ):
    ans += min (B,abs(Xs[i] - Xs[i-1])* A )

print(ans)