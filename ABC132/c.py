


def do():
    n = int(input())
    ds = list(map(int, input().split(" ")))
    ds.sort()
    sita = ds[n//2-1]
    ue = ds[n//2]
    print(ue-sita)

if __name__ == "__main__":
    do()