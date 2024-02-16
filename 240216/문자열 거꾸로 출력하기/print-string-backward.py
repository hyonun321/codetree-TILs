arr=[]
while True :
    a =input()
    if a =='END':
        break
    arr.append(a)

for item in arr :
    print(item[::-1])