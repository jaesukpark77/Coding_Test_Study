# problem link : https://www.codetree.ai/missions/9/problems/longest-palindrome-2?&utm_source=clipboard&utm_medium=text

MAX_N = 200001

temp = input()
A = [0] * MAX_N

input_str = '#' + '#'.join(temp) + '#'
n = len(input_str)
r, p = -1, -1

for i in range(n):
    if r < i:
        A[i] = 0
    else:
        ii = 2 * p - i
        A[i] = min(r - i, A[ii])

    while i - A[i] - 1 >= 0 and i + A[i] + 1 < n and \
          input_str[i - A[i] - 1] == input_str[i + A[i] + 1]:
        A[i] += 1 

    if i + A[i] > r:
        r, p = i + A[i], i

ans = 0
for i in range(n):
    ans = max(ans, 2 * A[i] + 1)

print(ans // 2)