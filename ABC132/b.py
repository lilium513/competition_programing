n = int(input())
Ps =  list(map(int,input().split(" ")))
ans = 0
for i in range(0,n-2):
    a,b,c = Ps[i:i+3]
    temp = Ps[i:i+3]
    temp.sort()
    if temp[1] == b:
        ans += 1
print(ans)

