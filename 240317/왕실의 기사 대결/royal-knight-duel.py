import sys
import copy
#sys.stdin = open('왕실의 기사 대결.txt','r')
from collections import deque
l,n,q = map(int,input().split())
dx=[-1,0,1,0]
dy=[0,1,0,-1]
maps = [list(map(int,input().split())) for _ in range(l)]
night_map = [ [0 for _ in range(l)] for _ in range(l)]
night_health = [0]
for number in range(1,n+1) : 
    r,c,h,w,k = map(int,input().split())
    r-=1
    c-=1
    for x1 in range(r,r+h):
        for y1 in range(c,c+w):   
            night_map[x1][y1] = number
    night_health.append(k)

out_night_arr = []
def in_range(x,y):
    return 0<=x<l and 0<=y<l

def bfs(number):
    for i in range(l):
        for j in range(l):
            if night_map[i][j] == number:
                queue =deque()
                queue.append((i,j))
                visitied = [ [False for _ in range(l)] for _ in range(l)]
                visitied[i][j] = True

                while queue : 
                    x,y = queue.popleft()
                    for num in range(4):
                        nx,ny = x+dx[num],y+dy[num]
                        if in_range(nx,ny) and visitied[nx][ny] == False and night_map[nx][ny] == number:
                            queue.append((nx,ny))
                            visitied[nx][ny] = True

    return visitied


def next_arr(arr,d,output_arr):
    output_arr =[[ False for _ in range(l)] for _ in range(l)]
    for i in range(l):
        for j in range(l):
            if arr[i][j] :
                nx,ny = i+dx[d],j+dy[d]
                if in_range(nx,ny) and maps[nx][ny] != 2:
                    output_arr[nx][ny] =True
                else : 
                    return False,output_arr
    return True,output_arr

def update_arr(before_arr,after_arr):
    for i in range(l) : 
        for j in range(l):
            if before_arr[i][j]: # 트루인곳에 기사가있다? 
                after_arr[i][j] = True
    return after_arr

def can_move_arr(one_night_arr,d):
    for i in range(l):
        for j in range(l):
            if one_night_arr[i][j] : 
                nx,ny = i+dx[d],j+dy[d]
                if not in_range(nx,ny): return False
                if maps[nx][ny] == 2 : return False

    return True

def can_move_night(number,d):
    one_night_arr = bfs(number)
    for x1 in range(l):
        for y1 in range(l):
            if one_night_arr[x1][y1] : 
                nx,ny = x1+dx[d],y1+dy[d]
                if in_range(nx,ny) and night_map[nx][ny] != 0 and night_map[nx][ny] != number : # 다르다면 ! 전파.
                    next_number = night_map[nx][ny]
                    temp_arr = bfs(next_number)
                    one_night_arr = update_arr(temp_arr,one_night_arr)
                elif in_range(nx,ny) and maps[nx][ny] == 2 : #그다음 아래에 돌이있다면 
                    return False,one_night_arr
    return True, one_night_arr    

def move_nights(one_night_arr,d):
    temp_night_map = [ [0 for _ in range(l) ] for _ in range(l) ]
    moved_night = [0]
    for i in range(l):
        for j in range(l):
            if one_night_arr[i][j] :
                temp_num = night_map[i][j]
                nx,ny = i+dx[d],j+dy[d]
                temp_night_map[nx][ny] = temp_num
                moved_night.append(temp_num)

    for i in range(l):
        for j in range(l):
            if not night_map[i][j] in moved_night : 
                temp_night_map[i][j] = night_map[i][j]

    for i in range(l):
        for j in range(l):
            night_map[i][j] = temp_night_map[i][j]

    return

def damage_check(numbers) : 
    for i in range(l):
        for j in range(l):
            if maps[i][j] == 1:
                if night_map[i][j] != 0 :
                    if night_map[i][j] == numbers: continue
                    number = night_map[i][j]
                    night_health[number] -= 1 
    return 
damage = 0 

def disapear():
    for i in range(l):
        for j in range(l):
            if night_map[i][j] != 0 : 
                if night_health[night_map[i][j]] <= 0 :
                    night_map[i][j] = 0
                    if not night_map[i][j] in out_night_arr:
                        out_night_arr.append(night_map[i][j]) 
    return

def cal_all_damaged_night():
    count = 0
    for k in range(len(night_health)):
        if k == 0 : continue
        if k in out_night_arr: continue
        count += night_health[k]
    return count
count =0
for _ in range(q):
    i,d = map(int,input().split())
    if i in out_night_arr: continue
    possible , one_night_arr = can_move_night(i,d)
    if possible:
        move_nights(one_night_arr,d)
        damage_check(i)
        disapear()
print(cal_all_damaged_night())