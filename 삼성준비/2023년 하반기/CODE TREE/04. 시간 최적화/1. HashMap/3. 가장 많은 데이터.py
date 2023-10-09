# problem link : https://www.codetree.ai/missions/8/problems/most-data?&utm_source=clipboard&utm_medium=text

# solution 1
n = int(input())
words = [input() for _ in range(n)]

freq = dict()
ans = 0

for word in words:
    if word not in freq:
        freq[word] = 1
    else:
        freq[word] += 1

    ans = max(ans, freq[word])

print(ans)

# solution 2

from collections import defaultdict

n = int(input())
words = [input() for _ in range(n)]

freq = defaultdict(lambda: 0)
ans = 0

for word in words:
    freq[word] += 1

    ans = max(ans, freq[word])

print(ans)