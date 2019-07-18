N = int(input()) * 2
Ls= list(map(int,input().split(" ")))
Ls.sort()
ans = 0
for i in range(0,N,2):
    ans+= Ls[i]

print(ans)