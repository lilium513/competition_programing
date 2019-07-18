
from math import sqrt
from collections import defaultdict
def furui(N):
    primes = []
    nums = list(range(2,N+100))#探索リスト
    limit = sqrt(N+1)

    while True:
        p = nums[0]
        if p > limit:
            primes += nums
            return primes

        primes.append(p)
        nums = [num for num in nums if num % p != 0]




N = int(input())
DIV = 10**9 + 7
primes = furui(N)
di = defaultdict(lambda :0)
for i in range(2,N+1):
    temp = i
    for p in primes:
        while True:
            if temp % p == 0:
                di[p] += 1
                temp /=p
            else:
                break

ans = 1
for v in di.values():
    ans *= (v+1)

print(ans%DIV)