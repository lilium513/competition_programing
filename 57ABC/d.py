from collections import defaultdict
def input_as_int():
    return list(map(int,input().split()))

def get_comb(n):  # n C n まで

    fac = get_fact(n)
    com  = [["error" for _ in range(n+1)] for _ in range (n + 1)]
    for i in range(n + 1):
        for j in range(i + 1):
            if  i >= j:
                com[i][j] = fac[i] // (fac[i-j] * fac[j])
    return com

def get_fact(n):
    temp = 1
    fac = [1]
    for i in range(1, n + 1):
        temp *= i
        fac.append(temp)
    return fac

N,A,B = input_as_int()
Vs = input_as_int()
Vs.sort(reverse= True)
nums = defaultdict(lambda :0)
kose = defaultdict(lambda :0)
com = get_comb(N)
for v in Vs:
    nums[v] += 1
total = 0
for i in range(A):
    total += Vs[i]
    kose[Vs[i]] += 1
av = total / A
i = A
ans = 0
while True:
    temp = 1
    for k,v in kose.items():
        n = nums[k]
        temp *= com[n][v]

    ans += temp
    if i ==B or Vs[i] != Vs[0] :
        break
    else:
        kose[Vs[i]] +=1
        i += 1
print(av)
print(ans)
