ans = 0

def rec(num,flag,co,N):
    global ans
    if num>N:
         return  0

    else:
        if flag  == 0b111:
            # print(ans)
            ans += 1
        return rec(num * 10 + 7, flag|0b001,co + 1,N ) + rec(num * 10 + 3,flag|0b100,co + 1,N ) +rec(num * 10 + 5,flag|0b010 ,co + 1,N )
def c():
    bit07 = 0b001
    bit05 = 0b010
    bit03 = 0b100
    global ans
    N = input()
    N = int(N)
    rec(3,bit03,0,N)
    rec(5,bit05,0,N)
    rec(7,bit07,0,N)

    print(ans)
if __name__ == "__main__":
    c()