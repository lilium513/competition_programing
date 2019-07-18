
N = int(input())
temp  = list(map(int, input().split(" ")))
temp.sort()
nums = temp[:]
nums[0] *= -1
for i in range(1,N-1):
    if nums[i] <0:
        nums[i] *= -1


nums = temp[:]
part = nums
part.sort(key=lambda x:abs(x))
sac = part[0] # 寄与しない数字
part = part[1:]
part.sort()


if len(nums) == 2:
    before = nums[1] - nums[0]
    print(nums[1],nums[0])
    exit()


before = part[0] - part[1]
ans = before
anss = []

anss.append((nums[0],nums[1]))
for p in part[1:]:
    anss.append((p,before))
    before = p -before
print(anss)
print(before - )




