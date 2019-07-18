from math import factorial
W,H =list(map(int,input().split(" ")))

NUM = 10** 9 + 7
print      (factorial(W+H-2)//(factorial(W-1) * (factorial(H-1) ))% NUM )