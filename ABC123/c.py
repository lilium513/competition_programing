import math
temp = input().split(" ")
k = temp[2]
c1 = input().split(" ")
c1 = list(map(int,c1))
c1.sort(reverse=True)
c2 = input().split(" ")
c2 = list(map(int,c2))
c2.sort(reverse=True)
c3 = input().split(" ")
c3 = list(map(int,c3))
c3.sort(reverse=True)
ans = []
for cc1 in c1:
    for cc2 in c2[:20]:
        for cc3 in c3[:20]:
            ans.append(cc1+cc2+cc3)
for cc1 in c1[:20]:
    for cc2 in c2[:20]:
        for cc3 in c3:
            ans.append(cc1+cc2+cc3)

for cc1 in c1[:20]:
    for cc2 in c2:
        for cc3 in c3[:20]:
            ans.append(cc1+cc2+cc3)

ans.sort(reverse=True)
for i in range(k):
    print(ans[k])