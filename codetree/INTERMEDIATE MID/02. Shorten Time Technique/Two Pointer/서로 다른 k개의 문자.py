# problem link : https://www.codetree.ai/missions/8/problems/k-distinct-characters?&utm_source=clipboard&utm_medium=text

word, k = input().split()
k = int(k)
word = "#" + word
n = len(word) - 1
count_array = dict()

def can_move(j):
    if j + 1 > n:
        return False
    if distinct_number == k and count_array.get(word[j + 1], 0) == 0:
        return False
    
    return True

ans = 0

distinct_number = 0
j = 0
for i in range(1, n + 1):
    while can_move(j):
        count_array[word[j + 1]] = count_array.get(word[j + 1], 0) + 1
        if count_array[word[j + 1]] == 1:
            distinct_number += 1
        j += 1
    
    ans = max(ans, j - i + 1)

    count_array[word[i]] -= 1

    if count_array[word[i]] == 0:
        distinct_number -= 1

print(ans)