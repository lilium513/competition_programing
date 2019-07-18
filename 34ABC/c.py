import itertools
S  = input()
if len(S) == 1:

    if S == "0":
        print(0)
    else:
        print(1)
else:
    l = len(S)
    for i in range(0,l,2):
        if S[i+1] == "*":
            if S[i] == 0 or S[i +2] == 0:

