import itertools
l1 = list(map(int,input().split(" ")))
l2 = list(map(int,input().split(" ")))
l3 = list(map(int,input().split(" ")))
diffs = []
for i in range(3):
    diffs.append(l1[i]-l2[i])
if set()