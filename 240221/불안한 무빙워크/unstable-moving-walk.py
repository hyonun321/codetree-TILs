from collections import deque
#import sys

#sys.stdin = open("불안한무빙워크.txt", 'r')
n, k = map(int, input().split())
maps = list(map(int, input().split()))

# 레일번호, 레일안정성, 레일 현 위치, 프론트/언더 유무
rail = []
for i in range(n) :
    rail.append((i+1,maps[i],i+1,True))
for j in range(n,n*2) :
    rail.append((j+1,maps[i],j+1,False))



def moving_walk_rotate():

    for i in range(2*n) :
        number,health,position,up_down = rail[i]
        next_position = position%(2*n) + 1
        if next_position > n :
            up_down = False
        else :
            up_down = True
        rail[i] = number,health,next_position,up_down

    # 사람들 위치가 n 인지 체크해야한다.
    return


def people_walking():
    possible = True

    for x in range(len(people)) :
        a,b = people[x] # 사람번호, 현재 레일 번호
        if b == -100 : continue
        next_b = (b)%(2*n) +1

        # 사람이있나 체크

        for k in range(len(people)) :
            a1,b1= people[k]
            if b1 == next_b :
                possible = False
        # 체력이 0 인가 체크
        for t in range(n*2) :
            number, health, position, up_down = rail[t]
            if next_b == number :
                if health == 0 :
                    possible = False
                else :
                    health -= 1
                    rail[t] = number, health, position, up_down
        if possible : # 만약 옮길 수 있다면?
            people[x] = (a,next_b)

    return


people = []  # (i번째 사람 ,j번째 레일 위)
p_number = 1


def add_people():
    global p_number
    possible = True
    for x in range(len(people)):
        a,b = people[x]
        if b == 1 :
            possible = False

    if possible:
        for k in range(n*2):
            number, health, position, up_down = rail[k]
            if position == 1 and health != 0:
                health -= 1
                rail[k] = number, health, position, up_down
                people.append((p_number, number)) # 지금 1번자리에있는 번호가들어가야함.
                p_number += 1

    return
def debug():
    print()
    for k in rail:
        print(*k)
    print(people)
    return

def check_zero_pan(k):
    count = 0
    for c in range(2*n) :
        number, health, position, up_down = rail[c]
        if health == 0 :
            count += 1
    if count >= k :
        return True
    else :
        return False


def check_position_n() :
    for k in range(len(people)) :
        a,b = people[k]
        for x in range(2*n) :
            number, health, position, up_down = rail[x]
            if number == b :
                if position == n :#n에 도착하면 우주로 보냄.
                    b = -100
                    people[k] = a,b
    return

answer = 0
while True:
    answer += 1

    moving_walk_rotate()
    check_position_n()
    #print(1)
    #debug()
    people_walking()
    check_position_n()
    #print(2)
    #debug()
    add_people()
    #print(3)
    #debug()
    if check_zero_pan(k): break

print(answer)