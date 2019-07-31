import math
N = int( input())
temp = list(map(int,input().split(" ")))
temp.sort()
def GCD( a,  b ):
    if b == 0:
        # print("--" * 10)
        return a
    else:
        # print(b)
        return GCD(b, a % b)
ans = [GCD(temp[0],temp[1])]
for i,num in enumerate(temp[2:]):
    ans.append(GCD(ans,num))

print(ans)