def combinations(arr, n):
    result = []

    if n == 0:
        return [[]]

    for i, num in enumerate(arr):
        for j in combinations(arr[i+1:], n-1):
            result.append([num] + j)
    return result

combination = combinations([1,2,3,4], 3)
print(combination)