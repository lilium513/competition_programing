import math
ans = []
def main(num):

    lim =int(math.ceil((-1 + math.sqrt(1 + 8 * num))/2))
    for i in range(lim,0,-1):
        if num - i >= 0:
            ans.append(i)
            num = num - i
    for j in ans:
        print(j)




if __name__ == '__main__':
    N = int(input())
    main(N)
