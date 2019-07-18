import itertools
N = input()
l = list(map(int,input().split(" ")))
l.sort(reverse=True)
N = int(N)
i = 0
hen =[]

while True:
    if i >= N-1 or len(hen) == 2:
        break
    if l[i] == l[i+1]:
        hen.append(l[i])
        i+=1
    i+= 1

if len(hen )< 2:
    print(0)
else:
    print(hen[0]*hen[1])