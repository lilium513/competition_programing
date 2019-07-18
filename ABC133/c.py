


def do():
    L, R = list(map(int, input().split(" ")))
    ans = 10 ** 15
    if R - L < 5000: #差が小さい場合は全探索
        for i in range(L,R + 1):
            for j in range(i+1,R + 1):
                if (i*j) % 2019 < ans:
                    ans = (i*j) % 2019
    else:#そうでなければ確実に一つ2019の倍数がある
        ans = 0
    print(ans)

