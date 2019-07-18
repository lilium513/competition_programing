N = int(input())
nums = list(map(int,input().split(" ")))
minus = 1
for num in nums:
    if num %2 == 0:
        minus *= 2

print(3 ** N -minus)