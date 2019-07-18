import itertools
A,B,C,X, Y = list(map(int,input().split(" ")))
C2 = C * 2
ans = 0

if A > C2:
    if B < C2:
        b_maisu = max(0,Y-X)
        (X *  C2) + b_maisu * B


    else:
        print(max(X,Y)*C2)

if A < C2:
    if B < C2:
        print(A*X + Y * B)
    else:
        a_maisu = max(0,X-Y)
        (Y *  C2) + a_maisu * A

