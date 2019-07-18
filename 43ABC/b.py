import itertools
S = input()
S = list(S)
ans = []
for s in S:
    if s == "B":
        if len(ans) > 0:
            ans.pop(len(ans) -1 )
    else:
        ans.append(s)
print("".join(ans))