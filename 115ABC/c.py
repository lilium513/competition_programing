N,K= list(map(int,input().split(" ")))
nums = []
for i in range(N):
    nums.append(int(input()))
nums.sort()
r = 0
l = 0
ans = []
for i,num in enumerate(nums[:-(K-1)]):
    r = nums[i+K-1]
    l = num
    # print("l:",l,"//r:",r)
    ans.append(r-l)
print(min(ans))