# problem link : https://www.codetree.ai/missions/8/problems/determine-subsequence?&utm_source=clipboard&utm_medium=text

n, m = map(int, input().split())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))

def is_sequence():
    i = 1

    for j in range(1, m + 1):
        while i <= n and A[i] != B[j]:
            i += 1
        
        if i == n + 1:
            return False
        else:
            i += 1

    return True

if is_sequence():
    print('Yes')
else:
    print('No')