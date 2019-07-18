import math
S = input()
l = len(S)
cs = ["A","G","C","T"]
ma = 0
for i in range (l):
    for j in range(i,l+1):
        sub = S[i:j]

        for c in sub:
            if c not in cs:
                break
        else:
            if len(sub) > ma:
                ma = len(sub)
print(ma)