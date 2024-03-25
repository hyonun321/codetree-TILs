import sys
#sys.stdin = open ('메이즈러너.txt','r')
dx=[-1,1,0,0]
dy=[0,0,-1,1]
n,m,k = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n) ]
p_map = [ [0 for _ in range(n)] for _ in range(n)]
def cal_dist(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)
def in_range(x,y):
    return 0<=x<n and 0<=y<n
for _ in range(m):
    a1,b1 = map(int,input().split())
    a1-=1
    b1-=1
    p_map[a1][b1] += 1
e_x,e_y = map(int,input().split())
e_x-=1
e_y-=1
maps[e_x][e_y] = -1 # -1이 출구.
all_move = 0
deb =0
def one_people_move(x,y):
    dist = cal_dist(x, y, e_x, e_y)
    movement = p_map[x][y]
    for num in range(4):
        nx, ny = x + dx[num], y + dy[num]
        n_dist = cal_dist(nx, ny, e_x, e_y)
        if in_range(nx, ny) and (maps[nx][ny] == 0 or maps[nx][ny] == -1) and dist > n_dist:
            x,y = nx,ny
            return x,y,movement

    return x,y,movement

def people_move():
    global all_move,p_map
    temp_p_map = [[ 0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if p_map[i][j] > 0 :
                nx,ny,movement = one_people_move(i,j)
                if deb:
                    print('번째사람',nx,ny)
                if not (i == nx and j == ny) :
                    all_move += movement
                temp_p_map[nx][ny] += movement
    p_map = [ [ temp_p_map[i][j] for j in range(n)] for i in range(n)]
    if deb:
        print('사람 이동 후 ')
        for k in temp_p_map:
            print(*k)
    return

def rotate_arr(x1,y1,w):
    global maps,p_map,e_x,e_y
    if deb:
        print('회전전')
        print('맵스')
        for k2 in maps:
            print(*k2)
        print('사람')
        for k in p_map:
            print(*k)


    temp_maps = [ [0 for _ in range(n)] for _ in range(n)]
    temp_p_maps = [ [0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if x1 <= i < x1+w and y1<= j< y1+w : continue
            temp_maps[i][j] = maps[i][j]
            temp_p_maps[i][j] = p_map[i][j]


    for i in range(w):
        for j in range(w):
            if maps[i+x1][j+y1] > 0 : # 벽내구도 감소
                maps[i + x1][j + y1] -=1
            if e_x == i+x1 and e_y == j+y1:
                e_x = j+x1
                e_y = w-1-i+y1
            temp_maps[j+x1][w-1-i+y1] = maps[i+x1][j+y1]
            temp_p_maps[j+x1][w-1-i+y1] = p_map[i+x1][j+y1]

    maps = [ [ temp_maps[i][j] for j in range(n)] for i in range(n)]
    p_map  = [ [ temp_p_maps[i][j] for j in range(n)] for i in range(n)]
    if deb:
        print('회전후')
        print('맵스')
        for k2 in maps:
            print(*k2)
        print('사람')
        for k in p_map:
            print(*k)


def rotate():
    for power in range(1,n): # 그리는 원 크기 1일때
            for k1 in range(power,-1,-1):
                for k2 in range(power,-1,-1):
                    # 왼쪽위 꼭지점을 잡았다.
                    # e_x+k1,e_y+k2
                    # 여기로부터 크기 2만큼 for 배열 2개 순회하면됨.
                    if deb:
                        print('왼쪽위 꼭지점',e_x-k1,e_y-k2)
                    if in_range(e_x-k1,e_y-k2) and in_range(e_x-k1+power,e_y-k2+power):
                        p_count = 0
                        for t1 in range(power+1):
                            for t2 in range(power+1):
                                #print(e_x-k1+t1,e_y-k2+t2,end=' ')
                                if p_map[e_x-k1+t1][e_y-k2+t2] != 0:
                                    p_count += p_map[e_x-k1+t1][e_y-k2+t2]
                        if p_count >= 1 : # 만약 바로 사람 최소 1명이상을 잡았다면
                            rotate_arr(e_x-k1,e_y-k2,power+1) #그녀석 다 돌려버리고
                            return

    return

def update_exit():
    global  e_x,e_y
    for i in range(n):
        for j in range(n):
            if maps[i][j] == -1 :
                e_x,e_y = i,j
                if deb:
                    print('출구위치')
                    print(e_x, e_y)
                return

def out_check():
    if deb:
        print('삭제한다',p_map[e_x][e_y],e_x,e_y,'부분')
    p_map[e_x][e_y] = 0
    return
def all_people_out():
    for i in range(n):
        for j in range(n):
            if p_map[i][j] != 0 : return False
    return True

for rounds in range(k) :
    people_move()
    out_check()
    if all_people_out(): break
    rotate()
    update_exit()
print(all_move)
print(e_x+1,e_y+1)