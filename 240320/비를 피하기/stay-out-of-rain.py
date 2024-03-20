#import sys
from collections import deque
#sys.stdin = open('샘플용.txt','r')


dx=[-1,0,1,0]
dy=[0,1,0,-1]

n,h,m=map(int,input().split())
maps = [ list(map(int,input().split())) for _ in range(n)]

# 0 이동
# 1 벽
# 2 사람
# 3 비 피하기 
def in_range(x,y):
    return 0<=x<n and 0<=y<n
def bfs(x,y):
    visitied = [ [0 for _ in range(n)] for _ in range(n) ]
    queue = deque()
    possible = False
    queue.append((x,y))
    visitied[x][y] = 0
    while queue:
        x,y = queue.popleft()
        if maps[x][y] == 3 : 
            possible = True
            break
        for num in range(4):
            nx,ny = x+dx[num],y+dy[num]
            if in_range(nx,ny) and  visitied[nx][ny] == 0 and ( maps[nx][ny] != 1) :
                queue.append((nx,ny))
                visitied[nx][ny] = visitied[x][y] +1
    if possible:       
        counts = visitied[x][y]
        return counts
    else : 
        return -1 


master = [ [0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if maps[i][j] == 2 : # 사람이면 
            count = bfs(i,j)
            if count == -1 : 
                master[i][j] = -1
            else : 
                master[i][j] = count

for k in master:
    print(*k)