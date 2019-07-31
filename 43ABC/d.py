import itertools
S = input()
l = len(S)

if l == 2:
    if S[0] == S[1]:
        print(1,2)
    else:
        print(-1, -1)
    exit()


else:
    for i in range(l-2):
        a,b,c = S[i],S[i+1],S[i+2]
        if a == b or b == c or a == c:
            print(i + 1,i+3)
            exit()

print(-1,-1)