import itertools
N = input()
N = int(N)
As = list(map(int,input().split(" ")))
ans = 0
l = 0
r = 0
before = 0
while l< N:
    while N > r >= l and before <As[r]:
        ans += r - l + 1
        before = As[r]
        r += 1
    before = 0
    l  = r
print(ans)