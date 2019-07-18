import itertools
S  = input()
parts = S.split("+")
ans = 0
for part in parts:
    if "0" not in part:
        ans += 1
print(ans)