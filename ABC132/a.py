import collections

S = input()
d = collections.defaultdict(lambda :0)

for c in S:
    d[c] += 1

ans = "Yes"
if len(d) == 2:
    print("Yes")
else:
    print("No")

