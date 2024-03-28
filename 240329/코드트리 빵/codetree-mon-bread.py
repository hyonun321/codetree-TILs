import sys
from collections import deque
sys.stdin = open('코드트리 빵.txt','r')
deb =0
n,m = map(int,input().split())

maps = [list(map(int,input().split())) for _ in range(n)]
people = [(-1,-1) for _ in range(31) ]


combini = [(-1,-1,False) for _ in range(31)]
for number in range(1,m+1):
    x1,y1 = map(int,input().split())
    x1-=1
    y1-=1
    combini[number]= (x1,y1,False)
dx=[-1,0,0,1]
dy=[0,-1,1,0]

def people_move():
    for number in range(1,31):
        px,py = people[number]
        cx,cy,_ = combini[number]
        if px == -1 : continue
        dist,next_step = cal_distance(px, py,cx, cy)
        people[number] =next_step
        if deb:
            print(next_step)
            print(people)
            print(maps)

    return


def combini_check():
    for number in range(1,m+1):
        cx,cy,_=combini[number]
        px,py = people[number]
        if cx == px and cy == py :
            maps[cx][cy] = -1
            people[number] = (-1,-1) # 우주로가
            combini[number] = (cx,cy,True)
    return

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def cal_distance(x1,y1,x2,y2):

    queue = deque()
    arr = []
    queue.append((x1,y1,arr))
    visited= [ [0 for _ in range(n)] for _ in range(n)]
    visited[x1][y1] = 1

    while queue:
        x,y,arr = queue.popleft()
        if x == x2 and y == y2 :
            arr = arr + [(x,y)]
            break
        for num in range(4):
            nx,ny = x+dx[num],y+dy[num]
            if in_range(nx,ny) and visited[nx][ny] == 0 and maps[nx][ny] != -1:
                queue.append((nx,ny,arr+[(x,y)]))
                visited[nx][ny] = visited[x][y] + 1


    #print(visited)
    return visited[x2][y2], arr[1] # 여기서문제날수도있음.

def basecamp_in(rounds):
    if rounds <= m :
        cx,cy,_ = combini[rounds]
        m_dist = 100000
        for i in range(n):
            for j in range(n):
                if maps[i][j] == 1 :
                    dist,_ = cal_distance(i,j,cx,cy)
                    if dist < m_dist :
                        m_dist = dist
                        rx,ry = i,j
        # 베이스 캠프에 이동처리하기
        people[rounds] = (rx,ry)
        # 베이스캠프 벽으로 막기
        maps[rx][ry] = -1
    return

def all_people_in_combini():
    count = 0
    for number in range(1+m+1):
        _,_,possible = combini[number]
        if possible :
            count +=1
    if count == m : return True
    return False

rounds = 0
while True:
    rounds +=1
    people_move()
    combini_check()
    basecamp_in(rounds)
    if all_people_in_combini(): break
print(rounds)