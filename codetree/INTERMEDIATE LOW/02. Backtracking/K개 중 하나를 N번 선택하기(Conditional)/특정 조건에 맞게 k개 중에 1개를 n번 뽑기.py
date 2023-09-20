# problem link : https://www.codetree.ai/missions/2/problems/n-permutations-of-k-with-repetition-under-constraint?&utm_source=clipboard&utm_medium=text

k, n = tuple(map(int, input().split()))
selected_nums = []

def print_permutation():
    for num in selected_nums:
        print(num, end=' ')

    print()

def find_duplicated_permuations(cnt):
    if cnt == n:
        print_permutation()
        return

    for i in range(1, k + 1):
        if cnt >= 2 and i == selected_nums[-1] and i == selected_nums[-2]:
            continue
        else:
            selected_nums.append(i)
            find_duplicated_permuations(cnt + 1)
            selected_nums.pop()

find_duplicated_permuations(0)