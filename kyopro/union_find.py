import sys

class UnionFind():
    def __init__(self,n):
        self.par = [i for i in range(n+1)]
        self.rank = [0 for _ in range(n+ 1)]
    def find(self,x):
        if self.par[x] == x:
            return x
        self.par[x] = self.find(self.par[x])
        return  self.par[x]

    def same_check(self,a,b):
            return self.find(a) == self.find(b)

    def union(self,x,y):
        if self.rank[x] > self.rank[y]:
            self.par[y] = self.par[x]
        else:
            self.par[x] = self.par[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1


def do():
    sys.setrecursionlimit(100000000000000)

    N,Q = list(map(int, input().split(" ")))
    querys = [list(map(int, input().split(" "))) for i in range(Q)]
    uf = UnionFind(N + 1)
    for query in querys:
        q,a,b= query
        if q == 0:
            uf.union(a,b)
        else:
            if uf.same_check(a,b):
                print("Yes")
            else:
                print("No")


if __name__ == "__main__":
    do()