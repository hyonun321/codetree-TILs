import sys
from collections import deque
#sys.stdin=open('코드트리오마카세.txt','r')
n = int(input())

maps = [list(map(int,input().split())) for _ in range(n)]

r,c,m1,m2,m3,m4,dir = map(int,input().split())
r-=1
c-=1
# 이는 기울어진 직사각형이 r행, c열에서 시작하여
# 1번, 2번, 3번, 4번 방향으로 각각 m1, m2, m3, m4만큼 순서대로 이동했을 때
# 그려지는 직사각형임을 의미하며, dir이 0인 경우에는 반시계 방향으로 1칸씩 회전해야 함을,
# dir이 1인 경우에는 시계 방향으로 1칸씩 회전해야 함을 의미합니다.

#dx는 반시계순회
dx=[-1,-1,1,1]
dy=[1,-1,-1,1]


num = 0
nx,ny = r,c
#print(maps[nx][ny],r,c)
queue = deque()
queue.append((r,c))
queue1 = deque()
queue1.append(maps[nx][ny])
#1 전진
for i in range(1,m1+1):
    nx,ny = nx+dx[num],ny+dy[num]
    #print(maps[nx][ny],nx,ny)
    queue.append((nx,ny))
    queue1.append(maps[nx][ny])
#2전진

num += 1
for j in range(1,m2+1):
    nx,ny = nx+dx[num],ny+dy[num]
    #print(maps[nx][ny],nx,ny)
    queue.append((nx,ny))
    queue1.append(maps[nx][ny])

num += 1
#3전진
for j1 in range(1,m3+1):
    nx,ny = nx+dx[num],ny+dy[num]
    #print(maps[nx][ny],nx,ny)
    queue.append((nx,ny))
    queue1.append(maps[nx][ny])
#4전진
num += 1
#3전진
for j1 in range(1,m4):
    nx,ny = nx+dx[num],ny+dy[num]
    #print(maps[nx][ny],nx,ny)
    queue.append((nx,ny))
    queue1.append(maps[nx][ny])

#print(queue1)
if dir == 0 :
    temp= queue1.pop()
    queue1.appendleft(temp)
else :
    temp = queue1.popleft()
    queue1.append(temp)
#print(queue)
#print(queue1)

for idx in range(len(queue)):
    tx,ty = queue[idx]
    tnumber = queue1[idx]
    maps[tx][ty] = tnumber

for k in maps:
    print(*k)