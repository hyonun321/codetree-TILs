n=int(input())
d={}
m=0
for _ in range(n):
    a =input()
    if not a in d:
        d[a]=1
        m=1
    else :
        d[a] += 1
        if m < d[a]:
            m=d[a]

print(m)