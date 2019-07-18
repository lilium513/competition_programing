from collections import defaultdict
import math
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors


N = int(input())
lim = int(10e12 ** (1/2))
lim = 10000000
ans = 0
yakusu = make_divisors(N)
for i in yakusu:
    if N%i == 0 and i < N:
        temp = N//i
        if temp > i:
            ans += N//i -1
        # print(i)
print(ans)