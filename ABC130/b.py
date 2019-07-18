N,X =  list(map(int,input().split(" ")))
Ls = list(map(int,input().split(" ")))

d = 0
ans = 1
for l in Ls:
    d += l
    if d <= X:
        ans+=1
print(ans)