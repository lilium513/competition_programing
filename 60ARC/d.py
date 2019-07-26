
n =100

for n in range(2, 200):
    for b in range(1,200):
        origin = b
        temp = 0

        while True:
            temp += b % n
            b //= n
            if b == 0:
                break
        print("n = " ,n , ", b= ",origin,": s= ",temp)

