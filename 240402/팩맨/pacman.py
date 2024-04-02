import sys


#sys.stdin = open('팩맨.txt','r')
# 몬스터 개수를 매번세는데,
# 4x4 인걸로봐서 4x4 순회를 하면 왠지더 빨리 풀 수 있을꺼같음. 만약 시간초과나면 4x4로 바꾸기 (3차원배열)
def in_range(x,y):
    return 0<=x<n and 0<=y<n

def monster_make_egg():
    global eggs
    eggs = []
    for mon in range(len(m_arr)):
        mx,my,md = m_arr[mon]
        if mx == -100 : continue # 수정예정
        eggs.append((mx,my,md))

    return

def monster_move(rounds):
    # 몬스터 시체
    # 팩맨
    # 반시계 45도 회전
    # 있으면 거기로 이동
    # 없으면 가만히
    for mon in range(len(m_arr)):
        mx,my,md = m_arr[mon]
        if mx == -100 : continue # 수정예정 
        nx, ny = mx + dx[md], my + dy[md]
        if in_range(nx,ny) and dead_body[nx][ny] <= rounds and not (nx == px and ny == py ):
            mx, my = nx, ny
        else :
            for num in range(1,8):
                mmd = (md+num)%8
                nx,ny = mx+dx[mmd],my+dy[mmd]
                if in_range(nx,ny) and dead_body[nx][ny] <= rounds and not (nx == px and ny == py ):
                    mx,my = nx,ny
                    md = mmd
                    break
        m_arr[mon] = mx,my,md


    return
def eat_monster(i,j,z):
    tarr=[]
    tarr.append(i)
    tarr.append(j)
    tarr.append(z)
    eat=0
    way_arr=[]
    nx,ny = px,py
    for times in tarr:
        # i로 이동하고 난다음 먹기
        nx,ny = nx+pdx[times],ny+pdy[times]
        if in_range(nx,ny):
            way_arr.append((nx,ny))
        else : #밖으로 나갈경우 그건 존재 x
            return -1,[]

    way_set_arr = set(way_arr)

    for wx,wy in way_set_arr:
        eat += monster_count_arr[wx][wy]
    # 시간초과 우려 ㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇ
    #for monster in range(len(m_arr)):
    #    mx,my,md = m_arr[monster]
    #    if (mx,my) in way_arr: # 안에있으면 죽는다
    #        eat +=1

    return eat,way_arr

def pacman_move(rounds):
    global px,py
    #64개의 이동방향 (상좌하우)
    #배열밖안나감
    #이동과정 몬스터만 먹음 (자기자리에있는애는 안먹음)
    mcount = 0
    m_way = []
    for i in range(4):
        for j in range(4):
            for z in range(4):
                tcount,way_arr = eat_monster(i,j,z)
                if tcount > mcount:
                    mcount = tcount
                    mi,mj,mz = i,j,z
                    m_way = way_arr
    px,py = (m_way[2])
    # 이제 최종 m 을 가지고 몬스터들을 다 죽음처리를 해주면된다.
    # 시간초과 우려
    for mn in range(len(m_arr)):
        mx,my,md = m_arr[mn]
        if (mx,my) in m_way:
            m_arr[mn]= -100,-100,-100 # 우주로 보내기..?
            # 시체만들기
            dead_body[mx][my] = rounds +3 # 시체턴?
    # 팩맨 위치 업데이트 필요.
    return

def monster_dead_disappear():

    return

def egg_up():
    for ex,ey,ed in eggs:
        m_arr.append((ex,ey,ed))
    return

def monster_count_update():
    global monster_count_arr
    monster_count_arr = [[0 for _ in range(n)] for _ in range(n)]
    for monster in range(len(m_arr)):
        mx,my,_ = m_arr[monster]
        if mx == -100 : continue # 수정예정
        monster_count_arr[mx][my] +=1

    return

def cal_monster():
    count = 0
    for monster in range(len(m_arr)):
        mx,my,_ = m_arr[monster]
        if mx == -100 : continue # 수정예정
        count +=1
    return count
pdx=[-1,0,1,0]
pdy=[0,-1,0,1]
dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,-1,-1,-1,0,1,1,1]
m_arr = []
n = 4
m,t = map(int,input().split())
px,py = map(int,input().split())
px-=1
py-=1
monster_count_arr = [ [0 for _ in range(n)] for _ in range(n)]

eggs=[]
dead_body = [ [0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    mr,mc,md = map(int,input().split())
    m_arr.append((mr-1,mc-1,md-1))

for rounds in range(t):
    monster_make_egg()
    monster_move(rounds)
    monster_count_update()
    pacman_move(rounds)
    egg_up()
print(cal_monster())