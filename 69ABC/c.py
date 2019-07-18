import itertools
import math
N = int(input())
As =list(map(int,input().split(" ")))
odds = 0
two = 0
four = 0
nums = []
for a in As:
    if a % 2 == 1:
        odds += 1
    elif a % 4 == 0:
        four += 1
    else:
        two += 1
if odds > 0:
    nums.append(1)
    odds -= 1
elif two > 0:
    nums.append(2)
    two -=1
else:
    nums.append(4)
    four-=1
ans = "Yes"

if N==2:
    if As[0] * As[1]%4 !=0:
       ans = "No"
else:
    for i in range(1,N):
        if nums[i-1] == 1:
            if four > 0:
                nums.append(4)
                four -=1
            else:
                ans = "No"
                break
        elif nums[i - 1] == 2:
            if two> 0:
                nums.append(2)
                two -= 1
            elif four > 0:
                nums.append(4)
                four -=1
            else:
                ans = "No"
                break
        elif nums[i - 1] == 4:
            if odds> 0:
                nums.append(1)
                odds -= 1
            elif two> 0:
                nums.append(2)
                two -= 1
            elif four > 0:
                nums.append(4)
                four -=1

print(ans)