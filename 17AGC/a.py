
def get_fact(n):
    temp = 1
    fac = [1]
    for i in range(1, n + 1):
        temp *= i
        fac.append(temp)
    return fac
def get_comb(n):  # n C n まで

    fac = get_fact(n)
    com  = [["error" for _ in range(n+1)] for _ in range (n + 1)]
    for i in range(n + 1):
        for j in range(i + 1):
            if  i >= j:
                com[i][j] = fac[i] // (fac[i-j] * fac[j])

    return com

N ,P  =list(map(int,input().split(" ")))
As = list(map(int,input().split(" ")))
As = list(map(lambda x :x%2 ,As))
one = As.count(1)
zero =As.count(0)
ans = 0
com = get_comb(N)
z = 0
for i  in range(zero + 1):
    z += com[zero][i]
o = 0
if P == 0:
    for i in range(0,one + 1 , 2):
        o += com[one][i]
else:
    for i in range(1,one + 1 , 2):
        o += com[one][i]
print(o * z)
