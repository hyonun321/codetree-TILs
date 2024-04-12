import sys
from collections import deque

#sys.stdin = open('포탑부수기2.txt', 'r')


# n x m

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def find_attacker(rounds):
    min_power = 1e8
    mx, my = -1, -1
    for size in range(n + m - 1):
        for item in range(m):  # m범위 위험
            j = item
            i = size - j
            if not in_range(i, j): continue
            if 0 < maps[i][j] < min_power:  # 가장낮음
                min_power = maps[i][j]
                mx, my = i, j
            elif maps[i][j] == min_power: # 같을때는 최근공격했는지 판단
                if recent_attack[mx][my] <= recent_attack[i][j]:
                    # 가장 최근
                    # 행과열
                    min_power = maps[i][j]
                    mx, my = i, j
    # 최종 공격자 선정
    recent_attack[mx][my] = rounds
    return (mx, my)


def find_enermy():
    max_power = -1
    px, py = -1, -1
    for size in range(n + m - 2, -1, -1):
        for item in range(m):  # m범위 위험
            i = item
            j = size - i
            if not in_range(i, j): continue
            # print(i,j)
            if maps[i][j] > 0 and maps[i][j] > max_power:  # 가장큼
                max_power = maps[i][j]
                px, py = i, j
            elif maps[i][j] == max_power :
                if recent_attack[px][py] >= recent_attack[i][j]:
                    # 가장 최근
                    # 행과열
                    max_power = maps[i][j]
                    px, py = i, j
    return px, py


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def lazer_attack(ax, ay, bx, by):
    queue = deque()
    visited = [[False for _ in range(m)] for _ in range(n)]
    queue.append((ax, ay,[(ax,ay)]))
    visited[ax][ay] = True
    while queue:
        x, y, arr = queue.popleft()
        if x == bx and y == by:
            return True, arr
        for num in range(4):
            nx, ny = x + dx[num], y + dy[num]
            nx, ny = (nx + n) % n, (ny + m) % m
            if in_range(nx, ny) and visited[nx][ny] == False and maps[nx][ny] != 0 :
                queue.append((nx, ny, arr + [(nx, ny)]))
                visited[nx][ny] = True

    return False, []


def bomb_attack(ax,ay,bx,by):
    power = maps[ax][ay]
    bdx=[-1,-1,0,1,1,1,0,-1]
    bdy=[0,1,1,1,0,-1,-1,-1]
    attacked_arr = [(ax,ay),(bx,by)]
    for num in range(8):
        nx,ny = bx+bdx[num],by+bdy[num]
        nx,ny = (nx+n)%n , (ny+m)%m
        if in_range(nx,ny) and maps[nx][ny] != 0 :
            maps[nx][ny] -= power//2
            attacked_arr.append((nx,ny))
    maps[bx][by] -= power

    return attacked_arr


def repair_pure_tower(moved_arr):

    for i in range(n) :
        for j in range(m):
            if maps[i][j] >0 :
                if (i,j) not in moved_arr:
                    maps[i][j]+= 1
    return


def find_most_powerful_tower():
    m1 = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] > m1:
                m1 = maps[i][j]
    return m1


def lazer(ax,ay,bx,by,move_arr):
    power = maps[ax][ay]
    for x,y in move_arr:
        if ax == x and ay == y :
            continue
        if x == bx and y == by :
            maps[x][y] -= power
            continue
        maps[x][y] -= power // 2

    return

n, m, k = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
recent_attack = [[0 for _ in range(m)] for _ in range(n)]
for rounds in range(1,k+1):
    ax, ay = find_attacker(rounds)
    bx, by = find_enermy()
    if ax == bx and ay == by : break # 포탑이 이제 없을때
    maps[ax][ay] += n + m # 공격자 선정후 공격력올리기(안그러면 가장큰놈찾을때 영향)
    possible , move_arr = lazer_attack(ax, ay, bx, by)
    if not possible :
        move_arr = bomb_attack(ax,ay,bx,by)
    else :
        lazer(ax,ay,bx,by,move_arr)
    repair_pure_tower(move_arr)
print(find_most_powerful_tower())