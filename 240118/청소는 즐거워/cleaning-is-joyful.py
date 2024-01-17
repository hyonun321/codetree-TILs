import sys

#sys.stdin = open("삼성기출/청소는즐거워.txt",'r')
deb = 0
def in_range(x,y) :
    return 0<=x<n and 0<=y < n

def find_marummo(x,y,direction) : #방향에 따라 달라진다.
    curr = maps[x][y]
    if deb :
        print('curr x,y',x,y)
        print('curr',curr)
    count = 0
    #1%
    a_1 = int((0.01)*curr)

    x_1,y_1 = x-dy[direction]-dx[direction],y-dy[direction]-dx[direction]
    x_1_,y_1_ =x+dy[direction]-dx[direction],y-dy[direction]+dx[direction]
    if deb:
        print(a_1)
        print(x_1,y_1)
        print(x_1_,y_1_)
    if in_range(x_1, y_1):
        maps[x_1][y_1] += a_1
    else:
        count += a_1

    if in_range(x_1_, y_1_):
        maps[x_1_][y_1_] += a_1
    else:
        count += a_1

    #7%
    a_7 = int((0.07) * curr)
    x_7,y_7 = x-dy[direction],y-dx[direction]
    x_7_,y_7_ =x+dy[direction],y+dx[direction]

    if in_range(x_7, y_7):
        maps[x_7][y_7] += a_7
    else:
        count += a_7

    if in_range(x_7_, y_7_):
        maps[x_7_][y_7_] += a_7
    else:
        count += a_7
    #2%
    a_2 = int((0.02)*curr)
    x_2,y_2 = x-2*dy[direction],y-2*dx[direction]
    x_2_,y_2_ =x+2*dy[direction],y+2*dx[direction]
    if in_range(x_2, y_2):
        maps[x_2][y_2] += a_2
    else:
        count += a_2

    if in_range(x_2_, y_2_):
        maps[x_2_][y_2_] += a_2
    else:
        count += a_2



    #10%
    a_10 = int((0.1)*curr)
    x_10_, y_10_ = x+dy[direction]+dx[direction],y+dy[direction]+dx[direction]
    x_10, y_10 = x-dy[direction]+dx[direction],y+dy[direction]-dx[direction]
    if in_range(x_10,y_10) :
        maps[x_10][y_10] += a_10
    else :
        count += a_10

    if in_range(x_10_, y_10_):
        maps[x_10_][y_10_] += a_10
    else:
        count += a_10

    #5%
    a_5 = int((0.05)*curr)
    x_5,y_5 = x+2*dx[direction],y+2*dy[direction]
    if in_range(x_5,y_5) :
        maps[x_5][y_5] += a_5
    else :
        count += a_5

    last_curr = curr - (a_1+a_1+a_7+a_7+a_2+a_2+a_10+a_10+a_5)
    x_last,y_last = x+dx[direction],y+dy[direction]

    if in_range(x_last,y_last) :
        maps[x_last][y_last] += last_curr
    else :
        count += last_curr
    #a%
    maps[x][y] = 0
    if deb :
        print('out:',count)
        debug()
        print()
    return count


dx=[0,1,0,-1]
dy=[-1,0,1,0]
def debug():
    for k in maps:
        print(*k)
    return

n = int(input())
maps = [list(map(int,input().split())) for _ in range(n)]
x,y = n//2,n//2
direction = 0
turn_count = 1 # 몇번 가고 도냐
movement_count = 0
turn_checker = 0 # 2번 돌았냐
answer= 0



while not (x==0 and y == 0) :
    x,y = x+dx[direction],y+dy[direction]
    answer += find_marummo(x, y, direction)
    movement_count += 1
    if movement_count == turn_count :
        turn_checker += 1
        movement_count = 0
        direction = (direction + 1) % 4
    if turn_checker == 2 :
        turn_checker = 0
        turn_count += 1



print(answer)