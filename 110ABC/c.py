s1 = input()
s2 = input()
di1 = {} #s1 → s2 の対応表
di2 = {} #s2 → s1 の対応表

ans = "Yes"
for c1,c2 in zip(s1,s2):
    if c1 not in di1:
        di1[c1] = c2
    else:
        if di1[c1] != c2:
            ans = "No"

    if c2 not in di2:
        di2[c2] = c1
    else:
        if di2[c2] != c1:
            ans = "No"

print(ans)