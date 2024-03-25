class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def insert_next(u, singleton): # u앞에 싱글톤을 붙임 
    singleton.prev = u
    singleton.next = u.next

    if singleton.prev is not None:
        singleton.prev.next = singleton
    if singleton.next is not None:
        singleton.next.prev = singleton

def insert_prev(u,singleton):
    singleton.prev = u.prev
    singleton.next = u

    if singleton.prev is not None:
        singleton.prev.next = singleton
    if singleton.next is not None:
        singleton.next.prev = singleton

def print_node(cur):


    if cur.prev is None : 
        a = '(Null)'
    else : 
        a = cur.prev.data
    if cur.next is None:
        b = '(Null)'
    else : 
        b = cur.next.data
    print(f'{a} {cur.data} {b}')

def pop(u):
    if u.prev is not None:
        u.prev.next = u.next
    if u.next is not None:
        u.next.prev = u.prev
    u.prev=None
    u.next=None

s_init = input()
n = int(input())
cur = Node(s_init)
for _ in range(n):
    strs = input().split()
    a = strs[0]
    if len(strs) == 2 :
        b = strs[1]
        node1 = Node(b)
    a = int(a)
    if a == 1:
        insert_prev(cur,node1)
    elif a ==2 :
        insert_next(cur,node1)

    elif a == 3 :
        if cur.prev is not None:
            cur = cur.prev
    
    else : 
        if cur.next is not None:
            cur = cur.next
    print_node(cur)