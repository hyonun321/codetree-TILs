import sys

from collections import deque

deb = 0

def debug() :
    print('maps')
    for k in maps:
        print(*k)
    print()
    print('rotate_level:',rotate_level)
#sys.stdin = open("회전하는빙하.txt",'r')

queue = deque()
#input
n,q = map(int,input().split())
maps = [ list(map(int,input().split())) for _ in range(2**n)]
rotate_level = list(map(int,input().split()))

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def make_same_maps(maps,temp_maps) :

    for i in range(2**n) :
        for j in range(2**n) :
            maps[i][j] = temp_maps[i][j]

    return

def in_range(x,y) :
    return 0<=x<2**n and 0<=y<2**n




def rotate_all_maps_and_melting() :
    global maps
    for levels in rotate_level :
        if levels == 0 :
            melt_ice()
            continue
        temp_maps = [[0] * (2 ** n) for _ in range(2 ** n)]
        # cut_level = 주어진 레벨단계에서 자르는 그리드 단위
        cut_level = 2**levels
        cut_4_level=2**(levels-1)
        # grid_size = 전체 2차원 배열의 한면 길이
        grid_size = 2**n
        for x in range(0, grid_size,cut_level):
            for y in range(0, grid_size,cut_level): #자르는 단위 만큼 i,j를 넣는다.
                if cut_4_level == 1 :
                    for i in range(cut_4_level+1) : # 레벨 1인 경우는 특수처리
                        for j in range(cut_4_level+1):
                            #print(i+x,j+y)
                            #print('move t o :',j+x,cut_4_level-i+y)
                            temp_maps[j+x][cut_4_level-i+y]=maps[i+x][j+y]
                else :
                    for i in range(0,cut_level,cut_4_level) : # 나머지의 가장 왼쪽위 인덱스
                        for j in range(0,cut_level,cut_4_level):
                            #print(i + x, j + y)
                            #print('move t o :', j + x, cut_4_level - i + y)
                            for q in range(cut_4_level) : # 거기서 순번대로 시계회전시킨 값을 붙여넣는다.
                                for p in range(cut_4_level):
                                    #print(i + x+q, j + y+p)
                                    #print('move t o :', j + x+q, cut_4_level - i + y+p)
                                    temp_maps[j + x+q][ cut_4_level - i + y+p]=maps[i + x+q][ j + y+p]



        #print(levels,'check')
        #print('after turn')
        #for a in temp_maps:
        #    print(*a)
        update_maps(maps,temp_maps)
        melt_ice()
    if deb == 1 :
        for a in maps:
            print(*a)
        print()
    return

def update_maps(maps,temp_maps) :
    for x in range(2**n):
        for y in range(2**n):
            maps[x][y] = temp_maps[x][y]
    if deb == 3 :
        for a in maps:
            print(*a)
        print()
    return

def melt_ice() :
    global maps
    temp_maps = [[0] * (2 ** n) for _ in range(2 ** n)]
    for i in range(2**n) :
        for j in range(2**n):
            if maps[i][j] >0 :
                count = 0
                for num in range(4) :
                    nx,ny = i+dx[num],j+dy[num]
                    if in_range(nx,ny) and maps[nx][ny] > 0 :
                        count+=1
                if count >= 3 :
                    temp_maps[i][j] = maps[i][j]
                else :
                    temp_maps[i][j] = maps[i][j] -1
    update_maps(maps,temp_maps)
    return

def cal_big_ice() :
    visited = [ [False for _ in range(2**n)] for _ in range(2**n)]
    big_ice_goonzip = 0
    for x in range(2**n) :
        for y in range(2**n) :
            if maps[x][y] > 0 :
                queue = deque()
                queue.append((x,y))
                visited[x][y] = True
                ice_goonzip = 1 #처음에 한개 세니까
                while queue:
                    xx,yy = queue.popleft()
                    for num in range(4) :
                        nx,ny = xx+dx[num],yy+dy[num]
                        if in_range(nx,ny) and visited[nx][ny] == False and maps[nx][ny] > 0 :
                            #print(xx,yy,'chk')
                            visited[nx][ny] = True
                            queue.append((nx,ny))
                            ice_goonzip += 1
                big_ice_goonzip = max(ice_goonzip,big_ice_goonzip)
    return big_ice_goonzip

def cal_all_ice() :
    counts = 0
    for i in range(2**n):
        for j in range(2**n) :
            counts += maps[i][j]
    return counts


rotate_all_maps_and_melting()
print(cal_all_ice())
print(cal_big_ice())