import math
N,Q = list(map(int,input().split(" ")))
S = input()
nums = [0] * len(S)
for i,(s1,s2) in enumerate(zip(S[:-1],S[1:])):
    if s1 == "A" and s2 == "C":
        nums[i+1] += nums[i] + 1
    else:
        nums[i+1] += nums[i]
ls = []
rs = []
for i in range(Q):
    l,r = list(map(int,input().split(" ")))
    l -= 1
    r -= 1
    ls.append(l)
    rs.append(r)
for l,r in zip(ls,rs):
    print(nums[r]-nums[l])
