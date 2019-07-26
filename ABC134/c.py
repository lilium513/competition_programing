
N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))
temp = nums[:]
temp.sort(reverse=True)
ma = temp[0]
ma2 = temp[1]
# print(nums)
for i in nums:
    if i == ma:
        print(ma2)
    else:
        print(ma)
