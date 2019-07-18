import  fractions

def lcm(x, y):
    return (x * y) //  fractions.gcd(x, y)


def do():
    A,B,C,D =  list(map(int,input().split(" ")))
    CD = lcm(C,D)
    A1 = A- 1
    ans = (B//C + B//D - B//CD) - (A1//C + A1//D - A1//CD)
    ans = (B-A+1) - ans
    print(ans)

if __name__ == "__main__":
    do()