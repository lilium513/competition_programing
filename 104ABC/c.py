import statistics
import math
# N = int( input())
D,G = list(map(int,input().split(" ")))

items = []

for i in range(D):
    p,c = list(map(int,input().split(" ")))
    items.append((p,c))

ans = 10e9
for  i in range(2**D):
    # print("--"*20)
    # print("i=",i)
    socre = 0
    co = 0
    notzenkan = []
    for j in range(D):
        if ((i >> j)& 1): #最初に全完する問題を解き終える
            socre += (j + 1 ) * 100 *items[j][0] +  items[j][1]
            co += items[j][0]
        else:
            notzenkan.append(j)
    notzenkan = notzenkan[::-1]
    # print(socre)
    for q in notzenkan:
        if socre >= G:
                break
        question_num = items[q][0]
        for num in range(question_num):
            socre += (q + 1 ) *100
            co += 1
            if socre >= G:
                break
        # print(socre)
    if co < ans and socre >= G:
        # print(co)
        ans = co
print(ans)




