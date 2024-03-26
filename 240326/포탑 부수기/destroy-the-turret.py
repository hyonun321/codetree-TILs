import sys
from collections import deque
#sys.stdin = open('포탑부수기.txt','r')

n,m,k = map(int,input().split())
maps = [ list(map(int,input().split())) for _ in range(n)]
recent_attack = [ [ 0 for _ in range(m)] for _ in range(n)]
now_attack = [ [False for _ in range(m)] for _ in range(n)]
def max_tower():
     count = 0
     for i in range(n):
         for j in range(n):
             t_c = maps[i][j]
             if t_c > count :
                 count = t_c
     return count

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def find_attack():
    l_power = 5001
    l_t = 0
    for k in range(n+m-2,-1,-1):
        for i in range(n):
            for j in range(m):
                if k == (i+j):
                    n_t = recent_attack[i][j]
                    if l_t <= n_t and l_power >= maps[i][j] and maps[i][j] > 0 :
                        l_power = maps[i][j]
                        l_t = recent_attack[i][j]
                        lx,ly = i,j

    #print(l_power,lx,ly)
    return lx,ly

def find_hitted():
    m_t = 100000
    m_power = 0
    for k in range(n+m-2):
        for j in range(m):
            for i in range(n):
                if k == (i+j):
                    n_t = recent_attack[i][j]
                    if n_t <= m_t and m_power < maps[i][j] and maps[i][j] > 0 :
                        m_power = maps[i][j]
                        mx,my = i,j

    #print(m_power,mx,my)
    return mx,my

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def lazer_attack(ax,ay,hx,hy):

    queue = deque()
    visited = [ [False for _ in range(m)] for _ in range(n)]
    queue.append((ax,ay))
    visited[ax][ay] = True
    come = [ [ 0 for _ in range(m)] for _ in range(n)]
    while queue:
        x,y = queue.popleft()
        for num in range(4):
            nx,ny = x+dx[num],y+dy[num]
            nx,ny = (nx + n)%n , (ny+m)%m
            if in_range(nx,ny) and visited[nx][ny] == False and maps[nx][ny] != 0  :
                queue.append((nx,ny))
                visited[nx][ny] = True
                come[nx][ny] = (x,y)

    if visited[hx][hy] :
        # 레이저 공격을 실행한다.
        a_power = maps[ax][ay]
        maps[hx][hy] -= a_power
        rx,ry = hx,hy
        half_power = a_power //2
        while not (rx == ax and ry == ay) :
            rx,ry = come[rx][ry]
            maps[rx][ry] -= half_power
            now_attack[rx][ry] = True
        #시작점 체력까진거 보정
        maps[rx][ry] += half_power
        # 공격에 관련있엇던놈들 배열에 표시
        now_attack[hx][hy] = True
        return True
    else :
        return False

def bomb_attack(ax,ay,hx,hy) :
    rdx=[-1,-1,-1,0,0,1,1,1]
    rdy=[-1,0,1,-1,1,-1,0,1]
    a_power=maps[ax][ay]
    half_power= a_power//2
    x,y = hx,hy
    for num in range(8):
        nx,ny = x+rdx[num],y+rdy[num]
        nx,ny = (nx+n)%n, (ny+m)%m
        # 공격자는 영향을 받지않음
        if nx == ax and ny == ay : continue
        if in_range(nx,ny) and maps[nx][ny] != 0 :
            maps[nx][ny] -= half_power
            now_attack[nx][ny] = True
    now_attack[ax][ay] = True
    now_attack[hx][hy] = True
    maps[hx][hy] -= a_power


    return
def health_up_non_attack():
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 0 and now_attack[i][j] == False :
                maps[i][j] += 1
    return



for rounds in range(1,k+1):

    #초기화
    now_attack = [ [False for _ in range(m)] for _ in range(n)]
    #공격자를 찾고 n+m 만큼 공격력을 올린다.
    ax,ay = find_attack()
    # 현재 라운드에 공격했다고 기록한다.
    recent_attack[ax][ay] = rounds
    #맞는놈을 찾는다.
    hx,hy = find_hitted()
    # 공격하는애 파워 보정
    maps[ax][ay] += (n+m)
    #레이저 공격이 가능한지 체크.
    possible = lazer_attack(ax,ay,hx,hy)
    if possible == False:
        bomb_attack(ax,ay,hx,hy)
    health_up_non_attack()
print(max_tower())