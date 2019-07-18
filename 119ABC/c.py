import math

N,A,B,C = list(map(int,input().split(" ")))
ls = []
for i in range(N):
    ls.append(int(input()))

def fun(rec,a,b,c):
    if rec == N:
        return abs(A-a) + abs(B-b) + abs(C-c)-30 if a*b*c != 0 else 10e20

    ans =  [fun(rec + 1 ,a,b,c) , fun(rec + 1 ,a+ls[rec],b,c) + 10 ,fun(rec + 1 ,a,b+ls[rec],c) + 10 ,fun(rec + 1 ,a,b,c+ls[rec])+10] 
    return min(ans)
print(fun(0,0,0,0))


