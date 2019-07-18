from itertools import product
N,K = list(map(int,input().split(" ")))
Ds =  list(map(int,input().split(" ")))
nums = [0,1,2,3,4,5,6,7,8,9]
nums = list(set(nums) - set(Ds))

cand = []
for j in range(1,6):
    for i in product(nums, repeat=j):
        i = list(map(str,i))
        temp = "".join(list(i))
        temp = int(temp)
        cand.append(temp)
cand.sort()

for i in cand:
    if i >= N:
        print(i)
        break
