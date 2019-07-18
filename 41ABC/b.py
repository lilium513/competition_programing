N,L =  list(map(int,input().split(" ")))
words = []
for _ in range(N):
    words.append(input())
words.sort()
print("".join(words))