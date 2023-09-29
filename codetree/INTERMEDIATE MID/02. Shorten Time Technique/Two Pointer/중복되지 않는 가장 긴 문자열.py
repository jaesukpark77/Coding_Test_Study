# problem link : https://www.codetree.ai/missions/8/problems/longest-not-duplicated-substring?&utm_source=clipboard&utm_medium=text

word = '#' + input()
n = len(word) - 1
count_array = dict()

ans = 0

j = 0
for i in range(1, n+1):
    while j + 1 <= n and count_array.get(word[j+1], 0) != 1:
        count_array[word[j+1]] = count_array.get(word[j+1], 0) + 1
        j += 1

    ans = max(ans, j - i + 1)

    count_array[word[i]] -= 1

print(ans)