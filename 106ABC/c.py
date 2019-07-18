def c():
    S = input()
    S = list(S)
    K = int(input())
    one = 0
    if K == 1:
        print(S[0])
        return 0
    else:
        for k in S:
            if k!="1":
                print(k)
                return 0
            else:
                one+=1
                if one == K:
                    print(1)
                    return 0
    print(1)
    return 0
if __name__ == '__main__':
    c()