# problem link : https://www.codetree.ai/missions/9/problems/tree-inorder?&utm_source=clipboard&utm_medium=text

k = int(input())

n = (1 << k) - 1

tree_num = [0] * (n + 1)
cnt = 1

a = [0] + list(map(int, input().split()))

def in_order(x):
    global cnt

    if x > n:
        return

    in_order(x * 2)
    tree_num[x] = a[cnt]
    cnt += 1
    in_order(x * 2 + 1)

in_order(1)

for i in range(1, k + 1):
    for j in range(1 << (i - 1), 1 << i):
        print(tree_num[j], end=" ")
    print()