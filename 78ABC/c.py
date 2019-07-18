N,M = list(map(int,input().split(" ")))
kaisu = 2 ** M
time = (N-M)*100 + M*1900
print(time*kaisu)