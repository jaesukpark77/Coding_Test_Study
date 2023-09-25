# problem link : https://www.codetree.ai/missions/8/problems/corresponding-numbers-and-characters?&utm_source=clipboard&utm_medium=text

n, m = map(int, input().split())

words = [input() for _ in range(n)]

string_to_num = dict()

for i in range(n):
    string_to_num[words[i]] = i + 1

for _ in range(m):
    word = input()

    if ord(word[0]) >= ord('0') and ord(word[0]) <= ord('9'):
        num = int(word)

        print(words[num - 1])
    else:
        print(string_to_num[word])