N,Z,W = list(map(int,input().split(" ")))
nums = list(map(int,input().split(" ")))
c1 = abs(nums[-1]-W)
c2 = -100
if len(nums) > 1:
    c2 = abs(nums[-1]-nums[-2])
print(max(c1,c2))