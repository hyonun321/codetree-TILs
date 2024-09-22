import copy


dx=[0,-1,-1,-1,0,1,1,1]
dy=[1,1,0,-1,-1,-1,0,1]

deb =0
def print_b(arr):
    for k in arr:
        print(*k)
    print()
n,m = map(int,input().split())
board  = [ list(map(int,input().split())) for _ in range(n)]
order = []
for _ in range(m):
    order.append((map(int,input().split())))
nutrient = [ [0 for _ in range(n)] for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<n


def move_tree(dir,power ):
    global nutrient
    temp_arr = [ [0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if nutrient[i][j] == 1 :
                nx,ny = (i+power*dx[dir-1]+n)%n,(j+power*dy[dir-1]+n)%n
                temp_arr[nx][ny] = 1
    if deb:
        print_b(temp_arr)
    nutrient =copy.deepcopy(temp_arr)
    return


def cut_and_update_nut():
    global nutrient,board
    new_board = [ [0 for _ in range(n)] for _ in range(n)]
    new_nut = [ [0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 2 and nutrient[i][j] == 0:
                new_board[i][j] = board[i][j] - 2
                new_nut[i][j] = 1
            else :
                new_board[i][j] = board[i][j]
    board = copy.deepcopy(new_board)
    nutrient = copy.deepcopy(new_nut)
    if deb:
        print_b(nutrient)
    return
def grow_up():

    for i in range(n):
        for j in range(n):
            if nutrient[i][j] == 1 :
                board[i][j] += 1
                # 먼저 영양제를 공급하고난다음에 대각탐색을한다.

    for i in range(n):
        for j in range(n):
            if nutrient[i][j] == 1 :
                for d in range(1,8,2):
                    nx,ny = i+dx[d],j+dy[d]
                    if in_range(nx,ny) and board[nx][ny] > 0:
                        board[i][j] += 1
    if deb:
        print_b(board)
    return

def cal_tree():
    count = 0
    for i in range(n):
        for j in range(n):
            count +=board[i][j]
    return count
## 초기는 왼쪽아래
nutrient[n-1][0]=1
nutrient[n-1][1]=1
nutrient[n-2][0]=1
nutrient[n-2][1]=1
for year in range(m):
    dir,power = order[year]
    #특수 영양제 이동
    move_tree(dir,power)
    #특수 영양제의 나무 흡수
    grow_up()
    # 2이상 높이 나무 1/2 하고 거기에 영양제 놓기.
    cut_and_update_nut()
print(cal_tree())