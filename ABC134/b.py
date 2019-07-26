import math
n,d =  list(map(int,input().split(" ")))

temp = d * 2 + 1

print(  math.ceil(n/temp))

