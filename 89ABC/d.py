import itertools
H,W,D = (map(int,input().split(" ")))
As = []
dic  = {}
for h in range(H):
    As = tuple((map(int,input().split(" "))))
    for w,A in enumerate(As):
        dic[A] = (h,w)

# print(dic)

Q = int(input())
qs =tuple(tuple((map(int,input().split(" ")))) for _ in range(Q))

for L,R in qs:
    ans = 0
    for i in range(L + D  , R + 1 , D):
        x1,y1 = dic[i]
        x2,y2 = dic[i - D]
        ans += abs(x1-x2) + abs(y1-y2)

    print(ans)
