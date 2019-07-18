import itertools
import math
N = int(input())
nums = list(map(int,input().split(" ")))
nums.sort()
ind = 0
maxcolor = 0
mincolor = 0
cols = []
while True:
    if ind == N or nums[ind] >= 3200:
        break
    cols.append(nums[ind]//400)
    ind += 1

cols = list(set(cols))
over3200 = nums[ind:]
maxcolor = mincolor = len(cols) #3200未満の色の種類

if len(over3200) > 0:
    if mincolor > 0: #3200以下が一人でもいたらそれに合わせて終わり
        pass
    else:
        mincolor = 1 #3200以下が居なかったら全員同じ色に

maxcolor = maxcolor + len(over3200)
print(mincolor,maxcolor)