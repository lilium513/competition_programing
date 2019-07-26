import math
N = int(input())
lim = int(math.sqrt(N))
ans = 9999
for i in range(1,lim+1):
    if N % i == 0:
        temp = N //i
        cand = max(len(str(i)),len(str(temp)))
        if ans > cand:
            ans = cand


print(ans)