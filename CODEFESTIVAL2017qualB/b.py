from collections import defaultdict
N = int(input())
Ds =  list(map(int,input().split(" ")))
M = int(input())
Ts =  list(map(int,input().split(" ")))

prob = defaultdict(lambda :0)
for d in Ds:
    prob[d] += 1

ans = "YES"
for t in Ts:

    if prob[t] == 0:
        ans = "NO"
    prob[t] -= 1
print(ans)
