n = int(input())

edges= [[] for _ in range(n+1)]
visited = [False] * (n+1)
parent = [0]*(n+1)

for _ in range(n-1) : 
    a,b = map(int,input().split())
    edges[a].append(b)
    edges[b].append(a)

def traversal(x) : 

    for y in edges[x]:
        if not visited[y] : 
            visited[y] = True
            parent[y] = x
            traversal(y)
            

visited[1] = True
traversal(1)
for m in range(2,n+1):
    print(parent[m])