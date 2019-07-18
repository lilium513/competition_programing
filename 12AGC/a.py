N = input()
N =int(N)
nums= list(map(int,input().split(" ")))
nums.sort()
ans = 0

for _ in  range(N):
    nums.pop()
    ans += nums.pop()
print(ans)