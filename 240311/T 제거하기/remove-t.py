a = list(input())
b = list(input())


def check_ok():
    global a,b
    #print('check',a,b)
    if len(a) < len(b): return False
    for i in range(len(a)):
            if a[i] == b[0]:
                point = 0
                for k in range(len(b)):
                    if a[i+k] == b[k] : 
                        point += 1 
                if point == len(b): # 다 들어맞는다면 
                    check_i = i
                    return True
    return False

def simulation():
    global a, b
    check_i = 1e6
    while check_ok():
        #print(len(a),'dhkdn')
        for i in range(len(a)):
            if a[i] == b[0]:
                point = 0
                #print(i)
                for k in range(len(b)):
                    if a[i+k] == b[k] : 
                        point += 1 
                if point == len(b): # 다 들어맞는다면 
                    check_i = i
                    break
        #print(check_i)
        for _ in range(len(b)):
            a.pop(check_i)
        #print(a)
        
    return

simulation()
for k in a:
    print(k,end='')