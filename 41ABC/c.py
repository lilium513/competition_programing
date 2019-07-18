N = int(input())
Stus =  list(map(int,input().split(" ")))
l = len(Stus)
se = []
for i in range(l):
    se.append((Stus[i],i+1))
se.sort(key=lambda x:x[0],reverse=True)
for s in se:
    print(s[1])