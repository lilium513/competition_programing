import math
N = int(input())
As =   list(map(int,input().split(" ")))

Asorted = As[:]
Asorted.sort()
diff = 0
for i in range(N):
    if Asorted[i] != As[i]:
        diff += 1
maif diff == 0 or diff == 2:
    print("YES")
else:
    print("NO")

