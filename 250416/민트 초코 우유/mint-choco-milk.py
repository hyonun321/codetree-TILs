
from collections import deque

N,T = map(int,input().split())
types = []
level =[]


# 민초우 민초 민우 초우 우 초 민 
#   1   2   3  4   5  6 7 


for i in range(N):
    temp = list(input())
    t_arr = [ 0 for _ in range(N)]
    for j in range(len(temp)):
        if(temp[j] == "T"):
            t_arr[j] = 7
        elif(temp[j] == "C"):
            t_arr[j] = 6
        else :
            t_arr[j] = 5
    types.append(t_arr)

for _ in range(N):
    temp_m = list(map(int,input().split()))
    level.append(temp_m)

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def print_all(rounds,texts):
    print(texts)
    print("현재라운드:",rounds)
    print("print_types")
    for k in types:
        print(*k)
    print()
    print("print_level")
    for x in level:
        print(*x)
    print()

def morning ():
    for i in range(N):
        for j in range(N):
            level[i][j] +=1
    return

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def make_group_pop_master(x,y,visited):
    m_r,m_c = x,y
    m_item = level[x][y]
    level[x][y] -=1
    queue = deque()
    queue.append((x,y))
    group_count = 1
    item= types[x][y]
    visited[x][y] = True
    while queue:
        x,y = queue.popleft()
        for num in range(4):
            nx,ny = x+dx[num],y+dy[num]
            if in_range(nx,ny) and visited[nx][ny] == False and types[nx][ny] == item :
                if(m_item < level[nx][ny]) : 
                    m_r = nx
                    m_c = ny
                    m_item = level[nx][ny]
                group_count +=1
                queue.append((nx,ny))
                level[nx][ny] -=1
                visited[nx][ny] = True

    # 대표자 신앙심 올리기
    level[m_r][m_c] += group_count


    return (level[m_r][m_c],m_r,m_c)

def lunch ():
    master_arr=[]
    visited = [[ False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if(visited[i][j] == False):
                m_type = types[i][j]
                m_l,m_r,m_c = make_group_pop_master(i,j,visited)
                # 대표자 신앙심레벨, r, c, 타입 번호 
                # 그룹 정보를 넣어준다.
                m_g = 2
                if(5 <= m_type <= 7) :
                    m_g = 0
                elif(2<= m_type<=4):
                    m_g = 1
                master_arr.append((m_l,m_r,m_c,m_type,m_g))
    return master_arr


def include_type (attack,defense):

    idx_to_char = {
        1:[1,1,1],
        2:[0,1,1],
        3:[1,0,1],
        4:[1,1,0],
        5:[1,0,0],
        6:[0,1,0],
        7:[0,0,1]
    }

    char_to_idx = {
        (1, 1, 1): 1,
        (0, 1, 1): 2,
        (1, 0, 1): 3,
        (1, 1, 0): 4,
        (1, 0, 0): 5,
        (0, 1, 0): 6,
        (0, 0, 1): 7
    }
    x = idx_to_char[defense]
    y = idx_to_char[attack]

    # 민초우 민초 민우 초우 우 초 민 
    #   1   2   3  4   5  6 7 
    for i in range(3) : 
        if(x[i] > 0): continue
        x[i] += y[i]
    
    after_x = char_to_idx[tuple(x)]

    return after_x


def dinner (master_arr):

    # 정렬 
    # 신앙심 높은순, 행번호, 열번호 작은순 
    master_arr.sort(key=lambda x: (x[4],-x[0], x[1], x[2]))
    defense = [ [ False for _ in range(N)] for _ in range(N)]
    # print(master_arr)
    def check_infect(master): # 전파

        ml,mr,mc,mt,_ = master
        if(defense[mr][mc] == True) :
            return
        power = ml -1 
        direction = ml%4
        x,y = mr,mc
        level[mr][mc] = 1
        def infect (nx,ny,power):
            y = level[nx][ny]
            if(power>y): # 강한전파 
                power -= (y+1)
                types[nx][ny] = mt
                level[nx][ny] += 1 
            else : # 약한전파 
                types[nx][ny] = include_type(mt,types[nx][ny])
                defense[nx][ny] = True
                # print(power,nx,ny,"여긴데") # 뭔가 power의 갱신이 잘안되는거같음. 잘봐야할듯.
                level[nx][ny] += power
                power = 0
            return power
        # print(x,y,"시작")

        while True : 
            # print("여ㅑ긴",x,y,power,types[x][y],mt,defense[x][y])
            nx,ny = x+dx[direction],y+dy[direction]
            
            if(not in_range(nx,ny) or power <= 0):
                break
            #print("다음",nx,ny,defense[nx][ny],types[nx][ny])
            if(types[nx][ny] == mt ): # 지금 0,2 -> 1,2 -> 2,2 가는게 이상하게감. 원래면 약한전파로 1,2 에서 끊겨야함. 
                x,y = nx,ny
                continue
            # print("before power")
            power = infect(nx,ny,power)
            x,y = nx,ny

        return
    
    for master in master_arr:
        check_infect(master)
        # print_all(rounds,"마스터")
    return

def print_type():
    answer = [0,0,0,0,0,0,0]
    for i in range(N):
        for j in range(N):
            answer[types[i][j]-1] +=level[i][j]
    for k in answer:
        print(k,end=" ")
    print()
    return

for rounds in range(T):
    morning()
    # print_all(rounds,"after morning")
    master_arr = lunch()
    # print_all(rounds,"after lunch")
    dinner(master_arr)
    # print_all(rounds,"after dinner")
    print_type()
    