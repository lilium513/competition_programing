N = input()
N =int(N)
NGs = [int(input()) for _ in range(3)]

if N in NGs:
    print("NO")
else:
    co = 0
    for _ in range(100):
        if co + 3 not in NGs:
            co += 3
        elif co + 2 not in NGs:
            co += 2
        elif co + 1 not in NGs:
            co += 1
        else:
            print("NO")
            exit()
        if co >= N:
            print("YES")
            exit()
    print("NO")