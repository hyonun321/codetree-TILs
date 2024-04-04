import sys

#sys.stdin = open('나무타이쿤.txt','r')

dx=[0,-1,-1,-1,0,1,1,1]
dy=[1,1,0,-1,-1,-1,0,1]

n,m = map(int,input().split())

maps = [list(map(int,input().split())) for _ in range(n)]
nutrient = [ [False for _ in range(n)] for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def cal_maps():
    count = 0
    for i in range(n):
        for j in range(n):
            count += maps[i][j]

    return count

def nutrient_move(nd,np):
    global nutrient
    t_nut=[[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if nutrient[i][j] :
                nx,ny = (i+np*dx[nd]+n)%n,(j+np*dy[nd]+n)%n
                t_nut[nx][ny] = True
                maps[nx][ny] += 1

    nutrient = [ [t_nut[i][j] for j in range(n)] for i in range(n)]

    return
def reebro_tree_growup():

    for i in range(n):
        for j in range(n):
            if nutrient[i][j] :
                count = 0
                for num in range(1,8,2):
                    nx,ny = i+dx[num],j+dy[num]
                    if in_range(nx,ny) and maps[nx][ny]  != 0 :
                        count += 1
                maps[i][j] += count
    return

nutrient[n-1][0]=True
nutrient[n-2][0]=True
nutrient[n-1][1]=True
nutrient[n-2][1]=True
#초기값

def cut_reebro_make_nutrient():
    global nutrient
    t_nutrient = [ [False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if maps[i][j]>=2 and nutrient[i][j] == False:
                maps[i][j] -=2
                t_nutrient[i][j]=True

    nutrient = [ [t_nutrient[i][j] for j in range(n)] for i in range(n)]
    return

for year in range(m):
    nd, np = map(int, input().split())
    nd -= 1
    nutrient_move(nd,np)
    reebro_tree_growup()
    cut_reebro_make_nutrient()

print(cal_maps())