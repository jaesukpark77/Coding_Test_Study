# problem link : https://www.codetree.ai/missions/8/problems/most-data?&utm_source=clipboard&utm_medium=text

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