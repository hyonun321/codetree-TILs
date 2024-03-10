import sys
#sys.stdin = open('T제거하기.txt','r')

a = list(input())
b = list(input())


def simulation():
    global a, b
    
    while True:
        check_i = 1e6
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