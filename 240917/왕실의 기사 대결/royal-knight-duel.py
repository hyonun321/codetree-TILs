import sys
from collections import deque
knight = [0]
L,N,Q = map(int,input().split())
board = [ list(map(int,input().split())) for _ in range(L)]
kboard = [ [0 for _ in range(L)] for _ in range(L)]
damaged_all = [0 for _ in range(N+1)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def update_night_map():
    global kboard
    kboard = [ [0 for _ in range(L)] for _ in range(L)]
    for knum in range(N+1):
        if knum == 0 : continue
        (r, c, h, w, k) = knight[knum]
        if k <= 0 : continue
        for x1 in range(h):
            for y1 in range(w):
                kboard[r+x1][c+y1] = knum
for number in range(N):
    (r,c,h,w,k) = map(int,input().split())
    r-=1
    c-=1
    for x1 in range(h):
        for y1 in range(w):
            kboard[r+x1][c+y1] = number+1
    knight.append((r,c,h,w,k))

def print_b(arr):
    print("함수")
    for k in arr:
        print(*k)
# 함수
def in_range(x,y):
    return 0<=x<L and 0<=y<L
def change_knight_move(move_knight,d):
    for m in move_knight:
        (kr,kc,kh,kw,knumber) = knight[m]
        kr,kc = kr+dx[d],kc+dy[d]
        knight[m] = (kr, kc, kh, kw, knumber)
    return
def knight_move(i,d):
    move_knight = []
    visited = [ [False for _ in range(L)] for _ in range(L)]
    (r1,c1,h1,w1,health) = knight[i]
    move_knight.append(i)
    if health <= 0: return []
    queue = deque()
    for x2 in range(h1):
        for y2 in range(w1):
            queue.append((r1 + x2, c1 + y2,i))
            visited[r1 + x2][c1 + y2] = True
    while queue:
        x,y,number = queue.popleft()
        nx,ny = x+dx[d],y+dy[d]
        if in_range(nx,ny) and visited[nx][ny] == False and kboard[nx][ny] != 0 and kboard[nx][ny] != number:
            queue.append((nx,ny,kboard[nx][ny]))
            move_knight.append(kboard[nx][ny])
            (r2,c2,h2,w2,nhealth) = knight[kboard[nx][ny]]
            for x3 in range(h2):
                for y3 in range(w2):
                    queue.append((r2 + x3, c2 +  y3, kboard[nx][ny]))
                    visited[r2 + x3][c2 + y3] = True
        elif in_range(nx,ny) and visited[nx][ny] == False and board[nx][ny] == 2 : #벽일때
            return []
        elif not in_range(nx,ny) :
            return []
    change_knight_move(move_knight,d)
    update_night_map()
    return move_knight
        # 다른 기사일때

def damaged(move_knight):
    for kn in range(len(move_knight)):
        if kn == 0 : continue # 움직인놈은 반영안함
        knum = move_knight[kn]
        (r,c,h,w,khealth) = knight[knum]
        count = 0
        for x1 in range(h):
            for y1 in range(w):
                if(board[r+x1][c+y1] == 1):
                    count +=1
        damaged_all[knum] += count
        knight[knum] = (r, c, h, w, khealth - count)
    update_night_map()
    return

def cal_damage():
    count = 0
    for km in range(N+1):
        if km == 0 : continue
        (r, c, h, w, khealth) = knight[km]
        if khealth > 0 :
            count += damaged_all[km]
    return count
# 라운드

#print_b(board)
for turn in range(Q):
    (i,d) = map(int,input().split())
    move_knight = knight_move(i,d)
    #print(move_knight)
    if (len(move_knight) == 0 ) : continue
    damaged(move_knight)
    #print_b(kboard)

print(cal_damage())