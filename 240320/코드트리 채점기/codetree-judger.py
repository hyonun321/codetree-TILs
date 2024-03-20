import heapq
import sys
from collections import deque,defaultdict
deb = 0
#sys.stdin = open("input_codecal.txt",'r')
q = int(input())
chejumgi = [] # 현재 채점기의 상태를 알려준다. 
# 여기에 숫자가 있으면 채점대기상태라는거. 
waiting_queue = defaultdict(list) #이걸 도메인별로 관리했다. 
judging = [] #start,u1,u2,Jid
judging_domain = {}
history = [] # Start,End,u1,u2,J_id
history_domain= {} #히스토리에 체점된 도메인값을 key, value는 체점시간과 gap을 가지고있음.  
waiting_url = {}
waitQ_cnt = 0
def ready_cal(N,u): # 100
    global waitQ_cnt
    N = int(N)
    temp_u = list(u.split('/'))
    for i in range(1,N+1):
        heapq.heappush(chejumgi,i)
    heapq.heappush(waiting_queue[temp_u[0]],(1,0,temp_u[0],temp_u[1]))
    waitQ_cnt += 1
    waiting_url[temp_u[0]+'/'+temp_u[1]] = True
    if deb :
        print(waiting_queue)
        print(chejumgi)
    #여기서 우선순위 잘 확보해야함. i번째에서 상태를 봐야한다. 

    #체점기는 1번부터 N 번까지. 
    # 0초에 채점우선순위가 1이면서 문제요청 채점이 들어온다. 그러면 대기큐에 들어감. 
    return
def  need_cal(t,p,u):# 200
    global waitQ_cnt
    # t초에 우선순위 p이면서 u문제의 채점요청이 들어온다. 
    # 어떤 채점 대기큐에 들어간다. 
    # 만약 이미 대기큐에 u와 존재하는게 있으면 추가하지않고 pass 
    temp_u = list(u.split('/'))
    t=int(t)
    p=int(p)
    if u in waiting_url : # 만약 들어있다면
        if waiting_url[u] :
            return
        else : 
            waiting_url[u] = True
            waitQ_cnt +=1
            heapq.heappush(waiting_queue[temp_u[0]],(p,t,temp_u[0],temp_u[1]))
    else : 
        waiting_url[u] = True
        waitQ_cnt += 1
        heapq.heappush(waiting_queue[temp_u[0]],(p,t,temp_u[0],temp_u[1]))
    return


def  lets_cal(t):#300
    global waitQ_cnt,judging_domain
    t=int(t)
    # 도메인을 기준으로 waiting queue를 작성해야한다. 왜냐하면, 

    # history와 judging 큐에서 도메인을 가지고 비교하니까 결국 
    # 해당하는 도메인을 걸러버리면, 원하는 도메인에서 우선순위가 높은값을 pop 해올 수 있다.
    # 체점될수 없는 조건인애들은 치우고, 체점 가능한 경우중 우선순위 높은애들 고르니까 .
    # 블로그에 정리해보기. 이 자료구조를 떠올릴 수있나?

    # 2. 체점기가 있나없나 체크 

    if waitQ_cnt == 0 : 
        return
    possible = True

    best_priority= 500001
    best_time = 999999999
    best_domain1 = ''
    best_domain2 = ''

    for keys in waiting_queue :
        tasks_arr = waiting_queue[keys]
        for tasks in tasks_arr:
            (p1,t1,u1,u2) = tasks

            # 1. 현재 체점중인 도메인이 있나 확인해야함 
            if u1 in judging_domain:
                test = judging_domain[u1]
                if test :
                #뺀거 다시 넣고 리턴 
                    continue #그다음으로 
                else : 
                    pass

            # 3. 최근진행된 체점시간 체크 해보기. 
            if u1 in history_domain :
                hs,he = history_domain[u1]
                start = hs
                gap = he-hs
                if t<start+3*gap : 
                    continue
            #체점큐에 넣기 
            #여기서 가장 큰 놈이 나오나 체크해줘야함 바로 pop하면 안됨. 
            if p1 < best_priority : 
                best_priority = p1
                best_domain1 = u1
                best_domain2 = u2
                best_time = t1
            elif p1 == best_priority : 
                if  t1 < best_time :
                    best_priority = p1
                    best_domain1 = u1
                    best_domain2 = u2
                    best_time = t1


    if best_priority == 500001 : 
        return

    if len(chejumgi) != 0 :
        judger_number = heapq.heappop(chejumgi)
    else : 
        return
    heapq.heappop(waiting_queue[best_domain1])
    
    waiting_url[best_domain1+'/'+best_domain2] = False
    waitQ_cnt -=1
    heapq.heappush(judging,(t,best_domain1,best_domain2,judger_number))
    judging_domain[best_domain1] = True
    #여기서 시간이 오래걸리네 ,,
    #for item_task in temp_waiting_tasks : 
    #    heapq.heappush(waiting_queue,item_task)
    #이제 tempwaitingtask 애들 다시 큐에 넣어줘야한다. 

    return

def  end_cal(t,jid):#400
    global judging_domain
    # t 초에 Jid 번 채점기가 종료되고 쉬는상태가된다.
    # Jid번 채점기가 진행하던 채점이 없으면 걍 패스 
    t = int(t)
    jid = int(jid)
    #(jid)
    #if (_,_,_,jid) in judging:
    temp_judging = deque()
    
    possible = True
    while possible :
        if len(judging) == 0 : 
            break

        items = heapq.heappop(judging) 
        es,eu1,eu2,ejid = items

        if ejid == jid : 
            #채점대기큐
            heapq.heappush(chejumgi,ejid)
            #히스토리큐
            heapq.heappush(history,(es,t,eu1,eu2,ejid))
            history_domain[eu1] = (es,t) #가장 최신으로 업데이트해줌. 
            judging_domain[eu1] = False
            for items1 in temp_judging:
                heapq.heappush(judging,items1)
            return
        else : 
            temp_judging.append(items)
            continue
            #다시넣어버리기 

    for items1 in temp_judging:
        heapq.heappush(judging,items1)

    return
def  cal_queue_see(t):#500
    t = int(t)
    # 해당 t에 채점대기큐에있는 채점 task들의 수를 출력한다. 
    print(waitQ_cnt)
    return





for _ in range(q) : 
    strings = list(input().split())
    num = int(strings[0])
    if num == 100:
        ready_cal(strings[1],strings[2])
    elif num == 200 :
        need_cal(strings[1],strings[2],strings[3])
    elif num == 300 : 
        lets_cal(strings[1])
    elif num == 400 : 
        end_cal(strings[1],strings[2])
    elif num == 500 :
        cal_queue_see(strings[1])
    else :
        pass