import math
def combinations_count(n, r,facs):
    return facs[n] // (facs[n - r] * facs[r])


N,K = list(map(int, input().split(" ")))
R = N-K
facs = [1 for _ in range(6000)]
facs[1] = 1
for i in range(1,3000):
    facs[i+1]  = facs[i] * (i+1)

NUM = 10**9 + 7
for q in range(1,K+1):
    spaces = R+1


    #端を使わないパターン

    choice = combinations_count(spaces,q,facs)
    walls = q -1
    minus = 2
    if walls == 0:
        minus = 0
    places = K - 1
    walls =  q-1
    distr = 1
    distr *= max(combinations_count((K-1),walls,facs),1)

    ans = choice * max(distr,1)

    print(ans % NUM)

  #(wallsが全部端っこのパターンを-2)(walls が0なら-2は無い)



    #R個のballをK + 1箇所に分配
    #両方共端のパターンは除外
