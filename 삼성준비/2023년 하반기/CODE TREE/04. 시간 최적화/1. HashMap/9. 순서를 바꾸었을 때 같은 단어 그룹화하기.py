# problem link : https://www.codetree.ai/missions/8/problems/group-same-word?&utm_source=clipboard&utm_medium=text

# solution 1

n = int(input())

count = dict()

for _ in range(n):
    inp = input()
    # 정렬을 하면 자동으로 타입이 배열로 변경
    inp = sorted(inp)

    string = ''
    for elem in inp:
        string += elem
    
    if string in count:
        count[string] += 1
    else:
        count[string] = 1

ans = 0

for key, value in count.items():
    ans = max(ans, value)

print(ans)

# solution 2

from collections import defaultdict

n = int(input())

count = defaultdict(lambda: 0)

for _ in range(n):
    inp = input()
    # 정렬을 하면 자동으로 타입이 배열로 변경
    inp = sorted(inp)

    string = ''
    for elem in inp:
        string += elem
    
    count[string] += 1

ans = 0

for key, value in count.items():
    ans = max(ans, value)

print(ans)