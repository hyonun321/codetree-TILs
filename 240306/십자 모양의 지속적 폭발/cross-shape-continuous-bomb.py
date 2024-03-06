n,m = map(int,input().split())
maps=[list(map(int,input().split())) for _ in range(n)]
bomb_arr = []
for _ in range(m):
    bomb_arr.append(int(input())-1)
def in_range(x,y):
    return 0<=x<n and 0<=y<n

def boom(x,y) : 
    size = maps[x][y]

    for i in range(size):
        nx,ny = x+i,y
        if in_range(nx,ny):
            maps[nx][ny] = 0
    for j in range(size):
        nx,ny = x,y+j
        if in_range(nx,ny):
            maps[nx][ny] = 0
            
    if size != 1 :
        for i in range(-size,0,1):
            nx,ny = x+i,y
            if in_range(nx,ny):
                maps[nx][ny] = 0
        for j in range(-size,0,1):
            nx,ny = x,y+j
            if in_range(nx,ny):
                maps[nx][ny] = 0

    return

def clear_up():
    for j in range(n):
        for check in range(n-1,-1,-1) : 
            if maps[check][j] != 0 :continue
            # 0일때
            for select in range(check,-1,-1):
                if maps[select][j] != 0 :
                    maps[check][j] = maps[select][j]
                    maps[select][j] = 0
                    break
            
    return

def boom_check(y) : 
    for i in range(n):
        if maps[i][y] != 0 : 
            boom(i,y)
            break
    return

for ys in bomb_arr:
    boom_check(ys)
    clear_up()

for k in maps:
    print(*k)