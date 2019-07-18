def c():
   
    K = int(input())
    ans = ""
    if K == 0:
        print(0)
        return 0
    while True:
        amari = -1*(K%-2) 
        # print(amari,end = "")
        ans += str(amari)
        K = (K-amari) / (-2)
        K = int(K)
        # print("K=",K)
        if K == 0 or K == 1:
            break
    ans += str(K)
    print(ans[::-1])
if __name__ == '__main__':
    c()