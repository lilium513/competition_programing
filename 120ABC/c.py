import math
N = int( input())
temp = list(map(int,input().split(" ")))
ans = 10**20
odd =[v for i,v in enumerate(temp) if i % 2 == 1]
even =[v for i,v in enumerate(temp) if i % 2 == 0]
dicodd = {}
diceven = {}
for i in temp:
    if i not in dicodd:
        dicodd[i] = 0
    if i not in diceven:
        diceven[i] = 0
for o in odd:
    dicodd[o] += 1
for e in even:
    diceven[e] += 1


maxOdd = max(dicodd.items(),key= lambda x:x[1])
dicodd.pop(maxOdd[0])

max2Odd = (0,0)
if len(dicodd) != 0:
    max2Odd = max(dicodd.items(),key= lambda x:x[1])

maxEven = max(diceven.items(),key= lambda x:x[1])
diceven.pop(maxEven[0])

max2Even = (0,0)
if len(diceven) != 0:
    max2Even = max(diceven.items(),key= lambda x:x[1])

if maxOdd[0] != maxEven[0]:
    print(N - maxOdd[1] - maxEven[1])
else:
    ans1 = N - maxOdd[1] - max2Even[1]
    ans2 = N - max2Odd[1] - maxEven[1]
    print(min(ans1,ans2))

# print(odd)
# print(even)

# print("---" * 30)
# print(dicodd)
# print(diceven)

