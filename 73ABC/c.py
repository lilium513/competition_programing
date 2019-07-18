

def do():
    di = {}
    N = int(input())
    for _ in range(N):
        temp = int(input())
        if temp not in di:
            di[temp] = 1
        else:
            di[temp] += 1
    ans = 0
    for k,v in di.items():
        if v % 2 == 1:
            ans += 1
    print(ans)



if __name__ == "__main__":
    do()