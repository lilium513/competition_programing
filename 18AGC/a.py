import math
#試し割法
def factorize(n):
    b = 2
    fct = []
    while b * b <= n:
        while n % b == 0:
            n //= b
            fct.append(b)
        b = b + 1
    if n > 1:
        fct.append(n)
    return fct
def main():
    N, P = map(int, input().split())
    ans = 1
    soinsu = factorize(P)
    # print(soinsu)
    di = {}
    for i in soinsu:
        if i not in di:
            di[i] = 1
        else:
            di[i] += 1
    for k,v in di.items():
        kosu = v//N

        if kosu > 0:
            ans *= (k ** kosu)

    print(ans)

if __name__ == "__main__":
    main()