from  collections import defaultdict

ans = 1
di = []
def rec(node,depth,K):
    global ans
    if depth == 1:
        of = 0
    if depth == 2:
        of = 1
    else:
        of = 2
    for i,temp in enumerate(node):
        ans *=( K - i - of)
        rec(di[temp],depth + 1 ,K)
    return 1

def do():
    global ans,di
    di = defaultdict(lambda : [])

    N,K =  list(map(int,input().split(" ")))
    graph = [list(map(int,input().split(" "))) for i in range(N-1)]
    for i in range(N-1):
        a,b = graph[i]
        if a > b:
            di[b].append(a)
        else:
            di[a].append(b)
    ans = K

    rec (di[1],2,K)
    print(max(ans%1000000007,0))

if __name__ == "__main__":
    do()