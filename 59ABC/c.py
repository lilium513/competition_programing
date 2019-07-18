import itertools
N = input()
l = list(map(int,input().split(" ")))
ruiseki = 0
ans = [0,0]
for pattern in [0,1]: #奇偶による+-を制御
    ruiseki = 0
    for i,num in enumerate(l):
        ruiseki += num
        if (i+pattern) %2 == 0:
            if ruiseki >= 0:
                ans[pattern] += ruiseki + 1
                ruiseki = -1
        else:
            if ruiseki <= 0:
                ans[pattern] +=1-ruiseki
                ruiseki = 1
print(min(ans))
