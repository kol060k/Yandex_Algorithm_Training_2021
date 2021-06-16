n, m, k = map(int, input().split())
arr = [[0] * m for i in range(n)]
for i in range(k):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    arr[x][y] = -10
    if x > 0:
        arr[x-1][y] += 1
        if y > 0:
            arr[x-1][y-1] += 1
        if y < m - 1:
            arr[x-1][y+1] += 1
    if x < n - 1:
        arr[x+1][y] += 1
        if y > 0:
            arr[x+1][y-1] += 1
        if y < m - 1:
            arr[x+1][y+1] += 1
    if y > 0:
        arr[x][y-1] += 1
    if y < m - 1:
        arr[x][y+1] += 1

for i in range(n):
    for j in range(m-1):
        if (arr[i][j] >= 0):
            print(arr[i][j], end=' ')
        else:
            print('*', end=' ')
    if (arr[i][m-1] >= 0):
        print(arr[i][m-1])
    else:
        print('*')