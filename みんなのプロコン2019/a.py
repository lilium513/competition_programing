temp = input().split(" ")
a = temp[0]
b = temp[1]
c = temp[2]

a = int(a)
b = int(b)
c = int(c)

if (c> a and c<b) or (c < a and c>b):
    print("Yes")
else:
    print("No")