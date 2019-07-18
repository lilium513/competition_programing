ans = 9999
S = input()
cands = list(set(list(S)))
for c in cands:
    temp = max(list(map(len,S.split((c)))))
    ans = min(ans,temp)
print(ans)