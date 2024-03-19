#import sys
from collections import deque
#sys.stdin = open('input_1-1.txt','r')
l,n,q = map(int,input().split())
maps=[list(map(int,input().split())) for _ in range(l)]
# 1이 함정, 2가 벽 ,0 은 빈칸 
night = {}
night_health = {}
night_damaged = {}
arr_night = [[0]*l for _ in range(l)]
isdie_night = {}
for num in range(1,n+1) : 
    zr,zc,zh,zw,zk = map(int,input().split())
    zr-=1
    zc-=1
    #인덱스 1부터 시작 
    night[num] = (zr,zc,zh,zw)

    for i in range(zr,zr+zh) :
        for j in range(zc,zc+zw) : 
            arr_night[i][j] =  num
    night_health[num]=zk
    night_damaged[num] = 0
    isdie_night[num] = False

def in_range(x,y) : 
    return 0<=x<l and 0<=y<l

dxs=[-1,0,1,0]
dys=[0,1,0,-1]


def personal_night_move(ri,rd,arr) : 
    final_can_move_night = []
    final_can_move_night.append(ri)
    # bfs써서 아래 방향으로 탐색 해버리기. 
    queue = deque()
    visited = [[0]*l for _ in range(l)]
    r,c,h,w = night[ri]

    for i in range(r,r+h) : 
        for j in range(c,c+w) : 
            queue.append((i,j))
            visited[i][j] = 1

    while queue : 
        x,y = queue.popleft()
        now_night_number = ri
        nx,ny = x+dxs[rd],y+dys[rd]
        if in_range(nx,ny) : 
            if arr_night[nx][ny] != now_night_number and arr_night[nx][ny] != 0  : # 가는곳에 다른애가있다면?  
                next_night_number = arr_night[nx][ny]
                #그녀석의 정보를다 queue에 넣어줘야한다. 
                if not next_night_number in final_can_move_night :
                    final_can_move_night.append(next_night_number)
                    nr,nc,nh,nw = night[next_night_number]
                    now_night_number = ri
                    for i in range(nr,nr+nh) : 
                        for j in range(nc,nc+nw) : 
                            queue.append((i,j))
                            visited[i][j] += 1
            elif maps[nx][ny] ==2 and arr_night[nx][ny] == now_night_number : #벽위에 올라가있으면, 
                continue
            elif maps[nx][ny] == 2 :# 벽이있다면? 
                return []
        else : # 벽이라면
            return []
            

    return final_can_move_night


def is_night_move(oi,od) : 
    # 이동할때 체스판 밖도 벽으로 간주한다. 즉, 이동할때 벽밖으로 밀지는 못함. 

    #해당 기사를 다음 칸으로 밀어버리고, 그 이동한 칸에 각 숫자가 있으면 그놈들을 다 이동시켜야한다. 
    temp_arr = [[0]*l for _ in range(l) ] 
    can_move = personal_night_move(oi,od,temp_arr)
    #움직일수있는 기사들의 번호를 리턴한다. 만약 길이가 0이면 움직일수없음. 
    if len(can_move) == 0 : 
        return False,[]
    
    for night_number in can_move: # 움직여지는놈들 움직이게 하기. 아닌애들도 해야함. 
        night_can_go(night_number,od,temp_arr)
    
    for nights in range(1,n+1) : 
        if nights in can_move:
            continue
        if isdie_night[nights] :continue
        stay_night_stand(nights,temp_arr)
        #여기에 그자리에 있어야함 
    

    for i in range(l) : 
        for j in range(l) : 
            arr_night[i][j] = temp_arr[i][j]

    return True,can_move

def stay_night_stand(night_number,temp_arr) : 
    r,c,h,w = night[night_number]
    for i in range(r,r+h):
        for j in range(c,c+w) : 
            temp_arr[i][j] = night_number
    return



def night_can_go(night_number,direction,temp_arr) : 
    r,c,h,w = night[night_number]

    for i in range(r,r+h):
        for j in range(c,c+w) : 
            nx = i+dxs[direction]
            ny = j+dys[direction]
            temp_arr[nx][ny] = night_number
    
        night[night_number] = (r+dxs[direction],c+dys[direction],h,w)

    return

def check_trap(night_number) : 
    r,c,h,w = night[night_number]
    cnt =0 
    for i in range(r,r+h):
        for j in range(c,c+w) : 
            if maps[i][j] == 1 :#함정이 있으면 
                cnt +=1
    return cnt 


def dienight(night_number) : 
    r,c,h,w = night[night_number]
    for i in range(r,r+h):
        for j in range(c,c+w) : 
            arr_night[i][j] = 0
    return

def battle_damage(i,d,moved_arr) : 

    #i,d 의 위치에있는 함정은 영향받지 않는다. 
    # moved_arr 는 기사의 번호다. 이녀석들이 움직여진 녀석들.
    for night_number in moved_arr: 
        if i == night_number: continue

        damage = check_trap(night_number)
        night_health[night_number] = night_health[night_number] - damage
        night_damaged[night_number] = night_damaged[night_number] + damage

        if night_health[night_number] <= 0 : # 빼고난 다음이 0보다 작으면 
            dienight(night_number)
            isdie_night[night_number] = True

    return 

def chk_live_night() : 
    point = 0
    for i in range(1,n+1) : 
        if isdie_night[i] : continue
        point += night_damaged[i]
    return point
answer = 0
for item in range(q) : #왕의명령 
    oi,od = map(int,input().split())
    if isdie_night[oi] : continue
    check,moved_arr = is_night_move(oi,od)
    if check:
        battle_damage(oi,od,moved_arr)

answer = chk_live_night()
print(answer)