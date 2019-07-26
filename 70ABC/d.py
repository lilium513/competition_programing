import itertools
import math
def gcd(a,b):
    r = a % b
    if r == 0:
        return b
    return gcd(b,r)

def lcm(a,b):
    return (a * b)//gcd(a,b)

N = int(input())
temp = 1
for _ in range(N):
    num = int(input())
    temp = lcm(temp,num)
print(temp)