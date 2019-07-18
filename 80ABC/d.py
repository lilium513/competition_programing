import numpy as np
LIM = int(10e5)
time = [0] * (LIM+1)
ruiseki = [0] * (LIM+1)
N,C = list(map(int,input().split(" ")))
for _ in range(N):
    s,t,_= list(map(int, input().split(" ")))
    time[s] += 1
    time[t-1] += -1

for i in range(1,LIM+1):
    ruiseki[i] =  ruiseki[i-1] + time[i]
print(max(ruiseki))