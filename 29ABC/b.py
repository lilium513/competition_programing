N,K =list(map(int,input().split(" ")))
As = []
l = 0
ans = 0
for _ in range(N):
    As.append(int(input()))
total = 1
if 0 in As != -1:
    print(N)
else:
    for r in range(N):
        total*= As[r]
        while total > K :
            total/= As[l]
            l+=1
        if ans < r-l + 1:
            ans = r-l + 1

    print(max(ans,0))