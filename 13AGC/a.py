N = input()
N =int(N)
nums= list(map(int,input().split(" ")))
tendency = 0
ans = 1
diff = []
for i in  range(N -1 ):
    diff.append(nums[i+1] - nums[i])
print(diff)
for d in diff:
    if d > 0:
        now = 1
    elif d < 0:
        now = -1
    else:
        now = 0
    if tendency * now < 0 and tendency != now:
        ans += 1
        tendency = 0
    tendency = now
print(ans)
