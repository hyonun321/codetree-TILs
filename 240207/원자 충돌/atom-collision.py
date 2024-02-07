import sys

#sys.stdin = open("원자충돌.txt", 'r')
deb = 0
dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]
n,m,k = map(int,input().split())
maps_3rd=[[[] for _ in range(n)] for _ in range(n)]

for _ in range(m) :
    x,y,m,s,d = map(int,input().split())
    maps_3rd[x-1][y-1].append((m,s,d))


def debug_maps(maps):
    for k in maps:
        print(k)

def cal_all_wonza_weight():
    count = 0
    for i in range(n) :
        for j in range(n) :
            if len(maps_3rd[i][j]) > 0 :
                for items in maps_3rd[i][j] :
                    m2,s2,d2 = items
                    count += m2

    return count
def in_range(x,y) :
    return 0<=x<n and 0<=y<n


def move_all_wonza():

    temp_maps_3rd = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            if not len(maps_3rd[i][j]) == 0 :
                for items in maps_3rd[i][j] :
                    m1,s1,d1 = items
                    if m1 ==1 : pass
                    nx,ny = (i+dx[d1]*s1+n)%n,(j+dy[d1]*s1+n)%n
                    temp_maps_3rd[nx][ny].append((m1,s1,d1))

    if deb :
        print('after moving : temp maps')
        debug_maps(temp_maps_3rd)

    for i in range(n) :
        for j in range(n) :
            maps_3rd[i][j] = []
            if len(temp_maps_3rd[i][j]) != 0 :
                for itemss in temp_maps_3rd[i][j]:
                    maps_3rd[i][j].append(itemss)

    return


def wonza_hapsung():

    temp_maps_3rd = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            if len(maps_3rd[i][j]) >= 2 : # 2개이상일경우
                master_m1,master_s1 = 0,0
                master_d1 = 0 # 0이면 상하좌우, 1이면 대각선
                for items in maps_3rd[i][j] :
                    m1,s1,d1 = items
                    master_m1 += m1
                    master_s1 += s1
                    if d1 == 0 or d1 == 2 or d1 == 4 or d1 == 6 : #상하좌우
                        pass
                    else :
                        master_d1 = 1
                master_m1 = master_m1 // 5
                master_s1 = master_s1 // (len(maps_3rd[i][j]))
                if deb == 2:
                    print(master_s1,master_m1,master_d1)
                if master_m1 == 0 :
                    continue
                if master_d1 == 1 :
                    new_m1,new_s1 = master_m1,master_s1
                    for num_d in range(1,9,2): # 1,3,5,7
                        temp_maps_3rd[i][j].append((new_m1,new_s1,num_d))
                else :
                    new_m1, new_s1 = master_m1, master_s1
                    for num_d in range(0,8,2): # 0,2,4,6
                        temp_maps_3rd[i][j].append((new_m1,new_s1,num_d))
            elif len(maps_3rd[i][j]) == 1 :
                for itemss in maps_3rd[i][j]:
                    xm1,xs1,xd1 = itemss
                    temp_maps_3rd[i][j].append((xm1,xs1,xd1))


    for i in range(n) :
        for j in range(n) :
            maps_3rd[i][j] = []
            if len(temp_maps_3rd[i][j]) != 0 :
                for itemss in temp_maps_3rd[i][j]:
                    maps_3rd[i][j].append(itemss)

    if deb == 3 :
        debug_maps((maps_3rd))

    return


answer = 0
for round in range(k) :
    move_all_wonza()
    wonza_hapsung()
    answer = cal_all_wonza_weight()
print(answer)