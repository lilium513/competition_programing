
N = int(input())
As =   list(map(int,input().split(" ")))
Bs =   list(map(int,input().split(" ")))
ans = 0
for i in range(N):
    ans += min(As[i],Bs[i]) #i町での討伐数
    Bs[i] = max(Bs[i] - As[i] , 0 ) #勇者iの余力
    ans +=min(As[i + 1],Bs[i]) #i + 1町での討伐数
    As[i + 1] = max(As[i + 1] - Bs[i], 0)
    # if As[i] <= Bs[i]: #全員倒せた
    #     ans += As[i]
    #     Bs[i] -= As[i]
    #     if As[i + 1] <= Bs[i]:
    #         ans += Bs[i]
    #
    #
    #     As[i + 1] = max ( As[i + 1] - Bs[i] ,0)
    #
    # else: #全員は倒せなかった
    #     ans += Bs[i]

print(ans)