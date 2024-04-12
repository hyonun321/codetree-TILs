import sys

#sys.stdin = open('냉방 시스템1.txt', 'r')

N, M, K = map(int, input().split())
maps = []
wind = []
wall_arr = [[[] for _ in range(N)] for _ in range(N)]
wall_1st_arr = []
cool = [[0 for _ in range(N)] for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
for k1 in range(N):
    strings = list(map(int, input().split()))

    for k2 in range(len(strings)):
        k3 = strings[k2]
        if 2 <= k3 <= 5:
            wind.append((k1, k2, k3 - 2))
    maps.append(strings)

for wall in range(M):
    wx, wy, ws = map(int, input().split())
    wx -= 1
    wy -= 1
    wall_1st_arr.append((wx, wy, ws))
    wall_arr[wx][wy].append(ws)
    # 0 은 위 1은 왼쪽


def in_range(x, y):
    return 0 <= x < N and 0 <= y < N


# 내가있는곳이 막혀있을때.
# 내가 가야하는곳이 막혀있을때.
cant_go = []


def make_wall():
    for x, y, z in wall_1st_arr:
        if z == 0:  # 바로위
            nx, ny = x + dx[1], y + dy[1]
            cant_go.append([(x, y), (nx, ny)])
            cant_go.append([(nx, ny), (x, y)])
        if z == 1:  # 바로왼쪽
            nx, ny = x + dx[0], y + dy[0]
            cant_go.append([(x, y), (nx, ny)])
            cant_go.append([(nx, ny), (x, y)])
    print(cant_go)

    return


make_wall()


def spread(power, x, y, d):
    global cool
    # 나는 대각의 임시 공간이다.
    # 나는 방향만 체크하고 직선을 다음칸으로 보낸다.
    # 대각선 반시계
    visited[x][y] = True
    cool[x][y] += power
    dd = (d - 1) % 4
    d1x, d1y = x + dx[dd], y + dy[dd]
    if not [(x, y), (d1x, d1y)] in cant_go:
        if in_range(d1x, d1y) and visited[d1x][d1y] == False:
            dd1x, dd1y = d1x + dx[d], d1y + dy[d]
            if not [(d1x,d1y),(dd1x,dd1y)] in cant_go:
                if in_range(dd1x, dd1y) and visited[dd1x][dd1y] == False:
                    spread(power - 1, dd1x, dd1y, d)
    # 대각선 시계
    dd = (d + 1) % 4
    d2x, d2y = x + dx[dd], y + dy[dd]
    # d방향에 따라 다르게 해줘야함.
    print(not [(d2x, d2y), (x, y)] in cant_go)
    if not [(x, y), (d2x, d2y)] in cant_go:
        if in_range(d2x, d2y) and visited[d2x][d2y] == False:
            dd2x, dd2y = d2x + dx[d], d2y + dy[d]
            if not [(d2x,d2y),(dd2x,dd2y)] in cant_go:
                if in_range(dd2x, dd2y) and visited[dd2x][dd2y] == False:
                    spread(power - 1, dd2x, dd2y, d)

    # 직선
    nx, ny = x + dx[d], y + dy[d]
    if not [(x, y), (nx, ny)] in cant_go:
        if in_range(nx, ny) and visited[nx][ny] == False:
            spread(power - 1, nx, ny, d)
    return


# 0이 위쪽벽
# 1 이 왼쪽벽


def blow_up():
    global visited
    for wx, wy, wd in wind:
        power = 5
        visited = [[False for _ in range(N)] for _ in range(N)]
        wx, wy = wx + dx[wd], wy + dy[wd]
        spread(power, wx, wy, wd)

    # spread 함수 (power,x,y,방향)visited체크
    return


def mix_wind():
    global cool
    t_cool = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            level = cool[i][j]
            bd, bb = False, False
            if 0 in wall_arr[i][j]:
                bd = True
            if 1 in wall_arr[i][j]:
                bb = True
            for num in range(4):
                if bd and num == 1: continue
                if bb and num == 0: continue
                nx, ny = i + dx[num], j + dy[num]
                if in_range(nx, ny):
                    n_level = cool[nx][ny]
                    if (level - n_level) >= 4:
                        diff = (level - n_level) // 4
                        t_cool[i][j] -= diff
                        t_cool[nx][ny] += diff

    for i in range(N):
        for j in range(N):
            cool[i][j] += t_cool[i][j]

    return


def side_cold_down():
    for i in range(1, N - 1):
        if cool[i][0] > 0:
            cool[i][0] -= 1
        if cool[i][N - 1] > 0:
            cool[i][N - 1] -= 1
    for j in range(1, N - 1):
        if cool[0][j] > 0:
            cool[0][j] -= 1
        if cool[N - 1][j] > 0:
            cool[N - 1][j] -= 1
    if cool[0][0] > 0:
        cool[0][0] -= 1
    if cool[N - 1][N - 1] > 0:
        cool[N - 1][N - 1] -= 1
    if cool[0][N - 1] > 0:
        cool[0][N - 1] -= 1
    if cool[N - 1][0] > 0:
        cool[N - 1][0] -= 1

    return


def room_cooling_check():
    count = 0
    all_count = 0
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 1:
                all_count += 1
                if cool[i][j] >= K:
                    count += 1
    if count == all_count:
        return True
    else:
        return False


rounds = 0
while True:
    rounds += 1
    blow_up()
    mix_wind()
    side_cold_down()
    # visited 초기화필요
    if room_cooling_check():
        print(rounds)
        break