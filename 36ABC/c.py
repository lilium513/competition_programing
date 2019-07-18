import itertools
N = input()
N = int(N)
nums = []
for i in range(N):
    temp = int(input())
    nums.append([i,temp])

nums.sort(key=lambda x:x[1])
c = 0
before = nums[0][1]
nums[0].append(c)
for num in nums[1:]:
    if before != num[1]:
        c += 1
        before = num[1]
    num.append(c)

nums.sort(key=lambda x:x[0])
# print(nums)

for num in nums:
    print(num[2])