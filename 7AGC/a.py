import itertools
def rec(x,y):
    if x == W - 1 and y == H -1:
        return True
    if x + 1 < W and masses[y][x + 1] != ".":
        return  rec(x + 1,y)
    if y + 1 < H and masses[y + 1][x ] != ".":
        return rec(x,y + 1)

    return False

H,W= list(map(int,input().split(" ")))
masses = [input() for _ in range(H)]

if rec(0,0):
    print("Possible")
else:
    print("Impossible")