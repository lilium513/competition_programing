a,b= list(map(int,input().split(" ")))
if a * b <= 0:
    print("Zero")

else:
    if a > 0:
        print("Positive")
    else:
        if (b -a) % 2 == 0:
            print("Negative")
        else:
            print("Positive")

