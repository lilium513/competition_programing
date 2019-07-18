
masterx,mastery= list(map(int,input().split(" ")))
ans = 10**15

for i in [1,-1]:
    for j in [1,-1]:
        temp = 0
        x = i * masterx
        y = j * mastery
        temp = temp + 1 if i == -1 else temp
        temp = temp + 1 if j == -1 else temp
        if y - x >= 0:
            temp +=  y - x
            ans = min(temp,ans)



print(ans)