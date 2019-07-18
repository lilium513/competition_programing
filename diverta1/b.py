r,g,b,n = list(map(int,input().split(" ")))
c = 0
rl = n//r + 1
bl = n//b + 1


for i in range(rl):
    for j in range(bl):
        if n-(i*r + b*j) >=0 and (n-(i*r + b*j)) % g == 0:
            c += 1
print(c)