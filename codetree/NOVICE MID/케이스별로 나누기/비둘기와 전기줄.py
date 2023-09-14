# problem link : https://www.codetree.ai/missions/5/problems/pigeons-and-electric-cords?&utm_source=clipboard&utm_medium=text

MAX_NUM = 10
UNDEFINED = -1

n = int(input())

movements = [tuple(map(int, input().split())) for _ in range(n)]

pos = [UNDEFINED] * (MAX_NUM + 1)

move_cnt = 0

for pigeon, move_dir in movements:
    if pos[pigeon] == UNDEFINED:
        pos[pigeon] = move_dir
    elif pos[pigeon] != move_dir:
        pos[pigeon] = move_dir
        move_cnt += 1

print(move_cnt)