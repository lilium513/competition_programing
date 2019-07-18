N = input()
N = int(N)
rest = []
for i in range(N):
    a,b = input().split(" ")
    b = int(b)
    rest.append([a,b,i+1])
rest.sort(key=lambda x: (x[0], -x[1]),reverse=False)
for i in range(N):
    print(rest[i][2])



