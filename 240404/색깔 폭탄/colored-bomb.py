import sys
from collections import deque
#sys.stdin = open('색깔폭탄.txt','r')


n,m = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]

# -1 검은돌
# 0 빨간돌
# 1~이상 색돌

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def is_not_bomb():
    for i in range(n):
        for j in range(n): pass
    return

def find_max_bomb():


    level = 1
    fine_bomb_arr = []
    max_bomb_count = -1
    checked = [ [0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if maps[i][j] >= 1 and checked[i][j] == 0:
                queue = deque()
                queue.append((i,j))
                visited = [[0 for _ in range(n)] for _ in range(n)]
                visited[i][j] = level
                temp_arr = [(maps[i][j],i,j)]
                while queue:
                    x,y = queue.popleft()
                    for num in range(4):
                        nx,ny = x+dx[num],y+dy[num]
                        if in_range(nx,ny) and visited[nx][ny] == 0 and (maps[nx][ny] == maps[i][j] or maps[nx][ny] == 0 ) :
                            queue.append((nx,ny))
                            temp_arr.append((maps[nx][ny],nx,ny))
                            visited[nx][ny] = level
                #2개이상의 폭탄 + 모두같은색깔 or 빨간포함해서 딱 2개의 색깔

                for num,sx,sy in temp_arr:
                    if num == 0 : continue
                    checked[sx][sy] = num


                if len(temp_arr) >= 2 : # 2개이상
                    # 다 같은색 or 빨간포함이다.
                    if max_bomb_count < len(temp_arr): #
                        max_bomb_count = len(temp_arr)
                        fine_bomb_arr = [temp_arr]
                    elif max_bomb_count == len(temp_arr):
                        fine_bomb_arr.append(temp_arr)
    #print(fine_bomb_arr,max_bomb_count)


    return max_bomb_count,fine_bomb_arr

def rotate():
    global maps
    t_map = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            t_map[n-1-j][i] = maps[i][j]
    maps = [ [t_map[i][j] for j in range(n)] for i in range(n)]
    return

def gravity():
    global maps
    t_map = [[-2 for _ in range(n)] for _ in range(n)]
    for j in range(n):
        idx = n-1
        for i in range(n-1,-1,-1):
            if maps[i][j] == -2 :continue
            if maps[i][j] == -1 : #돌이면?
                t_map[i][j] = -1
                idx = i-1
            else : #빨강돌이나 아무 돌이면
                t_map[idx][j] = maps[i][j]
                idx -=1

    maps = [ [t_map[i][j] for j in range(n)] for i in range(n)]
    return
answer = 0

def break_bomb(bomb_arr):
    rcount =0
    mx,my=-1,10000
    mred = 10000
    m_arr = []
    # 빨간색 폭탄이 가장 적어야함 = 0개여야함.
    for arr in bomb_arr:

        rcount = 0
        #print(arr)
        arr.sort(key=lambda x:(x[0],-x[1],x[2]))
        #print(arr)
        if arr[0][0] == 0 : #
            rcount +=1
        #print(mx <= arr[1][1])
        #print(-my <= -arr[1][2])
        if (rcount,mx,-my) <= (mred,arr[1][1],-arr[1][2]) :
            mred = rcount
            mx,my = arr[1][1],arr[1][2]
            m_arr = arr.copy()
    point = 0
    for aaa,aax,aay in m_arr:
        maps[aax][aay] = -2
        point += 1

    return point**2

while True :
    bomb_count, bomb_arr= find_max_bomb()
    if bomb_count <= 0: break
    answer += break_bomb(bomb_arr)
    gravity()
    rotate()
    gravity()
print(answer)