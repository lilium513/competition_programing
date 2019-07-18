import itertools
N = input()
l = list(map(int,input().split(" ")))
l.sort()
N = int(N)
flag = True
NUM = 10** 9 + 7
num = 2
if N %2 != 0:
    if l[0] != 0:
        flag =False
    num = 2
    start = 1
else:
    num = 1
    start = 0
for i in range(start,N,2):
    if l[i] != l[i + 1]   or l[i] != num:
        flag = False
    else:
        num += 2
if flag:
    temp = (N - start)//2
    print(2 ** temp %NUM )
else:
    print(0)
