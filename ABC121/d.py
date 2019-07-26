def F(x): # 0 から xまでの排他的論理和の和
    if x % 2 == 1:
        if (x + 1)  % 4 == 0:
            return 0
        else:
            return 1
    else:
        return F(x-1) ^ x


A,B = list(map(int,input().split(" ")))
print(F(A - 1) ^ F(B))

