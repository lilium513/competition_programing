import statistics
import math
N,M= list(map(int,input().split(" ")))
yobos = []

for _ in range(M):
     yobos.append(list(map(int, input().split(" "))))
yobos.sort(key=lambda x:x[1])
right = yobos[0][1]
ans = 1
for yobo in yobos[1:]:
    if yobo[0] >= right:
        right = yobo[1]
        ans += 1
print(ans)


