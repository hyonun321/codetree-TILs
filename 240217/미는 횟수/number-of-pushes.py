a=list(input())
b=list(input())
answer =0
for _ in range(len(a)):
    answer+=1
    temp =a[len(a)-1]
    for i in range(len(a)-1,0,-1):
        a[i]=a[i-1]
    a[0]=temp
    if a == b :
        print(answer)
        break
    
    if answer == len(a) :
        print(-1)