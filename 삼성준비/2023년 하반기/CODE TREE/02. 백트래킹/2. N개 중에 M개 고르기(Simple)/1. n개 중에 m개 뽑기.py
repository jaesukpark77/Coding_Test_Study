# problem link : https://www.codetree.ai/missions/2/problems/n-choose-m?&utm_source=clipboard&utm_medium=text

n, m = map(int, input().split())
combination = []

def print_combination():
    for elem in combination:
        print(elem, end=' ')

    print()

def find_combinations(curr_num, cnt):
    if curr_num == n + 1:
        if cnt == m:
            print_combination()
        return

    combination.append(curr_num)
    find_combinations(curr_num + 1, cnt + 1)
    combination.pop()

    find_combinations(curr_num + 1, cnt)

find_combinations(1, 0)