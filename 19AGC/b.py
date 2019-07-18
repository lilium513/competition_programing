import math

temp = input().split(" ")
k = int(temp[3])
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
xy =[]
yz = []
xz = []
lim = min([3000**(1/3) ,k**(1/3)])
lim = math.ceil(lim)
for a1 in c1[:lim]:
    for a2 in c2[:lim]:
        xy.append(a1+a2)
for a1 in c1[:lim]:
    for a3 in c3[:lim]:
        xz.append(a1+a3)
for a2 in c2[:lim]:
    for a3 in c3[:lim]:
        yz.append(a2+a3)
ans.sort(reverse=True)
print(ans)
for i in range(k):
    print(ans[i])