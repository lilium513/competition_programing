import itertools
import math
N = int(input())
S = input()
l = len(S)


#oxooxoxoox
#s → 1 w→-1
temp = []
for c in S:
    if c == "o":
        temp.append(1)
    else:
        temp.append(-1)

S = temp

flag = False
for i in [1,-1]: # 1匹目
    for j in [1,-1]: #2匹目
        nums = [i,j]
        temp = i * j
        for k in range(1,N-1):
            nums.append(temp * S[k])
            temp = nums[k] * nums[k  + 1]
        if temp * nums[0] == S[-1]  and nums[-1] * nums[0] * nums[1] == S[0]:
            flag = True
            break
    if flag:
        break

if flag:
    for num in nums:
        if num == -1:
            print("W",end="")
        else:
            print("S", end="")

else:
    print(-1)

