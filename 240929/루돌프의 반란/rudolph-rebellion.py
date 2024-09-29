import sys

deb = 0
N, M, P, C, D = map(int, input().split())
Rr, Rc = map(int, input().split())
santa_point = [0] * (P + 1)
santa = [0] * (P + 1)
board = [[0 for _ in range(N)] for _ in range(N)]
Rr -= 1
Rc -= 1
board[Rr][Rc] = -1
santa_sturn = [0] * (P + 1)
for _ in range(P):
    Pn, Sr, Sc = map(int, input().split())
    Sr -= 1
    Sc -= 1
    santa[Pn] = (Sr, Sc)
    board[Sr][Sc] = Pn


def in_range(x, y):
    return 0 <= x < N and 0 <= y < N


def cal_distance(r1, r2, c1, c2):
    return (r1 - r2) ** 2 + (c1 - c2) ** 2


def print_b(arr):
    for k in arr:
        print(*[f"{num:2}" for num in k])
    print()


def print_s():
    for (i, k) in enumerate(santa):
        if i == 0: continue
        print(i, "번째 산타 : ", k, "\n", end='')
    print_b(board)

    print()


def roodolf_m(turn):
    global Rr, Rc
    # 가장가까운 산타찾아야함
    # 탈락하면안됨.
    min_dist = 100000
    mr, mc = -1, -1
    board[Rr][Rc] = 0
    for num in range(1, P + 1):
        sr, sc = santa[num]
        if sr == -1: continue
        dist = cal_distance(Rr, sr, Rc, sc)
        if (dist, -sr, -sc) < (min_dist, -mr, -mc):
            min_dist = dist
            mr, mc = sr, sc

    if deb:
        print("루돌프가 노리는곳 : ", mr, mc)

    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    mx, my = (-1, -1)
    m_dist = 100000
    mdir = -1
    for d1 in range(8):
        nx, ny = Rr + dx[d1], Rc + dy[d1]
        dist1 = cal_distance(nx, mr, ny, mc)
        if in_range(nx,ny) and dist1 < m_dist:
            m_dist = dist1
            mx, my = (nx, ny)
            mdir = d1

    Rr, Rc = mx, my
    if deb:
        print(m_dist, "만큼 떨어져있고 루돌프는", mx, my, "로 이동")
    # 충돌검사 필요
    if board[Rr][Rc] > 0:  # 뭔가있따
        temp = board[Rr][Rc] # 문제 1번 -> -1 을 하나의 board맵에서 쓰려고하니까 발생한 순서 문제. 그냥 board 2개 나누는게 좋다.
        board[Rr][Rc] = -1
        santa_sturn[temp] = turn + 2
        santa_point[temp] += C
        nx, ny = Rr + C * dx[mdir], Rc + C * dy[mdir]
        if in_range(nx, ny) and board[nx][ny] == 0:
            santa[temp] = nx, ny
            board[nx][ny] = temp
        elif in_range(nx, ny) and board[nx][ny] != 0:  # 연쇄
            temp1 = board[nx][ny]
            santa[temp] = nx, ny
            board[nx][ny] = temp

            if deb == 1:
                print(temp, "가 밀려납니다.")
            # -------------------------
            # s_dir 방향으로 1칸씩 밀려나가며 체크해야한다.
            tx, ty = nx, ny
            while True:
                tx, ty = tx + dx[mdir], ty + dy[mdir]
                if in_range(tx, ty) and board[tx][ty] == 0:
                    santa[temp1] = tx, ty
                    board[tx][ty] = temp1
                    break
                elif in_range(tx, ty) and board[tx][ty] != 0:
                    santa[temp1] = tx, ty
                    temp1 = board[tx][ty]  # 기존에 있던 값 저장하고 다시.
                else:  # 밖에 나가버린 경우
                    santa[temp1] = -1, -1
                    break
        else:  # 나가버림
            if deb:
                print(temp, "가 우주로 밀려납니다.")
            santa[temp] = (-1, -1)

    return



