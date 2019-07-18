import itertools
l1 = list(map(int,input().split(" ")))
l2 = list(map(int,input().split(" ")))
l3 = list(map(int,input().split(" ")))

flag = True
diffs = []
for i in range(3):
    diffs.append(l1[i]-l2[i])

if len(set(diffs)) != 1:
    flag = False


diffs = []
for i in range(3):
    diffs.append(l2[i]-l3[i])

if len(set(diffs)) != 1:
    flag = False

if flag:
    print("Yes")
else:
    print("No")