N = int(input())
As = list(map(int,input().split(" ")))
As.sort(reverse=True)
Bs = list(map(int,input().split(" ")))
Bs.sort(reverse=True)
Cs = list(map(int,input().split(" ")))
Cs.sort(reverse=True)
bcruiseki = [0]
abruiseki = [0]
j = 0
i = 0
while True:
    temp= bcruiseki[j]
    while i < N and Bs[j] <Cs[i]  :
        temp += 1
        i+= 1
    bcruiseki.append(temp)
    j += 1
    if j == N:
        break
j = 0
i = 0
while True:
    temp= abruiseki[j]
    while i < N and As[j] <Bs[i]  :
        temp += bcruiseki[i+1]
        i+= 1
    abruiseki.append(temp)
    j += 1
    if j == N:
        break

print(sum(abruiseki))


