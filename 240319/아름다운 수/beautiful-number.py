a = int(input())

arr = []

def find_beautiful(arr):

    # 전부 같은수

    # 숫자만큼 나온수 
    for k in arr :
        select  = k 
        
    return


def back(num):
    if num == a :
        for k in arr:
            print(k,end='')
        print()
        return

    for b in range(5):
        arr.append(b)
        back(num+1)
        arr.pop()
    return


back(0)