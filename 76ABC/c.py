import itertools
import math



def do():
    S = input()
    T = input()
    s = len(S)
    t = len(T)
    flag = False
    for i in range(s-t,-1,-1):
        if S[i] == "?" or S[i] ==T[0]:
            flag = True
            for j in range(t):
                if T[j] == S[i+j] or S[i+j] == "?":
                    pass
                else:
                    flag = False
        if flag:
            break
    if flag:
        ans = list(S)
        for k in range(i,i+t):
            ans[k] = T[k-i]
        for i,temp in enumerate(ans):
            if temp == "?":
                ans[i] = "a"
        print("".join(ans))
    else:
        print("UNRESTORABLE")





if __name__ == "__main__":
    do()