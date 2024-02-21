#import sys
from collections import defaultdict
#sys.stdin = open("불안한무빙워크.txt", 'r')
n, k = map(int, input().split())
maps = list(map(int, input().split()))
rail_position = {}
rail_people= {}
rail_health = {}
# 레일번호, 레일안정성, 레일 현 위치, 프론트/언더 유무
rail = []
for i in range(n) :
    rail_position[i+1] = i+1
    rail_health[i+1] = maps[i]
    rail_people[i+1] = 0
    rail.append(True)
for j in range(n,n*2) :
    rail_position[j+1] = j+1
    rail_health[j+1] = maps[j]
    rail_people[j+1] = 0
    rail.append(False)

def moving_walk_rotate():

    for i in range(2*n) :
        position = rail_position[i+1]
        next_position = position%(2*n) + 1
        if next_position > n :
            up_down = False
        else :
            up_down = True
        rail[i] = up_down
        rail_position[i+1] = next_position
    return

def people_walking():
    temp = defaultdict(int)
    for x in range(n*2,0,-1) :
        possible = True
        b = rail_people[x]  # x번째 레일에 사람이있나없나

        if b == 1 :
            next_b = (x)%(2*n) +1
            # 사람이있나 체크
            if rail_people[next_b] == 1 or rail_health[next_b] == 0 :
                possible = False
            else :
                if possible :
                    health = rail_health[next_b]
                    health -= 1
                    rail_health[next_b] = health
                if possible : # 만약 옮길 수 있다면?
                    temp[next_b] = 1
    for k in range(1,n*2-1) :
        rail_people[k] = temp[k]
    return


def add_people():

    for k in range(n*2):
        possible = True
        if rail_position[k+1] == 1 :
            if rail_people[k+1] == 1 : #1위치에있는 레일에 사람이있다?
                possible = False
            if possible and rail_health[k+1] != 0:
                health = rail_health[k+1]
                health -=1
                rail_health[k+1] = health
                rail_people[k+1] = 1 # 지금 1번자리에있는 번호가들어가야함.


    return

def check_zero_pan(k):
    count = 0
    for c in range(2*n) :
        if rail_health[c+1] == 0 :
            count += 1
    if count >= k :
        return True
    else :
        return False


def check_position_n() :
    for keys in (rail_people):
        if rail_position[keys] == n and rail_people[keys] == 1 : # b의 레일위치가 n이고, 해당레일에 사람이있다면,
            rail_people[keys] = 0

    return

answer = 0

while True:
    answer += 1
    moving_walk_rotate()
    check_position_n()
    people_walking()
    check_position_n()
    add_people()
    if check_zero_pan(k): break

print(answer)