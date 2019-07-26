
import math
N,K = list(map(int,input().split(" ")))
X = list(map(int,input().split(" ")))
X.sort()
for i in range(K):
    temp = 0
    for x in X:
        print(x ^ i,":",str(bin(x ^ i)).zfill(8))
        temp += i^ x
    print(temp)
    print("---------------")