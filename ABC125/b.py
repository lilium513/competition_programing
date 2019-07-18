N = int(input())
l1 = list(map(int,input().split(" ")))
l2 = list(map(int,input().split(" ")))
ans = 0
for v,c in zip(l1,l2):
    if v - c > 0:
            ans += (v-c)

print(ans)    