def santa_m(turn):
    global board
    if deb:
        print("산타 스턴상태 체크 : ", santa_sturn)
    for number in range(1, P + 1):
        one_santa_move(turn, number)

    # 다시 색칠하기
    board = [[0 for _ in range(N)] for _ in range(N)]
    for idx in range(1, P + 1):
        sr, sc = santa[idx]
        if sr == -1: continue
        board[sr][sc] = idx
    board[Rr][Rc] = -1
    if deb:
        print_s()
    return


def one_santa_move(turn, number):  # 한명의 산타만 이동

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    sr, sc = santa[number]
    if santa_sturn[number] > turn:
        if deb == 1:
            print(number, "는 기절중")
        return  # 기절중
    if sr == -1: return
    board[sr][sc] = 0
    mx, my = -1, -1
    now_dist = cal_distance(sr, Rr, sc, Rc)
    s_dir = -1
    for num in range(4):
        nx, ny = sr + dx[num], sc + dy[num]
        after_dist = cal_distance(nx, Rr, ny, Rc)
        if in_range(nx, ny) and (board[nx][ny] == 0 or board[nx][ny] == -1) and after_dist < now_dist:  # 움직일 필요가 없을때도 추가
            mx, my = nx, ny
            now_dist = after_dist
            s_dir = num
    if s_dir == -1:  # 움직일수있는곳이 없다면
        board[sr][sc] = number
        return
    santa[number] = mx, my
    board[mx][my] = number

    # 루돌프가 있나 확인하고 튕겨져 나가야함
    if (mx == Rr and my == Rc):
        # 기절처리
        # [0,0,0,2,0]
        santa_sturn[number] = turn + 2
        if deb:
            print("루돌프와 부딫힘", number)
        santa_point[number] += D
        # 격자 밖으로 튕겨나가야함.
        s_dir = (s_dir + 2) % 4  # 반대편의 인덱스로 변환
        nnx, nny = mx + D * dx[s_dir], my + D * dy[s_dir]
        if in_range(nnx, nny) and board[nnx][nny] == 0:
            mx, my = nnx, nny
        elif in_range(nnx, nny) and board[nnx][nny] != 0:  # 누가있다면
            if deb:
                print(nnx, nny, "에 연쇄충돌 시작", board[nnx][nny], "이 밀리기 시작합니다.")
            temp = board[nnx][nny]  # 저장
            mx, my = nnx, nny

            # s_dir 방향으로 1칸씩 밀려나가며 체크해야한다.
            tx, ty = nnx, nny
            while True:
                tx, ty = tx + dx[s_dir], ty + dy[s_dir]
                if in_range(tx, ty) and board[tx][ty] == 0:
                    santa[temp] = tx, ty
                    break
                elif in_range(tx, ty) and board[tx][ty] != 0:
                    santa[temp] = tx, ty
                    temp = board[tx][ty]  # 기존에 있던 값 저장하고 다시.
                else:  # 밖에 나가버린 경우
                    santa[temp] = -1, -1
                    break

        else:
            mx, my = -1, -1
    santa[number] = mx, my

    return


def santa_p_up():
    for i, k in enumerate(santa):
        if i == 0: continue
        if k[0] == -1: continue
        santa_point[i] += 1
    return


def check_point():
    for i, k in enumerate(santa_point):
        if i == 0: continue
        print(k, end=' ')
if deb:
    print_s()
for turn in range(M):
    if deb:
        print(turn,"현재턴")
    roodolf_m(turn)
    santa_m(turn)
    # 루돌프 움직임
    # 가장 가까운 산타로
    # 충돌
    # 산타 움직임
    # 기절체크
    # 충돌

    # 산타가 탈락하면 바로 그즉시 게임 종료.
    santa_p_up()
    if deb:
        check_point()
        print()
check_point()