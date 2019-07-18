import math
N =int(input() )
trains = [list(map(int,input().split(" "))) for _ in range(N-1)]
for s in range(N):
    ans = 0
    spent = 0
    arrived_time = 0
    for train in trains[s:]:
        c,s,f = train
        n = max(0,math.ceil((ans-s) /f))
        wait = n * f + s - ans
        #待機時間

        ans += c + wait

    print(ans)