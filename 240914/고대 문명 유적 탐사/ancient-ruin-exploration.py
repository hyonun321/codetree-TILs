import sys
from collections import deque

# 0,1,2 인덱스에 따라 90~270도 회전시키는 함수


K,M = map(int,input().split())
board = [ list(map(int,input().split())) for _ in range(5)]
relics = list(map(int,input().split()))
result = []


def print_b(arr):
    for k in arr:
        print(*k)
    print()

def in_range(x,y):
    return 0<=x<5 and 0<=y<5

def rotate_board(x,y,mid,rotate_count,t_board):
    x-=1
    y-=1
    temp_arr = [ [t_board[i][j] for j in range(5)] for i in range(5)]
    for _ in range(rotate_count):
        for i in range(mid):
            for j in range(mid):
                temp_arr[x+j][mid+y-1-i] = t_board[i+x][y+j]

        for i in range(5):
            for j in range(5):
                t_board[i][j] = temp_arr[i][j]
    return t_board


def bfs(x,y,visited,t_board):
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    count = 1
    over_3rd_arr = [(x,y)]
    while queue:
        qx,qy = queue.popleft()
        for d in range(4):
            nx,ny=qx+dx[d],qy+dy[d]
            if in_range(nx,ny) and visited[nx][ny] == False and t_board[x][y] == t_board[nx][ny] :
                queue.append((nx,ny))
                visited[nx][ny] = True
                over_3rd_arr.append((nx,ny))
                count +=1
    if count >=3 :
        return (count,over_3rd_arr)
    return 0,[]

def gain_point(t_board,relic,fake):
    temp_relics = []
    for item in relic:
        temp_relics.append(item)
    max_point = 0 #17
    while True :
        visited = [ [False for _ in range(5)] for _ in range(5)]
        over_3rd_arr = []
        point = 0
        for i in range(5):
            for j in range(5):
                a,b = bfs(i,j,visited,t_board)
                #(count,over_3rd_arr)
                if a == 0 : continue
                point += a
                over_3rd_arr += b
        if point == 0 : break

        max_point += point
        for (ax,ay) in over_3rd_arr:
            t_board[ax][ay] = 0

        for qy in range(5):
            for qx in range(4,-1,-1):
                if t_board[qx][qy] == 0 :
                    t_board[qx][qy] = temp_relics.pop(0) # 더이상 팝할께없다고.. <?
        if (fake == True) : break
    return(max_point , t_board,temp_relics)



for turn in range(K):
    # 탐사진행
    high_point = 0
    mx,my = -1,-1
    rotate_count = 0
    for ty in range(1,4):
        for tx in range(1,4):
            t_relic = []
            for item in relics:
                t_relic.append(item)
            for rotate in range(1,4): # 1,2,3 -> 1 90도 2 180도 3 270도
                t_board = [[board[ax][ay] for ay in range(5)] for ax in range(5)]
                t_board = rotate_board(tx,ty,3,rotate,t_board)
                point, t_board,_ = gain_point(t_board,t_relic,True)
                if (point,-rotate) > (high_point, -rotate_count) :
                    rotate_count = rotate
                    mx,my = tx,ty
                    high_point = point

    if (mx == -1 and my == -1) : break
    board = rotate_board(mx,my,3,rotate_count,board)
    pp, board,relics = gain_point(board, relics,False)
    result.append(pp)
for item_p in result:
    print(item_p,end=' ')
    # 유물 연쇄진행 + result하기
    # 만약 없다면 break