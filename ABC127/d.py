N,M = list(map(int,input().split(" ")))
As = list(map(int,input().split(" ")))
As.sort()
BCs = []
for _ in range(M):
    BCs.append(list(map(int,input().split(" "))))
BCs.sort(key=lambda x:x[1],reverse= True)
ia = 0 # A のindex
ibc = 0 # bcのindex
Asl = len(As)
BCsl = len(BCs)
endflag = False
while True:
    if ibc >= BCsl:
        endflag = True
        break

    temp = BCs[ibc]
    for _ in range(temp[0]):
        if ia >= Asl:
            endflag = True
            break
        if temp[1] > As[ia]:
            As[ia] = temp[1]
            ia += 1
        else:
            break
            endflag = True

    ibc += 1

    if endflag:
        break
print(sum(As))