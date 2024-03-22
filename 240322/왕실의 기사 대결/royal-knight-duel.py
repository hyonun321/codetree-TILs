import sys
from collections import deque
#sys.stdin = open('왕실의기사대결2.txt','r')

deb = 0

l,n,q = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(l)]
night_info = [0]
damaged_arr = [0 for _ in range(n+1)]
for night_num in range(n) :
    r,c,h,w,k = map(int,input().split())
    r-=1
    c-=1
    night_info.append([r,c,h,w,k])


dx=[-1,0,1,0]
dy=[0,1,0,-1]
maps= [ [0 for _ in range(l)] for _ in range(l) ]

# 기사들 의 정보를 다 담는 배열 ?
# 기사들의 위치값을 가지는 2차원 배열을 다시 배열에 넣는방법?

def update_arr():
    temp_arr = [[] for _ in range(n+1)]
    for i in range(l):
        for j in range(l):
            if maps[i][j] != 0 :
                temp_arr[maps[i][j]].append((i,j))
    for night in range(1,n+1):
        if night_info[night][4] == 0 : continue
        a,b = temp_arr[night][0] #업데이트 하려고하는데 죽어서 2차원배열에 없어..
        night_info[night][0] = a
        night_info[night][1] = b

    return


def update_map():
    global maps
    maps = [[0 for _ in range(l)] for _ in range(l)] #초기화
    for num in range(1,n+1):
        r,c,h,w,k = night_info[num][0],night_info[num][1],night_info[num][2],night_info[num][3],night_info[num][4]
        for i in range(r,r+h):
            for j in range(c,c+w):
                maps[i][j] = num
    if deb:
        print()
        for k in maps:
            print(*k)
        print()

        for info in night_info:
            print(info)

    return
def in_range(x,y):
    return 0<=x<l and 0<=y<l
update_map()
update_arr()
def night_move(idx,d):
    global maps
    r,c,h,w = night_info[idx][0],night_info[idx][1],night_info[idx][2],night_info[idx][3]
    # 사라진 기사일 경우 명령 반응 없음.
    if k <= 0 : return
    visitied = [ [False for _ in range(l)] for _ in range(l)]
    queue = deque()
    can_move = [idx]
    possible = True
    for i in range(r,r+h):
        for j in range(c,c+w):
            queue.append((i,j,idx))
            visitied[i][j] = True
    while queue:
        x,y,idx = queue.popleft()
        nx,ny = x+dx[d],y+dy[d]
        if in_range(nx,ny) and visitied[nx][ny] == False and maps[nx][ny] != 0 and idx != maps[nx][ny]: # 가는방향에 새로운놈 발견
            n_idx = maps[nx][ny]
            can_move.append(n_idx)
            r, c, h, w = night_info[n_idx][0], night_info[n_idx][1], night_info[n_idx][2], night_info[n_idx][3]
            for i in range(r, r + h):
                for j in range(c, c + w):
                    queue.append((i, j,n_idx))
                    visitied[i][j] = True
        elif in_range(nx,ny) and visitied[nx][ny] == False and board[nx][ny] == 0 : pass # 그냥땅 pass
        elif in_range(nx,ny) and visitied[nx][ny] == False and board[nx][ny] == 2 : # 벽발견
            possible = False
        elif not in_range(nx,ny) :
            possible = False

    # 갈수있으면 전부다 이동시킴.
    # 갈수 없으면 그냥 끝내기
    temp_maps = [ [ 0 for _ in range(l)] for _ in range(l)]
    if possible :
        for night in range(1,n+1):
            if night in can_move:
                r, c, h, w = night_info[night][0], night_info[night][1], night_info[night][2], night_info[night][3]
                for i in range(r, r + h):
                    for j in range(c, c + w):
                        nx,ny = i+dx[d],j+dy[d]
                        temp_maps[nx][ny] = night
            else :
                if night_info[night][4] > 0 :
                    r, c, h, w = night_info[night][0], night_info[night][1], night_info[night][2], night_info[night][3]
                    for i in range(r, r + h):
                        for j in range(c, c + w):
                            temp_maps[i][j] = night
        # 안움직이는애 반영

        maps = [[temp_maps[i][j] for j in range(l)] for i in range(l)]


        return True, can_move
    # temp맵을 maps 로 반영
    else :
        return False, can_move

def cal_alive_night_damaged():
    count = 0
    for night in range(1,n+1):
        if night_info[night][4] > 0 :
            count += damaged_arr[night]
    return count

def damage_check(n_num,moved_arr):
    for i in range(l):
        for j in range(l):
            if maps[i][j] == n_num: continue
            if maps[i][j] != 0 and board[i][j] == 1 :
                if maps[i][j] in moved_arr :
                    if night_info[maps[i][j]][4] > 0 :
                        night_info[maps[i][j]][4] -= 1
                        damaged_arr[maps[i][j]] += 1
                        if night_info[maps[i][j]][4] == 0 : # 0은 다죽으니
                            for x1 in range(l):
                                for y1 in range(l):
                                    if maps[x1][y1] == maps[i][j] :
                                        maps[x1][y1] = 0
    #이동명령받은 기사는 데미지 안입음.

    return
for order in range(q):
    i,d = map(int,input().split())
    chk,moved_arr = night_move(i,d)
    update_arr()
    if chk:
        damage_check(i,moved_arr)
print(cal_alive_night_damaged())