def c():
    N,M= list(map(int,input().split(" ")))
    shops = []
    for i in range(N):
        shop = list(map(int, input().split(" ")))
        shops.append(shop)

    shops.sort(key = lambda x:x[0])
    drinks  = 0
    money = 0
    for shop in shops:
        a = shop[0]
        b = shop[1]
        if drinks + b >=M:
            temp = M - drinks #足りない分
            money += temp * a
            break

        else:
            money += b * a
            drinks += b

    print(money)


if __name__ == '__main__':
    c()