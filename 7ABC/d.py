def kinsi(N):

    l = len(N)
    dp = [      [ [0 for i in range(2)]   for _ in range(2)] for _ in range(l + 1)]

    iN = int(N[0])
    dp[0][0][0] = 1


    for i in range(0, l):
        for j in [1, 0]:  # 未満フラグ → 立ってればなんでもOK、そうでないと制限がかかる
            for contain49 in [1,0]: #前の桁までに4か9が現れたか
                lim = 9 if j == 1 else int(N[i])
                for d in range(0, lim + 1):  # i + 1桁目 に加える数字
                    flag49 = 0
                    if d == 4 or d == 9 or contain49 == 1:
                        flag49 = 1

                    mimanflag = 0
                    if j == 1 or (d < lim):  # 未満フラグ → 前の桁が未満か、この桁が未満だったら(j == 1が前者、 d< limが校舎に(多分)対応)
                        mimanflag = 1

                    dp[i + 1][mimanflag][flag49] += dp[i][j][contain49]
    return dp[l][0][1] +  dp[l][1][1]

A,B = input().split(" ")
l = len(B)


# e.g 8456



A = str(int(A) - 1)
print(kinsi(B) - kinsi(A))
