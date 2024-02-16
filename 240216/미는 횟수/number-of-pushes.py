a=list(input())
b=input()

temp =a[len(a)-1]
for i in range(len(a)-1,0,-1):
    a[i]=a[i-1]
a[0]=temp
a=str(a)
print(a)