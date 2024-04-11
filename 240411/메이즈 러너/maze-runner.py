import sys

#sys.stdin = open('메이즈러너2.txt', 'r')


def cal_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def rotate(x, y, l, arr, check):
    t_maps = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(l):
        for j in range(l):
            t_maps[j + x][l - i - 1 + y] = arr[i + x][j + y]
    # 회전벽 내구도 깎이기 넣어야함
    for i in range(l):
        for j in range(l):
            if check:
                if t_maps[i + x][j + y] > 0:
                    t_maps[i + x][j + y] -= 1
            arr[i + x][j + y] = t_maps[i + x][j + y]
    return


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def runner_move():
    global ex, ey, r_map
    count = 0
    t_rmap = [[0 for _ in range(n)] for _ in range(n)]
    for rx in range(n):
        for ry in range(n):
            if r_map[rx][ry] > 0:
                now = cal_dist(ex, ey, rx, ry)
                min_um = -1
                mx, my = -1, -1
                for um in range(4):
                    nx, ny = rx + dx[um], ry + dy[um]
                    if in_range(nx, ny) and (maps[nx][ny] == 0 or maps[nx][ny] == -1):
                        moved = cal_dist(nx, ny, ex, ey)
                        if moved < now:
                            min_um = um
                            now = moved
                            mx, my = nx, ny
                            count +=r_map[rx][ry]
                if min_um == -1:  # 그냥 가만히있기
                    t_rmap[rx][ry] += r_map[rx][ry]
                    continue
                t_rmap[mx][my] += r_map[rx][ry]
    r_map = [[t_rmap[i][j] for j in range(n)] for i in range(n)]
    return count


n, m, k = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
r_map = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    r_map[r][c] += 1
ex, ey = map(int, input().split())
ex -= 1
ey -= 1
maps[ex][ey] = -1


def rotate_exit():
    global ex, ey

    # for size in range(1,n): # 사이즈가 1부터
    for size in range(2, n):
        for i in range(size):
            for j in range(size):
                runner = 0
                exits = 0
                if not in_range(ex + i - (size - 1), ey + j - (size - 1)): continue
                for tx in range(size):
                    for ty in range(size):
                        nx, ny = ex + i - (size - 1) + tx, ey + j - (size - 1) + ty
                        if in_range(nx, ny) and r_map[nx][ny] > 0:  # 러너가 한명이라도 있다면
                            runner += 1
                        if in_range(nx, ny) and nx == ex and ny == ey:
                            exits += 1

                if runner > 0 and exits == 1:
                    return size, ex + i - (size - 1), ey + j - (size - 1)
                    # print(ex+i-(size-1)+tx,ey+j-(size-1)+ty)
            # print()

    return


def exit_update():
    global ex, ey
    for i in range(n):
        for j in range(n):
            if maps[i][j] == -1:
                ex, ey = i, j


def runner_exit_check():
    count = 0
    for i in range(n):
        for j in range(n):
            if r_map[i][j] >0 :
                count += 1
                if i == ex and j == ey:
                    r_map[i][j] = 0
                    count -= 1

    if count == 0 :
        return True
    return False
answer = 0
for rounds in range(k):
    answer += runner_move()
    if runner_exit_check() : break
    size, erx, ery = rotate_exit()
    rotate(erx, ery, size, maps, True)
    rotate(erx, ery, size, r_map, False)
    exit_update()
print(answer)
print(ex+1,ey+1)