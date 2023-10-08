# problem link : https://www.codetree.ai/missions/2/problems/max-of-xor?&utm_source=clipboard&utm_medium=text

n, m = tuple(map(int, input().split()))
a = list(map(int, input().split()))

ans = 0

def find_max_xor(curr_idx, cnt, curr_val):
    global ans

    if cnt == m:
        ans = max(ans, curr_val)
        return
    
    if curr_idx == n:
        return
    
    find_max_xor(curr_idx + 1, cnt, curr_val)

    find_max_xor(curr_idx + 1, cnt + 1, curr_val ^ a[curr_idx])

find_max_xor(0, 0, 0)

print(ans)