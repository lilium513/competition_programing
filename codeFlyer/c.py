import math
N,D = list(map(int,input().split(" ")))
Xs = list(map(int,input().split(" ")))

ans = 0
l = 0
r = 2
c = 1


while r < N:
    # rを動かす
    # rlが D を超えたら +1
    # lcをD以下である限り cを動かす
    # lcがDを超えたらlcがD未満になるように
    if abs(Xs[l] - Xs[c]) <= D and  abs(Xs[r] - Xs[c]) <= D and abs(Xs[l] - Xs[r]) > D: #条件を満たしたら
        ans += 1 #とりあえず +1

        # 1.lとrを固定してcを右に動かす
        #  ij が K を超えたら  ijがK以下になるまでl を右に動かす
        #

        while abs(Xs[l] - Xs[c]) <= D and  abs(Xs[r] - Xs[c]) <= D and abs(Xs[l] - Xs[r]) > D and l < c:
            l += 1
            ans += 1

        while  abs(Xs[l] - Xs[c]) <= D and  abs(Xs[r] - Xs[c]) <= D and abs(Xs[l] - Xs[r]) > D and c < r:
            c += 1
            ans += 1
        while  abs(Xs[l] - Xs[c]) <= D and  abs(Xs[r] - Xs[c]) <= D and abs(Xs[l] - Xs[r]) > D and  r < N :
            r += 1
            ans += 1
    else:

        if abs(Xs[l] - Xs[r]) <= D:
            r += 1
        elif


print(ans)
