# problem link : https://www.codetree.ai/missions/5/problems/moving-block?&utm_source=clipboard&utm_medium=text

n = int(input())
blocks = [int(input()) for _ in range(n)]

sum_of_block = sum(blocks)

avg = sum_of_block // n
ans = 0

for block_num in blocks:
    if block_num > avg:
        ans += block_num - avg

print(ans)