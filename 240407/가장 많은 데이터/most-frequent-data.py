n=int(input())
d={}
for _ in range(n):
    a =input()
    if not a in d:
        d[a]=1
    else :
        d[a] += 1

_,b= max(d.items())
print(b)