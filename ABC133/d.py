import math


N = int(input())
As = list(map(int, input().split(" ")))
Asdouble = list(map(lambda x:x * 2,As))
AsdoubleRev = Asdouble[::-1]
temp = AsdoubleRev[1] - AsdoubleRev[0]
for a,b in zip(AsdoubleRev[1:-2],AsdoubleRev[2:-1]):
    temp = b -temp
M1 =Asdouble[0] - temp
M1 //=2

ans = [M1]
temp = M1
for a in Asdouble[:-1]:
    temp = a - temp
    ans.append(temp)
ans = list(map(str,ans))
print(" ".join(ans))