import sys

#sys.stdin = open("Sam의 피자학교.txt", 'r')
deb = 0
dee = 1

def insert_mill():
    num_min = min(maps)
    for c in range(len(maps)):
        if maps[c] == num_min:
            maps[c] += 1
    return


# 도우 말기
def dou_roll():
    cut_index = 0

    row = 1
    r_count = 1
    rr_count = 2
    col = 1
    c_count = 1
    while True :

        if deb:
            print('컷인덱스 :', cut_index)
        if cut_index+(r_count) >= n :
            if deb :
                print(cut_index)
                print(row)
            break # 다음번껄 미리 예상해서 재본다.

        for i in range(1,row+1) :
            for j in range(1,col+1):
                if deb:
                    print('row', i)
                    print('col', j)
                maps_dou[n - i -1][cut_index + j] = maps_dou[n - j][cut_index-i+1]
                if deb:
                    print('값이동:',n - i-1,cut_index + j)
                    print('0이됨:',n - j,cut_index-i+1)
                maps_dou[n - j][cut_index-i+1] = 0
        cut_index += r_count
        c_count +=1
        rr_count += 1
        row += 1
        if rr_count >=2 :
            r_count += 1
            rr_count = 0
        if c_count %2 == 0 :
            col += 1
            c_count = 0
        if deb:
            debug('한번끝나고')

    #맨처음
    #maps_dou[n - 2][cut_index+1 ] = maps_dou[n - 1][cut_index]
    #maps_dou[n - 1][cut_index] = 0

    #두번째

    #maps_dou[n - 2][cut_index+1 ] = maps_dou[n - 1][cut_index]
    #maps_dou[n - 2][cut_index+2 ] = maps_dou[n - 2][cut_index]


    #세번째
    #maps_dou[n - 2][cut_index + 1] = maps_dou[n - 1][cut_index]
    #maps_dou[n - 2][cut_index + 2] = maps_dou[n - 2][cut_index]

    #maps_dou[n - 3][cut_index + 1] = maps_dou[n - 1][cut_index - 1]
    #maps_dou[n - 3][cut_index + 2] = maps_dou[n - 2][cut_index - 1]

    #maps_dou[n - 1][cut_index] = 0
    #maps_dou[n - 2][cut_index] = 0

    #maps_dou[n - 1][cut_index - 1] = 0
    #maps_dou[n - 2][cut_index - 1] = 0

    #debug('세번끝나고')
    #cut_index += fold_index
    #fold_index += 1
    #print(cut_index+fold_index)

    # maps_dou[n-1][cut_index+1] = [n-1][cut_index]

    return

def in_range(x,y) :
    return 0<=x<n and 0<=y<n

# 도우 누르기

def dou_push():

    global maps,maps_dou
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]


    temp_maps_dou = [ [0 for _ in range(n)] for _ in range(n)]

    for i in range(n) :
        for j in range(n) :
            if maps_dou[i][j] > 0 :

                for num in range(4):

                    nx,ny = i+dx[num],j+dy[num]
                    if in_range(nx,ny) and maps_dou[nx][ny] > 0 :
                        d = abs(maps_dou[nx][ny]-maps_dou[i][j])// 5
                        if maps_dou[nx][ny] > maps_dou[i][j] :
                            temp_maps_dou[nx][ny] -= d
                            temp_maps_dou[i][j] += d
                        else :
                            temp_maps_dou[nx][ny] += d
                            temp_maps_dou[i][j] -= d

    for i in range(n):
        for j in range(n) :
            temp_maps_dou[i][j] = temp_maps_dou[i][j]//2
            maps_dou[i][j] += temp_maps_dou[i][j]
    if deb:
        debug('누르고')

    maps = []

    for j in range(n) :
        for i in range(n - 1, -1, -1):
            if maps_dou[i][j] > 0 :
                maps.append(maps_dou[i][j])
    if deb:
        print(maps)

    return


# 도우 두번 접기

def dou_fold_twice():
    global  maps

    all_idx = len(maps)

    half_idx = (all_idx//2) -1
    temp_maps_dou = [[0 for _ in range(n)] for _ in range(n)]  # 밀가루 양이 담긴 말린 2차원 배열
    for iii in range(n):
        temp_maps_dou[n - 1][iii] = maps[iii]

    for i in range(half_idx+1) :
        temp_maps_dou[n-2][n-1-i] = temp_maps_dou[n-1][i]
        temp_maps_dou[n - 1][i] = 0
    if deb:
        print('temp확인한다!!!')
        for m in temp_maps_dou:
            print(*m)

    four_half_idx = half_idx + half_idx//2 +1
    if deb:
        print(four_half_idx)

    for j in range(half_idx,four_half_idx+1) :
        for t in range(2):
            temp_maps_dou[n-3-t][half_idx-j] = temp_maps_dou[n-2+t][j]
            temp_maps_dou[n - 2 + t][j] = 0
    if deb:
        print('temp 또또또  확인한다!!!')
        for m in temp_maps_dou:
            print(*m)


    for i in range(n) :
        for j in range(n) :
            maps_dou[i][j] = temp_maps_dou[i][j]

    return



# 도우 누르기




def debug(strg):
    print(strg)
    print('maps')
    for v in maps:
        print(v, end=' ')
    print()
    print('dou')
    for k in maps_dou:
        print(*k)
    print('---------')
    return




n, k = map(int, input().split())
maps = list(map(int, input().split()))  # 밀가루 양의 배열이 담긴 긴 1차원 배열

maps_dou = [[0 for _ in range(n)] for _ in range(n)]  # 밀가루 양이 담긴 말린 2차원 배열


def update_dou():
    global  maps_dou
    maps_dou =[[0 for _ in range(n)] for _ in range(n)]
    for iii in range(n):

        maps_dou[n - 1][iii] = maps[iii]
    return


answer = 0

def is_maps():
    global maps
    max_mill = max(maps)
    min_mill = min(maps)
    return abs(max_mill-min_mill)

while True:
    if (is_maps() <= k) : break
    if deb:
        print('현재',answer,'만큼 시도중')
    insert_mill()
    if deb :
        debug(0)
    update_dou()
    if deb:
        debug(0)
    dou_roll()
    dou_push()
    dou_fold_twice()
    dou_push()
    answer += 1

print(answer)