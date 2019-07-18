import itertools
import math
N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

nums.sort()
s = sum(nums)
ans = 0
if s % 10 != 0:
    ans = s
else:
    for num in nums:
        if num % 10 != 0:
           ans = s -num
           break

print(ans)