from collections import deque
import sys

sys.setrecursionlimit(50000000)


ans = {1: 1}


def dfs(tree, nodes):
    for node in nodes:
        nexts = tree[node]
        for next, l in nexts.items():
            if l % 2 == 0:
                ans[next] = ans[node]
            else:
                ans[next] = 1 - ans[node]
            tree[next].pop(node)

        dfs(tree, nexts)

    return 0


if __name__ == "__main__":
    tree = {}
    N = int(input())
    if N == 1:
        u, v, w = list(map(int, input().split(" ")))
        if w % 2 == 1:
            print(1)
            print(0)
        else:
            print(0)
            print(0)
    else:
        for i in range(N - 1):
            u, v, w = list(map(int, input().split(" ")))

            if u not in tree:
                tree[u] = {}
            tree[u][v] = w

            if v not in tree:
                tree[v] = {}
            tree[v][u] = w
        dfs(tree, [1])
        for i in range(1, N + 1):
            print(ans[i])