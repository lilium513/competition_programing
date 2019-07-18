n,d =  list(map(int,input().split(" ")))
dots = [list(map(int,input().split(" ")))  for _ in range(n)]

sqs = [i ** 2 for i in range(100000)]

ans = 0
for i in range(n):
    for j in range(i+1,n):
        d1 = dots[i]
        d2 = dots[j]
        temp = 0
        for dd1,dd2 in zip(d1,d2):
            temp += (dd1 - dd2) ** 2
        if temp in sqs:
            ans += 1



print(ans)

