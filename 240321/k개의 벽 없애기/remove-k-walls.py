import sys
#sys.stdin = open('연습.txt','r')
from collections import deque
n,k = map(int,input().split())

maps = []
temps = []
for k1 in range(n):
    its = list(map(int,input().split()))
    for k2 in range(len(its)):
        kk = its[k2]
        if kk == 1 : temps.append((k1,k2))
    maps.append(its)

dx=[-1,0,1,0]
dy=[0,1,0,-1]
sx,sy = map(int,input().split())
sx-=1
sy-=1
rx,ry = map(int,input().split())
rx-=1
ry-=1
def in_range(x,y):
    return 0<=x<n and 0<=y<n

def bfs(sx,sy,rx,ry):
    queue = deque()

    visited = [ [ 0 for _ in  range(n)] for _ in range(n)]
    queue.append((sx,sy))
    while queue:
        x,y = queue.popleft()
        if x== rx and y == ry:
            break
        for num in range(4):
            nx,ny = x+dx[num],y+dy[num]
            if in_range(nx,ny) and visited[nx][ny] == 0 and maps[nx][ny] == 0 :
                queue.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1
    if visited[rx][ry] == 0 :
        return False,-1
    else :
        return True,visited[rx][ry]
arr = []
zoongbok = []
l_count = 1000000
def backtracking(num):
    global l_count,maps
    if num == k :
        #print(arr)
        count = 0
        temp_maps = [ [ maps[i][j] for j in range(n)] for i in range(n)]
        for (a,b) in (arr):
            maps[a][b] = 0
        possi, count = bfs(sx,sy,rx,ry)
        if possi : # 도착가능함
            l_count = min(l_count, count)
        else : # 도작못함
            pass
        maps = [[temp_maps[i][j] for j in range(n)] for i in range(n)]

        return

    for items in temps:
        if items in arr : continue
        arr.append(items)
        backtracking(num+1)
        arr.pop()

backtracking(0)
if l_count == 1000000:
    print(-1)
else :
    print(l_count)