from sortedcontainers import SortedSet

s = SortedSet()      # treeset

n=int(input())
for _ in range(n):
    strings = input().split()
    if strings[0] =='add':
        s.add(int(strings[1]))

    elif strings[0] =='find':
        if int(strings[1]) in s :
            print('true')
        else :
            print('false')
    elif strings[0] =='remove':
        s.remove(int(strings[1]))
    elif strings[0] =='lower_bound':
        if len(s)!=0:
       
            idx = s.bisect_left(int(strings[1]))
            if idx < len(s):
                print(s[idx])
            else:
                print('None')
        else:
            print('None')
    elif strings[0] =='upper_bound':
        if len(s)!=0:
            idx = s.bisect_right(int(strings[1]))
            if idx < len(s):
                print(s[idx])
            else:
                print('None')
        else:
            print('None')
    elif strings[0] =='largest':
        if len(s)!=0 :
            print(s[-1])
        else :
            print('None')
    else:
        if len(s)!=0:
            print(s[0])
        else:
            print('None')