K , A,B=  list(map(int,input().split(" ")))
num = 1
if A>=B - 1 or A - 1 >  K:
    num += K

else:
    #1回目
    a = A -1
    num += a

    b = (K - a)//2
    nokori = (K - a)%2
    num += b* (B-A)

    num += nokori
print(num)
