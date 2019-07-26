def get_comb(n):  # n C n まで

    fac = get_fact(n)
    com  = [["error" for _ in range(n+1)] for _ in range (n + 1)]
    for i in range(n + 1):
        for j in range(i + 1):
            if  i >= j:
                com[i][j] = fac[i] // (fac[i-j] * fac[j])

    return com

def get_fact(n):
    temp = 1
    fac = [1]
    for i in range(1, n + 1):
        temp *= i
        fac.append(temp)
    return fac

n,m =list(map(int,input().split(" ")))
xs  =list(map(int,input().split(" ")))
ys =list(map(int,input().split(" ")))
MOD = (10**9) + 7

com = get_comb( max(n,m) )
ans = abs(xs[0]- xs[-1]) * abs(ys[0]- ys[-1]) * (com[n][2]) *  (com[m][2])

print(ans % MOD)