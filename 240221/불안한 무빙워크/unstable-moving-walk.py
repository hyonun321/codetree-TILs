n, k = map(int, input().split())
maps = list(map(int, input().split()))
rail_position = {}
rail_health = {}
# 레일번호, 레일안정성, 레일 현 위치, 프론트/언더 유무
rail = []
for i in range(n) :
    rail_position[i+1] = i+1
    rail_health[i+1] = maps[i]
    rail.append(True)
for j in range(n,n*2) :
    rail_position[j+1] = j+1
    rail_health[j+1] = maps[j]
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
    for x in range(len(people)) :
        possible = True
        a,b = people[x] # 사람번호, 현재 레일 번호
        if b == -100 : continue
        next_b = (b)%(2*n) +1

        # 사람이있나 체크
        for k in range(len(people)) :
            a1,b1= people[k]
            if b1 == next_b :
                possible = False
        # 체력이 0 인가 체크
        if rail_health[next_b] == 0 :
            possible = False
        else :
            if possible :
                health = rail_health[next_b]
                health -= 1
                rail_health[next_b] = health
        if possible : # 만약 옮길 수 있다면?
            people[x] = (a,next_b)
    return

people = []  # (i번째 사람 ,j번째 레일 위)
p_number = 1

def add_people():
    global p_number
    possible = True
    for k in range(n*2):

        if rail_position[k+1] == 1 :

            for z in range(len(people)) :
                a,b = people[z]
                if b == -100 : continue
                if b == k+1 : #1위치에있는 레일에 사람이있다?
                    possible = False
            if possible and rail_health[k+1] != 0:
                health = rail_health[k+1]
                health -=1
                rail_health[k+1] = health
                people.append((p_number, k+1)) # 지금 1번자리에있는 번호가들어가야함.
                p_number += 1

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
    global people
    temp= []
    for k in range(len(people)) :
        a,b = people[k]

        if rail_position[b] != n :
            temp.append((a,b))
    people = temp.copy()

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