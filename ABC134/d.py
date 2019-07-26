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
As = list(map(int, input().split(" ")))
As = [0] + As
kosu = [0] *(N+1)

anss = []
bs  = [0] *(N+1)
for i in range(N,N//2,-1):
    if As[i] == 0:
        bs[i] =0
    else:
        bs[i] = 1

for i in range(N// 2, 0, -1):
    temp = 0
    for k in range(1,N + 1):
        if i * k > N:
            break
        if bs[i * k] == 1:
            temp += 1
    if As[i] % 2  != temp %2:
        bs[i] = 1
print(bs.count(1))
for i,num in enumerate(bs):
    if num == 1:
        print(i)
# print(M)
# for i in ans:
#     print(i)