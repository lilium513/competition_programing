N,L =  list(map(int,input().split(" ")))
m = 100000
su = 0
apples = []
for i in range(N):
    apples.append(L+i)
apples.sort(key=lambda x:abs(x))

print(sum(apples[1:]))
