N = input()
N =int(N)
diff = 2025 - N
for i in range(1,10):
    for j in range(1,10):
        if i * j == diff:
            print('%d x %d' % (i, j))