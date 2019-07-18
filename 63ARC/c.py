S = input()
now = S[0]
ans = 0
for c in S[1:]:
    if c != now:
        now = c
        ans += 1
print(ans)