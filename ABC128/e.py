import bisect
import heapq
import sys
N,Q = [int(x) for x in sys.stdin.readline().split()]

hitos = []
ans = [-1 for _ in range(Q)]
queries =[]
jump = ans[::]



queries = [[int(x) for x in sys.stdin.readline().split()] for i in range(N)]
hitos = [int(sys.stdin.readline()) for i in range(Q)]


# for i in range(N):
    # S,T,X =list(map(int,input().split(" ")))
    # lt = S -X -0.5
    # rt = T -X -0.5
    # queries.append([lt,rt,X]) #-1 → 挿入クエリ lが時間、-1がクエリの種類、Xが場所


queries.sort(key=lambda x:x[2])





for l,r,x in queries:
     lind  = bisect.bisect_left(hitos,l-x - 0.5)
     rind  = bisect.bisect_left(hitos,r -x - 0.5)
     while lind < rind:
         if ans[lind] == -1:
            ans[lind] = x
            jump[lind] = rind
            lind += 1
         else:

             lind = jump[lind]

for i  in ans:
    print(i)
