N,Q = list(map(int,input().split(" ")))
kojis = []
hitos = {}

ans = [-1] * Q

for i in range(N):
    S,T,X =list(map(int,input().split(" ")))
    l = S -X
    r = T -X
    kojis.append((l,r,X))
kojis.sort(key=lambda x:x[2])


for i in range(Q):
    t = int(input())
    hitos[t] = (t,i)

for koji in kojis:
    rem = []
    l,r,x = koji
    for i,hito in enumerate(hitos.values()):
        hitoTime,hitoNum = hito
        if l <= hitoTime and hitoTime < r:
            ans[hitoNum] = x
            rem.append(hitoTime)
        elif r <= hitoTime:
            break

    for i in rem:
        hitos.pop(i)

for i in ans:
    print(i)