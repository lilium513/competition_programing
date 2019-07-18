import itertools
N = input()
l = list(map(int,input().split(" ")))
l.sort()
N = int(N)
flag = True

if N %2 == 0:
    for i in range(0 , N ,2):
        if l[i] == l[i+1] == i + 1 :
            pass
        else:
            flag = False
    if flag:
        print(2**(N//2))
    else:
        print(0)
else:
    of = 1
    if l[0] == 0:
        of = 1
    else:
        flag = False


    for i in range(of , N ,2):
        if l[i] == l[i+1] == i+of :
            pass
        else:
            flag = False
    if flag:
        print(2**(N//2))
    else:
        print(0)