import sys
from collections import deque
#sys.stdin = open('정육면체한번더굴리기.txt','r')
n,m = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]

dx=[-1,0,1,0]
dy=[0,1,0,-1]
def in_range(x,y) :
    return 0<=x<n and 0<=y<n


#
dice = {0:1,1:4,2:2,3:3,4:6,5:5}
def dice_control(direction) :
    global dice
    a_0= dice[0]
    a_1= dice[1]
    a_2=dice[2]
    a_3=dice[3]
    a_4=dice[4]
    a_5=dice[5]
    if direction == 0 :
        dice = {0:a_2,1:a_1,2:a_4,3:a_3,4:a_5,5:a_0}
    elif direction == 1 :
        dice = {0: a_1, 1: a_4, 2: a_2, 3: a_0, 4: a_3, 5: a_5}
    elif direction == 2 :
        dice = {0: a_5, 1: a_1, 2: a_0, 3: a_3, 4: a_2, 5: a_4}
    else :
        dice = {0: a_3, 1: a_0, 2: a_2, 3: a_4, 4: a_1, 5: a_5}
    return

def dice_moving() :
    global dice_x,dice_y,dice_direction
    n_dx,n_dy = dice_x+dx[dice_direction],dice_y+dy[dice_direction]
    if in_range(n_dx,n_dy): # 만약 이동할곳이 범위안이라면
        dice_x,dice_y=n_dx,n_dy
        dice_control(dice_direction)
    else :
        dice_direction = (dice_direction + 2 ) %4
        n_dx, n_dy = dice_x + dx[dice_direction], dice_y + dy[dice_direction]
        dice_x, dice_y = n_dx, n_dy
        dice_control(dice_direction)

    #print(dice_x,dice_y)

    return

def  bottom_get() :
    global dice_x,dice_y
    number = maps[dice_x][dice_y]
    visited = [ [False for _ in range(n)] for _ in range(n)]
    queue = deque()
    queue.append((dice_x,dice_y))
    visited[dice_x][dice_y] = True
    count = 1
    while queue:
        x,y = queue.popleft()
        for num in range(4) :
            nx,ny = x+dx[num],y+dy[num]
            if in_range(nx,ny) and visited[nx][ny] == False and maps[nx][ny] == number :
                queue.append((nx,ny))
                visited[nx][ny] = True
                count += 1
    point = count * number
    return point

def direction_change() :
    global dice_direction
    bottom_number = dice[4]
    #print(bottom_number)
    if bottom_number > maps[dice_x][dice_y] :
        dice_direction = (1+dice_direction)%4
    elif bottom_number < maps[dice_x][dice_y] :
        dice_direction = (dice_direction-1) % 4
    else : #같을때
        pass
    return


dice_x,dice_y = 0,0
point = 0
dice_direction = 1
for rounds in range(m) :
    dice_moving()
    point += bottom_get()
    direction_change()

print(point)