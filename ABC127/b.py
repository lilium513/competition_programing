r,d,x = list(map(int,input().split(" ")))
temp = x*r -d
for i in range(0,10):
    print(temp)
    temp = r * temp  - d