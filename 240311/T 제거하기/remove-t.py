import sys
#sys.stdin = open('T제거하기.txt','r')

a = list(input())
b = list(input())


def check_ok():
    global a,b
    #print('check',a,b)
    if len(a) < len(b): return False
    #print(len(a),len(b))
    for i in range(len(a)):
            if a[i] == b[0]:
                point = 0
                for k in range(len(b)):
                    #print(i+k,k)
                    if a[i+k] != b[k] : break
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
                possible = True
                if i+len(b) > len(a) : continue
                for k in range(len(b)):
                    
                    if a[i+k] == b[k] : continue
                    else : 
                        possible = False
                        break
                    
                if possible:
                    check_i = i
                    break
        #print(check_i)
        if check_i == 1e6: break
        else :
            for _ in range(len(b)):
                a.pop(check_i)
        #print(a)
        
    return

simulation()
for k in a:
    print(k,end='')