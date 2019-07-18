import itertools
import math
N = input()
N = int(N+1)
math.floor(N)
temp = math.log2(N)

if N ==1:
    ans = "Aoki"


elif temp % 2==0:

    ans = "Takahashi"

else:
    ans = "Aoki"
print(ans)