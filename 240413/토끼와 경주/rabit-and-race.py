import sys

#sys.stdin = open('토끼와경주.txt', 'r')

Q = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dist = {}  # 특정 고유번호를 가진 토끼의 이동거리
jumping = {}  # 점프횟수를 담는
priority = []  # 우선순위용 배열
max_point = 0
score = {}
for _ in range(Q):
    strings = input().split()
    if strings[0] == '100':
        N, M, P = strings[1], strings[2], strings[3]
        N = int(N)
        M = int(M)
        P = int(P)
        for tt in range(P):
            tpid, td1 = map(int, (strings[4 + tt * P], strings[5 + tt * P]))
            dist[tpid] = td1
            priority.append((0, 0, 0, 0, tpid))
            jumping[tpid] = 0
            score[tpid] = 0
    elif strings[0] == '200':
        K, S = map(int, (strings[1], strings[2]))
        #print(K, S)
        jumped = {}

        for _ in range(K):
            priority.sort(key=lambda x: (x[0], x[1], x[2], x[3], x[4]))
            p1, p2, p3, p4, ppid = priority[0]

            one_dist = dist[ppid]
            # 이동하는 도중 그 다음 칸이 격자를 벗어나게 된다면 방향을 반대로 바꿔 한 칸 이동
            temp = []
            for num in range(4):
                nx, ny = (p3 + one_dist * dx[num]), (p4 + one_dist * dy[num])
                #print('맨처음',nx,ny)
                if nx < 0 :
                    nx = abs(nx)
                    pass
                if ny <0 :
                    ny = abs(ny)
                    pass
                #print((2*(N-2)+2))
                nnx = nx%(2*(N-2)+2)
                nny = ny%(2*(M-2)+2)
                #print('체크',nnx)
                if nnx == 0 or nnx > (N-1) :
                    if nnx != 0 :
                        nnx=(2*(N-2)+2) - nnx
                if nny == 0 or nny > (M-1) :
                    if nny != 0 :
                        nny=(2*(M-2)+2) - nny
                #print('1보정후',nnx,nny)
                temp.append((nnx + nny, nnx, nny))  # 이거 안쓰고 그냥 if 튜플비교하면 더빠를듯

            temp.sort(key=lambda x: (-x[0], -x[1], -x[2]))
            _, max_x, max_y = temp[0]
            tj = jumping[ppid]
            tj += 1
            jumping[ppid] = tj
            priority[0] = (tj, max_x + max_y, max_x, max_y, ppid)
            jumped[ppid] = (max_x + max_y, max_x, max_y, ppid)
            for key, value in score.items():
                if key == ppid: continue
                score[key] = value + max_x + 1 + max_y + 1

                if max_point < score[key]:
                    max_point=score[key]
                # 최고스코어 비교
        # K다끝나고
        jumped = list(jumped.values())
        jumped.sort(key=lambda x: (-x[0], -x[1], -x[2], -x[3]))
        _, _, _, jpid = jumped[0]
        score[jpid] += S
        #최고스코어 비교
        if score[jpid] > max_point:
            max_point = score[jpid]
        pass
    elif strings[0] == '300':
        pid_t, L = strings[1], strings[2]
        pid_t = int(pid_t)
        L = int(L)
        dist[pid_t] *= L


    else:  # 최대값 출력
        print(max_point)