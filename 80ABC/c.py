
N = input()
N = int(N)
Fs =  [list(map(int,input().split(" "))) for _ in range(N)]
Ps =  [list(map(int,input().split(" "))) for _ in range(N)]
ans = -(10**10)
for flag in range(1,2 ** 10): #開店スケジュールに対応
    temp = 0
    for shop in range(N):
        op = 0

        for i in range(10): #曜日に対応
            if flag & (1 << i):
                c = 1#ある曜日にやっているか
            else:
                c = 0
            if Fs[shop][i] * c == 1:
                op += 1

        temp +=Ps[shop][op]
    if temp > ans:
        ans =temp
print(ans)