an = []
for i in range(5):
    temp = input()
    an.append(int())


N = int( input())
temp = list(map(int,input().split(" ")))

f = False
k  = int(input())
for a1 in an:
    for a2 in an:
        if abs(a1-a2) > k:
            f  =True
if f:
    print(":(")
else:
    print("Yay!")

