N = input()
N =int(N)
nums= list(map(int,input().split(" ")))
tendency = 0
ans = 1
diff = []
for i in  range(N -1 ):
    diff.append(nums[i+1] - nums[i])
temp = 1
for i in range(len(diff) -1 ):
    temp *= diff[i] * diff[i + 1]
    if temp < 0:
        ans += 1


print(ans)
