import statistics
import math
N = int( input())
temp = list(map(int,input().split(" ")))
for i in range(len(temp)):
    temp[i] = (temp[i] - (i+1))

m = statistics.median(temp)
nums = list(map(lambda x:abs(x-m),temp))
ans = sum(nums)
ans = int(ans)
print(ans)