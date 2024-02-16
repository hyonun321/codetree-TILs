n,a=input().split()
n =int(n)
answer =0
for _ in range(n) :
    k = input()
    if k == a :
        answer+=1

print(answer)