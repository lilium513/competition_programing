import math
N,M = list(map(int,input().split(" ")))
towns = {}
ans = [0] * M
for i in range(M):
    temp = list(map(int,input().split(" ")))
    num = temp[0]
    year = temp[1]
    if num not in towns:
        towns[num] = [(year,i)]
    else:
        towns[num].append((year,i))

# print(towns)
for k,v in towns.items():
    # print("key:",k)
    i1 = str(k).zfill(6)
    v_sorted = sorted(v,key = lambda x:x[0])
    # print("v:",v_sorted)
    for i,town in enumerate(v_sorted):
        # print("town:",town)
        i2 = str(i+1).zfill(6)
        # print(i1 + i2)
        ind = town[1]
        ans[ind] = i1 + i2
# print("ans","---"*20)
for a in ans:
    print(a)
    