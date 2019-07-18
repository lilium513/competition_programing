from collections import defaultdict

di = defaultdict(lambda :0)
S = input()
for c in S:
    di[c] += 1
flag = True
for v in di.values():
    if v %2 == 1:
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")



