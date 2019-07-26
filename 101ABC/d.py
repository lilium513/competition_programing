import statistics
import math
N = int( input())

for i in range(1,10):
    print(i)
    N -= 1
    if N == 0:
        break
i = 1
while N > 0:
    print(str(i) + "9")
    N -=1