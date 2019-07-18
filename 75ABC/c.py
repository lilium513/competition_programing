import itertools
import math

LIM = 50

graph =[[False  for _  in range(LIM)] for _ in range(LIM)]
visited = [False  for _  in range(LIM)]
bridges = []


def search(num):
    visited[num] = True
    for i, temp in enumerate(graph[num]):
        if not temp:  # つながってなかったら
            continue
        if visited[i]:  # 訪問済みならx
            continue
        search(i)


def do():
    ans = 0
    N ,M = list(map(int,input().split(" ")))
    for _ in range(M):
        a,b = list(map(int,input().split(" ")))
        a -= 1
        b -= 1

        bridges.append([a,b])
        graph[a][b] =  graph[b][a] = True
    for bridge in bridges: #M番目を落とす
        graph[bridge[0]][bridge[1]] = graph[bridge[1]][bridge[0]] = False
        for j in range(LIM):
            visited[j] = False
        search(0) #0から始めて良い∵連結グラフなので
        flag = False

        for i in range(N):
            if visited[i] == False:
                flag = True
        if flag:
            ans +=1
        graph[bridge[0]][bridge[1]] = graph[bridge[1]][bridge[0]] = True
    print(ans)





if __name__ == "__main__":
    do()