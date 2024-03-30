import sys
from collections import deque
#sys.stdin = open('예술성.txt','r')

n = int(input())
dx=[-1,0,1,0]
dy=[0,1,0,-1]
maps = [ list(map(int,input().split())) for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<n
def cal_beautiful():
    idx = 0
    visited = [ [-1 for _ in range(n)] for _ in range(n)]
    color_arr= []
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1 :
                #영역전개 시작
                color = maps[i][j]
                color_arr.append(1)
                queue = deque()
                queue.append((i,j))
                visited[i][j] = idx
                count = 0
                while queue:
                    x,y = queue.popleft()
                    for num in range(4):
                        nx,ny = x+dx[num],y+dy[num]
                        if in_range(nx,ny) and color == maps[nx][ny] and visited[nx][ny] == -1 :
                            visited[nx][ny] = idx
                            queue.append((nx,ny))
                            count += 1
                color_arr[idx] += count
                idx +=1

    #이제 조화로움을 계산할꺼임.
    # 1. 각 그룹마다 4방향으로 다른 숫자를 찾느다.
    # 2. 다른숫자가 있으면 그녀석과의 조화로움을 계산함.
    all_point = 0
    for i in range(n):
        for j in range(n):
            main_color = visited[i][j]
            for num in range(4):
                nx,ny = i+dx[num],j+dy[num]
                if in_range(nx,ny) and main_color != visited[nx][ny] :
                    #조화로움 계산해야함.
                    sub_color = visited[nx][ny]
                    aa = maps[i][j]
                    bb = maps[nx][ny]
                    a_num = color_arr[main_color]
                    b_num = color_arr[sub_color]
                    all_point += (a_num+b_num)*aa*bb
    all_point = all_point // 2
    return all_point

def rotate_maps():
    global maps
    t_maps = [ [0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == n//2 or j == n//2:
                t_maps[n-j-1][i] = maps[i][j]
    d = n//2
    mini_rotate(0,0,d,t_maps)
    mini_rotate(n-d,0,d,t_maps)
    mini_rotate(0,n-d,d,t_maps)
    mini_rotate(n-d,n-d,d,t_maps)

    maps = [ [ t_maps[i][j] for j in range(n)] for i in range(n)]
    return

def mini_rotate(x,y,d,t_maps):

    for i in range(d):
        for j in range(d):
            t_maps[j+x][d-1-i+y] = maps[i+x][j+y]
    return



answer = 0
answer += cal_beautiful() #초기점수
for rounds in range(3):
    rotate_maps()
    answer += cal_beautiful()

print(answer)