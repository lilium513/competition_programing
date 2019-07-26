import math


def rec(total,banme):
    global co
    if banme == N:
        co += 1
        if total == 0:
            print("Found")
            exit()

    else:
        for i in range(K):
            rec(total^nums[banme][i] , banme + 1)

N,K= list(map(int,input().split(" ")))
nums = [list(map(int,input().split(" "))) for _ in range(N)]
anss = []
co = 0
for i in range(K):
    rec(nums[0][i],1)


print("Nothing")