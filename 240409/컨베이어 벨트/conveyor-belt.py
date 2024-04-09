n,t = map(int,input().split())

one_map = list(map(int,input().split()))
two_map = list(map(int,input().split()))

def rotate(rounds):

    up_t=two_map[n-1]
    down_t=one_map[n-1]

    for i in range(n-1,0,-1):
        one_map[i]=one_map[i-1]

    for j in range(n-1,0,-1):
        two_map[j]=two_map[j-1]

    one_map[0] = up_t
    two_map[0] = down_t
    return



for rounds in range(t):
    rotate(rounds)

for k in one_map:
    print(k,end=' ')
print()
for k1 in two_map:
    print(k1,end=' ')