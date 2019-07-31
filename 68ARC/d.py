from collections import defaultdict

di = {}
N = int(input())
As = list(map(int,input().split(" ")))

for a in As:
    if a not in di:
        di[a] = 1
    else:
        di[a] += 1
even = 0
odd = 0
for v in di.values():
    if v % 2 == 0:
        even += 1
    if v %2 == 1 and v != 1:
        odd += 1
em = even * 2
om = max(odd - even , 0) * 2

print(N - em - om)
