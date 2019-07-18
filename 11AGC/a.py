
N,C,K= list(map(int,input().split(" ")))

ans = 1
passed = 0
nums = [ int(input()) for _ in range(N)]
nums.sort()
before = nums[0]
c = 1

for t in nums[1:]:

    c += 1
    passed += t - before
    if passed > K or c > C: #次のバス
        c = 1
        passed = 0
        ans += 1
    before = t
print(ans)


