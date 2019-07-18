from collections  import defaultdict
d = defaultdict(lambda :0)
N = int(input())
blues =[(input()) for _ in range(N)]

M = int(input())
reds =[(input()) for _ in range(M)]

for blue in blues:
    d[blue] += 1
for red in reds:
    d[red] -= 1

print(max(0,max(d.values()  )))