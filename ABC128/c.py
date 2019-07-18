
N,M = list(map(int,input().split(" ")))
denkyus = []
for _ in range(M):
    denkyus.append(list(map(int,input().split(" ")[1:])))

ps  = list(map(int,input().split(" ")))
ans = 0
for i in range(2 ** N):
    temp = [0] * M
    for j in range(0,N): #スイッチを押していく
        if ((i >> j) & 1): #スイッチjが押されている状態ならスイッチを押す
            for di,denkyu in enumerate(denkyus):
                if j+1 in denkyu:
                    temp[di] +=1

    for pind,p in enumerate(ps):
        flag = True
        if temp[pind] %2 != p:
            flag = False
            break
    if flag:
        ans += 1
print(ans)








