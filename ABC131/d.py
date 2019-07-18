N = int(input())
works = []
for i in range(N):
    temp= list(map(int,input().split(" ")))
    works.append(temp)
works.sort(key=lambda x:x[1])
sche ={}
for work in works:
    if work[1] not in sche:
        sche[work[1]] = work[0]
    else:
        sche[work[1]] += work[0]
acc = 0
sche = sorted(sche.items(), key=lambda x:x[0])

for k,v in sche:
    acc += v
    if acc > k:
        print("No")
        exit()

print("Yes")