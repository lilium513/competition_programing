import math
math.factorial()
N = int( input())
nums = [int(input()) for _ in range(N)]
ans = 0

for i in range(N): #ターゲットとなるコイン
    co = 0
    target = nums[i]
    for num in nums:
        if target % num == 0:
            co += 1
    all = math.factorial(co)
    if co % 2 == 0:
        ans += all /2
    else:
        ans += all * ()



