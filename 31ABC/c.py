import itertools
N =int(input())

As =list(map(int,input().split(" ")))
ans = []
for i in range(N):
    takmax = aomax =  -(10**10)
    for j in range(N):
        if i == j:
            continue
        if i > j:
            l = j
            r = i
        if i < j:
            l = i
            r = j
        tak = sum(As[l:r + 1:2])
        aok = sum(As[l+1:r + 1:2])

        if aok > aomax:
            aomax = aok
            takmax = tak
    ans.append(takmax)


print(max(ans))