import sys
from collections import deque
#sys.stdin = open('T제거하기.txt','r')
def remove_T_efficiently(a, b):
    stack = deque()
    len_b = len(b)
    
    for char in a:
        stack.append(char)
        # 현재 스택의 마지막 부분이 b와 일치하는지 확인
        if stack[-len_b:] == b:
            # 일치한다면, b의 길이만큼 스택에서 제거
            del stack[-len_b:]
            
    return ''.join(stack)

# 입력 예시
a = list(input())
b = list(input())

# 효율적인 함수를 사용하여 결과 출력
result = remove_T_efficiently(a, b)
print(result)