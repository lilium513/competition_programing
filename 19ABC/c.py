import math
N = int( input())
temp = list(map(int,input().split(" ")))
twojo = [2 ** i for i in range(31)]
l = len(twojo)
for i in range(N):
    div = 1
    for j in range ( l ):
        if temp[i] % twojo[j] == 0:
            div = twojo[j]
        else:
            break
    temp[i] //= div
temp = list(set(temp))
print(len(temp))