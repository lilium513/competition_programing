N = input()
N =int(N)
nums= list(map(int,input().split(" ")))
odds = list(filter(lambda x:x % 2 == 1 ,nums))
if len(odds) % 2 == 0:
    print("YES")
else:
    print("NO")
