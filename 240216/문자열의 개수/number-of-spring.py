arr=[]
while True :
    a=input(
    )
    if a=='0' :
        break
    arr.append(a)
print(len(arr))
for i in range(len(arr)):
    if i %2 ==0:
        print(arr[i])