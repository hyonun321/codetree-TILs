temp = input()
 
input_str = "#" + "#".join(temp) + "#"

n = len(input_str)

A = [0] * n
r, p = -1, -1

for i in range(n):
    if r < i:
        A[i] = 0
    else:
        ii = 2 * p - i
        A[i] = min(r - i, A[ii])

    # i를 중심으로 최대로 뻗어나갑니다.
    while i - A[i] - 1 >= 0 and i + A[i] + 1 < n and \
          input_str[i - A[i] - 1] == input_str[i + A[i] + 1]:
        A[i] += 1 

    # i + A[i] 중 최대가 선택되도록
    # r, p값을 갱신해줍니다.
    if i + A[i] > r:
        r, p = i + A[i], i

# 최장 팰린드롬의 길이를 계산합니다.
ans = 0
for i in range(n):
    ans = max(ans, 2 * A[i] + 1)

# 처음 주어진 문자열에서 
# #을 제외한 부분의 길이가 실제 답이 되기에
# 2로 나눴을 때의 몫이 답이 됩니다.
print(ans // 2)