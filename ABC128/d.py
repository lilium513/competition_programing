N,K = list(map(int,input().split(" ")))
Vs = list(map(int,input().split(" ")))
rev = Vs[::-1]
ans = -(10e15)
for b in range(K+1):
    lr = min(K - b,N)
    for l in range(lr + 1):
        rlim = min(lr - l,N)
        for r in range(rlim+1):
            temoti = []
            temoti.extend(Vs[:l])
            temoti.extend(rev[:r])
            temoti.sort()
            tempans = sum(temoti)
            toridasi = 0
            for num in temoti:
                if toridasi == b: #上限回数取り出してたら終わり
                    break
                if num < 0:
                    tempans -= num
                    toridasi += 1
                else:
                    break

            if tempans > ans:
                ans = tempans
print(ans)