import math
N = input()
N = int(N)

ans = (N //11)*2
nokori = N % 11
ans += math.ceil(nokori/6)
print(ans)