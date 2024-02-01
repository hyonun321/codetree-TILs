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
        if cut_index+(r_count) >= n :break # 다음번껄 미리 예상해서 재본다.

        for i in range(1,row+1) :
            for j in range(1,col+1):
                maps_dou[n - i -1][cut_index + j] = maps_dou[n - j][cut_index-i+1]
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

    maps = []

    for j in range(n) :
        for i in range(n - 1, -1, -1):
            if maps_dou[i][j] > 0 :
                maps.append(maps_dou[i][j])
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

    four_half_idx = half_idx + half_idx//2 +1

    for j in range(half_idx,four_half_idx+1) :
        for t in range(2):
            temp_maps_dou[n-3-t][half_idx-j] = temp_maps_dou[n-2+t][j]
            temp_maps_dou[n - 2 + t][j] = 0

    for i in range(n) :
        for j in range(n) :
            maps_dou[i][j] = temp_maps_dou[i][j]

    return

# 도우 누르기

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
    insert_mill()
    update_dou()
    dou_roll()
    dou_push()
    dou_fold_twice()
    dou_push()
    answer += 1

print(answer)