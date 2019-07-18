N,A,B =  list(map(int,input().split(" ")))
S = input()
for p in S:
    if p=="a":
        if A > 0:
            print("Yes")
            A -= 1
        elif B > 0:
            print("Yes")
            B -= 1
        else:
            print("No")
    if p=="b":
        if B > 0:
            print("Yes")
            B -= 1
        else:
            print("No")

    if p == "c":
        print("No")
