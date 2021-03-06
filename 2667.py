from collections import deque
q = deque()
n = int(input())
a = [list(map(int, input())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
check = [[0] * n for _ in range(n)]
cnt = []

def dfs(x, y):
    q.append([x, y])
    check[x][y] = 1
    cnt_temp = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n:
                if check[nx][ny] == 0 and a[nx][ny] == 1:
                    cnt_temp += 1
                    q.append([nx, ny])
                    check[nx][ny] = 1

    cnt.append(cnt_temp)

for i in range(n):
    for j in range(n):
        if check[i][j] == 0 and a[i][j] == 1:
            dfs(i, j)

print(len(cnt))
cnt.sort()
for k in cnt:
    print(k)
