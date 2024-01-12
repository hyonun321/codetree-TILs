import sys

#sys.stdin = open("놀이기구탑승.txt",'r')
deb =0
score_list = [0,1,10,100,1000]
# 상우하좌
dx=[-1,0,1,0]
dy=[0,1,0,-1]
n = int(input())
maps = [[None]*n for _ in range(n)]
student_likenum = [[None] for _ in range((n**2)+1)]
answer = 0
def in_range(x,y) :
    return 0<=x<n and 0<=y<n

def find_surround_cells(x,y) :
    count = 0
    for k in range(4) :
        nx,ny = x+dx[k],y+dy[k]
        if in_range(nx,ny) and maps[nx][ny] == None :
            count+=1
    return  count

def find_empty_cells_in_maps(n0) :
    max_count = -1
    fx, fy = -1, -1
    like_friend_count = 0
    for i in range(n) :
        for j in range(n) :
            if maps[i][j] == None :
                temp_count = find_surround_cells(i,j)
                temp_like_friend_count = find_like_friend(i,j,n0)
                if (temp_like_friend_count,temp_count) > (like_friend_count,max_count) :
                    fx,fy = i,j
                    max_count = temp_count
                    like_friend_count = temp_like_friend_count
    return (fx,fy)

def find_like_friend(i,j,n0) :
    t_count = 0
    for num in range(4) :
        nx,ny = i+dx[num],j+dy[num]
        if in_range(nx,ny) and maps[nx][ny] in student_likenum[n0] :
            t_count +=1
    return t_count

if deb:
    maps=[
        [None,None,None],
        [None,3,None],
        [None,None,None]
    ]


def cal_like_friend() :
    point = 0
    for i in range(n) :
        for j in range(n) :
            count = 0
            for num in range(4) :
                nx,ny = i+dx[num],j+dy[num]
                if in_range(nx,ny) and maps[nx][ny] in student_likenum[maps[i][j]]:
                    count +=1
            point += score_list[count]


    return point

for _ in range(n**2) :
    n0,n1,n2,n3,n4 = map(int,input().split())
    student_likenum[n0] = [n1,n2,n3,n4]
    tx,ty = find_empty_cells_in_maps(n0)
    maps[tx][ty] = n0
    #차례대로 들어온놈대로 넣어줘야한다.

answer = cal_like_friend()
print(answer)

if deb:
    for k in maps:
        print(*k)