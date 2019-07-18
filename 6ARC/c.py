import math
N = int( input())
dans = [int(input()) for _ in range(N)]
put = [dans[0]]
for dan in dans[1:]:
    for i in range(len(put)):
        if put[i] >= dan:
            put[i] = dan
            break
    else:
        put.append(dan)

    put.sort()


print(len(put))